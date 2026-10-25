"""Reproduce finite cross-polytope incidence graph checks (stdlib only)."""
from itertools import product, combinations
from math import comb


def model(m):
    vertices = [(i,s) for i in range(m) for s in (-1,1)]
    facets = list(product((-1,1),repeat=m))
    names = [('v',v) for v in vertices] + [('f',f) for f in facets]
    down = {}
    for v in vertices:
        down[('v',v)] = {('v',v)}
    for f in facets:
        down[('f',f)] = {('f',f)} | {('v',(i,f[i])) for i in range(m)}
    up = {n:{k for k in names if n in down[k]} for n in names}
    def graph(mode):
        neighborhoods = down if mode=='ins' else up
        return {n:{k for k in names if k!=n and neighborhoods[n]&neighborhoods[k]} for n in names}
    return vertices,facets,names,graph('ins'),graph('cm')


def f_vector(G, names):
    names=list(names)
    out=[]
    for r in range(1,len(names)+1):
        c=sum(all(b in G[a] for a,b in combinations(S,2)) for S in combinations(names,r))
        if c:out.append(c)
        else:break
    return out


def rank_mod2(rows):
    piv={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i in piv:row ^= piv[i]
            else:
                piv[i]=row
                break
    return len(piv)


def betti_mod2(G,names):
    """Compute reduced homology via exact F2 matrices (small m only)."""
    names=list(names)
    faces={k:[] for k in range(1,len(names)+1)}
    for r in range(1,len(names)+1):
        for S in combinations(range(len(names)),r):
            if all(names[b] in G[names[a]] for a,b in combinations(S,2)):
                faces[r].append(S)
    faces={r:val for r,val in faces.items() if val}
    ranks={}
    for r in faces:
        if r==1:
            ranks[r]=1 # augmented boundary to F2
            continue
        lookup={f:i for i,f in enumerate(faces[r-1])}
        rows=[]
        for S in faces[r]:
            row=0
            for T in combinations(S,r-1): row ^= 1<<lookup[T]
            rows.append(row)
        ranks[r]=rank_mod2(rows)
    betti={r-1:len(faces[r])-ranks[r]-ranks.get(r+1,0) for r in faces}
    return {k:v for k,v in betti.items() if v}


def check(m):
    vertices,facets,names,gi,gc=model(m)
    mi=[('v',v) for v in vertices]
    ma=[('f',f) for f in facets]
    # All x_i minimal vertices dominated by each incident maximal vertex in Ins.
    for v in mi:
        incident=[f for f in ma if v[1][1]==f[1][v[1][0]]]
        assert incident
        assert all((gi[v]|{v})<=(gi[f]|{f}) for f in incident)
    # All facets dominated by each of their incident minimal vertices in Cm.
    for f in ma:
        incident=[v for v in mi if v[1][1]==f[1][v[1][0]]]
        assert len(incident)==m
        assert all((gc[f]|{f})<=(gc[v]|{v}) for v in incident)
    for a,b in combinations(mi,2):
        assert (b in gc[a]) == (a[1][0] != b[1][0])
    for a,b in combinations(ma,2):
        assert (b in gi[a]) == (b[1] != tuple(-s for s in a[1]))
    fi=f_vector(gi,ma)
    fc=f_vector(gc,mi)
    assert fc==[comb(m,k)*2**k for k in range(1,m+1)]
    p=2**(m-1)
    assert fi==[comb(p,k)*2**k for k in range(1,p+1)]
    print('m=',m,'points=',len(names),'Ins-reduced f=',fi,'Cm-reduced f=',fc)
    if m<=3:
        bi=betti_mod2(gi,ma)
        bc=betti_mod2(gc,mi)
        assert bi=={p-1:1},(bi,p)
        assert bc=={m-1:1},bc
        print('   mod2 reduced Betti Ins:',bi,'Cm:',bc)

if __name__=='__main__':
    for m in (2,3,4): check(m)
