"""Exact finite checks for random-source distinct scattered Dyck words. Python 3 stdlib."""
from fractions import Fraction
from itertools import product
from math import isclose,sqrt,pi


def dyck(s):
    if not s or len(s)%2:return False
    balance=0
    for a in s:
        balance+=1 if a=='0' else -1
        if balance<0:return False
    return balance==0


def brute(p,N):
    first=[]; checked=0
    for n in range(N+1):
        value=Fraction(0)
        for tup in product('01',repeat=n):
            w=''.join(tup); ss={''}
            for a in w:ss|={v+a for v in tuple(ss)}
            count=sum(dyck(s) for s in ss)
            value+=p**w.count('1')*(1-p)**w.count('0')*count
            checked+=1
        first.append(value)
    return first,checked


def convolution(A,B,N):
    C=[Fraction(0)]*(N+1)
    for i,a in enumerate(A):
        for j,b in enumerate(B[:N+1-i]):C[i+j]+=a*b
    return C


def formal(p,N):
    t=p*(1-p)
    # u(z)=t*z^2 / (1-z+t*z^2)
    u=[Fraction(0)]*(N+1)
    for n in range(2,N+1):u[n]=(t if n==2 else 0)+u[n-1]-(t*u[n-2] if n>=4 else 0)
    # C(u)-1=sum_{m>=1} Catalan_m*u^m
    powers=[Fraction(1)]+[Fraction(0)]*N
    F=[Fraction(0)]*(N+1)
    catalan=1
    for m in range(1,N//2+1):
        catalan=catalan*2*(2*m-1)//(m+1)
        powers=convolution(powers,u,N)
        for j in range(N+1):F[j]+=catalan*powers[j]
    # 1/(1-z) integration by prefix sum
    out=[];running=Fraction(0)
    for v in F:running+=v;out.append(running)
    return out


def run():
    cases=[(Fraction(1,2),12),(Fraction(1,3),11),(Fraction(2,5),11),(Fraction(3,7),10)]
    total=0
    for p,N in cases:
        expected,k=brute(p,N);calc=formal(p,N)
        assert expected==calc,(p,expected,calc)
        total+=k
        assert formal(p,90)[:N+1]==expected
        t=p*(1-p)
        rad=2/(1+sqrt(1+12*float(t)))
        assert abs(3*float(t)*rad*rad+rad-1)<1e-12
    r=Fraction(2,3);h=Fraction(3)
    assert 3*Fraction(1,4)*r*r+r==1
    assert h==3*(2-r)/(4*(1-r))
    # The fair asymptotic leading constant is 3*sqrt(3/pi).
    assert isclose(sqrt(float(h))/float(1-r)/sqrt(pi),3*sqrt(3/pi))
    print('VERIFY_OK source_words=%d probability_vectors=%d exact_coefficients_through=%d' %(total,len(cases),90))
if __name__=='__main__':run()
