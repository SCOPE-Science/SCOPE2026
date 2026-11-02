"""Finite reproducibility checks for logarithmic Bergman Hilbert-matrix constants.

The infinite-dimensional statements are proved analytically; this script checks
exact finite identities, reference integrals, and the shape of asymptotic terms.
Uses only the Python standard library.
"""
import math

ZETA2=math.pi**2/6

def harmonic(n,p=1):
    return sum(1/k**p for k in range(1,n+1))

def S(n):
    if n==0:
        return sum(1/k**3 for k in range(1,200001)) + 1/(2*200001**2)
    return harmonic(n)/n**2 - (ZETA2-harmonic(n,2))/n

def V2(n):
    return ((1+harmonic(n+1))**2 + harmonic(n+1,2))/(n+1)

def reference_v2(n):
    # u=-log(1-t) gives a rapidly decaying nonsingular integral
    m=20000; h=35/m
    def f(u):return (1-math.exp(-u))**n*(1+u)**2*math.exp(-u)
    return h/3*(f(0)+f(35)+4*sum(f(h*j) for j in range(1,m,2)) +2*sum(f(h*j) for j in range(2,m,2)))

def direct_s(n,M=50000):
    ans=sum(1/(k*(k+n)**2) for k in range(1,M+1))
    # tail <= integral_M^inf 1/[x(x+n)^2] <= 1/(2*M^2)
    return ans

count=0
for n in range(0,9):
    val=V2(n); ref=reference_v2(n)
    assert abs(val-ref)<2e-10, (n,val,ref)
    count+=1
for n in range(1,11):
    val=S(n); ref=direct_s(n)
    assert 0<val-ref<2.1e-10, (n,val,ref)
    count+=1
for n in (100,300,1000,3000,10000):
    s=S(n); v=V2(n)
    assert s>0 and v>0
    assert 0.5 < n*n*s/math.log(n) < 1.5
    assert 0.8 < n*v/(math.log(n)**2) < 2.2
    count+=2
for n in (100,1000,10000):
    a=S(n)/V2(n)
    b=1/(n*math.log(n))
    assert 0.1 < a/b < 1.5, (n,a,b)
    count+=1
print(f'PASS: {count} finite checks; no finite check substitutes for the analytic proof.')
