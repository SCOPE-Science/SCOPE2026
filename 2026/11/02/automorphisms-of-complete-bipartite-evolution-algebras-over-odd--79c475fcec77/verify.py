"""Finite-field verification of complete-bipartite evolution-algebra automorphisms.

Only prime fields in this checker; the theorem covers all odd finite fields.
No external packages are needed. Each count uses direct Gram and distinguished-vector equations.
"""
from itertools import product
from collections import Counter
from math import gcd

def stabilizer_counts(d,p):
    result=Counter()
    for vals in product(range(p),repeat=d*d):
        M=[vals[i*d:(i+1)*d] for i in range(d)]
        b=sum(M[i][0]*M[i][0] for i in range(d))%p
        if b==0: continue
        if any(sum(M[k][i]*M[k][j] for k in range(d))%p != (b if i==j else 0)
               for i in range(d) for j in range(d)): continue
        row_sums=[sum(row)%p for row in M]
        if len(set(row_sums))!=1 or row_sums[0]==0: continue
        result[(row_sums[0],b)]+=1
    return result

def direct_aut_order(m,n,q,stabs):
    v=sum(c*d for (a,b),c in stabs[m].items()
          for (s,t),d in stabs[n].items() if s==b and t==a)
    return (1+(m==n))*v

def predicted_order(m,n,p):
    # For these checks orthogonal groups have dimensions zero or one.
    assert m in (2,3) and n in (2,3)
    def F(d,a,b):
        if d%p:
            return 2 if b==a*a%p else 0 # |O_1(q)|=2 for d=2
        assert d==3 and p==3
        return p*2 if b in {x*x%p for x in range(1,p)} else 0
    s=sum(F(m,a,b)*F(n,b,a) for a in range(1,p) for b in range(1,p))
    return (1+(m==n))*s

stabs={}
checks=0
for p,dims in [(3,(2,3)),(5,(2,)),(7,(2,))]:
    for d in dims:
        stabs[(p,d)]=stabilizer_counts(d,p)
    for m in dims:
        for n in dims:
            checked=direct_aut_order(m,n,p,{d:stabs[(p,d)] for d in dims})
            predicted=predicted_order(m,n,p)
            assert checked==predicted,(p,m,n,checked,predicted)
            print('q,m,n,aut:',p,m,n,checked)
            checks+=1
print('BIPARTITE_EVOLUTION_AUTOMORPHISMS_OK', checks)
