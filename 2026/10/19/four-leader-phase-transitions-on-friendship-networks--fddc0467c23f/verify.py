"""Exact checks for four-leader placement on friendship graphs.
Run with Python 3 and SymPy >= 1.12: python verify.py.
The infinite-size assertions are symbolic polynomial identities;
finite inverse checks independently test the block derivation.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp
m,k=sp.symbols('m k',integer=True,positive=True)

def Bdata(t):
    B=sp.Matrix([[2+k*int(t>0),-1],[-1,2+k*int(t==2)]])
    U=B.inv()
    v=U*sp.ones(2,1)
    return (sp.factor(sp.trace(U)),sp.factor(sum(v)),sp.factor((v.T*v)[0]))

data=[Bdata(t) for t in range(3)]

def T(h,singles,pairs):
    ns=[m-singles-pairs,singles,pairs]
    assert sum(ns)==m
    D=2*m+k*h-sum(ns[t]*data[t][1] for t in range(3))
    return sp.factor(sum(ns[t]*data[t][0] for t in range(3))+
              (1+sum(ns[t]*data[t][2] for t in range(3)))/D)

H=T(1,3,0)
Hp=T(1,1,1)
Q=T(0,4,0)
Qp=T(0,2,1)
Qpp=T(0,0,2)

identities={
 'hub_cluster_penalty': (Hp-H,
 (4*k**5+78*k**4+(24*m+465)*k**3+(144*m+1053)*k**2+(270*m+729)*k+162*m+81)/
 (6*(k+3)*(k+6)*(2*k+3)*(k**2+6*k+6))),
 'one_leaf_cluster_penalty':(Qp-Q,
 ( (8*m+52)*k**3+(48*m+252)*k**2+(90*m+189)*k+54*m+27 )/
 (12*(k+3)*(2*k+3)*(5*k+6))),
 'two_leaf_cluster_penalty':(Qpp-Q,
 ((4*m+22)*k**3+(22*m+103)*k**2+(36*m+66)*k+18*m+9)/
 (12*(k+1)*(k+3)*(2*k+3))),
 'hub_leaf_switch':(Q-H,
 ((8*m-44)*k**2+(24*m-222)*k+18*m-99)/
 (12*(k+6)*(2*k+3))),
 'm2_leaf_superiority':((Qpp-Hp).subs(m,2),
 -(k**4+11*k**3+33*k**2+37*k+6)/(4*(k+1)*(k+3)*(k**2+6*k+6))),
 'm3_pair_distribution':((Qpp-Qp).subs(m,3),
 (94*k**4+577*k**3+1029*k**2+711*k+189)/
 (12*(k+1)*(k+3)*(2*k+3)*(5*k+6))),
 'm3_transition':((Qp-H).subs(m,3),
 -(4*k**4+53*k**3+150*k**2+117*k-54)/
 (2*(k+3)*(k+6)*(2*k+3)*(5*k+6))),
}
for name,(left,right) in identities.items():
    assert sp.cancel(left-right)==0,name

assert sp.cancel((Q-H).subs(m,6)-(4*k*k-78*k+9)/(12*(k+6)*(2*k+3)))==0
assert sp.cancel((Q-H).subs(m,7)-(4*k*k-18*k+9)/(4*(k+6)*(2*k+3)))==0
assert sp.expand(((8*m-44)*k*k+(24*m-222)*k+18*m-99).subs(m,8)) == 20*k*k-30*k+45
assert (sp.Rational(9,4)-((39-3*sp.sqrt(165))/4)*((39+3*sp.sqrt(165))/4)).simplify()==0
assert (sp.Rational(9,4)-((9-3*sp.sqrt(5))/4)*((9+3*sp.sqrt(5))/4)).simplify()==0
q3=4*k**4+53*k**3+150*k**2+117*k-54
assert q3.subs(k,sp.Rational(3,10))<0 and q3.subs(k,sp.Rational(1,3))>0

def inv_trace(M):
    size=len(M); a=[[F(v) for v in row]+[F(i==j) for j in range(size)] for i,row in enumerate(M)]
    for i in range(size):
        p=next(r for r in range(i,size) if a[r][i]!=0)
        a[i],a[p]=a[p],a[i]
        scale=a[i][i]
        a[i]=[v/scale for v in a[i]]
        for j in range(size):
            if j!=i:
                v=a[j][i]
                if v: a[j]=[x-v*y for x,y in zip(a[j],a[i])]
    return sum(a[i][size+i] for i in range(size))

def graph(mv):
    n=2*mv+1; A=[[0]*n for _ in range(n)]
    for b in range(mv):
        u=2*b+1;v=u+1
        for i,j in [(0,u),(0,v),(u,v)]:
            A[i][j]=A[j][i]=1
    return A

def direct(mv,leads,gain):
    A=graph(mv); n=len(A); return inv_trace([[F(sum(A[i]))+F(gain)*(i in leads) if i==j else -F(A[i][j]) for j in range(n)] for i in range(n)])

def profile(leads,mv):
    h=int(0 in leads)
    nums=[sum((2*b+1 in leads,2*b+2 in leads)) for b in range(mv)]
    return h,nums.count(1),nums.count(2)

check=0
for mv in range(2,6):
    opts=list(combinations(range(2*mv+1),4))
    gains=[F(1,7),F(1),F(3),F(25)]
    for gain in gains:
        known={}
        for leads in opts:
            p=profile(leads,mv)
            if p not in known:
                known[p]=direct(mv,leads,gain)
                predicted=F(sp.cancel(T(*p).subs({m:mv,k:sp.Rational(gain.numerator,gain.denominator)})))
                assert known[p]==predicted,(mv,leads,gain,p)
            else:
                # independent direct check even in the same graph orbit
                assert known[p]==direct(mv,leads,gain),(mv,leads,gain)
            check+=1
        winner=min(known.values())
        if mv==2:
            assert min(known,key=known.get)==(0,0,2)
        if mv==3:
            expected=(1,3,0) if gain<F(3,10) else (0,2,1)
            assert min(known,key=known.get)==expected
        if mv in (4,5):assert min(known,key=known.get)==(0,4,0)

# Symbolic sign identities, coupled with Descartes' rule, certify the
# all-gain sign phase diagram; this loop also checks representative phases.
for mv in [6,7,8,9,12,25]:
    for gain in [sp.Rational(1,100),sp.Rational(1,2),sp.Rational(1),sp.Rational(3),sp.Rational(5),sp.Rational(100)]:
        vals={z:sp.cancel(T(*p).subs({m:mv,k:gain})) for z,p in
              {'H':(1,3,0),'Hp':(1,1,1),'Q':(0,4,0),'Qp':(0,2,1),'Qpp':(0,0,2)}.items()}
        best=min(vals.values());assert best==min(vals['H'],vals['Q'])
print('VERIFY_OK symbolic_identities=%d exhaustive_direct_inverse_comparisons=%d large_graph_sample_checks=%d' % (len(identities),check,6*6))
