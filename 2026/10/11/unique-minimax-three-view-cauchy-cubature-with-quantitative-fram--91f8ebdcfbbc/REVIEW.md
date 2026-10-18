# Independent mathematical audit

## correctness

PASS

The actual frozen RESULT.md reduces the worst full-dimensional convex-body relative error to max_{|v|=1}|2 sum_i w_i |u_i·v| - 1| using Cauchy projection and an even zero-centroid surface-area measure approximated by antipodal atoms plus positive spherical mass (Minkowski existence); the upper bound is immediate from integration. For each i choose a unit v_i orthogonal to the other two vectors: q(v_i)<=w_i. Calibration forces some w_i<=1/3, yielding E>=1/3. An orthonormal equal-weight frame has q∈[1/3,1/sqrt(3)] and achieves E=1/3; equality forces all w_i=1/3 and every u_i orthogonal to its two companions. Under E<=1/3+epsilon<1, the lower q bound L=1/3-epsilon/2, together with w_i<=1/3+epsilon, implies |u_i·u_j|<=sqrt(1-(L/(1/3+epsilon))^2) =3 sqrt(epsilon(4+3epsilon))/(2(1+3epsilon)). Orthogonal weight perturbations attain the two-sided weight bounds, and the equal-weight tilt with u2=sin(theta)e1+cos(theta)e2 (0<=theta<=pi/6) has E=1-2 cos(theta)/3 and pairwise inner product sin(theta), proving the sqrt(epsilon) exponent. Independent normalization/linear-algebra checks confirm the formulas; the finite verifier is supplementary, not the proof of the convex-body supremum.

## originality

PASS

Global calibrated three-axis optimization and quantitative uniqueness are not consequences of the previously known orthogonal coordinate-rule error 1/3. Fixed-rule Crofton error estimates, upper-tail unweighted spherical-design minimization, and spherical-quadrature defect reduction each solve distinct parts, not the full weighted two-sided stability problem.

## value

PASS

A globally unique calibrated optimal surface-area measurement configuration, with explicit near-minimizer guarantees on weights and frame geometry, is a motivated geometric-design theorem. It is not merely the already-known fixed orthogonal-rule numerical error; frame stability is independently informative for noisy measurements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
