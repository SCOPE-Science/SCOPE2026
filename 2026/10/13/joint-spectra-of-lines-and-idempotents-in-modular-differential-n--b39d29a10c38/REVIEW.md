# Independent mathematical audit

## correctness

PASS

Differentiation descends modulo t^p in characteristic p; right commutativity follows from commutative multiplication and the associator is -fg (T h)' for T=partial_t+M_a. The line condition for a normalized generator is fT(f)=lambda f. For a unit normalize its constant coefficient to 1 and cancel f: T(f)=lambda. The lower coefficients uniquely solve this as h_a+lambda g_a, since each division is by 1 through p-1. The remaining equation is sigma_a+lambda tau_a=0. A valuation-one generator normalized at t has lambda=1 by its leading coefficient, and cancellation modulo t^(p-1) forces g_a, which already is idempotent. For valuation r>=2 a nonzero lambda is impossible; the leading term of ff' is of order 2r-1 with nonzero coefficient r times the square of the leading coefficient if that degree survives. Both terms of fT(f) vanish exactly for 2r-1>=p, giving a projective tail of dimension floor((p-1)/2) before projectivizing. On any closed line, nonzero multiplication coefficient gives exactly one nonzero idempotent by scaling, and zero gives none. Holding the lower p-2 parameters fixed, varying a_(p-2) does not change g_a and shifts tau_a by the same amount (g_a begins in degree one); after this choice varying a_(p-1) does not change h_a and shifts sigma_a by the same amount. This gives the uniform fibers and all four rows. At p=2, g_a=t, h_a=1+a_0 t, sigma_a=a_1+a_0^2, tau_a=a_0, and the projective tail is empty; the four count pairs are still distinct even at q=2. Read VERIFICATION.md and checker.py without executing the frozen code. Its direct tests and its separate recurrence-fiber enumerations are finite corroboration; the argument here needs neither extrapolation from small fields nor a simplicity classification.

## originality

PASS

The supported claim is the exact joint spectrum with uniform multiplicities across all labeled finite-field differential parameters, with explicit line representatives. Neither the established differentiable-product construction, isomorphism normal forms of simple algebras, nor existence of idempotents is new. The strongest matched normal-form result has a genuine overlap in dimension p, but the inspected statements are over an algebraically closed field of characteristic greater than two and do not count finite-field embedded lines, nonzero idempotents or labeled parameter fibers.

## value

PASS

This is a natural joint census for a standard family, not a chart of a few small products. It explains why the line count alone cannot tell whether a second idempotent exists and gives the exact frequency of that distinction over any finite field of the characteristic. It separates the high-valuation square-zero geometry from a two-obstruction locus controlling unit representatives, and precisely identifies the statistic on labeled products rather than making an isomorphism-class claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
