# Independent mathematical audit

## correctness

PASS

For B>3c²/4 the objective Hessian is uniformly positive: its v diagonal minimizes to 1-3c²/(4B)>0. At a start (x,0) the cubic Taylor model omits Bv⁴, and Hessian lower-right positivity at h=0 forces t≥3c²/4. At t0, every unit-direction Hessian quadratic form has global minimum (1-q²)²(1+2q²)≥0; nonhomogeneous two-variable quartic convexity is SOS-convexity by Ahmadi–Parrilo. Symmetry and strict convexity force v_+=0. Boundary derivative of λy+y²/2+(3c²/4)(y-x)^4 is λ-3c²x³, establishing iff, including equality. For λ=0, unique interior iterate solves x_+=3c²(x-x_+)³, remains positive, decreases to zero and gives exact cubic coefficient; finite nonidentification is proved analytically. I independently re-derived the Hessian, discriminant, convexity factorization and boundary derivative with symbolic algebra.

## originality

PASS

Best-of-knowledge original exact active-set capture boundary and explicit zero-multiplier nonidentification trajectory for the specific constrained cubic SOS Taylor method; prior work supplies the method and bivariate quartic equivalence, and abstracts do not establish this sharp source-specific calculation. No novelty inference from failed access.

## value

PASS

The model isolates a mathematically motivated issue in higher-order constrained optimization: local cubic convergence with LICQ and strong convexity need not yield finite capture under a zero multiplier. The explicit sharp multiplier-distance threshold and exact recurring obstruction distinguish sufficiency of strict complementarity from mere convergence, and can inform active-set diagnostics. It is a meaningful sharp boundary, not a generic quadratic test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
