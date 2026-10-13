from fractions import Fraction as F

# Polynomials are coefficient lists in ascending powers.
def add(a,b):
    n=max(len(a),len(b)); c=[F(0) for _ in range(n)]
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c

def sub(a,b):
    return add(a,[-x for x in b])

def mul(a,b):
    c=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def scale(a,s): return [s*x for x in a]

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

# T=(3q^2+2q+3)/8; PB=(9q^8+60q^2+59)/128; PK=(3q^8+5)/8.
T=[F(3,8),F(1,4),F(3,8)]
PB=[F(59,128),F(0),F(60,128)]+[F(0)]*5+[F(9,128)]
PK=[F(5,8)]+[F(0)]*7+[F(3,8)]

FB=[F(-11),F(21),F(9),F(9),F(9),F(9),F(9),F(9)]
FK=[F(-2),F(0),F(3),F(3),F(3),F(3),F(3),F(3)]
one_minus_q=[F(1),F(-1)]

assert trim(sub(T,PB))==trim(scale(mul(one_minus_q,FB),F(1,128)))
assert trim(sub(T,PK))==trim(scale(mul(one_minus_q,FK),F(1,8)))

q=F(3,4)
def peval(a,x):
    s=F(0)
    for c in reversed(a): s=s*x+c
    return s

assert peval(FB,q)>0
assert peval(FK,q)>0
assert F(21)*q-F(11)>0
assert F(3)*(q*q+q*q*q)-F(2)==F(61,64)>0

# Exact endpoint purities and the threshold T(3/4)=99/128.
assert peval(PB,q)==F(6137513,8388608)
assert peval(PK,q)==F(347363,524288)
assert peval(T,q)==F(99,128)
assert peval(PB,q)<peval(T,q)
assert peval(PK,q)<peval(T,q)

# Witness spectrum at q=3/4 is {0,1/8,7/8}; its mean input energy is 3/2.
assert (F(1)-q)/2==F(1,8)
assert (F(1)+q)/2==F(7,8)
assert F(1,2)*1+F(1,2)*2==F(3,2)

print('VERIFY_OK')
print('endpoint_q = 3/4')
print('binomial_purity =', peval(PB,q))
print('kappa_purity =', peval(PK,q))
print('largest_eigenvalue_threshold_purity =', peval(T,q))
print('proved_interval = 3/4 <= q < 1, equivalently 0 < t <= log(4/3)')
