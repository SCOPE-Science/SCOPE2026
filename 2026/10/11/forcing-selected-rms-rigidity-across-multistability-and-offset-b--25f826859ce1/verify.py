from fractions import Fraction

# Minimal exact polynomial arithmetic in variables (x,y,b).
# A polynomial is {exponent_tuple: Fraction coefficient}.
def add(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,Fraction(0))+c
        if r[m]==0:
            del r[m]
    return r

def neg(p):
    return {m:-c for m,c in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(a+b for a,b in zip(m,n))
            r[k]=r.get(k,Fraction(0))+c*d
    return {m:c for m,c in r.items() if c}

def scale(p,c):
    c=Fraction(c)
    return {m:c*v for m,v in p.items() if c*v}

one={(0,0,0):Fraction(1)}
x={(1,0,0):Fraction(1)}
y={(0,1,0):Fraction(1)}
b={(0,0,1):Fraction(1)}

# Qdot = zdot - (x/a) xdot = (xy-b) - x(y-x).
qdot=sub(sub(mul(x,y),b),mul(x,sub(y,x)))
target=sub(mul(x,x),b)
assert qdot == target, (qdot,target)

# Activity algebra: (y-x)^2 = y^2 - 2xy + x^2.
lhs=mul(sub(y,x),sub(y,x))
rhs=add(sub(mul(y,y),scale(mul(x,y),2)),mul(x,x))
assert lhs == rhs, (lhs,rhs)

# Published parameter specialization.
a0=Fraction(31)
b0=Fraction(25)
assert a0*a0 == 961
assert 5*5 == b0

# Finite-time identity is the integrated form Q(T)-Q(0)=int(x^2-b)dt;
# no numerical trajectory is used here.
print('VERIFY_OK')
