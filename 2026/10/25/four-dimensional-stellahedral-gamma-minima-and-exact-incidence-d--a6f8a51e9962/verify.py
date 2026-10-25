"""Exact rank-five face-lattice and augmented-Chow-gamma checks.

Uses only Python's standard library. Combinatorial face sets are computed as
intersections of defining facets for canonical four-polytopes.
"""
from itertools import product, combinations
from math import comb


def add(a,b):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}

def mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items(): out[i+j]=out.get(i+j,0)+x*y
    return {k:v for k,v in out.items() if v}

def T(k):
    if k%2==0:return {}
    j=(k-1)//2
    return {j:(-1)**j*comb(2*j,j)//(j+1)}

def S(k):
    a={0:1}
    for i in range(k):
        a=add(a,mul({1:1},T(k-i)))
    return a

def gamma_word(seq):
    # e.g. cdc -> c^1 d c^1, represented (1,1).
    r=len(seq)-1
    result={}
    for l in range(r+1):
        term={0:2**l}
        term=mul(term,S(seq[l]))
        for j in range(l+1,r+1):
            term=mul(term,T(seq[j]+1))
        term={d+r:c for d,c in term.items()}
        result=add(result,term)
    return result

basis=[(4,),(2,0),(1,1),(0,2),(0,0,0)]
values=[gamma_word(seq) for seq in basis]
expect=[{0:1,1:1,2:-1},{1:3,2:1},{1:2,2:2},{1:2,2:1},{2:7}]
assert values==expect,(values,expect)


def polytope_faces(n,facets):
    all_vertices=frozenset(range(n))
    current={all_vertices}
    for f in facets:
        f=frozenset(f)
        assert 0<len(f)<n
    # All nonempty intersections of any subcollection of facet sets.
    for f in facets:
        cur=list(current)
        for s in cur:
            x=s.intersection(f)
            if x: current.add(x)
    assert all(frozenset([i]) in current for i in range(n))
    ranks={}
    for s in sorted(current,key=lambda x:(len(x),sorted(x))):
        smaller=[ranks[t] for t in ranks if t<s]
        ranks[s]=max(smaller,default=0)+1
    assert ranks[all_vertices]==5,(n,len(facets),ranks[all_vertices])
    rankfaces={j:[s for s,r in ranks.items() if r==j] for j in range(1,5)}
    f0,f1,f2,f3=[len(rankfaces[j]) for j in range(1,5)]
    inc12=sum(e<face for e in rankfaces[2] for face in rankfaces[3])
    assert f0-f1+f2-f3==0
    assert inc12>=3*f2
    # Verify each polygon's number of edges and each polygon belongs to exactly 2 facets.
    for p in rankfaces[3]:
        assert sum(e<p for e in rankfaces[2])>=3
        assert sum(p<fac for fac in rankfaces[4])==2
    return ranks,(f0,f1,f2,f3,inc12)


def cd_ab(word):
    pol={"":1}
    for letter in word:
        factor={"a":1,"b":1} if letter=="c" else {"ab":1,"ba":1}
        out={}
        for w,c in pol.items():
            for q,d in factor.items():out[w+q]=out.get(w+q,0)+c*d
        pol=out
    return pol

def flag_ab(ranks):
    rankfaces={j:[s for s,r in ranks.items() if r==j] for j in range(1,5)}
    fs={}
    for mask in range(16):
        S=[j for j in range(1,5) if mask&(1<<(j-1))]
        count=1
        for j in S:
            if j==S[0]:
                count=len(rankfaces[j]);previous=j
            else:
                count=sum(1 for parts in product(*[rankfaces[k] for k in S[:S.index(j)+1]]) if all(parts[t]<parts[t+1] for t in range(len(parts)-1)))
        fs[mask]=count
    # The flag h-vector inversion.
    hs={m:sum((-1)**(m.bit_count()-b.bit_count())*fs[b] for b in range(16) if b&m==b) for m in range(16)}
    return {''.join('b' if m&(1<<i) else 'a' for i in range(4)):hs[m] for m in range(16)}

def check(name,n,facets):
    ranks,(v,e,r,s,m)=polytope_faces(n,facets)
    # Expansion of the cd-index in the ab-basis, checked against *all* flag-h values.
    coeff=(1,s-2,r-s,v-2,m-e-r-v-s+4)
    ab={w:0 for w in flag_ab(ranks)}
    for word,c in zip(('cccc','ccd','cdc','dcc','dd'),coeff):
        for w,mult in cd_ab(word).items():ab[w]+=mult*c
    actual=flag_ab(ranks)
    assert ab==actual,(name,ab,actual)
    gamma={}
    for dcoeff,poly in zip(coeff,values):
        gamma=add(gamma,{j:dcoeff*x for j,x in poly.items()})
    U,W,D,X=v-5,s-5,e-2*v,m-3*r
    assert min(U,W,D,X)>=0,(name,U,W,D,X)
    K=m-3*e
    assert K>=0,(name,K)
    expected={0:1,1:26+4*U+2*D+3*W,2:43-4*U+8*W+9*D+7*X}
    assert gamma==expected,(name,gamma,expected)
    assert 3*(gamma[2]-43)==12*W+27*D+4*K+17*X
    assert gamma[1]>=26 and gamma[2]>=43
    if gamma[1]==26 or gamma[2]==43:
        assert (v,e,r,s,m)==(5,10,10,5,30)
    print(name,(v,e,r,s,m),"cd",coeff,"gamma",gamma,"defects",(U,W,D,K,X))

# Four-simplex.
check('simplex4',5,[set(range(5))-{i} for i in range(5)])
# Four-cube.
vs=list(product(range(2),repeat=4))
check('cube4',len(vs),[{j for j,x in enumerate(vs) if x[k]==value} for k in range(4) for value in range(2)])
# Four-cross-polytope (ordered vertices (axis,sign)).
vs=list(product(range(4),range(2)))
check('cross4',len(vs),[{j for j,(axis,sign) in enumerate(vs) if sign==assignment[axis]} for assignment in product(range(2),repeat=4)])
# Products of simplices.
for n1,n2 in ((4,2),(3,3),(2,4)):
    verts=list(product(range(n1),range(n2)))
    facets=[{j for j,(a,b) in enumerate(verts) if a!=i} for i in range(n1)]
    facets+=[{j for j,(a,b) in enumerate(verts) if b!=i} for i in range(n2)]
    check(f'delta{n1-1}xdelta{n2-1}',len(verts),facets)

# Pyramids over three-dimensional cube and octahedron.
basecube=list(product(range(2),repeat=3))
facets=[set(range(8))]+[{j for j,x in enumerate(basecube) if x[k]==a}|{8} for k in range(3) for a in range(2)]
check('pyramid_cube3',9,facets)
baseoct=list(product(range(3),range(2)))
facets=[set(range(6))]+[{j for j,(axis,sgn) in enumerate(baseoct) if sgn==a[axis]}|{6} for a in product(range(2),repeat=3)]
check('pyramid_octahedron3',7,facets)
print('EXACT_OK basis=5 convex_4_polytopes=8')
