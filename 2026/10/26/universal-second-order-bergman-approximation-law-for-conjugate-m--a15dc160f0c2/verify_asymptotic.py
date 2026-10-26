"""Exact rational algebra checks for fixed-m Bergman Hankel spectral asymptotics."""
from fractions import Fraction as Q

def mul(u,v):
    return [sum(u[i]*v[k-i] for i in range(k+1)) for k in range(3)]

def product(m,t,up):
    out=[Q(1),Q(0),Q(0)]
    for j in range(1,m+1):
        a=j if up else 1-j
        b=1+j if up else 2-j
        w=t+1
        factor=[t/w,Q(a,1)/w-t*b/w**2,t*b*b/w**3-Q(a*b,1)/w**2]
        out=mul(out,factor)
    return out

assertions=0
for m in range(2,17):
  for t in [Q(1,4),Q(1,2),Q(1),Q(3,2),Q(7,3),Q(m-1,2)]:
    diff=[a-b for a,b in zip(product(m,t,True),product(m,t,False))]
    F=Q(m*m)*t**(m-1)/(1+t)**(m+1)
    G=Q(m*m,2)*t**(m-2)*(2*t*t-2*(m+1)*t+m-1)/(1+t)**(m+2)
    assert diff[0]==0 and diff[1]==F and diff[2]==G
    assertions+=3
  t=Q(m-1,2)
  F=Q(m*m)*t**(m-1)/(1+t)**(m+1)
  G=Q(m*m,2)*t**(m-2)*(2*t*t-2*(m+1)*t+m-1)/(1+t)**(m+2)
  assert G==-F
  assertions+=1
print(f'PASS: {assertions} exact rational coefficient and peak checks; m=2..16')

# Independent exact-moment identity: for integer alpha the Beta moments
# M_k = k! (alpha+1)!/(k+alpha+1)! are rational.
def moment(k,alpha):
    v=Q(1)
    for j in range(1,k+1):
        v*=Q(j,alpha+1+j)
    return v

def eigen_from_products(n,alpha,m):
    u=Q(1)
    for j in range(1,m+1): u*=Q(n+j,n+alpha+1+j)
    if n < m:return u
    v=Q(1)
    for j in range(m): v*=Q(n-j,n+alpha+1-j)
    return u-v

for m in range(3,10):
    for a in [5,13,70]:
        for n in range(0,45):
            v=moment(n+m,a)/moment(n,a)
            if n>=m: v-=moment(n,a)/moment(n-m,a)
            assert eigen_from_products(n,a,m)==v and v>=0
            assertions+=2
print(f'PASS: {assertions} total exact rational tests, including moment identities.')
