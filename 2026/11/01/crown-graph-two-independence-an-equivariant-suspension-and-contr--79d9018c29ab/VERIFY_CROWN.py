"""Standalone finite checks for the 2-independence complexes of crown graphs.

Run: python3 VERIFY_CROWN.py
No third-party packages required. Finite checks illustrate, but do not replace,
the all-n nerve-cover proof in RESULT.md.
"""
from itertools import combinations, permutations


def faces_of_crown(n):
    edges = [(i, n+j) for i in range(n) for j in range(n) if i != j]
    faces = set()
    for mask in range(1, 1 << (2*n)):
        parent = list(range(2*n))
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for u,v in edges:
            if (mask >> u)&1 and (mask >> v)&1:
                a,b=root(u),root(v)
                parent[a]=b
        sizes={}
        for v in range(2*n):
            if (mask >> v)&1:
                r=root(v)
                sizes[r]=sizes.get(r,0)+1
        if max(sizes.values(),default=0)<=2:
            faces.add(mask)
    return faces


def predicted_faces(n):
    a=(1<<n)-1
    b=a<<n
    facets=[a,b]+[(1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j))
                  for i in range(n) for j in range(i+1,n)]
    faces=set()
    for mask in facets:
        sub=mask
        while sub:
            faces.add(sub)
            sub=(sub-1)&mask
    return faces


def boundary_rank(faces, k, p):
    """Rank over F_p of the oriented k-boundary, including augmentation."""
    domain=sorted(m for m in faces if m.bit_count()==k+1)
    if k==0:
        return int(bool(domain))
    codomain=sorted(m for m in faces if m.bit_count()==k)
    rid={m:i for i,m in enumerate(codomain)}
    pivots={}
    for mask in domain:
        verts=[i for i in range(mask.bit_length()) if mask>>i&1]
        v={rid[mask^(1<<a)]: ((-1)**i)%p
           for i,a in enumerate(verts)}
        while v:
            lead=min(v)
            if lead not in pivots:
                inv=pow(v[lead],-1,p)
                pivots[lead]={r:(c*inv)%p for r,c in v.items()}
                break
            b=pivots[lead]
            coeff=v[lead]
            for r,c in b.items():
                x=(v.get(r,0)-coeff*c)%p
                if x: v[r]=x
                elif r in v: del v[r]
    return len(pivots)


def homology_dimensions(faces,p):
    maximum=max(m.bit_count() for m in faces)-1
    chain=[sum(m.bit_count()==k+1 for m in faces)
           for k in range(maximum+1)]
    rank=[boundary_rank(faces,k,p) for k in range(maximum+1)]+[0]
    return [chain[k]-rank[k]-rank[k+1] for k in range(maximum+1)]


def parity(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inv%2 else 1


def character(faces, pi, swap):
    n=len(pi)
    def map_vertex(v):
        if v<n:
            return pi[v]+(n if swap else 0)
        return pi[v-n]+(0 if swap else n)
    out=-1  # augmented chain contribution
    for mask in faces:
        original=[i for i in range(2*n) if mask>>i&1]
        mapped=[map_vertex(i) for i in original]
        if {map_vertex(i) for i in original}!=set(original):
            continue
        sign=parity(mapped)
        out += ((-1)**(len(original)-1))*sign
    return out


def predicted_character(pi,swap):
    n=len(pi)
    fixed=sum(pi[i]==i for i in range(n))
    fixed2=sum(pi[pi[i]]==i for i in range(n))
    u=fixed-1
    u2=fixed2-1
    dim=(u*u-u2)//2
    return -dim if swap else dim


def verify(n):
    f=faces_of_crown(n)
    assert f==predicted_faces(n), ('cover',n)
    vector=tuple(sum(m.bit_count()==k for m in f)
                 for k in range(1,max(m.bit_count() for m in f)+1))
    target=(n-1)*(n-2)//2
    for p in (2,3,5):
        betti=homology_dimensions(f,p)
        assert betti==[0,0,target]+[0]*(len(betti)-3),(n,p,betti)
    checked=0
    for pi in permutations(range(n)):
        for swap in (0,1):
            actual=character(f,pi,swap)
            expected=predicted_character(pi,swap)
            assert actual==expected,(n,pi,swap,actual,expected)
            checked+=1
    return {'n':n,'f_vector':vector,'beta_2':target,'characters_checked':checked}


if __name__=='__main__':
    for n in range(3,7):
        print(verify(n))
    print('CROWN_TWO_INDEPENDENCE_NERVE_CHARACTER_FINITE_CHECKS_OK')
