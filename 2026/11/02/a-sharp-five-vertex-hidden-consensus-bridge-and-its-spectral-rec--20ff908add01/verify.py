"""Exact-rational checks for an adaptive-confidence averaging example.

This checker complements, but does not replace, the analytic proof.
Python >=3.9; standard library only.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

EDGE_LIST = ((0,1), (1,2), (2,3), (3,4))
X0 = (F(3,10), F(0), F(1,5), F(2,5), F(3,5))
C0 = F(1,4)
GAMMA = F(1,2)


def step(x, c, delta):
    active = {e for e in EDGE_LIST if abs(x[e[0]]-x[e[1]]) < c[e]}
    neighbors = [{i} for i in range(5)]
    for i,j in active:
        neighbors[i].add(j)
        neighbors[j].add(i)
    xp = tuple(sum((x[j] for j in neighbors[i]), F(0))/len(neighbors[i]) for i in range(5))
    cp = {e: c[e]+GAMMA*(1-c[e]) if e in active else delta*c[e] for e in EDGE_LIST}
    return xp, cp, active


def recurrence(N):
    a,b=F(3,10),F(1,10)
    for t in range(N):
        yield t,a,b
        a,b=(a+b)/2,a/3


def test(delta, N, expected_first):
    x=X0; c={e:C0 for e in EDGE_LIST}; first=None
    expected=list(recurrence(N))
    for t,a,b in expected:
        xp, cp, active=step(x,c,delta)
        if first is None:
            assert x[0]==F(3,10) and x[1]==F(3,10)-a
            assert x[2]==F(3,10)-b and x[3]==F(3,10)+b and x[4]==F(3,10)+a
            assert all(e in active for e in EDGE_LIST[1:])
            if (0,1) in active:
                first=t
        if first is None:
            assert c[(0,1)]==C0*delta**t
            assert (a < C0*delta**t)==((0,1) in active)
        x,c=xp,cp
    assert first==expected_first,(delta,first,expected_first)
    return f'delta={delta}, first-receptive={first}, time-steps={N}'


def run():
    assert abs(X0[0]-X0[1])>C0
    for i,j in EDGE_LIST[1:]:
        assert abs(X0[i]-X0[j])<C0
    print(test(F(1,2), 60, None))
    print(test(F(7,10), 60, None))
    print(test(F(3,4), 20, 5))
    print(test(F(4,5), 20, 2))
    print(test(F(9,10), 20, 1))
    # Decay/average predictions for the never-receptive dynamics, exact rational.
    arr=list(recurrence(61))
    for t,a,b in arr:
        assert 0<=b<=F(1,10) and b<=a<=F(3,10)
        assert a-b<C0 and 2*b<C0
        if t>0:
            assert a==F(1,2)*arr[t-1][1]+F(1,2)*arr[t-1][2]
            assert b==arr[t-1][1]/3
        if t>=2:
            assert a==arr[t-1][1]/2 + arr[t-2][1]/6
    # Verify the 4-path stationary averaging weights give the isolated opinion.
    assert (2*X0[1]+3*X0[2]+3*X0[3]+2*X0[4])/10==X0[0]
    getcontext().prec=60
    lam=(Decimal(3)+Decimal(33).sqrt())/Decimal(12)
    nu=(Decimal(3)-Decimal(33).sqrt())/Decimal(12)
    A=Decimal(3)/20+Decimal(33).sqrt()/44
    B=Decimal(3)/20-Decimal(33).sqrt()/44
    assert 0<lam<1 and -1<nu<0 and A>Decimal(1)/4 and B>0
    assert abs(lam*lam-lam/2-Decimal(1)/6)<Decimal('1e-55')
    for t,a,b in arr:
        at=Decimal(a.numerator)/Decimal(a.denominator)
        assert abs(at-A*lam**t-B*nu**t)<Decimal('1e-53')
        assert at>Decimal(1)/4*lam**t
        assert at<=Decimal(3)/10*lam**t+Decimal('1e-55')
    print('PASS: 61 recurrence states and eigenvalue decomposition')
    print('lambda=',lam)
    print('asymptotic amplitude A=',A)
    print('PASS')

if __name__=='__main__':
    run()
