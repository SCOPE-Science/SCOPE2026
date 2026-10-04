from fractions import Fraction
from math import comb

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def eval_poly(c,x):
    return sum(v*(x**i) for i,v in enumerate(c))

# P6/P0 = 81/80 * product(x+3,x+2,x+1,x-1,x-2)/x^5.
p=[1]
for a in (3,2,1,-1,-2):
    p=mul(p,[a,1])
# Check 81*product - 80*x^5 = (x-3)Q(x).
left=[81*v for v in p]
left += [0]*(6-len(left))
left[5]-=80
Q=[-324,-216,333,246,1]
right=mul([-3,1],Q)
assert left==right
# Check Q = x^4+246x^3+333(x-4)^2+2448(x-4)+4140.
for x in range(-20,21):
    q=eval_poly(Q,x)
    dec=x**4+246*x**3+333*(x-4)**2+2448*(x-4)+4140
    assert q==dec
# Supplementary exact stress tests only.
def alpha(n,i):
    probs=[Fraction(comb(n,k)*3**k*(n-3)**(n-k), n**n) for k in range(n+1)]
    return sum(probs[:4-i])-sum(probs[3+i:])
for n in range(6,31):
    a=[alpha(n,i) for i in (1,2,3)]
    if n==6:
        assert a==[0,0,0]
    else:
        assert a[0]>0 and a[2]<0
        assert (a[1]>=0 and a[0]>=0 and a[2]<=0) or (a[1]<0 and a[0]>=0 and a[1]<=0 and a[2]<=0)
print('VERIFY_OK')
