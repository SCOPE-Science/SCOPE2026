import math, random

def F(k):
    num=-4*k*k+(k*k-1)**2*math.cos(2*k)-(k*k+1)**2*math.cos(4*k)
    den=(k*k-1)**2*math.sin(k)**2
    return num/den

def exact_member(k):
    if k <= 1 or abs(math.sin(k))<1e-14:
        return False
    s=math.sin(k)**2
    a=1/(k*k+1)
    c=2*k*k/(k*k+1)**2
    b=k*k/(k*k+1)
    return (a <= s <= c) or (0.5 <= s <= b)

def bisect(fun, lo, hi, it=60):
    flo=fun(lo); fhi=fun(hi)
    if flo==0: return lo
    if fhi==0: return hi
    if flo*fhi>0: raise RuntimeError((lo,hi,flo,fhi))
    for _ in range(it):
        mid=(lo+hi)/2; fm=fun(mid)
        if flo*fm<=0: hi=mid; fhi=fm
        else: lo=mid; flo=fm
    return (lo+hi)/2

def cell_measure(n):
    # One momentum-period cell, with n>=1
    L=n*math.pi; R=(n+1)*math.pi; C=(n+0.5)*math.pi
    a=lambda k: math.sin(k)**2-1/(k*k+1)
    q=lambda k: math.sin(k)**2-2*k*k/(k*k+1)**2
    cg=lambda k: math.cos(k)**2-1/(k*k+1)
    iaL=bisect(a,L+1e-12,L+math.pi/4)
    iqL=bisect(q,L+1e-12,L+math.pi/4)
    iqR=bisect(q,L+3*math.pi/4,R-1e-12)
    iaR=bisect(a,L+3*math.pi/4,R-1e-12)
    gL=bisect(cg,L+math.pi/4,C-1e-12)
    gR=bisect(cg,C+1e-12,L+3*math.pi/4)
    narrow=(iqL-iaL)+(iaR-iqR)
    gap=gR-gL
    wide=math.pi/2-gap
    return narrow+wide,narrow,gap

# Exact-criterion consistency checks
mx=0.0
for _ in range(1000):
    k=1.1+50*random.Random(12345+_).random()
    if abs(math.sin(k))<1e-8: continue
    member=(-2 <= F(k) <= 2)
    if member != exact_member(k):
        raise AssertionError((k,F(k),member,exact_member(k)))

for n in (50,200,1000):
    m,nb,g=cell_measure(n)
    N=n*math.pi
    print(n, 'narrow_scaled', nb*N, 'target',2*(math.sqrt(2)-1), 'gap_scaled', g*((n+0.5)*math.pi),'target',2)

def residual(Ncells):
    S=0.0
    for n in range(1,Ncells+1):
        S += cell_measure(n)[0]
    K=(Ncells+1)*math.pi
    base=(K-math.pi)/2
    return K,S-base
K1,r1=residual(500)
K2,r2=residual(4000)
coef=(r2-r1)/(math.log(K2)-math.log(K1))
target=2*(math.sqrt(2)-2)/math.pi
print('coef_slope',coef,'target',target,'difference',coef-target)
assert abs(coef-target)<1e-5
print('VERIFY_OK')
