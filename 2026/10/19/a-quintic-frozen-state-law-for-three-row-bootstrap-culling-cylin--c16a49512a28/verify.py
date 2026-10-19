"""Self-contained exact verification of 3-core fixed-state counts on three-row cyclic grids.
Python 3 standard library only. The infinite-limit proof is in RESULT.md.
"""
from itertools import permutations, product
from collections import Counter
from math import isclose, log

# Each symbolic polynomial is a dict (power_lambda, power_a, power_b) -> integer.
ZERO = {}
ONE = {(0,0,0): 1}
L = {(1,0,0): 1}
A = {(0,1,0): 1}
B = {(0,0,1): 1}

def add(x,y):
    d = dict(x)
    for e,c in y.items(): d[e] = d.get(e,0)+c
    return {e:c for e,c in d.items() if c}

def neg(x): return {e:-c for e,c in x.items()}

def mul(x,y):
    d = {}
    for (i,j,k),c in x.items():
        for (u,v,w),d0 in y.items():
            e = (i+u,j+v,k+w)
            d[e] = d.get(e,0)+c*d0
    return {e:c for e,c in d.items() if c}

def powp(x,n):
    out=ONE
    for _ in range(n): out=mul(out,x)
    return out

def scale(x,c): return {e:c*d for e,d in x.items() if c*d}

def det_of_lambda_minus(matrix):
    n=len(matrix)
    total=ZERO
    for pi in permutations(range(n)):
        inv=sum(pi[i]>pi[j] for i in range(n) for j in range(i+1,n))
        prod=ONE
        for i,j in enumerate(pi):
            entry=add(L if i==j else ZERO, neg(matrix[i][j]))
            prod=mul(prod,entry)
            if not prod:break
        total=add(total,scale(prod,-1 if inv%2 else 1))
    return total

# Orbit quotient for four colour-invariant pair states and the three D-colour orbits.
# Ordered EE, EF, FE, FF, DD, DF, FD. D is any one of three missing-row types.
Q7 = [
  [ONE,ONE,ZERO,ZERO,ZERO,ZERO,ZERO],
  [ZERO,ZERO,ZERO,B,ZERO,ZERO,ZERO],
  [ONE,ONE,ZERO,ZERO,ZERO,ZERO,ZERO],
  [ZERO,ZERO,B,B,ZERO,ZERO,scale(B,3)],
  [ZERO,ZERO,ZERO,ZERO,A,A,ZERO],
  [ZERO,ZERO,ZERO,B,ZERO,ZERO,scale(B,2)],
  [ZERO,ZERO,ZERO,ZERO,A,A,ZERO],
]
# On each copy of the standard two-dimensional colour representation.
R3 = [[A,A,ZERO],[ZERO,ZERO,neg(B)],[A,A,ZERO]]

P = add(add(powp(L,5), neg(mul(powp(L,4), add(ONE,add(A,B))))),
        add(mul(powp(L,3),add(add(A,B),neg(mul(A,B)))),
        add(mul(powp(L,2),add(add(mul(A,B),neg(mul(A,powp(B,2)))),neg(powp(B,2)))),
        add(scale(mul(L,mul(A,powp(B,2))),2),scale(mul(A,powp(B,3)),2)))))
Q = add(powp(L,2),add(neg(mul(L,A)),mul(A,B)))
assert det_of_lambda_minus(Q7)==mul(powp(L,2),P)
assert det_of_lambda_minus(R3)==mul(L,Q)
print('Exact symbolic orbit and standard-representation characteristic-polynomial identities: PASS')

symbols=(0,3,5,6,7)
def allowed(x,y,z):
    if y==0:return True
    if y==7:return (x|z)==7
    if y.bit_count()==2:return (x&y)==y and (z&y)==y
    return False

def physical_stable(col):
    n=len(col)
    for x in range(n):
        for y in range(3):
            if (col[x]>>y)&1:
                neighbours = ((col[x]>>((y+1)%3))&1)+((col[x]>>((y-1)%3))&1)
                neighbours+=((col[(x-1)%n]>>y)&1)+((col[(x+1)%n]>>y)&1)
                if neighbours < 3:return False
    return True

for n in range(3,7):
    direct=Counter()
    for mask in range(1<<(3*n)):
        cols=tuple((mask>>(3*x))&7 for x in range(n))
        if physical_stable(cols):direct[mask.bit_count()]+=1
    transfer=Counter()
    for cols in product(symbols,repeat=n):
        if all(allowed(cols[(i-1)%n],cols[i],cols[(i+1)%n]) for i in range(n)):
            transfer[sum(t.bit_count() for t in cols)]+=1
    assert direct==transfer,(n,direct,transfer)
    print('n=',n,'total=',sum(direct.values()),'occupancy-graded counts=',sorted(direct.items()))

# Physical occupation-fugacity polynomial P(lambda,z) from a=z**2, b=z**3.
coeff={(5,0):1,(4,3):-1,(4,2):-1,(4,0):-1,(3,5):-1,
       (3,3):1,(3,2):1,(2,8):-1,(2,6):-1,(2,5):1,
       (1,8):2,(0,11):2}
def derivative_eval(dl,dz,ll,z):
    total=0.0
    for (i,j),c in coeff.items():
        if i>=dl and j>=dz:
            f=1
            for t in range(dl):f*=i-t
            for t in range(dz):f*=j-t
            total+=c*f*ll**(i-dl)*z**(j-dz)
    return total

def p_at(x):return derivative_eval(0,0,x,1.)
lo,hi=2.6,2.7
assert p_at(lo)<0<p_at(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if p_at(mid)>0:hi=mid
    else:lo=mid
alpha=(lo+hi)/2
lprime=-derivative_eval(0,1,alpha,1)/derivative_eval(1,0,alpha,1)
lsecond=-(derivative_eval(0,2,alpha,1)+2*derivative_eval(1,1,alpha,1)*lprime+derivative_eval(2,0,alpha,1)*lprime*lprime)/derivative_eval(1,0,alpha,1)
mu=lprime/alpha
sigma2=(lsecond+lprime)/alpha-mu**2
assert isclose(alpha,2.60749099620413,abs_tol=1e-11)
assert isclose(mu/3,0.821488917669425,abs_tol=1e-11)
assert isclose(sigma2,0.44512511235352,abs_tol=1e-10)
assert sigma2>0
print('Perron root=',repr(alpha),'entropy/site=',log(alpha)/3,'occupation/site=',mu/3,'variance/column=',sigma2)
print('VERIFY_OK')
