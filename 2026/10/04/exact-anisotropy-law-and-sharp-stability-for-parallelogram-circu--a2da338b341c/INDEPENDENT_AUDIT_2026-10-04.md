# Independent mathematical audit

## correctness

PASS

After translating the parallelogram to its center and applying the linear map sending one antipodal vertex pair to plus or minus e1 and the other to plus or minus e2, every centered circumellipse has quadratic matrix K_c with diagonal entries one and off-diagonal entry c, where |c|<1. Its normalized area is pi/(2*sqrt(1-c^2)). Relative to the minimum-area member K_0, the two generalized eigenvalues are 1+c and 1-c, so the affine-invariant half-log anisotropy is atanh(|c|). Consequently the area ratio is exactly (pi/2)*cosh(delta), and the excess is pi*sinh(delta/2)^2. The global lower bound excess >= (pi/4)*delta^2 follows from cosh(delta)-1 >= delta^2/2, and the coefficient is sharp as delta tends to zero. Independent symbolic substitution confirmed the cosh identity; the assigned randomized checker also verifies incidence, affine covariance, the area formula and the near-zero sharp coefficient.

## originality

PASS

Classical and modern primary sources establish existence of the circumellipse pencil and the unique minimum-area member. Li et al. prove that the minimum circumscribed-ellipse area of a parallelogram is pi/2 times the parallelogram area, but do not give the full affine-invariant area-versus-anisotropy profile. Horwitz gives general circumellipse equations and extremal results; his detailed area formulas in the inspected 2007 article are explicitly developed for nontrapezoid quadrilaterals. A 2024 Horwitz monograph has dedicated parallelogram equation, minimal-area and area-inequality sections and is therefore a genuine bibliographic risk, but only publisher-level contents were accessible in this run, so no whole-book noncoverage claim is made. Current exact searches found no prior cosh law or sharp half-log stability theorem.

## value

PASS

The theorem upgrades a qualitative minimum-area fact to an exact affine-invariant stability profile for the entire circumellipse pencil and identifies the sharp quadratic deficit constant. The condition-number coordinate is natural in ellipsoidal geometry, so the result is a structural quantitative refinement rather than an arbitrary parameter evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
