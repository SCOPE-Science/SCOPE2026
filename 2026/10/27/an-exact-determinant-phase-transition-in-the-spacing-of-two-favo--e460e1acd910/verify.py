"""Exact checks of the seasonal two-stage matrix spacing theorem (stdlib only)."""
from fractions import Fraction as Q
from itertools import product

def mm(x,y):
    return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def mpow(x,n):
    z=((Q(1),Q(0)),(Q(0),Q(1)))
    for _ in range(n):z=mm(z,x)
    return z

def tr(x):return x[0][0]+x[1][1]

def check(r,b,c,d,delta,n):
    B=((r,b),(c,d));A=((r+delta,b),(c,d))
    assert r>=0 and d>=0 and r+d>0 and b>0 and c>0 and delta>0
    det=r*d-b*c
    vals=[]
    for k in range(1,n):
        P=mm(mm(A,mpow(B,k-1)),mm(A,mpow(B,n-k-1)))
        predicted=tr(mpow(B,n))+2*delta*mpow(B,n-1)[0][0]+delta*delta*mpow(B,k-1)[0][0]*mpow(B,n-k-1)[0][0]
        assert tr(P)==predicted,(r,b,c,d,delta,n,k)
        vals.append(tr(P))
    assert vals==vals[::-1]
    assert vals[0]==max(vals) and all(vals[0]>v for v in vals[1:-1])
    minimum=min(vals)
    if det>0:
        targets={n//2-1} if n%2==0 else {(n-1)//2-1,(n+1)//2-1}
    elif det==0:targets=set(range(1,n-2))
    else:targets={1,n-3}
    assert {i for i,v in enumerate(vals) if v==minimum}==targets,(n,det,vals,targets)
    return n-1

cases=[]
for r,d in [(Q(0),Q(1,3)),(Q(1,3),Q(0)),(Q(1,4),Q(1,2)),(Q(3,5),Q(3,5)),(Q(1,5),Q(1,5))]:
    for b,c in [(Q(1,5),Q(1,5)),(Q(1,2),Q(1,2)),(Q(3,5),Q(3,5))]:
        if r+d>0:cases.append((r,b,c,d,Q(2,5)))
# Determinant exactly zero with positive entries
cases.extend([(Q(1,2),Q(1,2),Q(1,2),Q(1,2),Q(1,3)),
              (Q(1,3),Q(2,3),Q(1,3),Q(2,3),Q(1,4))])
checked=0
for n in range(4,17):
    for x in cases:checked+=check(*x,n)
# Four exact identities in the sharp six-year case.
for r,b,c,d,delta in cases:
    B=((r,b),(c,d));A=((r+delta,b),(c,d))
    t=[tr(mm(mm(A,mpow(B,k-1)),mm(A,mpow(B,5-k)))) for k in (1,2,3)]
    assert t[0]-t[1]==b*c*delta**2*(b*c+d*d+d*r+r*r)
    assert t[0]-t[2]==b*c*delta**2*(r+d)**2
    assert t[1]-t[2]==b*c*delta**2*(r*d-b*c)
print('PASS: exact traces, reflections, ordering and six-year identities')
print('Cases:',len(cases),'period lengths:',13,'exact schedule traces checked:',checked)
