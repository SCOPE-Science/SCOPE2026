"""Independent finite checks for strict-exchange antiferromagnetic Potts blocking.
Run: python verify.py. Requires SymPy for the symbolic all-q check.
"""
from itertools import product
from collections import deque
import sympy as S


def pattern(values):
    seen = {}
    return tuple(seen.setdefault(x, len(seen)) for x in values)

PATTERNS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 1, 2)]

def permitted(a,b,c,d,anti=True):
    if b == c:
        return True
    delta = (a == c) + (b == d) - (a == b) - (c == d)
    return delta >= 0 if anti else delta <= 0

def full_matrix(q,anti=True):
    triples = list(product(range(q),repeat=3))
    idx = {s:i for i,s in enumerate(triples)}
    edges = [[] for _ in triples]
    for i,(a,b,c) in enumerate(triples):
        for d in range(q):
            if permitted(a,b,c,d,anti): edges[i].append(idx[(b,c,d)])
    return triples,edges

def quotient_from_full(q,anti=True):
    triples,edges=full_matrix(q,anti)
    representatives={p:next(i for i,t in enumerate(triples) if pattern(t)==p) for p in PATTERNS}
    mat=S.zeros(5)
    for i,p in enumerate(PATTERNS):
        for nxt in edges[representatives[p]]:
            mat[i,PATTERNS.index(pattern(triples[nxt]))]+=1
    for v,t in enumerate(triples):
        row=[sum(pattern(triples[j])==p for j in edges[v]) for p in PATTERNS]
        assert row==list(mat[PATTERNS.index(pattern(t)),:])
    return mat

def trace_power(edges,n):
    total=0
    for i in range(len(edges)):
        mass={i:1}
        for _ in range(n):
            new={}
            for v,a in mass.items():
                for j in edges[v]:new[j]=new.get(j,0)+a
            mass=new
        total+=mass.get(i,0)
    return total

def direct_count(q,n,anti=True):
    total=0
    for word in product(range(q),repeat=n):
        count=sum(word[i]==word[(i+1)%n] for i in range(n))
        good=True
        for i in range(n):
            if word[i]==word[(i+1)%n]:continue
            shifted=list(word)
            shifted[i],shifted[(i+1)%n]=shifted[(i+1)%n],shifted[i]
            after=sum(shifted[j]==shifted[(j+1)%n] for j in range(n))
            if (after<count if anti else after>count): good=False;break
        total+=good
    return total

def connected(edges):
    def reach(e,start):
        seen={start};todo=[start]
        for u in todo:
            for v in e[u]:
                if v not in seen:seen.add(v);todo.append(v)
        return len(seen)==len(e)
    reverse=[[] for _ in edges]
    for i,row in enumerate(edges):
        for j in row:reverse[j].append(i)
    return reach(edges,0) and reach(reverse,0)


def run():
    x=S.symbols('x');q=S.symbols('q',integer=True)
    # Symbolic quotients from equality-type combinatorics, in PATTERNS order.
    A=S.Matrix([[1,q-1,0,0,0],[0,0,1,0,0],[0,0,1,1,q-2],
                [1,q-1,0,0,0],[0,0,1,0,q-2]])
    F=S.Matrix([[1,q-1,0,0,0],[0,0,1,1,q-2],[0,0,0,1,0],
                [1,q-1,0,0,0],[0,0,0,1,q-2]])
    pA=x**4-q*x**3+(q-1)*x**2-(q-1)*x+(q-1)*(q-2)
    pF=x**4-(q-1)*x**3-x**2-(q-1)*x+(q-1)*(q-2)
    assert S.expand(A.charpoly(x).as_expr()-x*pA)==0
    assert S.expand(F.charpoly(x).as_expr()-x*pF)==0
    assert S.expand(pA-pF-x*x*(q-x))==0
    for k in range(3,8):
        for anti,symbolic in [(True,A),(False,F)]:
            Q=quotient_from_full(k,anti)
            assert Q==symbolic.subs(q,k)
            triples,edges=full_matrix(k,anti)
            assert connected(edges)
    cases=0
    for k,maxn in [(3,9),(4,7),(5,6)]:
        for anti in (True,False):
            _,edges=full_matrix(k,anti)
            for n in range(4,maxn+1):
                exact=direct_count(k,n,anti)
                calculated=trace_power(edges,n)
                assert exact==calculated,(k,n,anti,exact,calculated)
                cases+=1
    _,ed3=full_matrix(3,True)
    T3=S.zeros(27)
    for i,row in enumerate(ed3):
        for j in row:T3[i,j]=1
    assert S.factor(T3.charpoly(x).as_expr()) == x**13*(x-1)*(x**3-2*x**2-2)*(x**5-x**3-2*x**2-x-3)**2
    seq=[(n,trace_power(ed3,n)) for n in range(4,13)]
    assert seq==[(4,45),(5,123),(6,213),(7,507),(8,1149),(9,2529),(10,5919),(11,13467),(12,31329)]
    print('PASS: symbolic all-q characteristic polynomials, identity and exact q=3 full spectrum')
    print('PASS: quotient lumpability and strong connectivity for both signs and q=3..7')
    print('PASS: %d independent finite energy/transfer count comparisons'%cases)
    print('PASS: q=3 antiferromagnetic finite trace counts:',seq)
if __name__=='__main__':run()
