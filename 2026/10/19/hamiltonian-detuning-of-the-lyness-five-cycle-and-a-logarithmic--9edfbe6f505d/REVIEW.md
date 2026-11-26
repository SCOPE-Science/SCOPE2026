# Independent mathematical audit

## correctness

PASS

The first integral and log-area preservation follow by substitution, and the log-sum-exponential representation gives a positive-definite Hessian for H_a on the positive quadrant. At a=1, H differs by at most log 12 from its proper homogeneous polygon gauge; locally in a the difference H_a−H is uniformly bounded, giving properness. The noncritical fixed-r oval therefore persists, with the center at x=y=(1+√5)/2 when a=1. I independently propagated the exact tangent recurrence along the resonant scalar orbit x,y,(1+y)/x,(1+x+y)/(xy),(1+x)/y,x,y. With p₀=p₁=0, it is p_{j+2}=(1+p_{j+1}−x_{j+2}p_j)/x_j; rational simplification verifies (p₅,p₆)=(xy∂_y log V₁,−xy∂_x log V₁). In log coordinates this gives the clockwise Hamiltonian field with the asserted physical time. Conjugating the fifth iterate by a smooth moving-oval frame does not change its first variation, because its resonant map is the identity. Uniform Taylor bounds in normalized time then trap every one-step displacement between (a−1)/P(r)±C_r(a−1)², so the translation number obeys the same bound by iteration. The lift of the fifth iterate subtracts one resonant turn, giving the factor 1/5. The positive-definite center Hessian has determinant (25−11√5)/2 and its small-oval period tends to the corresponding linear period, e.g. by rescaling in a quadratic normal form and taking the coarea derivative there. For high energy the tropical polygon has area 5/2, giving √A(z)/z→√(5/2) for log energy z. Convex sublevel sets and Brunn–Minkowski make √A(z) concave; its derivative tends to the same slope, justifying A′(z)∼5z without differentiating an uncontrolled error. Coarea makes A′(log r) the physical period (speed |∇H|), yielding the constant 1/25 for the derivative already taken at a=1, not a uniform two-parameter expansion. The supplied SymPy checker was inspected, not executed; replay is `python verify.py` in the source directory. Its numeric check is a forward parameter difference of the linearized fixed-point angle, not a centered difference or an all-level rotation test. The all-level and infinite-energy conclusions use the proofs, not those checks.

## originality

PASS

Best of current knowledge: the all-level torsion detuning identified with the specific natural Hamiltonian period, and its differentiated high-energy prefactor, are the supported distinct content. Elliptic integrability, exact rotation quadratures, five-periodicity, the undifferentiated energy limits and the center angle law are prior. The center coefficient is consistent with, and obtainable by differentiating, the classical explicit center angle; it is not credited as a separate new invariant.

## value

PASS

At global order-five resonance, the first parameter response is a natural measurable invariant that is invisible in the constant resonant rotation or the known high-energy rotation limit. Its identification with a natural Hamiltonian period gives a workable description on every noncritical oval and explains both positivity and logarithmic loss of susceptibility, with a sharp prefactor. The proof avoids expanding degenerating elliptic roots for the first variation, and its fixed-energy qualification is meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
