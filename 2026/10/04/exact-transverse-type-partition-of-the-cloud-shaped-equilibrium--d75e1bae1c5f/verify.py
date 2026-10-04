from fractions import Fraction as F

# Polynomials are low-to-high coefficient lists over Q.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(p,q):
    n=max(len(p),len(q)); r=[F(0)]*n
    for i in range(n): r[i]=(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
    return trim(r)

def sub(p,q):
    return add(p,[-c for c in q])

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)

def scale(p,c): return trim([c*a for a in p])
def deriv(p): return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])
def divrem(p,q):
    p=trim(p); q=trim(q)
    if q==[0]: raise ZeroDivisionError
    r=p[:]; out=[F(0)]*max(1,len(p)-len(q)+1)
    while len(r)>=len(q) and r!=[0]:
        k=len(r)-len(q); c=r[-1]/q[-1]; out[k]=c
        r=sub(r,[F(0)]*k+scale(q,c))
    return trim(out),trim(r)

def evalp(p,x):
    y=F(0)
    for c in reversed(p): y=y*x+c
    return y

def sturm(p):
    seq=[trim(p),deriv(p)]
    while seq[-1]!=[0]:
        _,r=divrem(seq[-2],seq[-1])
        if r==[0]: break
        seq.append(scale(r,F(-1)))
    return seq

def signs_at(seq,x):
    vals=[]
    for p in seq:
        if x=='-inf':
            deg=len(p)-1; s=1 if p[-1]>0 else -1
            vals.append(s*((-1)**deg))
        elif x=='+inf': vals.append(1 if p[-1]>0 else -1)
        else:
            v=evalp(p,x)
            vals.append(0 if v==0 else (1 if v>0 else -1))
    vals=[v for v in vals if v]
    return sum(vals[i]!=vals[i-1] for i in range(1,len(vals)))

def root_count(seq,a,b): return signs_at(seq,a)-signs_at(seq,b)

def poly_eq(p, coeffs): return trim(p)==trim([F(c) for c in coeffs])

# Elimination for the two smooth sign regions s=+1 and s=-1.
# For s=+1, 2T = A_+ x + B_+.
Aplus=[4,8,5]
Bplus=[0,-2,-16,-10]
# For s=-1, an equivalent zero equation is A_- x + B_-=0.
Aminus=[-4,8,5]
Bminus=[0,-2,16,10]
y=[0,1]
y2m1=[-1,0,1]

def elimination(A,B,s):
    # q=x^2-sxy+y^2-1 and x=-B/A => A^2 q = B^2+s*A*B*y+A^2(y^2-1)
    return add(add(mul(B,B),scale(mul(mul(A,B),y),F(s))),mul(mul(A,A),y2m1))

Pplus=elimination(Aplus,Bplus,1)
Pminus=elimination(Aminus,Bminus,-1)
assert poly_eq(Pplus,[-16,-64,-92,-32,197,240,75])
assert poly_eq(Pminus,[-16,64,-12,-128,137,240,75])

Sp=sturm(Pplus); Sm=sturm(Pminus)
assert root_count(Sp,'-inf','+inf')==2
assert root_count(Sm,'-inf','+inf')==2
Ip_neg=(F(-4060,10000),F(-4059,10000))
Ip_pos=(F(7438,10000),F(7439,10000))
Im_neg=(F(-9193,10000),F(-9192,10000))
Im_pos=(F(2913,10000),F(2914,10000))
assert root_count(Sp,*Ip_neg)==1 and root_count(Sp,*Ip_pos)==1
assert root_count(Sm,*Im_neg)==1 and root_count(Sm,*Im_pos)==1

# Root-validity signs for x=-B/A on each isolating interval.
def sign_interval_poly(p,lo,hi):
    # all polynomials below have no zero on the tiny interval, so endpoint signs suffice
    vl,vr=evalp(p,lo),evalp(p,hi)
    assert vl and vr and (vl>0)==(vr>0)
    return 1 if vl>0 else -1

# s=+1: A+ is globally positive. x has sign -B+.
assert sign_interval_poly(Aplus,*Ip_neg)==1
assert sign_interval_poly(scale(Bplus,-1),*Ip_neg)==1  # x>0 while y<0 => invalid for s=+1
assert sign_interval_poly(scale(Bplus,-1),*Ip_pos)==1  # x>0, y>0 => valid Q1
# s=-1: both real resultant roots have x>0; only the negative-y root is valid.
assert sign_interval_poly(Aminus,*Im_neg)==-1 and sign_interval_poly(scale(Bminus,-1),*Im_neg)==-1
assert sign_interval_poly(Aminus,*Im_pos)==-1 and sign_interval_poly(scale(Bminus,-1),*Im_pos)==-1
# same signs numerator/denominator in the preceding representation imply x>0.

# Exact sign samples of T at smooth equilibria for a=4, b=5/2.
def T(xv,yv,s):
    h=F(4)*yv+F(5,2)*yv*yv
    return (F(2)*xv-F(s)*yv)-h*(F(2)*yv-F(s)*xv)
assert T(F(1),F(1),1)==F(-11,2)
assert T(F(-1),F(1),-1)==F(-15,2)
assert T(F(-1),F(-1),1)==F(-5,2)
assert T(F(1),F(-1),-1)==F(-1,2)
# One-sided T limit at (1,0) on both right-hand arcs is +2.
assert T(F(1),F(0),1)==2 and T(F(1),F(0),-1)==2
print('VERIFY_OK')
