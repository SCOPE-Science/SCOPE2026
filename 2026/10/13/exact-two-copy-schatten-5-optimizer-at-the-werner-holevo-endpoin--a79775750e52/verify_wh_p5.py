from fractions import Fraction as F

# Exact fifth power sums from Newton recurrences.
# lambda roots: z^3-z^2+e2*z-e3 = 0
# Represent polynomials in (e2,e3) by dict[(i,j)] = coefficient.
def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def scale(a,s): return {k:v*s for k,v in a.items() if v*s}
def mul_e2(a): return {(i+1,j):v for (i,j),v in a.items()}
def mul_e3(a): return {(i,j+1):v for (i,j),v in a.items()}

p={0:{(0,0):F(3)},1:{(0,0):F(1)},2:{(0,0):F(1),(1,0):F(-2)}}
for k in range(3,6):
    p[k]=add(add(p[k-1],scale(mul_e2(p[k-2]),F(-1))),mul_e3(p[k-3]))
expected={(2,0):F(5),(1,1):F(-5),(1,0):F(-5),(0,1):F(5),(0,0):F(1)}
assert p[5]==expected

# gamma roots: z^3-2*z^2+z-4*e3 = 0
q={0:{(0,0):F(3)},1:{(0,0):F(2)},2:{(0,0):F(2)}}
for k in range(3,6):
    q[k]=add(add(scale(q[k-1],F(2)),scale(q[k-2],F(-1))),scale(mul_e3(q[k-3]),F(4)))
assert q[5]=={(0,1):F(60),(0,0):F(2)}

# Verify the one-variable factorization coefficientwise.
# D(u)=344/81 - (4-30u^2+70u^3+90u^4-30u^5)
D=[F(344,81)-4,F(0),F(30),F(-70),F(-90),F(30)]
Q=[F(-2),F(-6),F(-261),F(-216),F(81)]
# (10/81)*(3u-1)*Q
R=[F(0)]*6
for i,a in enumerate([F(-1),F(3)]):
    for j,b in enumerate(Q):
        R[i+j]+=F(10,81)*a*b
assert D==R

# Exact optimum and violation ratio.
opt=F(344,81)/F(1024)
assert opt==F(43,10368)
product_benchmark=F(1,256)
assert opt/product_benchmark==F(86,81)

# Supplementary rational grid for the one-variable upper bound.
def f(u): return F(4)-30*u*u+70*u**3+90*u**4-30*u**5
for k in range(1001):
    u=F(k,3000)  # 0 <= u <= 1/3
    assert f(u) <= F(344,81)

print('VERIFY_OK')
print('optimum_fifth_moment = 43/10368')
print('fifth_power_violation_ratio = 86/81')
print('grid_points = 1001 (supplementary only)')
