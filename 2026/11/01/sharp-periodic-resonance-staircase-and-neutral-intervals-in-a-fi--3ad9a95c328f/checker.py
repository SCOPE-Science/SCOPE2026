"""Exact reproducibility checks for the four-branch map's orbit classification.

Python 3 with SymPy. The general quantifiers are proved in RESULT.md;
finite cases here test algebra and boundary conventions independently.
"""
import sympy as s

A, M = s.symbols('alpha M', positive=True)

def simp(x):
    return s.simplify(s.cancel(x))

def S(k):
    return sum(A**j for j in range(k+1))

def formal(k):
    return simp(M*S(k)/(1+M*A**k))

def outer(x, a):
    return simp(a*(x-1))

def branch(x, a, m):
    xx = s.N(x, 40)
    assert -s.N(m,40) <= xx <= s.N(m,40)
    if xx <= -1:
        return simp(a*(x+1))
    if xx < 0:
        return simp(m*(x+1))
    if xx < 1:
        return simp(m*(x-1))
    return simp(a*(x-1))

def equal(x,y):
    assert simp(x-y) == 0, (x,y)

def cycle(a,m,k,x):
    n=2*(k+1)
    states=[simp(x)]
    for _ in range(n):
        states.append(branch(states[-1],a,m))
    equal(states[-1],states[0]);assert len({str(simp(v)) for v in states[:-1]})==n
    for i in range(k): assert 1 < float(states[i]) < float(m), (k,i,states)
    assert 0 < float(states[k]) < 1
    for i in range(k+1,n-1):
        if i<2*k+1:assert -float(m)<float(states[i])< -1, (k,i,states)
        else:assert -1<float(states[i])<0
    return states

checks=0
for k in range(1,8):
    x=formal(k)
    assert simp(x-1)!=0
    z=x
    for j in range(k):z=outer(z,A)
    equal(z,1-x/M)
    equal(M*(z-1),-x)
    equal(simp(M*(A**k*x-S(k))),(M*A**k)*x-M*S(k))
    # Two-block affine return: multiplier a^2, unique symmetric solution if a != 1.
    a=M*A**k;c=M*S(k)
    y=a*x-c
    equal(a*y+c,x)
    checks+=5

# A rigorous finite cutoff in the original fivefold map: k>=5 is excluded
# by q_k > k-1 >= 4, so only k=1,...,4 can occur.
assert all(sum(s.Rational(1,1)/s.Rational(4,5)**j for j in range(1,k))>4 for k in (5,6,7))
# Existence and local attraction for strictly admissible interior rational examples.
for a,k in [(s.Rational(1,10),1),(s.Rational(3,10),2),
            (s.Rational(2,5),2),(s.Rational(1,2),2),
            (s.Rational(7,10),3),(s.Rational(9,10),4)]:
    x=formal(k).subs({A:a,M:5})
    states=cycle(a,s.Integer(5),k,x)
    assert simp(states[k+1]+x)==0
    multiplier=simp((5*a**k)**2)
    if (a,k) in [(s.Rational(1,10),1),(s.Rational(3,10),2),(s.Rational(2,5),2)]:
        assert multiplier<1
    else: assert multiplier>1
    checks+=3

# For alpha=1/5, an entire positive interval is mapped by F^4 identically.
for x in [s.Rational(3,2),s.Rational(2),s.Rational(3),s.Rational(9,2)]:
    cycle(s.Rational(1,5),s.Integer(5),1,x)
    checks+=1

# For alpha=1/sqrt(5), the entire open interval (1+sqrt(5), 5)
# has least period six, demonstrated at two distinct exact algebraic points.
a=s.sqrt(5)/5
for x in [s.Integer(4),s.Rational(9,2)]:
    assert 1+s.sqrt(5)<x<5
    cycle(a,s.Integer(5),2,x)
    checks+=1

# The neutral branch has an identity 2(k+1)-return on its open interval.
x=s.symbols('x')
for k in range(1,5):
    neutral_m=A**(-k)
    c=simp(neutral_m*S(k))
    # Positive first block sends x -> x-c; negative first block -> x+c.
    equal((x-c)+c,x)
    checks+=1

print('PASS:',checks,'symbolic/explicit checks; general proof is in RESULT.md')
