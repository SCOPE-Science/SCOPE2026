# Independent mathematical audit

## correctness

PASS

For fixed 1/2<alpha<1 and distinct nonnegative rates, the endpoint kernel is g_i(t)=t^(alpha-1) E_{alpha,alpha}(-lambda_i t^alpha) in L2(0,T). Its first two linearly independent powers, t^(alpha-1) and t^(2alpha-1), have Gram determinant alpha^2*T^(6alpha-2)/[(2alpha-1)(4alpha-1)(3alpha-1)^2]. The coefficient determinant is (lambda_1-lambda_2)/[Gamma(alpha)Gamma(2alpha)]. Hence trace W~2*T^(2alpha-1)/[Gamma(alpha)^2(2alpha-1)] and det/trace gives lambda_min~(lambda_1-lambda_2)^2 alpha^2 T^(4alpha-1)/[2 Gamma(2alpha)^2(4alpha-1)(3alpha-1)^2]. Positive-definiteness follows from distinct analytic kernels, and Gramian inversion gives the supremal minimum energy over unit terminal targets. Independently checked the exact shape-Gram identity; finite checks are not the proof. Null-mode eigenvector tends to antisymmetric direction; no uniformity as rates merge.

## originality

PASS

Best-of-knowledge PASS: prior fractional-control papers provide controllability/Gramian nonsingularity and regional tracking, and recent small-time eigenvalue hierarchy literature covers classical alpha=1. Their inspected conclusions do not entail the fixed-fractional two-mode explicit exponent 4alpha-1 with sharp rate-separation constant. A generic Taylor/Gramian method is a proof technique, not a prior explicit numerical theorem; unindexed equivalent derivations remain a priority risk.

## value

PASS

This is a motivated exact model of how a single actuator reaches a weak antisymmetric fractional mode. Its sharp control-energy blowup and dependence on modal separation quantify short-horizon ill-conditioning, a natural control-theoretic invariant not implied by Gramian invertibility alone. The result does not claim PDE-level generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
