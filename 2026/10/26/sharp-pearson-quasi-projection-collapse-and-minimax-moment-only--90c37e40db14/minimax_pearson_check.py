"""Exact-rational checks for a three-state Pearson projection and minimax regret theorem.
Run: python minimax_pearson_check.py
Only finite identities and parameter-sample inequalities are tested; general theorems use the written proof.
"""
from fractions import Fraction as F


def dist(m, s):
    return ((s-m)/2, 1-s, (s+m)/2)


def model(t):
    return (F(1,3)-t, F(1,3), F(1,3)+t)


def div(p, q):
    return (sum((x-y)**2/y for x,y in zip(p,q)))/2


def oracle(m, s):
    return m/(3*s)


def loss(m,s,t):
    p=dist(m,s)
    return div(p,model(t))-div(p,model(oracle(m,s)))


def minimax_param(m):
    return 2*m/(3*(1+m))


def minimax_value(m):
    return 3*m*m*(1-m)/(4*(1+3*m))


def test():
    checked=0
    for den in range(5,31):
        for j in range(1,den):
            m=F(j,den)
            if m >= F(2,3):
                continue
            tmin=minimax_param(m)
            assert 0<tmin<F(1,3)
            assert minimax_value(m) < F(3,4)*m*m
            for l in range(j+1,den):
                s=F(l,den)
                assert m<s<1
                p=dist(m,s)
                assert all(x>0 for x in p)
                t_oracle=oracle(m,s)
                t_moment=m/2
                assert 0<t_oracle<F(1,3)
                assert 0<t_moment<F(1,3)
                dmin=div(p,model(t_oracle))
                dmm=div(p,model(t_moment))
                assert dmin == (3*(1-s)-1)**2/4
                assert dmm == ((4-6*m*m)/(4-9*m*m))*dmin
                assert loss(m,s,tmin) == 3*(m-3*s*tmin)**2/(4*(1-9*tmin*tmin))
                assert loss(m,s,tmin) <= minimax_value(m)
                # Every sampled competitor has worst-case boundary loss at least the exact minimax value.
                for gridnum in range(-9,10):
                    t=F(gridnum,30)
                    b1=F(3,4)*(m-3*m*t)**2/(1-9*t*t)
                    b2=F(3,4)*(m-3*t)**2/(1-9*t*t)
                    assert max(b1,b2)>=minimax_value(m)
                checked+=1
    for m in [F(1,12),F(1,3),F(1,2),F(3,5),F(13,20)]:
        if m>=F(2,3): continue
        t=minimax_param(m)
        b1=F(3,4)*(m-3*m*t)**2/(1-9*t*t)
        b2=F(3,4)*(m-3*t)**2/(1-9*t*t)
        assert b1==b2==minimax_value(m)
    print('PASS: exact rational parameter instances =', checked)
    print('PASS: projection/divergence/ratio identities and bounded minimax regret')
    print('Analytic proofs, not this finite check, establish all real-parameter claims.')


if __name__=='__main__':
    test()
