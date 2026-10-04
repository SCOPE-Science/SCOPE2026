import math, random
PI=math.pi
Q0=math.sqrt(3.0/5.0)
U0=math.atan(Q0)

def roots(q):
    s=math.sqrt(4*q*q+3)
    return 2*q-s, 2*q+s, 3/q, -(3+q*q)/(2*q)

def h_low_q(q):
    if q == 0.0: return 2.0/3.0
    a,b,g,e=roots(q)
    return 1.0+(math.atan(e)+math.atan(b)-math.atan(a)-math.atan(g))/PI

def h_high_q(q):
    if math.isinf(q): return 0.0
    a,b,g,e=roots(q)
    return 1.0+(math.atan(e)+math.atan(g)-math.atan(a)-math.atan(b))/PI

def f1(u):
    if u == 0.0: return 2.0/3.0
    return h_low_q(math.tan(u))

def f2(u):
    if u == PI/2: return 0.0
    return h_high_q(math.tan(u))

def simpson(f,a,b):
    c=(a+b)/2
    return (b-a)*(f(a)+4*f(c)+f(b))/6

def adaptive(f,a,b,eps,whole=None,depth=25):
    if whole is None: whole=simpson(f,a,b)
    c=(a+b)/2
    left=simpson(f,a,c); right=simpson(f,c,b)
    if depth<=0 or abs(left+right-whole)<=15*eps:
        return left+right+(left+right-whole)/15
    return adaptive(f,a,c,eps/2,left,depth-1)+adaptive(f,c,b,eps/2,right,depth-1)

# Root ordering and crossover.
a,b,g,e=roots(Q0)
assert abs(b-g) < 2e-14
for q in [0.02,0.1,0.5,Q0*0.999, Q0*1.001,1.0,2.0,10.0,100.0]:
    a,b,g,e=roots(q)
    assert e < a < 0 < b
    if q < Q0: assert b < g
    if q > Q0: assert g < b

# Deterministic sign check of the tangent factorization at many nonsingular points.
def trig_product(x,y):
    return (2*math.cos((y-2*x)/2)+math.cos(y/2)) * (math.cos((y-x)/2)+2*math.cos((y+x)/2)) * (math.cos((2*y-x)/2)+2*math.cos(x/2))
def poly_product(x,y):
    p=math.tan(x/2); q=math.tan(y/2)
    return (3-p*p+4*p*q)*(3-p*q)*(3+q*q+2*p*q)
for i in range(1,38):
    for j in range(1,41):
        x=-PI + 2*PI*(i+0.31)/39
        y=-PI + 2*PI*(j+0.47)/43
        t=trig_product(x,y); f=poly_product(x,y)
        if abs(t)>1e-11 and abs(f)>1e-9:
            assert (t>0)==(f>0)

# One-dimensional quadrature.
I1=adaptive(f1,0.0,U0,2e-13)
I2=adaptive(f2,U0,PI/2,2e-13)
P=2/PI*(I1+I2)
TARGET=0.6390804227921295452
assert abs(P-TARGET) < 2e-12, (P,TARGET)
assert abs(P-0.639081) < 1e-6

# Independent midpoint area check of the original two-variable criterion.
N=900
cnt=0
for i in range(N):
    x=-PI+(i+0.5)*(2*PI/N)
    for j in range(N):
        y=-PI+(j+0.5)*(2*PI/N)
        if trig_product(x,y)>=0: cnt += 1
P2=cnt/(N*N)
assert abs(P2-P)<0.0025,(P2,P)

print('VERIFY_OK')
print('P_1D=%.15f'%P)
print('P_2D_midpoint=%.9f'%P2)
print('q0=%.15f'%Q0)
