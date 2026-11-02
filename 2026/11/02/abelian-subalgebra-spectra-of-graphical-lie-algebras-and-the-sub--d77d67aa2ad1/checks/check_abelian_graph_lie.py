#!/usr/bin/env python3
"""Independent finite-field enumerator for abelian subalgebra counts in graph Lie algebras."""
from itertools import combinations, product
from math import prod, comb


def gaussian(n, r, q):
    if r < 0 or r > n:
        return 0
    num = prod(q**(n-i)-1 for i in range(r))
    den = prod(q**(r-i)-1 for i in range(r))
    return num // den


def gl(r, q):
    return prod(q**r-q**i for i in range(r))


def components(n, edges, S):
    left=set(S); count=0
    while left:
        count += 1
        stack=[left.pop()]
        while stack:
            v=stack.pop()
            for w in tuple(left):
                if (min(v,w),max(v,w)) in edges:
                    left.remove(w); stack.append(w)
    return count


def spanning_lines(r,c,q):
    total=0
    for j in range(r+1):
        moebius=(-1)**(r-j)*q**((r-j)*(r-j-1)//2)
        projective=(q**j-1)//(q-1)
        total += gaussian(r,j,q)*moebius*(projective**c)
    return total


def formula_horizontal(n, edges, r, q):
    if r == 0: return 1
    count=0
    for mask in range(1<<n):
        S=[i for i in range(n) if mask&(1<<i)]
        count+=(q-1)**len(S)*spanning_lines(r,components(n,edges,S),q)
    assert count%gl(r,q)==0,(n,edges,r,q,count)
    return count//gl(r,q)


def formula_full(n,edges,d,q):
    z=len(edges)
    return sum(formula_horizontal(n,edges,r,q)*gaussian(z,d-r,q)*q**(r*(z-(d-r)))
               for r in range(max(0,d-z), min(n,d)+1))


def rref_subspaces(n,r,q):
    if r == 0:
        yield []
        return
    for pivots in combinations(range(n),r):
        slots=[(i,j) for i in range(r) for j in range(pivots[i]+1,n) if j not in pivots]
        for values in product(range(q),repeat=len(slots)):
            mat=[[int(j==pivots[i]) for j in range(n)] for i in range(r)]
            for (i,j),v in zip(slots,values):mat[i][j]=v
            yield mat


def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    raw=0
    for i in range(2):
        if b&(1<<i):raw ^= (a<<i)
    if raw&8:raw^=0b1110 # x^3 -> x^2+x, since x^2=x+1
    if raw&4:raw^=0b111  # x^2 -> x+1
    return raw

def sub(a,b,q):
    return a^b if q==4 else (a-b)%q


def abelian_horizontal(mat,edges,q):
    for i in range(len(mat)):
        for j in range(i+1,len(mat)):
            for a,b in edges:
                if sub(mul(mat[i][a],mat[j][b],q),mul(mat[i][b],mat[j][a],q),q):return False
    return True


def abelian_full(mat,n,edges,q):
    return abelian_horizontal([row[:n] for row in mat],edges,q)


def q_eval(n,edges,q,y):
    return sum((q-1)**len(S)*y**components(n,edges,S)
               for mask in range(1<<n)
               for S in [[i for i in range(n) if mask>>i&1]])

def recover_eval_from_horizontal(n,edges,q):
    recovered=[]
    for r in range(n+1):
        total=formula_horizontal(n,edges,r,q)*gl(r,q)
        for j in range(r):
            moebius=(-1)**(r-j)*q**((r-j)*(r-j-1)//2)
            total-=moebius*gaussian(r,j,q)*recovered[j]
        recovered.append(total)
    direct=[q_eval(n,edges,q,(q**j-1)//(q-1)) for j in range(n+1)]
    assert recovered==direct,(n,edges,q,recovered,direct)


def check_graph(n,edges,q,full=False):
    edges=frozenset(tuple(sorted(e)) for e in edges)
    actual=[]
    for r in range(n+1):
        got=sum(abelian_horizontal(M,edges,q) for M in rref_subspaces(n,r,q))
        expected=formula_horizontal(n,edges,r,q)
        assert got==expected,("horizontal",n,edges,q,r,got,expected)
        actual.append(got)
    recover_eval_from_horizontal(n,edges,q)
    if full:
        z=len(edges)
        for d in range(n+z+1):
            got=sum(abelian_full(M,n,edges,q) for M in rref_subspaces(n+z,d,q))
            expected=formula_full(n,edges,d,q)
            assert got==expected,("full",n,edges,q,d,got,expected)
    return actual


def main():
    tests=0
    for n in range(1,5):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if mask>>i&1]
            check_graph(n,edges,2,full=(n<=3))
            tests+=1
    for n,edges in [(3,[(0,1),(1,2)]),(3,[(0,1),(0,2),(1,2)]),
                    (4,[(0,1),(1,2),(2,3)]),(5,[(0,1),(1,2),(2,3),(3,4)])]:
        for q in (3,4):
            check_graph(n,edges,q,full=(n==3 and q==3))
            tests+=1
    # Independent path transfer recurrence, valid at every integer evaluation.
    for q in (2,3,4,5):
        for y in (0,1,2,3,7):
            before,previous=1,1+(q-1)*y
            assert q_eval(0,frozenset(),q,y)==before
            assert q_eval(1,frozenset(),q,y)==previous
            for n in range(2,9):
                now=q*previous-(q-1)*(1-y)*before
                assert now==q_eval(n,frozenset((i,i+1) for i in range(n-1)),q,y)
                before,previous=previous,now
    # Also test odd-characteristic algebra and graph with isolated vertices.
    check_graph(3,[(0,1)],5,full=False);tests+=1
    p5=frozenset((i,i+1) for i in range(4))
    for q in (2,3,4,5,7,9):
        assert formula_horizontal(5,p5,2,q)==4*q*q+q+1
        assert formula_horizontal(5,p5,3,q)==1
    print('GRAPH_LIE_ABELIAN_SUBALGEBRA_CENSUS_OK',tests,
          'all_graphs_upto4_F2','selected_F3_F4_F5','path5_polynomial')
    print('PATH5',[(q,formula_horizontal(5,p5,2,q),formula_full(5,p5,2,q)) for q in (2,3,4)])
    print('TRIANGLE_F2', [formula_full(3,frozenset([(0,1),(0,2),(1,2)]),d,2) for d in range(7)])

if __name__=='__main__':main()
