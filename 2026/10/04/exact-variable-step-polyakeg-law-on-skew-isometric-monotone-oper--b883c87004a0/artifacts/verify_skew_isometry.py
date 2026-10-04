from fractions import Fraction as Q

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def scale(c,a): return (c*a[0], c*a[1])
def J(a): return (-a[1], a[0])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def norm2(a): return dot(a,a)

def one_step(e,s):
    ehat = add(e, scale(-s, J(e)))
    fhat = J(ehat)
    diff = add(e, scale(-1, ehat))
    alpha = dot(fhat, diff) / norm2(fhat)
    eplus = add(e, scale(-alpha, fhat))
    expected = scale(Q(1,1)/(1+s*s), add(e, scale(-s, J(e))))
    assert eplus == expected
    assert norm2(eplus) * (1+s*s) == norm2(e)
    f = J(e)
    fdelta = add(fhat, scale(-1, f))
    assert norm2(fdelta) == s*s*norm2(f)
    return eplus

steps = [Q(1,7), Q(1,3), Q(2,3), Q(1,1)]
seeds = [(Q(3,2),Q(-5,4)), (Q(2,1),Q(7,3))]
for e in seeds:
    for s in steps:
        one_step(e,s)

e = (Q(5,3), Q(-7,5))
initial = norm2(e)
den = Q(1,1)
for s in [Q(1,5),Q(2,5),Q(3,5),Q(4,5)]:
    e = one_step(e,s)
    den *= (1+s*s)
assert norm2(e) * den == initial
print("VERIFY_OK")
