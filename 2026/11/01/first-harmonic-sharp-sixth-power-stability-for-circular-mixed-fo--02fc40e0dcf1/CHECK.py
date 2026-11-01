"""Exact integer-arithmetic interval certificate for circle Bessel sixth moments.
No external dependencies; requires Python 3. All divisions in interval propagation
are outward integer floors or ceilings. The Bessel truncation is justified below.
"""
from math import factorial
S=10**90
NGRID=2000 # 0 <= r <= 40; r=j/50
TERMS=150
assert 400*10 < TERMS*(TERMS+1)

def bessel_interval(k,j):
    # J_k(j/50) Taylor terms: (j/100)^(2n+k)/(n!(n+k)!)
    den=100**k*factorial(k)
    lo=(S*j**k)//den
    hi=(S*j**k+den-1)//den
    outlo=outhi=0
    for n in range(TERMS):
        if n%2==0:
            outlo+=lo;outhi+=hi
        else:
            outlo-=hi;outhi-=lo
        d=10000*(n+1)*(n+k+1)
        lo=lo*j*j//d
        hi=(hi*j*j+d-1)//d
    # error from alternating tail: magnitude <= first omitted term if n>=20.
    # Rounding interval of omitted term <= hi/S. Bound enlarges each side by hi.
    return outlo-hi, outhi+hi

def simpson_bracket(k):
    low=high=0
    for j in range(NGRID+1):
        l,u=bessel_interval(k,j)
        amin=0 if l<=0<=u else min(abs(l),abs(u))
        amax=max(abs(l),abs(u))
        w=1 if j in (0,NGRID) else (4 if j%2 else 2)
        low+= w*j*amin**6
        high+=w*j*amax**6
    return low,high

# Exact constants Simpson: integral over [0,40], h=1/50, x_j=j/50.
# composite Simpson T = sum_j (w_j j/7500) J_k(j/50)^6.
DEN=7500*S**6
# Fourth derivative of r*J_k(r)^6 bounded by 4*6^3 + 40*6^4,
# from all derivatives of integer-order J_k bounded by 1 via angular formula.
# Simpson error is < 1/500 (exact integer check).
E_NUM=40*(4*216+40*1296)
E_DEN=180*50**4
assert E_NUM*500 < E_DEN
count=1
for k in range(1,12):
    lo,hi=simpson_bracket(k)
    if k==1:
        assert lo*500 > DEN*51, ('lower failed', k)
        print('SIMPSON k=1 > 51/500')
    else:
        assert hi*100 < DEN*7, ('upper failed',k)
        print(f'SIMPSON k={k} < 7/100')
    count+=1
# For k<=11, r>=40, use the bound |J_k(r)|^2<=2/(pi sqrt(r²-k²)) from Xu Lemma 3.7;
# tail <=(2/pi)^3/sqrt(1600-k²) < (8/27)/38 < 1/100.
assert 1600-11**2 > 38**2
assert 800 < 27*38
# k>=12, the high-mode inequality I_k(5)<13/40 and sup|J_k|<7/(10*k^(1/3)) give
# I_k(6)<91/(400*k^(1/3))<=91/(400*12^(1/3)) < 1/10.
assert 91**3*1000 < 400**3*12
print('CHECK_OK',count+3)
