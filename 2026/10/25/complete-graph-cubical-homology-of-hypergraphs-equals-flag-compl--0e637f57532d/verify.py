"""Finite exact checks for the integral cube/simplicial comparison theorem.
Pure standard-library verifier; mathematical proof is independent of samples.
"""
from itertools import combinations, product
from collections import defaultdict


def faces(vertices, edges):
    E={frozenset(e) for e in edges}
    ans=[]
    for r in range(1,len(vertices)+1):
        for s in combinations(vertices,r):
            if all(frozenset(e) in E for e in combinations(s,2)):
                ans.append(s)
    return ans


def is_deg(cube,n):
    if n==0:return False
    return any(all(cube[i]==cube[i|(1<<j)] for i in range(1<<n) if not (i & (1<<j))) for j in range(n))


def face(cube,n,i,value):
    return tuple(cube[(t & ((1<<i)-1)) | (value<<i) | ((t>>i)<<(i+1))] for t in range(1<<(n-1)))


def boundary(cube,n):
    ans=defaultdict(int)
    for i in range(n):
        for value, coeff in [(0,(-1)**(i+1)), (1,(-1)**i)]:
            v=face(cube,n,i,value)
            if not is_deg(v,n-1):ans[v]+=coeff
    return {k:v for k,v in ans.items() if v}


def corner(s):
    n=len(s)-1
    return tuple(s[(t.bit_length())] if t else s[0] for t in range(1<<n))


def cubes(K,n):
    out=set()
    for s in K:
        for x in product(s,repeat=1<<n):
            if not is_deg(x,n):out.add(x)
    return sorted(out)


def rank_mod2(columns):
    piv={}
    for col in columns:
        x=col
        while x:
            j=x.bit_length()-1
            if j in piv:x ^= piv[j]
            else:
                piv[j]=x
                break
    return len(piv)


def checksum_boundary(basis, previous, n):
    idx={c:i for i,c in enumerate(previous)}
    arr=[]
    for c in basis:
        d=boundary(c,n); x=0
        for target,val in d.items():
            assert target in idx
            if val%2: x^=1<<idx[target]
        arr.append(x)
    return arr


def simplicial_betti(K,n,ranks):
    c=sum(len(s)==n+1 for s in K)
    return c-(ranks[n] if n<len(ranks) else 0)-(ranks[n+1] if n+1<len(ranks) else 0)


def simplicial_ranks(K):
    bydim=[[s for s in K if len(s)==i+1] for i in range(3)]
    out=[0]
    for n in [1,2]:
        idx={s:i for i,s in enumerate(bydim[n-1])}
        cols=[sum(1<<idx[s[:j]+s[j+1:]] for j in range(n+1)) for s in bydim[n]]
        out.append(rank_mod2(cols))
    out.append(0)
    return out


def test_case(name, verts, edges):
    K=faces(verts,edges)
    B=[cubes(K,n) for n in range(4)]
    ranks=[0]
    for n in (1,2,3):
        columns=checksum_boundary(B[n],B[n-1],n)
        ranks.append(rank_mod2(columns))
    sp=simplicial_ranks(K)
    h0,h1=(len(B[n])-ranks[n]-ranks[n+1] for n in (0,1))
    s0,s1=(simplicial_betti(K,n,sp) for n in (0,1))
    assert (h0,h1)==(s0,s1),(name,(h0,h1),(s0,s1))
    for s in K:
        if len(s)>4:continue
        n=len(s)-1
        if n==0:continue
        actual=boundary(corner(s),n)
        expected=defaultdict(int)
        for j in range(n+1):
            v=s[:j]+s[j+1:]
            expected[corner(v)]+=(-1)**j
        expected={k:v for k,v in expected.items() if v}
        assert actual==expected,(s,actual,expected)
    # Check normalized cubical chain contraction for every cube in dimensions 0,1,2
    w=verts[0]
    for n in range(3):
        for c in B[n]:
            def H(z,d):
                q=tuple(list(z)+[w]*(1<<d))
                return {} if is_deg(q,d+1) else {q:(-1)**(d+1)}
            lhs=defaultdict(int)
            for q,coef in H(c,n).items():
                for v,k in boundary(q,n+1).items():lhs[v]+=coef*k
            if n>0:
                for q,coef in boundary(c,n).items():
                    for v,k in H(q,n-1).items():lhs[v]+=coef*k
            rhs={c:1}
            if n==0:
                rhs[w,]=-1 if (w,)!=c else 0
            assert {k:v for k,v in lhs.items() if v}=={k:v for k,v in rhs.items() if v},(name,n,c)
    print(f'{name}: simplices={len(K)} cubes0..3={[len(x) for x in B]}, beta0={h0}, beta1={h1}, rank_d3={ranks[3]} CHAIN_AND_CONE_OK')
    return len(K),sum(map(len,B))


def main():
    cases={
      'four_cycle':(range(4),[(0,1),(1,2),(2,3),(3,0)]),
      'triangle':(range(3),list(combinations(range(3),2))),
      'diamond':(range(4),[(0,1),(0,2),(1,2),(1,3),(2,3)]),
      'three_vertex_path':(range(3),[(0,1),(1,2)]),
      'two_disjoint_edges':(range(4),[(0,1),(2,3)]),
      'four_isolated_vertices':(range(4),[]),
    }
    a=b=0
    for name,(v,e) in cases.items():
        x,y=test_case(name,list(v),e);a+=x;b+=y
    print(f'VERIFY_OK cases={len(cases)} simplices={a} normalized_cubes={b}')
if __name__=='__main__':main()
