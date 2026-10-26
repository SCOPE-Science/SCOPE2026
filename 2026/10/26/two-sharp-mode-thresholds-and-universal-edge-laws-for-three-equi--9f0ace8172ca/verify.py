"""Independent, standard-library finite-chain and edge-law checks for a three-defect mass chain.
Run: python3 verify.py
"""
from math import sqrt, isclose


def channel(q, gap):
    t = q ** gap
    a = (2 + t*t + t * sqrt(8 + t*t)) / 2
    b = 1 - t*t
    c = (2 + t*t - t * sqrt(8 + t*t)) / 2
    return (a,b,c)


def mass_contrast(q, gap, j):
    return (1-q)/((1+q)*channel(q,gap)[j])


def bisect_q(gap, delta, j):
    lo,hi = 0.0,1.0
    for _ in range(95):
        q=(lo+hi)/2
        if mass_contrast(q,gap,j)>delta:
            lo=q
        else:
            hi=q
    return (lo+hi)/2


def count_above_four_finite(gap, delta, size=1201):
    # Sylvester inertia of the symmetric mass-normalized Jacobi matrix minus 4I.
    # Dirichlet outer boundary, impurities at center-gap and center+gap.
    n=size
    masses=[1.0]*n
    center=n//2
    for k in (-gap,0,gap):
        masses[center+k]=1-delta
    negative=0
    pivot=2/masses[0]-4
    if pivot<0: negative+=1
    for i in range(1,n):
        if abs(pivot)<1.e-13:
            pivot=-1.e-13
        offsq=1/(masses[i-1]*masses[i])
        pivot=2/masses[i]-4-offsq/pivot
        if pivot<0:negative+=1
    return n-negative


def check():
    tested=0
    for d in (1,2,3,5,10):
        th2=1/(4*d); th3=3/(4*d)
        for delta in (th2/2, (th2+th3)/2,(th3+1)/2):
            expected=1+(delta>th2)+(delta>th3)
            got=count_above_four_finite(d,delta)
            if got!=expected:
                raise AssertionError((d,delta,expected,got))
            for j in range(expected):
                q=bisect_q(d,delta,j)
                vals=channel(q,d)
                assert 0<q<1
                assert abs(mass_contrast(q,d,j)-delta)<1e-12
                assert vals[0]>vals[1]>vals[2]>0
                tested+=1
        for j,critical,coefficient in ((1,th2,16),(2,th3,144)):
            h=1e-5 if d<5 else 1e-6
            q=bisect_q(d,critical+h,j)
            gap_squared=(1-q)**2/q
            ratio=gap_squared/h**2
            assert abs(ratio/coefficient-1)<0.008,(d,j,ratio)
            tested+=1
    assert tested==sum((1+2+3)+2 for d in (1,2,3,5,10))
    print(f'PASS: {tested} exact-secular and finite-chain/edge checks; all three mode-count regions for five separations')

if __name__=='__main__':
    check()
