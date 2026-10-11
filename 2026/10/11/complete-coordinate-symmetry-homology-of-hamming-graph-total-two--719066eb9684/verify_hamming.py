"""Independent finite checks for total-two-cut Hamming graph homology characters.
Only finite tests; the accompanying paper supplies all-parameter arguments.
"""
from itertools import product,permutations,combinations
from collections import Counter


def graph(shape):
    vertices=list(product(*(range(n) for n in shape)))
    idx={v:i for i,v in enumerate(vertices)}
    N=len(vertices)
    adj=[0]*N
    for a in range(N):
        for b in range(a+1,N):
            if sum(vertices[a][j]!=vertices[b][j] for j in range(len(shape)))==1:
                adj[a]|=1<<b
                adj[b]|=1<<a
    return vertices,idx,adj

def legal_faces(shape):
    vertices,_,adj=graph(shape)
    N=len(vertices)
    full=(1<<N)-1
    legal=[]
    for mask in range(1<<N):
        comp=full^mask
        is_clique=True
        x=comp
        while x:
            lowest=x&-x
            i=lowest.bit_length()-1
            x^=lowest
            if x&~adj[i]:
                is_clique=False
                break
        if not is_clique:
            legal.append(mask)
    return legal

def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def groupperm(shape,axisperm,alphperms):
    # Each old axis i moves to axis axisperm[i]. alphperms indexed by target axis.
    assert sorted(axisperm)==list(range(len(shape)))
    assert all(shape[i]==shape[axisperm[i]] for i in range(len(shape)))
    vertices,idx,_=graph(shape)
    p=[]
    for v in vertices:
        out=[None]*len(shape)
        for i,x in enumerate(v):
            j=axisperm[i]
            out[j]=alphperms[j][x]
        p.append(idx[tuple(out)])
    assert sorted(p)==list(range(len(vertices)))
    return p

def predicted(shape,p,axisperm):
    V,_,_=graph(shape)
    fixedverts=sum(p[i]==i for i in range(len(V)))
    fixdirs=sum(axisperm[i]==i for i in range(len(shape)))
    lines=set()
    for i in range(len(shape)):
        for fix in product(*(range(shape[j]) for j in range(len(shape)) if j!=i)):
            line=[]
            for x in range(shape[i]):
                z=list(fix)
                z.insert(i,x)
                line.append(V.index(tuple(z)))
            lines.add(frozenset(line))
    fixedlines=sum(frozenset(p[v] for v in line)==line for line in lines)
    return parity(p)*(1-fixedlines+(fixdirs-1)*fixedverts), (fixedverts,fixdirs,fixedlines)

def signed_trace(shape,p,faces=None):
    if faces is None:faces=legal_faces(shape)
    N=len(p)
    total=0
    for mask in faces:
        old=[i for i in range(N) if mask>>i&1]
        new=[p[i] for i in old]
        if sum(1<<i for i in new)!=mask:continue
        s=parity(new)
        total+=(-1 if len(old)%2==0 else 1)*s # (-1)^(|face|-1)
    return (-1 if (N-4)%2 else 1)*total

def rank_mod2(columns):
    piv={}
    for c in columns:
        while c:
            k=c.bit_length()-1
            if k not in piv:
                piv[k]=c
                break
            c^=piv[k]
    return len(piv)

def homology_ranks(shape,faces):
    levels={}
    for m in faces:
        levels.setdefault(m.bit_count()-1,[]).append(m)
    lev=sorted(k for k in levels if k>=0)
    br={}
    for d in lev:
        if d==0:
            br[d]=0
            continue
        lookup={v:i for i,v in enumerate(levels[d-1])}
        cols=[]
        for f in levels[d]:
            x=f
            col=0
            while x:
                b=x&-x; x^=b
                col^=1<<lookup[f^b]
            cols.append(col)
        br[d]=rank_mod2(cols)
    red={}
    for d in lev:
        red[d]=len(levels[d])-br[d]-br.get(d+1,0)-(1 if d==0 else 0)
    return red

def test():
    tested=0
    homs=0
    records=[]
    for shape in [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,2,2,2)]:
        V,_,_=graph(shape)
        n=len(V)
        faces=legal_faces(shape)
        assert n>=4
        # Some full symmetry generators: all alphabet transpositions and axis permutations.
        transforms=[]
        ids=tuple(range(len(shape)))
        basic=tuple(tuple(range(a)) for a in shape)
        transforms.append((ids,basic))
        for j,a in enumerate(shape):
            p=list(basic)
            tr=list(range(a));tr[0],tr[1]=tr[1],tr[0]
            p[j]=tuple(tr)
            transforms.append((ids,tuple(p)))
        for i in range(len(shape)):
            for j in range(i+1,len(shape)):
                if shape[i]!=shape[j]:continue
                axis=list(ids);axis[i],axis[j]=axis[j],axis[i]
                transforms.append((tuple(axis),basic))
        if len(set(shape))==1 and len(shape)>2:
            transforms.append((tuple((i+1)%len(shape) for i in range(len(shape))),basic))
        for a,ps in transforms:
            p=groupperm(shape,a,ps)
            expected,details=predicted(shape,p,a)
            found=signed_trace(shape,p,faces)
            assert expected==found,(shape,a,ps,expected,found,details)
            tested+=1
        if n<=12:
            ranks=homology_ranks(shape,faces)
            betti=(len(shape)-1)*n+1-sum(n//a for a in shape)
            assert ranks.get(n-4)==betti,(shape,ranks,betti)
            assert all(v==0 for k,v in ranks.items() if k!=n-4),(shape,ranks)
            homs+=1
        records.append((shape,n,len(faces),len(transforms)))
    print('VERIFY_OK',f'trace_cases={tested}',f'full_F2_homology_cases={homs}', 'records=',records)

def exhaustive_small_groups():
    """Check every element of the full natural group on four small Hamming graphs."""
    cases=0
    for shape in ((2,2),(2,3),(3,3),(2,2,2)):
        faces=legal_faces(shape)
        axes=range(len(shape))
        for ap in permutations(axes):
            if any(shape[i]!=shape[ap[i]] for i in axes):
                continue
            for ps in product(*(tuple(permutations(range(d))) for d in shape)):
                p=groupperm(shape,ap,ps)
                expected,_=predicted(shape,p,ap)
                found=signed_trace(shape,p,faces)
                assert found==expected,(shape,ap,ps,found,expected)
                cases+=1
    assert cases==140,cases
    print('EXHAUSTIVE_GROUP_OK',f'elements={cases}')

if __name__=='__main__':
    test()
    exhaustive_small_groups()
