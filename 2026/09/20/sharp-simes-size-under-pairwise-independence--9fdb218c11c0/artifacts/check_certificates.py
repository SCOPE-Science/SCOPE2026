from fractions import Fraction as F
from itertools import product

# Category order: A=(0,r], B=(r,2r], C=(2r,3r], D=(3r,1], r=alpha/3.
TYPES = [t for t in product(range(4), repeat=4) if sum(t) == 3]
PAIRS = [(i,j) for i in range(4) for j in range(i,4)]

Z = [
    [1,3,3,3,3,0,0,3,0,0],
    [1,2,3,3,2,1,1,2,0,0],
    [1,2,2,4,1,2,2,1,0,0],
]

def reject(t):
    a,b,c,d = t
    return int(a >= 1 or a+b >= 2 or d == 0)

def psi(t,i,j):
    if i == j:
        return F(t[i]*(t[i]-1), 6)
    return F(t[i]*t[j], 6)

# Polynomial c0+c1*r+c2*r^2, exact rational coefficients.
def padd(x,y): return tuple(x[k]+y[k] for k in range(3))
def pscale(c,x): return tuple(c*v for v in x)
def pmul(x,y):
    out=[F(0),F(0),F(0)]
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            if i+j <= 2: out[i+j] += a*b
            elif a*b: raise AssertionError('degree > 2')
    return tuple(out)
ZERO=(F(0),F(0),F(0)); ONE=(F(1),F(0),F(0)); R=(F(0),F(1),F(0))
D=(F(1),F(-3),F(0))
P=[R,R,R,D]

def poly(c0=0,c1=0,c2=0): return (F(c0),F(c1),F(c2))

W1 = {
 (0,0,0,3): poly(1,-9,23),
 (0,0,1,2): poly(0,3,-12),
 (0,1,0,2): poly(0,3,-15),
 (0,1,2,0): poly(0,0,3),
 (0,2,0,1): poly(0,0,3),
 (1,0,0,2): poly(0,3,-15),
 (1,0,1,1): poly(0,0,6),
 (1,1,0,1): poly(0,0,6),
 (3,0,0,0): poly(0,0,1),
}
W2 = {
 (0,0,0,3): poly(1,-7,13),
 (0,0,1,2): poly(0,3,-12),
 (0,1,2,0): poly(0,0,3),
 (0,2,0,1): poly(0,0,3),
 (1,0,1,1): poly(0,0,6),
 (1,1,0,1): poly(0,6,-24),
 (2,1,0,0): poly(0,-3,15),
 (3,0,0,0): poly(0,1,-4),
}
W3 = {
 (0,0,0,3): poly(1,-6,9),
 (0,1,2,0): poly(0,0,3),
 (0,2,0,1): poly(0,3,-9),
 (1,0,1,1): poly(0,6,-18),
 (1,2,0,0): poly(0,-3,12),
 (2,0,1,0): poly(0,-3,12),
 (2,1,0,0): poly(0,3,-9),
}
TARGETS=[poly(0,3,4), poly(0,4,-1), poly(0,6,-9)]

def verify_certificates():
    for k,z in enumerate(Z,1):
        for t in TYPES:
            rhs=sum(F(z[m])*psi(t,*PAIRS[m]) for m in range(10))
            assert rhs >= reject(t), (k,t,rhs,reject(t))
        print(f'certificate {k}: all 20 occupancy types passed')

def verify_construction(W,target,name):
    total=ZERO
    for w in W.values(): total=padd(total,w)
    assert total == ONE
    # Ordered-coordinate pair probabilities are fixed by factorial moments.
    for i,j in PAIRS:
        moment=ZERO
        for t,w in W.items():
            factor = F(t[i]*(t[i]-1),6) if i==j else F(t[i]*t[j],6)
            moment=padd(moment, pscale(factor,w))
        assert moment == pmul(P[i],P[j]), (name,i,j,moment,pmul(P[i],P[j]))
    obj=ZERO
    for t,w in W.items():
        if reject(t): obj=padd(obj,w)
    assert obj == target, (name,obj,target)
    print(f'{name}: normalization, all 10 pair laws, and rejection polynomial passed')

if __name__ == '__main__':
    verify_certificates()
    verify_construction(W1,TARGETS[0],'construction I')
    verify_construction(W2,TARGETS[1],'construction II')
    verify_construction(W3,TARGETS[2],'construction III')
    print('all exact checks passed')
