"""Exact checks of three-allele fixation and arithmetic-mean compression."""
from fractions import Fraction as F
from itertools import product
import sympy as s


def linear_solve(A, v):
    """Rational Gauss-Jordan elimination on the finite transient Markov system."""
    n = len(v)
    m = [[F(A[i][j]) for j in range(n)] + [F(v[i])] for i in range(n)]
    for k in range(n):
        idx = next(i for i in range(k, n) if m[i][k])
        m[k], m[idx] = m[idx], m[k]
        pivot = m[k][k]
        m[k] = [x / pivot for x in m[k]]
        for i in range(n):
            if i != k:
                scale = m[i][k]
                m[i] = [x - scale * y for x, y in zip(m[i], m[k])]
    return [row[-1] for row in m]


def independent_markov_value(a, b, c):
    """Solve every nonabsorbing composition, including all six two-allele edges."""
    fitness = (F(a), F(b), F(c))
    states = [(i,j,3-i-j) for i in range(4) for j in range(4-i)]
    absorbing = {(3,0,0), (0,3,0), (0,0,3)}
    transient = [x for x in states if x not in absorbing]
    idx = {st:i for i,st in enumerate(transient)}
    mat = [[F(i == j) for j in range(len(transient))] for i in range(len(transient))]
    rhs = [F(0)] * len(transient)
    for st in transient:
        i = idx[st]
        total_fitness = sum(st[k]*fitness[k] for k in range(3))
        for parent, dead in product(range(3), repeat=2):
            prob = F(st[parent], 1)*fitness[parent]/total_fitness*F(st[dead], 3)
            if not prob: continue
            after = list(st)
            after[parent] += 1
            after[dead] -= 1
            t = tuple(after)
            if t in idx: mat[i][idx[t]] -= prob
            elif t == (3,0,0): rhs[i] += prob
    return linear_solve(mat,rhs)[idx[(1,1,1)]]


a,b,c = s.symbols('a b c',positive=True)
m,d = s.symbols('m d',real=True)
K1=lambda other:a*a/(a*a+a*other+other*other)
K2=lambda other:a*(a+other)/(a*a+a*other+other*other)
first_step=(a*K2(b)+b*K1(b)+a*K2(c)+c*K1(c))/(2*(a+b+c))
closed=a*a*(2*a*a+a*(b+c)+2*b*c)/(2*(a*a+a*b+b*b)*(a*a+a*c+c*c))
average=a*a/(a*a+a*(b+c)/2+(b+c)**2/4)
assert s.factor(first_step-closed)==0
variance_identity=(a*a*d*d*((m-a)*(m+2*a)-d*d)/((a*a+a*(m+d)+(m+d)**2)*(a*a+a*(m-d)+(m-d)**2)*(a*a+a*m+m*m)))
assert s.factor((closed-average).subs({b:m+d,c:m-d})-variance_identity)==0
for val_a, val_b, val_c in [
    (F(1),F(1),F(5)),(F(5,2),F(1),F(5)),(F(3),F(1),F(5)),
    (F(2),F(2),F(4)),(F(2),F(1,4),F(23,4)),
    (F(1),F(1),F(1)), (F(7,9),F(5,11),F(13,7))
]:
    exact_chain=independent_markov_value(val_a,val_b,val_c)
    predicted=F(str(closed.subs({a:s.Rational(val_a.numerator,val_a.denominator), b:s.Rational(val_b.numerator,val_b.denominator), c:s.Rational(val_c.numerator,val_c.denominator)})))
    assert exact_chain==predicted, (val_a,val_b,val_c,exact_chain,predicted)
assert s.factor((closed-average).subs({a:2,b:2,c:4}))==s.Rational(1,266)
assert s.factor((closed-average).subs({a:2,b:s.Rational(1,4),c:s.Rational(23,4)}))==-s.Rational(1452,359233)
print('VERIFY_OK')
