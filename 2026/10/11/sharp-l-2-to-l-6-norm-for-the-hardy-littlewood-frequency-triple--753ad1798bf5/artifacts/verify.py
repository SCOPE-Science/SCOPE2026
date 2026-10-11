from fractions import Fraction
import math, random

# Polynomials use ascending Fraction coefficients.
def trim(p):
    p=[Fraction(x) for x in p]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(p,q):
    n=max(len(p),len(q)); out=[Fraction(0)]*n
    for i,a in enumerate(p): out[i]+=a
    for i,a in enumerate(q): out[i]+=a
    return trim(out)

def neg(p): return [-a for a in p]
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    out=[Fraction(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return trim(out)
def scale(p,c): return trim([c*a for a in p])
def deriv(p): return trim([Fraction(i)*p[i] for i in range(1,len(p))] or [0])
def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    q=[Fraction(0)]*max(1,(len(a)-len(b)+1))
    rr=a[:]
    while rr != [0] and len(rr)>=len(b):
        k=len(rr)-len(b); c=rr[-1]/b[-1]
        if k>=len(q): q.extend([Fraction(0)]*(k+1-len(q)))
        q[k]+=c
        for j,bj in enumerate(b): rr[j+k]-=c*bj
        rr=trim(rr)
    return trim(q),trim(rr)
def eval_poly(p,x):
    s=Fraction(0)
    for a in reversed(p): s=s*x+a
    return s

def sturm(p):
    seq=[trim(p),deriv(p)]
    while seq[-1] != [0]:
        _,rem=divmod_poly(seq[-2],seq[-1])
        if rem==[0]: break
        seq.append(neg(rem))
    return seq

def variations(seq,x):
    signs=[]
    for p in seq:
        v=eval_poly(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
    return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
def root_count(seq,a,b): return variations(seq,a)-variations(seq,b)

# R(r) = r^10+13r^9+44r^8+42r^7+6r^6-207r^5-148r^4+120r^3+81r^2+36r+32.
R=[32,36,81,120,-148,-207,6,42,44,13,1]
S=sturm(R)
assert root_count(S,Fraction(1),Fraction(23,20))==1
assert root_count(S,Fraction(547,500),Fraction(219,200))==1
assert root_count(S,Fraction(219,200),Fraction(23,20))==0

# Exact elimination identity for the two stationarity equations.
# A=r^3+4r^2-3r-4 and N=2(1-r^2), so X=N/A.
A=[-4,-3,4,1]
N=[2,0,-2]
r2=[0,0,1]; r3=[0,0,0,1]; r4=[0,0,0,0,1]
# Q(X,r) = -3X^2r^3-6X^2r^2 + 2Xr^4+4Xr^3+10Xr^2+2X -r^4-r^3-2r^2-1.
# A^2 Q(N/A,r) + R = 0.
N2=mul(N,N); A2=mul(A,A); NA=mul(N,A)
expr=[0]
expr=add(expr, scale(mul(N2,r3),-3))
expr=add(expr, scale(mul(N2,r2),-6))
expr=add(expr, scale(mul(NA,r4),2))
expr=add(expr, scale(mul(NA,r3),4))
expr=add(expr, scale(mul(NA,r2),10))
expr=add(expr, scale(NA,2))
base=add(add(add(scale(r4,-1),scale(r3,-1)),scale(r2,-2)),[-1])
expr=add(expr,mul(A2,base))
assert trim(add(expr,R))==[0]

# Feasible interval: beta is the positive root of B=r^3+6r^2-3r-6.
B=[-6,-3,6,1]
assert eval_poly(B,Fraction(57,50))<0
assert eval_poly(B,Fraction(23,20))>0
# X at the root-isolating endpoints is strictly between 0 and 1.
def Xfrac(t):
    return 2*(1-t*t)/(t**3+4*t*t-3*t-4)
for t in (Fraction(547,500),Fraction(219,200)):
    xx=Xfrac(t)
    assert 0<xx<1

# Numerically isolate r*, reconstruct the optimizer, and check the sharp value.
def Rf(t):
    return ((((((((((t+13)*t+44)*t+42)*t+6)*t-207)*t-148)*t+120)*t+81)*t+36)*t+32)
lo=547/500; hi=219/200
flo=Rf(lo); fhi=Rf(hi)
assert flo>0 and fhi<0
for _ in range(100):
    mid=(lo+hi)/2
    fm=Rf(mid)
    if fm>0: lo=mid
    else: hi=mid
r=(lo+hi)/2
X=2*(1-r*r)/(r**3+4*r*r-3*r-4)
Y=(1-X)*r*r/(1+r*r)
Z=(1-X)/(1+r*r)
assert abs(X+Y+Z-1)<1e-14 and min(X,Y,Z)>0

def phi(X,r):
    return (6*X**3*r**3+12*X**3*r**2-6*X**2*r**4-12*X**2*r**3-30*X**2*r**2-6*X**2+6*X*r**4+6*X*r**3+12*X*r**2+6*X+r**4+8*r**2+1)/(1+r*r)**2
K=phi(X,r)
C=K**(1/6)
assert 3.6766908847 < K < 3.6766908849
assert 1.2423468210 < C < 1.2423468213
assert K > 11/3 > 5/2

# Corroborative random replay of the full complex coefficient formula.
def moment6(a,b,c):
    coeff={
        0:a**3,
        1:3*a*a*b,
        2:3*a*b*b,
        3:b**3+3*a*a*c,
        4:6*a*b*c,
        5:3*b*b*c,
        6:3*a*c*c,
        7:3*b*c*c,
        9:c**3,
    }
    return sum(abs(v)**2 for v in coeff.values())
random.seed(2705)
mx=0.0
for _ in range(20000):
    mags=[random.expovariate(1.0) for _ in range(3)]
    norm=math.sqrt(sum(t*t for t in mags)); mags=[t/norm for t in mags]
    ph=[random.random()*2*math.pi for _ in range(3)]
    a=mags[0]*complex(math.cos(ph[0]),math.sin(ph[0]))
    b=mags[1]*complex(math.cos(ph[1]),math.sin(ph[1]))
    c=mags[2]*complex(math.cos(ph[2]),math.sin(ph[2]))
    q=moment6(a,b,c)
    mx=max(mx,q)
    assert q <= K + 5e-12
# Exact aligned optimizer replay.
a=math.sqrt(X); b=math.sqrt(Y); c=math.sqrt(Z)
assert abs(moment6(a,b,c)-K)<2e-13
print(f"VERIFY_OK sturm_feasible_roots=1 r={r:.15f} X={X:.15f} Y={Y:.15f} Z={Z:.15f} K={K:.15f} C6={C:.15f} random_cases=20000 max_random={mx:.15f}")
