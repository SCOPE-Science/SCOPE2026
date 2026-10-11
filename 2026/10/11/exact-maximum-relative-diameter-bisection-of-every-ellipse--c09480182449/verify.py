#!/usr/bin/env python3
import sympy as s
import math

a,b,u=s.symbols('a b u', positive=True, real=True)
A=a*a-b*b
Q=4*u*(a*a-A*u)
u_star=s.simplify(a*a/(2*A))
M2=s.simplify(Q.subs(u,u_star))
assert s.simplify(M2-a**4/A)==0
assert s.simplify(Q.subs(u,1)-4*b*b)==0
# threshold equality at a^2=2b^2
assert s.simplify((a**4/A).subs(a**2,2*b**2)-4*b**2)==0
# elongated direction certificates
Ld2=s.simplify(4*(a*a*(1-u_star)+b*b*u_star))
assert s.simplify(Ld2-2*a*a)==0
assert s.simplify(Ld2-M2-a**2*(a**2-2*b**2)/(a**2-b**2))==0

# Exact chord identity.
t,ss=s.symbols('t ss', real=True)
m=(t+ss)/2
d=(t-ss)/2
lhs=s.expand_trig(a*a*(s.cos(t)-s.cos(ss))**2+b*b*(s.sin(t)-s.sin(ss))**2)
rhs=4*s.sin(d)**2*(a*a*s.sin(m)**2+b*b*s.cos(m)**2)
assert s.simplify((lhs-rhs).rewrite(s.exp))==0

# Regression: sample the diameter of a center-line half by dense boundary pairs.
def pt(a,b,t): return (a*math.cos(t),b*math.sin(t))
def half_diam(a,b,t0,N=900):
    pts=[pt(a,b,t0+math.pi*i/N) for i in range(N+1)]
    best=0.0
    # sufficient for regression only; vectorized-ish nested thinning would be enough, full ~0.8m pairs
    for i in range(N+1):
        xi,yi=pts[i]
        for j in range(i+1,N+1):
            xj,yj=pts[j]
            q=(xi-xj)**2+(yi-yj)**2
            if q>best: best=q
    return math.sqrt(best)

def formula(a,b):
    if a*a <= 2*b*b+1e-14: return 2*b
    return a*a/math.sqrt(a*a-b*b)

for ratio in [1.0,1.2,math.sqrt(2),1.6,2.0,4.0]:
    aa=ratio; bb=1.0
    M=formula(aa,bb)
    got=half_diam(aa,bb,math.pi/2,260)
    assert abs(got-M)<3e-4, (ratio,got,M)
    # sampled competing center lines cannot beat the minor-axis value
    for k in range(41):
        t0=(math.pi/2)*k/40
        got2=half_diam(aa,bb,t0,120)
        assert got2 >= M-8e-4, (ratio,t0,got2,M)

print('VERIFY_OK')
print('threshold aspect ratio =', math.sqrt(2))
print('symbolic elongated value squared =', M2)
