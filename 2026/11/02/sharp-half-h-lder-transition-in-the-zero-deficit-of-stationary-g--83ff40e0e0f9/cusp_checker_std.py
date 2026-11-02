"""Independent finite checks of Fourier formulas and limiting constants.

Usage: python3 cusp_checker_std.py
Standard-library only. Finite numerical tests support but do not prove the theorem.
"""
import math

def gamma_coeff(alpha,k):
    return -math.gamma(alpha+1)*math.sin(math.pi*alpha/2)/math.pi * math.exp(
        math.lgamma(k-alpha/2)-math.lgamma(k+1+alpha/2))

def midpoint_coeff(alpha,k,n=300000):
    # g is even; Fourier cosine coefficient on [0, pi], no endpoint sampling
    s=0.0
    for j in range(n):
        theta=(j+.5)*math.pi/n
        s+=abs(2*math.sin(theta/2))**alpha*math.cos(k*theta)
    return s/n

def shell_series(alpha,eps,n=700000):
    # Exact gamma coefficient for k=1, recurrence for remaining frequencies.
    coeff=gamma_coeff(alpha,1)
    h=math.log1p(-eps)
    ans=0.0
    for k in range(1,n+1):
        term=1.0 if k*eps>25 else -math.expm1(2*k*h)
        ans+=k*coeff*coeff*term
        coeff*=(k-alpha/2)/(k+1+alpha/2)
    # Leading asymptotic tail. For n*eps >= 25, omitted decay in (1-r^(2k))
    # and the gamma-ratio error are both negligible at the printed precision.
    A=math.gamma(alpha+1)*math.sin(math.pi*alpha/2)/math.pi
    ans+=A*A*n**(-2*alpha)/(2*alpha)
    return ans

def predicted(alpha,eps):
    A=math.gamma(alpha+1)*math.sin(math.pi*alpha/2)/math.pi
    if alpha < .5:
        return A*A*2**(2*alpha)*math.gamma(1-2*alpha)/(2*alpha)*eps**(2*alpha)
    if alpha == .5:
        return 2*A*A*eps*math.log(1/eps)
    raise ValueError('Only singular/critical regimes have this constant')

def main():
    assertions=0
    for a in (.25,.4,.5,.75):
        for k in (1,2,3,5,8):
            g=gamma_coeff(a,k)
            h=midpoint_coeff(a,k,n=40000)
            assert abs(g-h)<2e-6,(a,k,g,h)
            assertions+=1
        for k in (1,2,3,5):
            lhs=gamma_coeff(a,k+1)/gamma_coeff(a,k)
            rhs=(k-a/2)/(k+1+a/2)
            assert abs(lhs-rhs)<2e-11
            assertions+=1
    for a, bounds in ((.25,(.96,1.01)),(.4,(.84,.90)),(.5,(1.03,1.07))):
        eps=0.0001
        ratio=shell_series(a,eps)/predicted(a,eps)
        print(f'alpha={a}: shell/predicted at epsilon={eps}: {ratio:.7f}')
        assert bounds[0]<ratio<bounds[1]
        assertions+=1
    s1=shell_series(.25,0.002)/predicted(.25,0.002)
    s2=shell_series(.25,0.0001)/predicted(.25,0.0001)
    assert s1<s2<=1.01
    assertions+=1
    print(f'PASS: {assertions} independent finite checks (not an infinite proof)')
if __name__=='__main__':main()
