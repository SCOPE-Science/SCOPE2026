# Independent mathematical audit

## correctness

PASS

The Müller–Tomilov essential-range formula is twice the ellipse hull. Substituting r^p/s^p=e^{2v} and dividing the imaginary coordinate by 2δ gives axes 2cosh(δv)/cosh v and sinh(δv)/(δ cosh v). Both vanish at infinity for δ<1 (the limiting axes do too), so the hulls are compact; the dependence only on δ establishes conjugate symmetry. At (2,0) one must have a≥0, and with a=0 only b=0 works. For a>0 the exact support inequality follows from sinh(δv)/δ<sinh v and holds at equality in b²=4a²(1−δ²); the v² coefficient in the squared comparison excludes larger |b|. For δ≤1/2 the coordinate errors are bounded by δ² times a polynomial in v times e^{v/2}/cosh v, uniformly bounded. Matching convex combinations give the Hausdorff upper bound, and the vertical support difference at v* has positive leading coefficient v*³/(6cosh v*), giving the lower bound. For b≠0 the sign of the positive-v support derivative is the sign of v coth v−v²−4a²/b²; v coth v−v² decreases strictly from one to minus infinity by tanh(2v)<2v, including at the threshold. The b=0 and zero-normal cases are immediate. The frozen script's ellipse function and its direct comparison jointly used |p−2| instead of 2δ, scaling the normalized ordinate by an extra factor 2/p, so agreement between them did not test the stated normalization. The replacement /workspace/repairs/3/verification.py was independently constructed and run (same contents as /workspace/repro/toeplitz_normalized_range.py; finite checks passed, height 0.662743419349182). It compares correctly rescaled direct axes across conjugates and checks selected cone, maximizer and vertical excess consequences; the uploaded script was not executed. RESULT and VERIFICATION scientific notes were corrected; the universal claims rest on the analytic proof.

## originality

PASS

The underlying ellipse hull and axes are prior, and conjugate symmetry is immediate from reparameterizing that known hull. The supported distinct contribution is the sharp finite-exponent cone, common singular limit with its full support-maximizer transition, and matching quadratic Hausdorff rate. These are not asserted as a new determination of the essential numerical range itself.

## value

PASS

The normalization resolves the transverse geometry lost when the unnormalized range collapses to a Hilbert segment. The exact cones identify all slopes for which an endpoint remains exposed, the limiting support equation determines what happens beyond the threshold, and the matching rate quantifies the error in using the limit shape. These are motivated geometric data of a standard infinite-dimensional operator, beyond just rewriting its known range or computing a decimal axis value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
