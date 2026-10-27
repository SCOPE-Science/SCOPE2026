"""Exact finite-grid Ising cross-atom Poisson inversion certificate (stdlib)."""
from math import comb, exp, log, fsum
from decimal import Decimal, getcontext
getcontext().prec=70

def trim(v):
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def power(a,n):
    v=[1]
    for _ in range(n): v=mul(v,a)
    return v

a=[1,0,0,1];b=[1,1];t4=[0,0,0,0,1]
p=[add(power(a,k),mul(t4,power(b,k))) for k in range(5)]
h=sub(mul(p[0],mul(power(p[2],6),p[4])),mul(power(p[1],4),power(p[3],4)))
q=[-1,12,-78,352,-1221,3432,-8074,16236,-28305,43180,-57950,68532,-71207,64384,-49506,30592,-12493,-980,8324,-10228,8732,-5948,3370,-1592,624,-196,48,-8,1]
fac=neg(mul([0]*8+[1],mul(power([-1,1],4),power([1,1],16))))
assert h==mul(fac,q)
r=[sum(q[k]*comb(28-k,j-k) for k in range(j+1)) for j in range(29)]
assert r==[-1,-16,-132,-740,-3146,-10752,-30614,-74360,-156642,-289544,-473518,-688884,-894228,-1036304,-1069782,-977884,-782196,-534968,-297388,-115684,-7447,36724,40606,28052,14449,5680,1648,320,32]
assert sum(x*y<0 for x,y in zip(r,r[1:]))==1
assert sum(q)==32

def eval_poly(c,t):
    ret=type(t)(0)
    for x in c[::-1]: ret=ret*t+x
    return ret
l=Decimal(0);u=Decimal(1)
for _ in range(260):
    mid=(l+u)/2
    if eval_poly(q,mid)<0:l=mid
    else:u=mid
troot=(l+u)/2; beta=-(troot.ln())/2
assert Decimal('0.6276872898128175')<troot<Decimal('0.6276872898128176')
print('polynomial factorization: PASS; deg(H)=',len(h)-1,'deg(Q)=',len(q)-1,'deg(R)=',len(r)-1)
print('Descartes transformed signs: 21 negative, 8 positive; exactly one positive root: PASS')
print('root t*=',troot)
print('beta*=',beta)
# Independent 2^9 configuration enumeration of local avoidance probabilities.
V=tuple(range(9));S=(1,3,4,5,7)
edges=[(i,j) for i in V for j in V if (i//3==j//3 and j==i+1) or (j==i+3)]
assert len(edges)==12

def direct(beta):
    weights=[]
    for m in range(512):
        cut=sum(((m>>i)&1)!=((m>>j)&1) for i,j in edges)
        weights.append(exp(-2*beta*cut))
    z=fsum(weights)
    # F(B) = sum configurations whose positive spins are a subset of B; true avoidance outside B.
    val=0.
    for mask in range(32):
        B=sum(1<<S[j] for j in range(5) if mask>>j&1)
        constrained=fsum(weights[m] for m in range(512) if m&~B==0)
        val+=((-1)**(5-mask.bit_count()))*log(constrained/z)
    return val

def compressed(beta):
    t=exp(-2*beta)
    f=lambda k:(1+t**3)**k+t**4*(1+t)**k
    return log(f(0))+6*log(f(2))+log(f(4))-4*log(f(1))-4*log(f(3))
for bt in [.05,.2,.24,.6,1.0]:
    d=direct(bt);c=compressed(bt)
    assert abs(d-c)<2e-11,(bt,d,c)
    print('beta=',bt,'direct=',format(d,'.12g'),'formula=',format(c,'.12g'),'PASS')
print('All exact and independent finite-state checks PASSED.')
