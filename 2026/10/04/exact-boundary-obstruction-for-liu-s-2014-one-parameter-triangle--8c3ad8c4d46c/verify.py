from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
sqrt=lambda x: x.sqrt()
r3=sqrt(D(3))
t=(D(1)+D(2)*sqrt(-D(3)+D(2)*r3))/(D(3)*r3-D(2))
q=(D(3)*r3-D(2))*t*t-D(2)*t+(r3-D(2))
assert abs(q) < D('1e-60')
assert D(2)-r3 < t < D(1)

def L(x):
    return (D(8)*r3*x-D(8)*x-D(2)*(D(1)+x*x))/(x*x+D(2)*r3*x-D(1))
lam=L(t)
expected=D('0.5866991537979094260837651704184658551027745410913687657047877553190322')
assert abs(lam-expected) < D('1e-60')

def Q(x):
    return (D(3)*r3-D(2))*x*x-D(2)*x+(r3-D(2))
assert Q((t+(D(2)-r3))/D(2)) < 0
assert Q((t+D(1))/D(2)) > 0

# Basic high-precision geometry helpers.
def hypot(x,y): return sqrt(x*x+y*y)
def dist(P,Q): return hypot(P[0]-Q[0],P[1]-Q[1])
def line_dist(P,U,V):
    num=abs((V[0]-U[0])*(U[1]-P[1])-(U[0]-P[0])*(V[1]-U[1]))
    return num/dist(U,V)
def defect(A,B,C,w,la):
    P=(w[0]*A[0]+w[1]*B[0]+w[2]*C[0],w[0]*A[1]+w[1]*B[1]+w[2]*C[1])
    a=dist(B,C); b=dist(C,A); c=dist(A,B)
    R=[dist(P,A),dist(P,B),dist(P,C)]
    rr=[line_dist(P,B,C),line_dist(P,C,A),line_dist(P,A,B)]
    lhs=(R[1]+R[2]-la*rr[0])/a+(R[2]+R[0]-la*rr[1])/b+(R[0]+R[1]-la*rr[2])/c
    rhs=(D(4)-la)*r3/D(2)
    return lhs-rhs

# Isosceles interior representative at lambda=0.58.
# theta satisfies tan(theta/2)=t; sin and cos from the half-angle formulas.
sin_theta=D(2)*t/(D(1)+t*t)
cos_theta=(D(1)-t*t)/(D(1)+t*t)
A=(D(0),cos_theta); B=(-sin_theta,D(0)); C=(sin_theta,D(0))
d=D('1e-6')
f_low=defect(A,B,C,[D(1)-D(2)*d,d,d],D('0.58'))
assert f_low < D('-0.004')

# Slender right-triangle interior representative at lambda=2.01.
eps=D('1e-3'); di=eps*eps
A=(D(0),D(0)); B=(D(1),D(0)); C=(D(1),eps)
f_high=defect(A,B,C,[D('0.4')-di,D('0.6'),di],D('2.01'))
assert f_high < D('-3')

# Boundary scaled-limit diagnostic, q0=0.6 and lambda=2.01.
def boundary_defect(eps,la,q0=D('0.6')):
    A=(D(0),D(0)); B=(D(1),D(0)); C=(D(1),eps); P=(q0,D(0))
    a=dist(B,C); b=dist(C,A); c=dist(A,B)
    R=[dist(P,A),dist(P,B),dist(P,C)]
    rr=[line_dist(P,B,C),line_dist(P,C,A),line_dist(P,A,B)]
    return (R[1]+R[2]-la*rr[0])/a+(R[2]+R[0]-la*rr[1])/b+(R[0]+R[1]-la*rr[2])/c-(D(4)-la)*r3/D(2)
target=(D(2)-D('2.01'))*(D(1)-D('0.6'))
for ep,tol in [(D('1e-3'),D('0.004')),(D('1e-4'),D('0.0004')),(D('1e-5'),D('0.00004'))]:
    scaled=ep*boundary_defect(ep,D('2.01'))
    assert abs(scaled-target) < tol
print('VERIFY_OK')
print('t_star =',t)
print('lambda_star =',lam)
print('lower_interior_defect =',f_low)
print('upper_interior_defect =',f_high)
