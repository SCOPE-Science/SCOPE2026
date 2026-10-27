"""Standalone finite-field verification of commutator coordinate/matroid identities.
Run: python3 check_commutator_matroid.py
No dependencies beyond Python's standard library.
"""
from itertools import product,combinations
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q in (2,4) else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        raw=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):raw^=1<<(i+j)
        if raw&8:raw^=0b1110  # not reached for degree<=2
        if raw&4:raw^=0b111  # x^2=x+1
        return raw
    def sub(self,a,b):return self.add(a,self.neg(b))

def mul_alg(x,y,edges,field,n):
    out=[field.mul(x[v],y[v]) for v in range(n)]
    for j,(s,t) in enumerate(edges):
        out.append(field.add(field.mul(x[s],y[n+j]),field.mul(x[n+j],y[t])))
    return tuple(out)

def component_count(n,edges,selected):
    parent=list(range(n))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for j in selected:
        a,b=edges[j]
        ra,rb=root(a),root(b)
        if ra!=rb:parent[ra]=rb
    return len(set(root(v) for v in range(n)))

def predicted_fiber(q,edges,n,support):
    # Independent counting via FK expansion and proper colorings of contractions.
    m=len(edges)
    zero=[i for i in range(m) if i not in support]
    Q=q*q
    value=0
    for choices in product((0,1),repeat=len(zero)):
        a=[zero[k] for k,b in enumerate(choices) if b]
        p=list(range(n))
        def rt(v):
            while p[v]!=v:v=p[v]
            return v
        for j in a:
            s,t=edges[j];s,t=rt(s),rt(t)
            if s!=t:p[s]=t
        blocks=sorted(set(rt(v) for v in range(n)))
        idx={v:i for i,v in enumerate(blocks)}
        cpairs=[(idx[rt(edges[j][0])],idx[rt(edges[j][1])]) for j in support]
        if any(a==b for a,b in cpairs):continue
        c=0
        for coloring in product(range(Q),repeat=len(blocks)):
            if all(coloring[a]!=coloring[b] for a,b in cpairs):c+=1
        value+=(q-1)**len(a)*c
    return q**m*value

def test(q,n,edges):
    fld=Field(q);m=len(edges)
    if not all(s!=t for s,t in edges):raise AssertionError('loops excluded')
    if any(t==a for s,t in edges for a,b in edges):
        raise AssertionError('oriented paths of length two forbidden')
    elems=list(product(range(q),repeat=n+m))
    fibers=Counter()
    for x in elems:
        for y in elems:
            xy=mul_alg(x,y,edges,fld,n)
            yx=mul_alg(y,x,edges,fld,n)
            comm=tuple(fld.sub(xy[n+j],yx[n+j]) for j in range(m))
            assert all(fld.sub(xy[j],yx[j])==0 for j in range(n))
            fibers[comm]+=1
    assert sum(fibers.values())==q**(2*(n+m))
    for c in product(range(q),repeat=m):
        S=frozenset(j for j in range(m) if c[j])
        expect=predicted_fiber(q,edges,n,S)
        assert fibers[c]==expect,(q,n,edges,c,fibers[c],expect)
    # Every subset of coordinates: joint independence iff its graph is a forest.
    Q=q*q
    p0=(q*q*q+q*q-q)/q**4
    p1=(q*q*q-q)/q**4
    for k in range(m+1):
      for J in combinations(range(m),k):
        # independence is equivalent to zero-event equality, and for forests follows
        # from independence of the incidence gradients.
        independent=component_count(n,edges,J)==n-k
        pairs=sum(v for c,v in fibers.items() if all(c[j]==0 for j in J))
        # exact rational comparison
        numerator=(q**3+q**2-q)**k*q**(4*m-4*k)
        denom=q**(4*m)
        # instead compare probabilities to p0^k with integers
        is_equal=(pairs*(q**4)**k == (q**(2*(n+m)))*(q**3+q**2-q)**k)
        assert is_equal==independent,(q,n,edges,J,is_equal,independent)
    return (q,n,len(edges),len(elems),len(elems)**2)

cases=[
 (2,2,[(0,1)]),
 (2,2,[(0,1),(0,1)]),
 (2,2,[(0,1),(0,1),(0,1)]),
 (2,3,[(0,1),(2,1)]),
 (2,3,[(0,1),(0,1),(2,1)]),
 (2,4,[(0,1),(2,1),(2,3)]),
 (2,4,[(0,1),(0,2),(0,3)]),
 (2,4,[(0,2),(0,3),(1,2),(1,3)]),
 (2,4,[(0,1),(2,3)]),
 (3,2,[(0,1)]),
 (3,3,[(0,1),(2,1)]),
 (4,2,[(0,1)]),
 (4,2,[(0,1),(0,1)]),
]
if __name__=='__main__':
   total=0
   for q,n,edges in cases:
       result=test(q,n,edges)
       total+=result[-1]
       print('PASS',*result)
   print('ALL_GRAPH_COMMUTATOR_CHECKS_PASSED',len(cases),total)
