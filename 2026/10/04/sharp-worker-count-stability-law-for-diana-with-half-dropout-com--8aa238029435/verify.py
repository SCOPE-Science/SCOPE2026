from fractions import Fraction
from itertools import product
import cmath
import math

def moment_matrix(n, s):
    n = Fraction(n)
    s = Fraction(s)
    return [
        [(1-s)**2+s*s/n, -2*s*s/n, s*s/n],
        [(n*(1-s)-s)/(2*n), (1-s)/2+s/n, -s/(2*n)],
        [Fraction(1,2), Fraction(0), Fraction(1,2)],
    ]

def branch_moments(n, s, x, e):
    vals = []
    for bits in product((0,1), repeat=n):
        z = sum(e)/n
        for i,b in enumerate(bits):
            z += Fraction(2,n)*b*(x-e[i])
        xp = x-s*z
        ep = [e[i]+bits[i]*(x-e[i]) for i in range(n)]
        eb = sum(ep)/n
        w = sum(v*v for v in ep)/n
        vals.append((xp*xp, xp*eb, w))
    den = 2**n
    return tuple(sum(v[j] for v in vals)/den for j in range(3))

for n in (1,2,3,4):
    s = Fraction(3,10)
    x = Fraction(7,5)
    e = [Fraction(i+1,7)-Fraction(2,5) for i in range(n)]
    X = x*x
    Y = x*(sum(e)/n)
    W = sum(v*v for v in e)/n
    M = moment_matrix(n,s)
    direct = branch_moments(n,s,x,e)
    calc = tuple(M[j][0]*X+M[j][1]*Y+M[j][2]*W for j in range(3))
    assert direct == calc

def coeffs(n,s):
    n=float(n); s=float(s)
    a1=-(2*(n+1)*s*s+(2-5*n)*s+4*n)/(2*n)
    a2=-(2*(n+1)*s**3+(2-8*n)*s*s+(11*n-6)*s-5*n)/(4*n)
    a3=(s-1)*(n*(s-1)**2+2*s)/(4*n)
    return a1,a2,a3

def jury(n,s):
    a1,a2,a3=coeffs(n,s)
    return (
        1+a1+a2+a3,
        1-a1+a2-a3,
        1-a3,
        1+a3,
        1-a2+a1*a3-a3*a3,
    )

def threshold(n):
    return (n-4+math.sqrt(9*n*n+8*n+16))/(2*(n+2))

for n in (1,2,3,4,5,8,16,50,200):
    t=threshold(n)
    for f in (0.01,0.2,0.5,0.9,0.999999):
        vals=jury(n,f*t)
        assert min(vals)>-2e-9, (n,f,vals)
    vals=jury(n,1.000001*t)
    assert vals[0] < 2e-9, (n,vals)

for n in range(1,101):
    t=threshold(n)
    a1,a2,a3=coeffs(n,t)
    assert abs(1+a1+a2+a3)<2e-10

assert abs(threshold(1)-(math.sqrt(33)-3)/6)<1e-14
assert abs(threshold(2)-(math.sqrt(17)-1)/4)<1e-14
assert abs(threshold(3)-1)<1e-14

prev=0.0
for n in range(1,10000):
    cur=threshold(n)
    assert cur>prev
    assert cur<2
    prev=cur

def roots_cubic(a1,a2,a3):
    roots=[1+0j, -0.4+0.9j, -0.6-0.8j]
    for _ in range(100):
        new=[]
        for i,z in enumerate(roots):
            val=z**3+a1*z*z+a2*z+a3
            den=1+0j
            for j,w in enumerate(roots):
                if i!=j:
                    den*=z-w
            new.append(z-val/den)
        if max(abs(new[i]-roots[i]) for i in range(3))<1e-14:
            roots=new
            break
        roots=new
    return roots

for n in (1,2,4,10,100):
    t=threshold(n)
    for f,inside in ((0.999,True),(1.001,False)):
        a1,a2,a3=coeffs(n,f*t)
        rho=max(abs(z) for z in roots_cubic(a1,a2,a3))
        if inside:
            assert rho<1
        else:
            assert rho>1

print("verification passed")
