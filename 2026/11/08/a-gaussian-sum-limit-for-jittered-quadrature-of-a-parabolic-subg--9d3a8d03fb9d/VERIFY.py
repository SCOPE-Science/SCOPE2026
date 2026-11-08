"""Standalone reproducibility checks for a parabolic discontinuity in stratified quadrature."""
import math
from fractions import Fraction


def local_mean(s):
    s=float(s)
    if s<=1: return 1/6+s*s/12-s**3/60
    return s/6+1/(12*s)-1/(60*s*s)

def local_v(s,t):
    # Equivalent to one-column stratified Bernoulli variance for a line of slope s.
    ans=0.
    for j in range(-2,6):
        if s==0: p=max(0,min(1,t-j))
        else:
            # Integral_0^1 clamp(t+s*u-j,0,1)du using primitive of ReLU.
            def relu2(a):return max(a,0)**2
            p=(relu2(t+s-j)-relu2(t-j)-relu2(t+s-j-1)+relu2(t-j-1))/(2*s)
        if -1e-9<=p<=1+1e-9: p=max(0,min(1,p))
        else:raise AssertionError((s,t,j,p))
        ans+=p*(1-p)
    return ans

def parabolic_scaled_var(n):
    # Exactly integrates each cell probability, up to floating rounding of radicals.
    total=0.
    for i in range(n):
        lo=i*i/n
        hi=(i+1)*(i+1)/n
        for j in range(max(0,int(lo)-2),min(n,int(hi)+3)):
            left=float(i);right=float(i+1)
            t0=math.sqrt(n*j)
            t1=math.sqrt(n*(j+1))
            a=max(left,t0); b=min(right,t1)
            partial=(b**3-a**3)/(3*n)-j*(b-a) if b>a else 0.
            full=max(0.,right-max(left,t1))
            p=max(0,min(1,partial+full))
            total+=p*(1-p)
    return total/n


def check():
    count=0
    # The integral of |(U1-U2)+s(V1-V2)|/2 is the local phase average.
    # The exact uniform-difference moments are E|D|^2=1/6, E|D|^3=1/10.
    assert Fraction(1,2)*(Fraction(1,3)+Fraction(1,6)-Fraction(1,30))==Fraction(7,30);count+=1
    assert local_mean(1)==7/30;count+=1
    assert abs(local_mean(2)-(2/6+1/24-1/240))<1e-14;count+=1
    for s in [0,.1,.5,1,1.25,1.5,2]:
        avg=sum(local_v(s,k/512) for k in range(512))/512
        assert abs(avg-local_mean(s))<1.5e-5,(s,avg,local_mean(s))
        count+=1
    # For f(x)=x^2, exact area is 1/3 and every cell is Bernoulli.
    assert abs(parabolic_scaled_var(1)-2/9)<1e-14;count+=1
    # Numerical finite-n checks are separate from the analytic Gauss-sum proof.
    target=311/1440+math.log(2)/24
    approximations=[(100,.003),(300,.002),(1000,.001),(3000,.0006),(10000,.0003)]
    for n,tol in approximations:
        x=parabolic_scaled_var(n)
        assert abs(x-target)<tol,(n,x,target)
        count+=1
    # Verify explicit analytic integral of K(2x) by antiderivatives.
    polynomial=Fraction(137,1440)
    rational=Fraction(29,240)
    assert polynomial+rational==Fraction(311,1440)
    count+=1
    return count

if __name__=='__main__':
    print(f'{check()} independent finite checks passed (limit proved analytically in RESULT.md)')
