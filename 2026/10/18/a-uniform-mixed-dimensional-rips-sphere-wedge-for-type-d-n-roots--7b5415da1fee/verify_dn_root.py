"""Exact small-case verifier for inclusive sqrt(2) Vietoris--Rips complexes of type-D roots."""
from itertools import combinations, product
from math import comb

def roots(n):
    return [tuple((i,s,j,t)) for i,j in combinations(range(n),2) for s,t in product((-1,1),repeat=2)]

def dot(a,b):
    aa={a[0]:a[1],a[2]:a[3]};bb={b[0]:b[1],b[2]:b[3]}
    return sum(x*bb.get(i,0) for i,x in aa.items())

def faces_and_adjacency(n):
    r=roots(n);N=len(r)
    adj=[set(j for j in range(N) if j!=i and dot(r[i],r[j])==1) for i in range(N)]
    faces={}
    def go(face,cands):
        if face:faces.setdefault(len(face)-1,[]).append(face)
        for p,i in enumerate(cands):go(face+(i,),[j for j in cands[p+1:] if j in adj[i]])
    go((),list(range(N)))
    return r,adj,faces

def rank_gf2(columns):
    piv={}
    for mask in columns:
        while mask:
            p=mask.bit_length()-1
            if p not in piv:
                piv[p]=mask
                break
            mask^=piv[p]
    return len(piv)

def bettis(faces):
    rs={}; f={k:len(v) for k,v in faces.items()}
    for d in range(1,max(f)+1):
        loc={s:i for i,s in enumerate(faces[d-1])}
        columns=[]
        for simplex in faces[d]:
            mask=0
            for q in range(len(simplex)):
                mask ^= 1<<loc[simplex[:q]+simplex[q+1:]]
            columns.append(mask)
        rs[d]=rank_gf2(columns)
    return {d:f[d]-rs.get(d,0)-rs.get(d+1,0) for d in f},rs

def star_center(simplex,r):
    common=None
    for ix in simplex:
        rr=r[ix]
        here={(rr[0],rr[1]),(rr[2],rr[3])}
        common=here if common is None else common & here
    return common or set()

def check(n):
    r,adj,F=faces_and_adjacency(n)
    assert len(r)==2*n*(n-1)
    assert all(len(a)==4*(n-2) for a in adj)
    assert len(F[0])==2*n*(n-1)
    assert len(F[1])==4*n*(n-1)*(n-2)
    external=[s for d,z in F.items() for s in z if len(s)>=3 and not star_center(s,r)]
    assert len(external)==8*comb(n,3)
    assert all(len(s)==3 for s in external)
    for s in external:
        labels=set((r[v][0] for v in s))|set((r[v][2] for v in s))
        assert len(labels)==3
    H=2*n*(n-1)
    b2=8*comb(n,3)-H+2*n-1
    bet,rs=bettis(F)
    expected={0:1,2:b2}
    if n==4:expected[2]+=2*n
    else:expected[n-2]=2*n
    assert {k:v for k,v in bet.items() if v}==expected, (n,bet,expected)
    print('n=',n,'f=',[len(F[k]) for k in sorted(F)],'ranks=',rs,'betti=',bet,'triangles_no_star=',len(external))

if __name__=='__main__':
    for n in (4,5,6,7):check(n)
    print('VERIFY_OK')
