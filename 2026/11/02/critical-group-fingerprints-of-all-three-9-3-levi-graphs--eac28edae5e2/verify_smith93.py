"""Exact integer Laplacian/Smith verification for the three (9_3) Levi graphs.
Run: python -m pip install sympy; python verify_smith93.py
No floating-point arithmetic is used.
"""
from sympy import Matrix, ZZ, factorint
from sympy.matrices.normalforms import smith_normal_form
from math import prod

DESIGNS = {
 27: [[0,3,6],[1,4,7],[2,5,8],[0,4,8],[1,5,6],[2,3,7],[0,5,7],[1,3,8],[2,4,6]],
 29: [[2,4,7],[1,4,8],[3,6,7],[3,5,8],[0,2,5],[1,5,7],[0,6,8],[1,2,6],[0,3,4]],
 30: [[0,1,8],[1,3,6],[5,6,8],[2,3,8],[2,5,7],[3,4,5],[1,4,7],[0,6,7],[0,2,4]],
}
EXPECTED = {
 27: ([2,6,6,18,18,54],1259712,{2:6,3:9}),
 29: ([2,6,48,2160],1244160,{2:10,3:5,5:1}),
 30: ([214,5778],1236492,{2:2,3:3,107:2}),
}

def evaluate(lines):
    assert len(lines)==9
    counts=[0]*9
    pairset=set()
    adj=[set() for _ in range(18)]
    for j,line in enumerate(lines):
        assert len(set(line))==3 and all(0<=p<9 for p in line)
        for p in line:
            counts[p]+=1; adj[p].add(9+j); adj[9+j].add(p)
        for a in line:
            for b in line:
                if a<b:
                    assert (a,b) not in pairset
                    pairset.add((a,b))
    assert counts==[3]*9 and all(len(nei)==3 for nei in adj)
    visited={0}; todo=[0]
    while todo:
        for nxt in adj[todo.pop()]:
            if nxt not in visited:
                visited.add(nxt);todo.append(nxt)
    assert len(visited)==18
    triangles=sum((a,b) in pairset and (a,c) in pairset and (b,c) in pairset
                  for a in range(9) for b in range(a+1,9) for c in range(b+1,9))
    L=Matrix(18,18,lambda i,j:(3 if i==j else -1 if j in adj[i] else 0))
    assert L==L.T and all(sum(L.row(i))==0 for i in range(18))
    red=L[:17,:17]
    factors=[abs(int(d)) for d in smith_normal_form(red,domain=ZZ).diagonal()]
    assert all(q>0 for q in factors) and all(b%a==0 for a,b in zip(factors,factors[1:]))
    det=red.det(method='bareiss')
    assert det>0 and prod(factors)==det
    return triangles,factors,int(det)

if __name__=='__main__':
    for t,lines in DESIGNS.items():
        real_t,factors,det=evaluate(lines)
        ef,ed,prime=EXPECTED[t]
        assert real_t==t and [x for x in factors if x>1]==ef and det==ed
        assert factorint(det)==prime
        print('SMITH_PASS', 'point_triangles='+str(t),'invariant_factors='+str(ef),
              'spanning_trees='+str(det),'prime_factorization='+str(prime))
    print('THREE_CONFIGURATIONS_EXACT_SANDPILE_PASS')
