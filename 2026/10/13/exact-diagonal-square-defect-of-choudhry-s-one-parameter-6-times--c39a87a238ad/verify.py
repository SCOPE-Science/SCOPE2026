from fractions import Fraction

# Polynomials are coefficient lists in ascending powers.
def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def scale(a,k): return [k*x for x in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def evalp(a,x):
    s=0
    for c in reversed(a): s=s*x+c
    return s

def from_desc(v): return list(reversed(v))

def P(v): return from_desc(v)  # source notation is c0 t^8+...+c8

X11=scale(P([0,1,0,-1,-24,-9,24,9,0]),12)
X22=scale(P([0,0,1,-7,-6,6,-3,9,0]),-24)
X33=scale(P([0,0,1,-5,6,6,-15,-9,0]),24)
Y11=scale(P([0,1,8,-9,-72,-9,0,81,0]),4)
Y22=scale(P([0,1,-1,6,-18,-63,27,0,0]),-8)
Y33=scale(P([0,1,5,-6,-18,45,-27,0,0]),-8)

def sq(a): return mul(a,a)
diag=[0]
for a in (X11,X22,X33,Y11,Y22,Y33): diag=add(diag,sq(a))
# F=(t^4+30t^2+9)(t^2+3)^2, and each squared row sum is 2F^2.
F=mul([9,0,30,0,1], mul([3,0,1],[3,0,1]))
defect=add(diag,scale(sq(F),-2))
Q=from_desc([1,0,-75,-384,285,18432,6129,-103680,18387,165888,7695,-31104,-18225,0,2187])
expected=scale(mul([3,0,1],Q),-2)
assert defect==expected, (defect,expected)
# Rational-root certificate: Q is monic. An integer root must be 0 mod 3;
# if r=3u, every nonconstant term is 0 mod 3^8 while Q(0)=3^7.
assert Q[-1]==1
for power,coef in enumerate(Q[1:],1):
    if coef:
        # coefficient*3^power divisible by 3^8
        assert (coef*(3**power))%(3**8)==0, (power,coef)
assert Q[0]==3**7
# Mod 3, Q(r)=r^14.
for r in range(3): assert evalp(Q,r)%3 == pow(r,14,3)
# Source numerical specialization t=2.
M=[
[-2952,-2736,-5855,5855,2736,2952],
[3361,4848,-3960,3960,-4848,-3361],
[5520,-4415,-720,720,4415,-5520],
[-2976,6207,1760,-1760,-6207,2976],
[-5793,-3424,2280,-2280,3424,5793],
[2840,-480,6495,-6495,480,-2840],
]
rows=[sum(x*x for x in row) for row in M]
diag_num=sum(M[i][i]**2 for i in range(6))
anti_num=sum(M[i][5-i]**2 for i in range(6))
assert len(set(rows))==1 and rows[0]==100962050
assert diag_num==anti_num==55622784
assert diag_num-rows[0]==evalp(defect,2)==-45339266
# Spot-check affine-defect invariance on the numerical matrix.
for a,b in [(2,7),(-3,11),(5,-19)]:
    N=[[a*x+b for x in row] for row in M]
    r=sum(x*x for x in N[0])
    d=sum(N[i][i]**2 for i in range(6))
    assert d-r==a*a*(diag_num-rows[0])
print('VERIFY_OK factorization=exact rational_roots=none t2_defect=-45339266 affine_invariance=checked')
