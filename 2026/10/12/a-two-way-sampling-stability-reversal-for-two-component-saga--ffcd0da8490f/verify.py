"""Exact-rational verification of the two SAGA sampling-stability reversals.

Requires Python 3 and SymPy. Execute: python verify.py
All matrices, probabilities, and certificates are specified here.
"""
import sympy as sp

x, y1, y2, t = sp.symbols('x y1 y2 t')
monomials = [x*x, y1*y1, y2*y2, x*y1, x*y2, y1*y2]

def matrices(a, b, step):
    a, b, h = map(sp.Rational, (a, b, step))
    M1 = sp.Matrix([[1-h*a, h/2, -h/2], [a, 0, 0], [0, 0, 1]])
    M2 = sp.Matrix([[1-h*b, -h/2, h/2], [0, 1, 0], [b, 0, 0]])
    return M1, M2

def lift(M):
    u = M * sp.Matrix([x, y1, y2])
    return sp.Matrix([
        [sp.Poly(m.subs({x:u[0], y1:u[1], y2:u[2]}, simultaneous=True),
                 x, y1, y2).coeff_monomial(k)
         for k in monomials]
        for m in monomials
    ])

def sym_pd(Q):
    assert Q == Q.T
    determinants = [sp.factor(Q[:j, :j].det()) for j in (1,2,3)]
    assert all(v > 0 for v in determinants), determinants
    return determinants

def expected_x2_by_paths(mats, initial, rounds):
    # Exhaust all equally likely paths; each entry is an exact rational state.
    states = [(sp.Matrix(initial), sp.Rational(1))]
    for _ in range(rounds):
        states = [(M*z, prob/2) for z, prob in states for M in mats]
    return sp.factor(sum(prob * z[0]**2 for z, prob in states))

def verify_case(a, b, step, stable, unstable, certificate, numerator, denominator):
    A, B = matrices(a,b,step)
    assert A[1,:] == sp.Matrix([[a,0,0]])
    assert B[2,:] == sp.Matrix([[b,0,0]])
    LA, LB = lift(A), lift(B)
    assert lift(A*B) == LA*LB
    assert lift(B*A) == LB*LA
    paths = {'iid':(A,B), 'rr':(B*A, A*B)}
    operators = {'iid':(LA+LB)/2,
                 'rr':(lift(B*A)+lift(A*B))/2}
    Q = sp.Matrix(certificate)
    L = paths[stable]
    S = Q - sum((M.T*Q*M for M in L), sp.zeros(3))/2
    minors_Q = sym_pd(Q)
    minors_S = sym_pd(S)
    print(f'stable: a={a}, b={b}, step={step}, scheme={stable}')
    print('  P leading principal minors:', minors_Q)
    print('  Lyapunov residual leading principal minors:', minors_S)
    Ku = operators[unstable]
    I = sp.eye(6)
    z0=sp.Matrix([1, a*a, b*b, a, b, a*b])
    e0 = sp.Matrix([[1,0,0,0,0,0]])
    assert sp.factor(sp.together((e0*(I-t*Ku).inv()*z0)[0]
                                    - numerator/denominator)) == 0
    assert denominator.subs(t,0) > 0 and denominator.subs(t,1) < 0
    assert sp.gcd(sp.Poly(numerator,t),sp.Poly(denominator,t)).degree()==0
    # A zero of the denominator strictly between zero and one is an
    # uncancelled pole.  The generating coefficients are nonnegative
    # squared-error expectations, hence have an exponential subsequence.
    print(f'unstable: a={a}, b={b}, step={step}, scheme={unstable}')
    print('  denominator(0), denominator(1):',
          denominator.subs(t,0),denominator.subs(t,1))
    # The lift and finite-path enumerations are genuinely independent routes.
    Mlist=paths[unstable]
    for k in range(6):
        lhs=(e0*Ku**k*z0)[0]
        rhs=expected_x2_by_paths(Mlist, [1,a,b], k)
        assert lhs==rhs, (k,lhs,rhs)
        print('  exact moment at grouped round',k,':',lhs)

# Equal-curvature example: with replacement is stable, reshuffling is not.
num_equal=20*(529*t-1600)*(206839*t*t+1405760*t-2560000)
den_equal=328253493*t**4-1825585348*t**3-11250326720*t*t-72110592000*t+81920000000
# The numerator has no zeros on [0,1]: both factors are negative.
assert (529-1600)<0 and (206839+1405760-2560000)<0
verify_case(1,1,sp.Rational(23,20), 'iid', 'rr',
            [[253,-53,-53],[-53,230,-114],[-53,-114,230]],
            num_equal,den_equal)

# Unequal curvatures: reshuffling is stable, with replacement is not.
num_unequal=-2*(54347409*t**4-173494916*t**3-101122080*t*t+679180800*t-512000000)
den_unequal=16342911*t**5-123128728*t**4+265787536*t**3+269193600*t*t-1466521600*t+1024000000
# Bernstein coefficients of the inner quartic on [0,1] are all negative.
quartic=-num_unequal/2
coeffs=[sp.expand(quartic).coeff(t,j) for j in range(5)]
bernstein=[sum(coeffs[j]*sp.binomial(k,j)/sp.binomial(4,j)
               for j in range(k+1)) for k in range(5)]
assert bernstein==[-512000000,-342204800,-189263280,-96549169,-53088787]
verify_case(1,4,sp.Rational(27,100), 'rr', 'iid',
            [[259,5,-34],[5,3,-3],[-34,-3,9]],
            num_unequal,den_unequal)
print('PASS: exact Lyapunov, pole, noncancellation, and path-enumeration checks')
