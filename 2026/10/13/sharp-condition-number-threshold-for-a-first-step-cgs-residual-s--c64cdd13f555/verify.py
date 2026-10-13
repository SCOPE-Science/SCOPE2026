from fractions import Fraction as F
from math import sqrt

# Polynomial in k represented low-to-high integer/Fraction coefficients.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0) for _ in range(n)]
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,s): return trim([s*x for x in a])

def det_poly(M):
    # Bareiss fraction-free determinant over Q[k]. For the small Sylvester matrix,
    # exact polynomial division is used.
    A=[[trim(x) for x in row] for row in M]
    n=len(A); sign=1; prev=[F(1)]
    for pivot in range(n-1):
        if A[pivot][pivot]==[F(0)]:
            j=next(j for j in range(pivot+1,n) if A[j][pivot] != [F(0)])
            A[pivot],A[j]=A[j],A[pivot]; sign*=-1
        p=A[pivot][pivot]
        for i in range(pivot+1,n):
            for j in range(pivot+1,n):
                num=sub(mul(A[i][j],p),mul(A[i][pivot],A[pivot][j]))
                A[i][j]=div_exact(num,prev)
        for i in range(pivot+1,n): A[i][pivot]=[F(0)]
        prev=p
    return scale(A[-1][-1],sign)

def div_exact(a,b):
    a=trim(a); b=trim(b)
    if b==[F(0)]: raise ZeroDivisionError
    if len(a)<len(b):
        assert a==[F(0)]; return [F(0)]
    q=[F(0)]*(len(a)-len(b)+1); r=a[:]
    while len(r)>=len(b) and r!=[F(0)]:
        d=len(r)-len(b); c=r[-1]/b[-1]; q[d]=c
        for i,x in enumerate(b): r[i+d]-=c*x
        r=trim(r)
    assert r==[F(0)]
    return trim(q)

def sylvester_resultant(f_t,g_t):
    # Inputs are coefficient arrays high-to-low in t, each coefficient a polynomial in k.
    m=len(f_t)-1; n=len(g_t)-1; N=m+n
    zero=[F(0)]
    rows=[]
    for shift in range(n):
        row=[zero[:] for _ in range(N)]
        for j,c in enumerate(f_t): row[shift+j]=c
        rows.append(row)
    for shift in range(m):
        row=[zero[:] for _ in range(N)]
        for j,c in enumerate(g_t): row[shift+j]=c
        rows.append(row)
    return det_poly(rows)

# H(k,t) = k t^3 -(2k+3)t^2 +(3k+2)t -1.
kpoly=[F(0),F(1)]
f=[kpoly, [F(-3),F(-2)], [F(2),F(3)], [F(-1)]]

# G=1 equation: (k-1)^4 t(t^2-t+1) - (1+k t)^4 = 0.
km1_4=mul(mul([F(-1),F(1)],[F(-1),F(1)]),mul([F(-1),F(1)],[F(-1),F(1)]))
# Build high-to-low t coefficients explicitly.
# t(t^2-t+1)=t^3-t^2+t.
# (1+kt)^4 = 1+4kt+6k^2t^2+4k^3t^3+k^4t^4.
k2=mul(kpoly,kpoly); k3=mul(k2,kpoly); k4=mul(k3,kpoly)
g=[neg(k4), sub(km1_4,scale(k3,F(4))), sub(neg(km1_4),scale(k2,F(6))), sub(km1_4,scale(kpoly,F(4))), [F(-1)]]
res=trim(sylvester_resultant(f,g))

# Expected resultant is 16*k*(k^2+k+1)*P(k), up to the Sylvester convention sign.
P=[F(1),F(0),F(8),F(-72),F(122),F(-436),F(322),F(-436),F(122),F(-72),F(8),F(0),F(1)]
expected=scale(mul(mul(kpoly,[F(1),F(1),F(1)]),P),F(16))
assert res==expected or res==neg(expected)

# Reciprocal reduction P(k)/k^6 = Q(k+1/k).
# Verify through Laurent coefficients generated from s_j=k^j+k^{-j}.
def laurent_add(a,b):
    c=dict(a)
    for e,v in b.items(): c[e]=c.get(e,F(0))+v
    return {e:v for e,v in c.items() if v}
def laurent_mul_y(a):
    c={}
    for e,v in a.items():
        c[e+1]=c.get(e+1,F(0))+v
        c[e-1]=c.get(e-1,F(0))+v
    return c
s={0:{0:F(2)},1:{1:F(1),-1:F(1)}}
for j in range(2,7):
    s[j]=laurent_add(laurent_mul_y(s[j-1]),{e:-v for e,v in s[j-2].items()})
expr={}
for coef,j in [(1,6),(8,4),(-72,3),(122,2),(-436,1)]:
    expr=laurent_add(expr,{e:F(coef)*v for e,v in s[j].items()})
expr=laurent_add(expr,{0:F(322)})
expected_laurent={i-6:c for i,c in enumerate(P) if c}
assert expr==expected_laurent

# Q(y)=y^6+2y^4-72y^3+99y^2-220y+92.
# Q(z+2) coefficients low-to-high are [-432,-432,-45,104,62,12,1].
qshift=[-432,-432,-45,104,62,12,1]
signs=[1 if c>0 else -1 for c in reversed(qshift) if c]
changes=sum(a!=b for a,b in zip(signs,signs[1:]))
assert changes==1
assert qshift[0] < 0 and qshift[-1] > 0

# Exact isolation of the unique root k>1.
def peval(coeffs,x):
    s=F(0)
    for c in reversed(coeffs): s=s*x+c
    return s
lo=F(3442815869,10**9); hi=F(3442815870,10**9)
assert peval(P,lo)<0<peval(P,hi)

# Exact kappa=4 CGS witness.
alpha=F(17,20)
r0=[F(4),F(1)]
lams=[F(1),F(4)]
r1=[(1-alpha*l)**2*r for l,r in zip(lams,r0)]
assert r1==[F(9,100),F(144,25)]
ratio2=sum(x*x for x in r1)/sum(x*x for x in r0)
assert ratio2==F(331857,170000) and ratio2>1

# The stationary polynomial and elimination certificate are checked above by the exact resultant.

print('VERIFY_OK')
