"""Independent finite-word and exact-probability checks for dyadic fibers."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, pi

P,QDOWN=Q(2,3),Q(1,3)

def merge(intervals):
    out=[]
    for a,b in sorted(intervals):
        if not out or a > out[-1][1]:
            out.append([a,b])
        elif b > out[-1][1]:
            out[-1][1]=b
    return [(a,b) for a,b in out]

def explicit_image(intervals,digit):
    out=[]
    for lo,hi in intervals:
        if digit==0: out.append((lo/2,hi/2))
        elif digit==1: out.append((Q(1,2)+lo/2,Q(1,2)+hi/2))
        else:
            if lo<Q(1,2):
                a,b=lo,min(hi,Q(1,2))
                if a<b:out.append((2*a,2*b))
            if hi>Q(1,2):
                a,b=max(lo,Q(1,2)),hi
                if a<b:out.append((2*a-1,2*b-1))
    return merge(out)

def state_step(k,j,d):
    if d==0:return k+1,j
    if d==1:return k+1,j+2**k
    if k==0:return 0,0
    return k-1,j%(2**(k-1))

for n in range(9):
    word_total=Q(0)
    for digits in product((0,1,2),repeat=n):
        k,j=0,0
        actual=[(Q(0),Q(1))]
        for d in digits:
            k,j=state_step(k,j,d)
            actual=explicit_image(actual,d)
        expected=[(Q(j,2**k),Q(j+1,2**k))]
        assert actual==expected,(digits,actual,expected)
        word_total+=Q(1,2**k)
    word_total/=3**n
    # Independent Markov chain on dyadic depth.
    probs=[Q(1)]+[Q(0)]*n
    for _ in range(n):
        new=[Q(0)]*(n+1)
        for k,pr in enumerate(probs):
            if not pr: continue
            if k<n:new[k+1]+=P*pr
            new[max(k-1,0)]+=QDOWN*pr
        probs=new
    moment=sum(pr/Q(2**k) for k,pr in enumerate(probs))
    assert moment==word_total,(n,moment,word_total)
    print('n=%d words=%d mean_fiber=%s P_depth_zero=%s'%(n,3**n,moment,probs[0]))

# Generating-function identity:  A(z)=2/[1-2qz+sqrt(1-4pqz^2)].
# As a coefficient identity, (1-qz)A-pzT A=1 and T=z(q+pT^2).
N=22
T=[Q(0)]*(N+1)
A=[Q(0)]*(N+1);A[0]=1
for n in range(1,N+1):
    T[n]=(QDOWN if n==1 else Q(0)) + P*sum(T[i]*T[n-1-i] for i in range(n))
    A[n]=QDOWN*A[n-1]+P*sum(T[j]*A[n-1-j] for j in range(1,n))
probs=[Q(1)]+[Q(0)]*(N+1)
for n in range(N+1):
    assert probs[0]==A[n],(n,probs[0],A[n])
    if n<N:
        new=[Q(0)]*(N+2)
        for k,pr in enumerate(probs):
            if pr:
                new[k+1]+=P*pr
                new[max(k-1,0)]+=QDOWN*pr
        probs=new

# Decay envelope: compare exact distribution at large n to derived two-branch asymptotics.
RINV=2*sqrt(2)/3
DPLUS=1-1/sqrt(2);DMINUS=1+1/sqrt(2)
probs=[1.0]
for n in range(1,1301):
    new=[0.0]*(len(probs)+1)
    for k,pr in enumerate(probs):
        new[k+1]+=float(P)*pr
        new[max(0,k-1)]+=float(QDOWN)*pr
    probs=new
    if n in [500,800,1300]:
        E=sum(pr*2.0**(-k) for k,pr in enumerate(probs))
        factor=sqrt(2/pi)/3*(RINV**n)*n**(-1.5)
        approx=factor*(1/(DPLUS**2*(1-RINV)) + (-1)**n/(DMINUS**2*(1+RINV)))
        ratio=E/approx
        assert 0.88<ratio<1.05,(n,ratio)
        print('n=%d moment=%.18g asymptotic=%.18g ratio=%.10f'%(n,E,approx,ratio))
print('DYADIC_FIBER_EXACT_AND_ASYMPTOTIC_CHECKS_OK')
