"""Exact finite algebra checks for the two-patch anonymous-occupancy theorem.
Run: python3 CHECK.py (standard library only).
The proof in RESULT.md establishes all-parameter statements; these checks are safeguards.
"""
from fractions import Fraction as F
from itertools import product


def one_joint(p,z):
    # P(X(0)=x,X(t)=y), with stationary occupancy p and e^(-lambda*t)=z.
    ans={}
    for x,y in product((0,1),repeat=2):
        pi=p if x else 1-p
        nextp=p+(F(x)-p)*z
        ans[x,y]=pi*(nextp if y else 1-nextp)
    return ans


def moments(p,q,z,w):
    j1,j2=one_joint(p,z),one_joint(q,w)
    mean=p+q
    first=F(0); second=F(0); third=F(0); prob0=F(0)
    for (x,xt),(y,yt) in product(j1.items(),j2.items()):
        mass=xt*yt
        a=x[0]+y[0]-mean
        b=x[1]+y[1]-mean
        first+=mass*a
        second+=mass*a*b
        third+=mass*a*a*b
        if x[0]+y[0]==0: prob0+=mass
    return first,second,third,prob0

n=0
for p,q,z,w in product([F(1,4),F(1,3),F(1,2),F(2,3),F(3,4)],
                       [F(1,5),F(1,2),F(4,5)],
                       [F(1,3),F(2,5),F(1)],
                       [F(1,5),F(3,4)]):
    first,cov,t,pr0=moments(p,q,z,w)
    v1=p*(1-p);v2=q*(1-q)
    assert first==0
    assert cov==v1*z+v2*w
    assert t==v1*(1-2*p)*z+v2*(1-2*q)*w
    assert pr0==(1-p)*(1-q)
    n+=1

# Two distinct, positive decay rates and complementary occupancies:
p,q=F(1,4),F(3,4)
l1,l2=F(2),F(5)
p2,q2=q,p
z,w=F(1,3),F(1,7)
_,cov_a,third_a,_=moments(p,q,z,w)
_,cov_b,third_b,_=moments(p2,q2,z,w)
assert cov_a==cov_b and third_a==-third_b and third_a!=0
assert p+q==p2+q2
assert l1*p+l2*q!=l1*p2+l2*q2

# Equal decay rates: sum and lag-zero covariance recover the roots uniquely.
for p,q in product([F(1,6),F(1,4),F(2,5),F(3,4)], repeat=2):
    m=p+q
    W=p*(1-p)+q*(1-q)
    prod=(W-m+m*m)/2
    assert p*p-m*p+prod==0 and q*q-m*q+prod==0

# In the exceptional case, one nonzero-time third-moment sign resolves the labels.
for p in [F(1,8),F(1,3),F(3,5),F(7,8)]:
    if p==F(1,2): continue
    q=1-p
    v=p*(1-p)
    assert v*(1-2*p)*(z-w)!=0

print('VERIFY_OK exact_two_time_joint_cases=%d complementary_ambiguity=1 equal_rate_reconstruction=16 third_order_resolution=4'%n)
