"""Exact rational verification of negative-bias max-plus reset formulas.

Run with Python 3, no third-party dependencies. Finite tests supplement an analytic proof.
"""
from fractions import Fraction as Q


def xy_map(x, y, eps, t, d):
    return (y + max(Q(0), t*x), -eps - max(Q(0), d*x))


def seeded_sequences(u, v, t, d, length):
    U=[u,t*u+v]
    h=[Q(0),Q(0)]
    for _ in range(2,length):
        U.append(t*U[-1]-d*U[-2])
        h.append(t*h[-1]-d*h[-2]+1)
    return U,h


def trial(u,v,t,d,eps,limit=20000):
    U,h=seeded_sequences(u,v,t,d,limit+1)
    x,y=u,v
    hit=None
    for n in range(limit+1):
        if hit is None:
            assert x == U[n]-eps*h[n], (n,x,U[n],h[n])
        if n>=1 and x<=0 and hit is None:
            hit=n
            assert y < 0
            x,y=xy_map(x,y,eps,t,d)
            assert x<0 and y==-eps
            x,y=xy_map(x,y,eps,t,d)
            assert x==y==-eps
            return hit
        x,y=xy_map(x,y,eps,t,d)
    raise AssertionError('No crossing in finite test range')


def main():
    cases=[(Q(9,10), Q(3,10)),(Q(1),Q(1,4)),(Q(11,10),Q(6,25))]
    initials=[(Q(1),Q(1)),(Q(2,3),Q(1,5)),(Q(7,3),Q(0))]
    count=0
    examples=[]
    for t,d in cases:
        delta=1-t+d
        assert d>0 and d<1 and t>0 and t<1+d
        for u,v in initials:
            U,h=seeded_sequences(u,v,t,d,320)
            for k in range(2,319):
                assert h[k] == t*h[k-1]-d*h[k-2]+1
            for p in (2,4,6,8):
                eps=Q(1,10**p)
                tau=trial(u,v,t,d,eps,limit=450)
                assert tau>=2
                assert U[tau]-eps*h[tau] <= 0
                assert all(U[j]-eps*h[j]>0 for j in range(tau))
                examples.append((str(t),str(d),str(u),str(v),p,tau))
                count+=1
            if t*t >=4*d:
                assert all(h[k+1]>h[k] for k in range(1,200))
                assert all(U[k]>0 for k in range(300))
                # The first crossing is ultimately governed by decreasing exact thresholds.
                ratios=[U[k]/h[k] for k in range(20,180)]
                assert all(ratios[k+1]<ratios[k] for k in range(len(ratios)-1))
                if t*t==4*d:
                    r=Q(1,2)
                    for n in range(1,100):
                        assert U[n] == (u+n*(u+v/r))*r**n
                        C=(1+n*(1/r-1))*r**n
                        assert h[n] == (1-C)/delta
                else:
                    lp,lm=Q(4,5),Q(3,10)
                    assert t==lp+lm and d==lp*lm
                    for n in range(1,100):
                        f=((lp*u+v)*lp**n-(lm*u+v)*lm**n)/(lp-lm)
                        C=((1-lm)*lp**n-(1-lp)*lm**n)/(lp-lm)
                        assert U[n]==f
                        assert h[n]==(1-C)/delta
    print('PASS: {} exact finite trajectories; recurrence, reset, thresholds, and eigenvalue formulas.'.format(count))
    for row in examples:
        if row[2]=='1' and row[3]=='1':
            print('sample T,D,u,v,10^(-p),tau:',row)


if __name__=='__main__':
    main()
