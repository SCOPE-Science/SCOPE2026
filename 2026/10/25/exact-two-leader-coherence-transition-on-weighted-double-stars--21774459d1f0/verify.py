"""Independent exact arithmetic spot checks for the weighted bistar leader-pair theorem.
Run: python verify.py (requires SymPy >=1.12). Finite checks supplement the written proof.
"""
from fractions import Fraction
from itertools import combinations
from sympy import Matrix, Rational, simplify


def graph_laplacian(p, q, t):
    n = p + q + 2
    L = Matrix.zeros(n)
    edges = [(0, 1, Rational(1) / t)]
    edges += [(0, i, Rational(1)) for i in range(2, p + 2)]
    edges += [(1, i, Rational(1)) for i in range(p + 2, n)]
    for a, b, weight in edges:
        L[a, a] += weight
        L[b, b] += weight
        L[a, b] -= weight
        L[b, a] -= weight
    return L


def predicted_cost(p, q, t, a, b):
    n = p + q
    if {a,b} == {0,1}:
        return Rational(n)
    if a in (0, 1) or b in (0, 1):
        hub, leaf = (a, b) if a in (0,1) else (b, a)
        is_A = leaf < p + 2
        if hub == 0 and is_A:
            return n - 1 + t * (q + 1)
        if hub == 1 and not is_A:
            return n - 1 + t * (p + 1)
        if hub == 0 and not is_A:
            return n + (t * (q - 1) - 1)/(t + 1)
        return n + (t * (p - 1) - 1)/(t + 1)
    is_A_a = a < p + 2
    is_A_b = b < p + 2
    if is_A_a and is_A_b:
        return n + (n-4 + 2*t*(q+1))/2
    if not is_A_a and not is_A_b:
        return n + (n-4 + 2*t*(p+1))/2
    return n + (n-4 + t*(n-2))/(t+2)


def theorem_value(p, q, t):
    s=min(p,q)
    return p+q+min(Rational(0),(t*(s-1)-1)/(t+1))


def theorem_pairs(p,q,t):
    n=p+q+2
    m=theorem_value(p,q,t)
    return {pair for pair in combinations(range(n),2)
            if simplify(predicted_cost(p,q,t,*pair)-m)==0}


cases = 0
pairs_checked = 0
for p in range(2, 7):
    for q in range(2, 7):
        for t in (Rational(1,5), Rational(2,3), Rational(1), Rational(3)):
            L=graph_laplacian(p,q,t)
            values={}
            for pair in combinations(range(p+q+2),2):
                F=[i for i in range(p+q+2) if i not in pair]
                G=L.extract(F,F)
                # LUsolve of diagonal unit columns; inverse computed exactly.
                value=sum(G.inv()[k,k] for k in range(len(F)))
                expectation=predicted_cost(p,q,t,*pair)
                assert simplify(value-expectation)==0, (p,q,t,pair,value,expectation)
                values[pair]=value
                pairs_checked+=1
            optimum=min(values.values())
            assert optimum==theorem_value(p,q,t),(p,q,t,optimum,theorem_value(p,q,t))
            assert {pair for pair,v in values.items() if v==optimum}==theorem_pairs(p,q,t)
            cases+=1

for p,q in [(2,2),(2,5),(3,3),(3,7),(8,11)]:
    critical=Rational(1,min(p,q)-1)
    for t in (critical/2,critical,critical*2):
        # Exact finite formulas capture both sides and every equality at threshold.
        choices=theorem_pairs(p,q,t)
        if t<critical:
            assert (0,1) not in choices
        elif t==critical:
            assert (0,1) in choices and len(choices)>1
        else:
            assert choices=={(0,1)}

print(f'VERIFY_OK exact_grounded_inverses={pairs_checked} parameter_instances={cases} boundary_instances=15')
