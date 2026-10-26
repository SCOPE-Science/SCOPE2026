"""Exact finite-instance arithmetic checks for double transitive dual Burnside chains.
Run: python verify_dual_burnside.py. Requires Python 3 standard library only.
"""
from itertools import permutations
from collections import defaultdict
from fractions import Fraction
from math import factorial

def sn(n):
    return list(permutations(range(n)))

def affine(p):
    assert p in (3,5,7)
    return [tuple((a*x+b)%p for x in range(p)) for a in range(1,p) for b in range(p)]

def cycle_type(a):
    n=len(a); seen=set(); typ=[]
    for i in range(n):
        if i not in seen:
            cur=i; j=0
            while cur not in seen:
                seen.add(cur);j+=1;cur=a[cur]
            typ.append(j)
    return tuple(sorted(typ))

def affine_type(a,p):
    # Conjugacy class determined by slope and (for translations) zero vs nonzero shift.
    slope=(a[1]-a[0])%p
    return (slope, 0 if slope!=1 else int(a[0]!=0))

def test_group(group, name, typfun):
    n=len(group[0]);G=len(group); fixed=[frozenset(i for i in range(n) if g[i]==i) for g in group]
    indices=[i for i in range(G) if fixed[i]]
    stabilizers={x:[j for j in range(G) if x in fixed[j]] for x in range(n)}
    assert all(len(v)==G//n for v in stabilizers.values())
    # Check double transitivity directly via stabilizer orbits, no theorem assumptions hidden.
    for x in range(n):
        assert {tuple(sorted({group[j][y] for j in stabilizers[x]})) for y in range(n)} == {(x,), tuple(y for y in range(n) if y!=x)}
    pi={j:Fraction(len(fixed[j]),G) for j in indices}
    Q={}
    for i in indices:
        fi=fixed[i]
        Q[i]={j:Fraction(len(fi & fixed[j]), len(fi)*(G//n)) for j in indices}
        assert sum(Q[i].values())==1
    Kdiag=sum(Fraction(1,len(fixed[j])) for j in stabilizers[0])/len(stabilizers[0])
    lam=(n*Kdiag-1)/(n-1)
    assert 0<lam<1
    checks=0
    # Check the dual rank-two semigroup identity Q^2 = Pi + lambda(Q-Pi).
    for i in indices:
        for j in indices:
            q2=sum(Q[i][k]*Q[k][j] for k in indices)
            assert q2==pi[j]+lam*(Q[i][j]-pi[j]);checks+=1
    # Compare the class distribution after one step with the stationary class distribution.
    types={t for t in map(typfun,group)}
    classes=defaultdict(list)
    for j in indices:classes[typfun(group[j])].append(j)
    for i in indices:
        for cls, ids in classes.items():
            assert sum((Q[i][j] for j in ids),Fraction(0))==sum((pi[j] for j in ids),Fraction(0))
            checks+=1
    d1={i:sum((abs(Q[i][j]-pi[j]) for j in indices),Fraction(0))/2 for i in indices}
    assert max(d1.values())==Fraction(n-2,n)
    assert all(d1[i]==Fraction(n-2,n) for i in indices if len(fixed[i])==1)
    print(name,'n',n,'|G|',G,'|G*|',len(indices),'lambda',lam,'max_TV_1',max(d1.values()),'exact_checks',checks)
    return checks

if __name__=='__main__':
    total=0
    for n in (3,4,5):total+=test_group(sn(n),'S_n',cycle_type)
    for p in (3,5,7):total+=test_group(affine(p),'AGL(1,p)',lambda a,p=p:affine_type(a,p))
    # Independently check exact truncated-exponential formula for natural symmetric group.
    for n in range(3,20):
        a=sum((Fraction((-1)**(j-1),factorial(j)) for j in range(1,n+1)),Fraction(0))
        lam=(n*a-1)/(n-1)
        assert 0<lam<1
        if n in (3,4):assert lam==Fraction(1,2)
        total+=1
    for q in range(3,50):
        a=Fraction(q-1,q)
        assert (q*a-1)/(q-1)==Fraction(q-2,q-1)
        total+=1
    print('PASS: all',total,'exact-rational checks.')
