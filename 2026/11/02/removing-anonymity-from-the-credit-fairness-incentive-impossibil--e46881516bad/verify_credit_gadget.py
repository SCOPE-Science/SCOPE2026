"""Exact-rational sanity checks for a two-history credit-fairness obstruction.

Only rational test points are enumerated; the universal claim is proved in RESULT.md.
No external packages or data files are required.
"""
from fractions import Fraction as F

A = ((1,2,0,0,3),(3,0,1,1,2),(0,2,2,2,0))
B = ((0,2,2,2,0),(3,0,1,1,2),(1,2,0,0,3))
AT = ((1,1,0,0,2),(2,0,1,1,1),(0,2,2,2,0))
BT = ((0,2,2,2,0),(2,0,1,1,1),(1,1,0,0,2))


def col(rows, t): return [F(row[t]) for row in rows]


def verify_cf_and_pe(demands, allocations):
    """Directly test five published credit-fairness axioms in the E=3,e_i=1 case."""
    c = [F(0)]*3
    for t in range(5):
        d = col(demands,t)
        a = col(allocations,t)
        assert all(z>=0 for z in a)
        assert sum(a)==3
        u = [min(d[i],a[i]) for i in range(3)]
        if any(a[i]<d[i] for i in range(3)):
            assert sum(u)==3, ('PE',t,d,a)
        dc = [F(1)-a[i] for i in range(3)]
        for i in range(3):
            target = F(1)-u[i]
            assert min(F(0),target) <=dc[i]<=max(F(0),target), ('CF1',t,i)
            others=sum(u)-u[i]
            if others>2:
                assert dc[i]>=others-2, ('CF2',t,i)
            assert a[i]>=min(d[i],F(1)+min(F(0),c[i])), ('CF4',t,i,c)
        assert sum(dc)<=0, ('CF3',t)
        if any(a[j]>max(F(0),F(1)+c[j]) for j in range(3)):
            for i in range(3):
                assert a[i]>=d[i] or a[i]>=F(1)+c[i], ('CF5',t,i,c,a,d)
        c=[c[i]+dc[i] for i in range(3)]
    return c


def deviation(which,x):
    if which=='A':
        reported=[list(row) for row in A]
        reported[0][0]=0
        allocations=((0,x,0,0,3),(3,0,1,1,0),(0,3-x,2,2,0))
    else:
        reported=[list(row) for row in B]
        reported[2][0]=0
        allocations=((0,x,2,2,0),(3,0,1,1,0),(0,3-x,0,0,3))
    return reported,allocations


def sum_utility(actual, alloc,agent):
    return sum(min(F(actual[agent][t]),F(alloc[agent][t])) for t in range(5))

assert verify_cf_and_pe(A,AT)==[F(1),F(0),F(-1)]
assert verify_cf_and_pe(B,BT)==[F(-1),F(0),F(1)]
assert sum_utility(A,AT,0)==4
assert sum_utility(B,BT,2)==4
number=0
for k in range(101):
    x=F(1)+F(k,100)
    da,aa=deviation('A',x)
    db,ab=deviation('B',x)
    assert [F(v) for v in col(da,0)]==[F(v) for v in col(db,0)]
    assert col(da,1)==col(db,1)
    assert col(aa,1)==col(ab,1)
    verify_cf_and_pe(da,aa)
    verify_cf_and_pe(db,ab)
    gain_A=sum_utility(A,aa,0)-4
    gain_B=sum_utility(B,ab,2)-4
    assert gain_A==x-1 and gain_B==2-x
    assert gain_A+gain_B==1 and max(gain_A,gain_B)>=F(1,2)
    number+=1

# Independent discrete feasibility check for both truthful second and final rounds.
# Each candidate allocation is a 1/10 lattice point, not a substitute for proof.
from itertools import product

def one_round_check(d,a,c):
    d=list(map(F,d)); a=list(map(F,a)); c=list(map(F,c))
    if sum(a)!=3 or any(a[i]<0 or a[i]>d[i] for i in range(3)):
        return False
    for i in range(3):
        if a[i]<min(d[i],1+min(F(0),c[i])): return False
    if any(a[j]>max(F(0),1+c[j]) for j in range(3)):
        if any(not(a[i]>=d[i] or a[i]>=1+c[i]) for i in range(3)):
            return False
    return True

sizes=[]
for d,c,expected in [((2,0,2),(0,-1,1),(1,0,2)),((3,2,0),(2,0,-2),(2,1,0)),((2,0,2),(1,-2,1),None)]:
    feasible=[]
    for a1 in range(31):
        for a2 in range(31-a1):
            ar=(F(a1,10),F(a2,10),F(30-a1-a2,10))
            if one_round_check(d,ar,c):feasible.append(ar)
    if expected:
        assert feasible==[tuple(map(F,expected))],(d,c,feasible)
    else:
        assert feasible and all(F(1)<=a[0]<=F(2) and a[1]==0 for a in feasible)
    sizes.append(len(feasible))

print(f'VERIFY_OK rational_split_points={number} truthful_round_feasible={sizes[:2]} altered_round_feasible={sizes[2]} max_min_gain=1/2')
