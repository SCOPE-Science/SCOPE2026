# Independent mathematical audit

## correctness

PASS

For fixed s>0 write a+sZ=R exp(iΘ) under the stated circular Gaussian normalization. Differentiation under the expectation is justified by the pointwise bounded displacement derivative of the norm away from a null event. Using E[R cosΘ]=a, the derivative of Var(R)=a²+s²−(ER)² is 2 Cov(R,cosΘ). Polar conditioning gives density proportional to exp(2ar cosθ/s²), so the derivative of E[cosΘ|R=r] in r is (2a/s²)Var(cosΘ|R=r)>0 for a>0. The independent-copy covariance identity proves strict monotonicity for a>0. At a=0 the Rayleigh variance is s²(1−π/4), giving (ER)²≤a²+c²s², with equality only on the two axes, including s=0 directly. Gaussian unitary invariance reduces any affine F to A+sZ with A=|a|, s=‖b‖₂ and r=‖F‖₂=√(A²+s²). The squared difference between the chord c r+(1−c)A and the preceding square-root upper bound is 2c(1−c)A(r−A) in the sense of difference of their squares. Thus the chord bound is strictly improved in every mixed case. Expanding the two squared distances using ∫F=a proves the radial inequality and axis equality cases. The unit pure linear wave has squared phase distance 2 and squared modulus distance 2−√π, forcing the exact Lipschitz constant; equality at positive distance in that bound additionally requires r=1. Constants of nonunit norm saturate the radial remainder, so its coefficient cannot be raised with the phase-distance coefficient fixed. Direct numerical evaluation of the exact constant agreed with the printed decimal 2.9646965828533536. Inspected the 64-point Bessel checker, not executed; the replay of the global claim is the analytic covariance and chord proof, not its finite grid.

## originality

PASS

The supported distinction relative to earlier verified work is the exact sharp Gaussian-affine vacuum inequality and equality profile, not the Rician mean formula, a new distribution, or the existence of Fock stability. The distinct Resultary record 51e0f1878311 demonstrably covers this exact claim mathematically: its strict convex normalized modulus mean implies the full dimension-free radial remainder as well as the sharp constant, by Gaussian reduction and expanding squares. It is a later catalogue release, not evidence of an earlier result; the reported one-dimensional phrasing does not make the frozen general-d assertion a new independent extension of that convexity. Older inspected analytic estimates are nonsharp or for different observations. An independently verified earlier sharp Rice variance lower bound or mean chord would be covering; the bounded comparisons did not establish such an antecedent, and inaccessible method papers do not constitute negative coverage evidence.

## value

PASS

An optimal global constant and equality classification on the vacuum plus first Hermite band give a natural calibrated test for an established full-space stability problem, rather than an arbitrary finite slice. The positive remainder explains the distinction between norm mismatch and genuine phase-orbit error; the pure-linear extremizers give a lower benchmark for any full-space vacuum constant. The sharp quantitative fact is not supplied by the earlier verified qualitative full-space theorems. The result does not assert the full-space constant or a discrete-sampling guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
