# Independent mathematical audit

## correctness

PASS

For 2n signed nodes ±sqrt(n) Ue_j, direct sign pairing gives predicted mean tr(B), exact cross covariance ell and innovation s_U=R+||ell||^2+n sum_j (U^T B U)jj^2-(tr B)^2. Independent direct NumPy node evaluation verified this for random symmetric B and orthogonal U in dimensions 2–5. Gaussian fourth moments give s*=R+||ell||^2+2||B||F^2. The equal-diagonal-basis induction constructs the sharp lower endpoint w, and eigenframes attain upper w+nF-t^2; connected SO(n) supplies every value. The exact affine estimator MSE difference is (s*-s_U)ell ell^T/s_U^2, not a conditional Bayesian posterior. Therefore calibration iff n >= 2+t^2/F, with eigenframe rigidity at equality. Rank-one, traceless and scalar B boundaries are consistent.

## originality

PASS

Earlier CKF work explicitly establishes the signed-node formulas and rotation sensitivity, and Jiang et al. 2026 already present general covariance compensation and a Haar-averaged quadratic bound. Their inspected Sections II–III do not state the optimized all-frame spectral interval or necessary-and-sufficient exact calibration boundary. This boundary is a specialization needing the additional equal-diagonal/eigenframe extremal argument, but Schur–Horn and general per-frame formulas are important prior ingredients.

## value

PASS

The same Gaussian prior and nonlinear scalar measurement can produce opposite covariance miscalibration merely by changing a legitimate orthogonal square root. The exact trace/Frobenius phase criterion, equality frames, complete attainable interval and arbitrarily large MSE underreporting at fixed reported gain are meaningful complete diagnostics for a natural cubature method, beyond a generic covariance positivity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
