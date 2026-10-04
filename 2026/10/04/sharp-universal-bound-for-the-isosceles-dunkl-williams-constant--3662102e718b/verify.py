from fractions import Fraction as Q

# Exact scalar identity at the maximizing point and exact l_infinity^2 witness.
def linf(v):
    return max(abs(z) for z in v)

def add(x,y):
    return tuple(a+b for a,b in zip(x,y))

def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))

def scale(c,x):
    return tuple(c*a for a in x)

for k in range(0,101):
    t=Q(k,100)
    envelope=Q(2)+t-t*t
    remainder=Q(9,4)-envelope
    assert remainder==(t-Q(1,2))**2
    assert envelope<=Q(9,4)

x=(Q(0),Q(1))
y=(Q(1),Q(1))
u=add(x,y)
v=sub(x,y)
a=linf(u)
b=linf(v)
assert (a,b)==(Q(2),Q(1))
diff=sub(scale(Q(1,a),u),scale(Q(1,b),v))
value=Q(a+b,2)*linf(diff)
assert value==Q(9,4)
print('VERIFY_OK')
