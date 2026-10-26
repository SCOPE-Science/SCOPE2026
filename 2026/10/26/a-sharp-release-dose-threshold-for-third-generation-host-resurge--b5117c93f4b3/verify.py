"""Independent recurrence/composition checks for a single Nicholson-Bailey parasitoid introduction.
Scientific mathematics only: no unbounded external dependencies.
"""
import math,random
from scipy.optimize import brentq

random.seed(10232026)
def host_after(R,a,c,H,P,q,n):
    P+=q
    for k in range(n):
        e=math.exp(-a*P)
        H,P=R*H*e,c*H*(1-e)
    return H

def direct_formula(R,a,c,H,P,q):
    W=a*c*H
    Y=W*math.exp(-a*(P+q))
    return R**3*H*math.exp(-a*(P+q)-W+(1-R)*Y+R*Y*math.exp(Y-W))

def G(R,W,Y):
    return -1+(R-1)*Y-R*Y*(1+Y)*math.exp(Y-W)

count=0
for _ in range(5000):
    R=math.exp(random.uniform(-1.5,1.5))
    a=math.exp(random.uniform(-1.0,0.6))
    c=math.exp(random.uniform(-1.0,0.6))
    H=math.exp(random.uniform(-1.5,2))
    P=random.uniform(0.02,3.3)
    q=random.uniform(0,2)
    W=a*c*H
    Y=W*math.exp(-a*(P+q))
    x=host_after(R,a,c,H,P,q,3)
    y=direct_formula(R,a,c,H,P,q)
    assert math.isclose(x,y,rel_tol=4e-13,abs_tol=1e-13), ('composition',R,a,c,H,P,q,x,y)
    eps=1e-5
    d=(math.log(host_after(R,a,c,H,P,q+eps,3))-math.log(host_after(R,a,c,H,P,q-eps,3)))/(2*eps*a)
    assert math.isclose(d,G(R,W,Y),rel_tol=3e-6,abs_tol=2e-6),('derivative', d,G(R,W,Y))
    assert host_after(R,a,c,H,P,q+0.15,1)<host_after(R,a,c,H,P,q,1)
    assert host_after(R,a,c,H,P,q+0.15,2)<host_after(R,a,c,H,P,q,2)
    count+=1

for R in [1.001,1.03,1.2,1.5,2,3,5,20]:
    aa=R-1
    root=brentq(lambda y:aa*y*y*(y+2)-(y*y+3*y+1),1/aa+1e-6,max(6+15/aa,20))
    Wcrit=root+math.log(R*root*(1+root)/(aa*root-1))
    assert abs(G(R,Wcrit,root))<1e-10
    assert abs((R-1)-R*math.exp(root-Wcrit)*(1+3*root+root**2))<1e-10
    for scale in [0.75,0.99,1.0,1.01,1.2,2.]:
        W=Wcrit*scale
        ys=[W*i/10000 for i in range(1,10000)]
        vals=[G(R,W,y) for y in ys]
        if scale<1: assert max(vals)<0
        if scale>1: assert max(vals)>0
        assert G(R,W,W)<0 and G(R,W,0)<0

# Explicit analytic sign witness R=3,a=c=1,H0=6,P0=log3, q=log2.
a=c=1;R=3;H=6;P=math.log(3)
H1_0=host_after(R,a,c,H,P,0,1);H1_q=host_after(R,a,c,H,P,math.log(2),1)
H2_0=host_after(R,a,c,H,P,0,2);H2_q=host_after(R,a,c,H,P,math.log(2),2)
H3_0=host_after(R,a,c,H,P,0,3);H3_q=host_after(R,a,c,H,P,math.log(2),3)
assert H1_q < H1_0 and H2_q < H2_0 and H3_q > H3_0
lr=2-math.log(2)+3*math.exp(-5)-6*math.exp(-4)
assert math.isclose(math.log(H3_q/H3_0),lr,abs_tol=1e-13)
print('PASS',count,'randomized recurrence/exact expression/derivative and early generation monotonicity checks; 48 critical-threshold tests')
print('exact witness',H1_0,H1_q,H2_0,H2_q,H3_0,H3_q,lr)
print('R3 threshold critical',next((1 for rr in [R] if rr==3),None))
