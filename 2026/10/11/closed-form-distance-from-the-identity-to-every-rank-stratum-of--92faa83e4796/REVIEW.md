# Independent mathematical audit

## correctness

PASS

Under Chen’s default ambient d_orb,n, pick the identity factor I_n. Registered rank-s candidate row vectors all lie in one s-dimensional subspace U with orthogonal projection P and p_i=P_ii, Σ p_i=s. Cauchy–Schwarz bounds each row cosine above by sqrt(p_i), hence its squared angle below by f(p_i)=acos²sqrt(p_i). Calculus gives fʺ(p)=2(sin2θ−2θcos2θ)/sin³(2θ)>0 for p=cos²θ, as the numerator vanishes at θ=0 and has derivative 4θsin2θ>0. Jensen gives Σf(p_i)≥n f(s/n)≥n f(r/n). Real Schur–Horn majorization supplies rank-r projection with uniform diagonal r/n in every dimension, and Y=√(n/r)P attains the bound; strict convexity and equality in rowwise Cauchy–Schwarz yield exactly (n/r)P, with no other minima. Rank n gives zero distance and unique I_n; rank1 gives sign-cut matrices; corank1 projections I−ssᵀ/n give exactly 2^(n−1) signed-simplex correlations. The proof addresses n≥2 and all 1≤r≤n and explicitly distinguishes smaller ambient k metrics. Independent DFT projections for all 170 n/r pairs n≤18 and 1620 sampled rank-bounded row subspaces numerically corroborated its claims; the universal proof is analytic and does not follow from finite tests.

## originality

PASS

The exact source Chen (arXiv:2401.03126, metric definition and distance-computation section) supplies the O(n)-registered sum-of-squared-spherical-angles cost and discusses its general nonclosed form, but not its minimization from the identity to every rank stratum. The more recent Bisson–Loiseaux–Pennec (arXiv:2610.28475) studies low-rank correlation quotient geometry, geodesics and rank-dependent phenomena, not the explicit identity-centered formula or tight-frame equality class. Classical tight-frame/frame-potential and Schur–Horn theorems supply the optimizer objects and existence, not the angular orbit-metric optimization. The checked published Schur–Horn-orbitope Frobenius and spherical-isotropization Wasserstein results use materially different metrics and feasible objects. No independent stronger claim or exact table implying the full value and optimizer classification was found; Resultary indexed the exact assigned mirror, which is not counted as independent antecedent. Verdict is best-of-knowledge with specified terminology/indexing risk, not priority certification.

## value

PASS

Rank strata are intrinsic organizing subsets of the elliptope quotient geometry, and exact metric clearance from the canonical full-rank basepoint I_n to rank loss is a natural stability/nearest-degeneracy question. The finding supplies a nontrivial closed form simultaneously for every n and r, a complete variational/equality classification by uniform-diagonal projections, and all exactly 2^(n−1) signed regular-simplex nearest singular correlations. The angular cost is not the familiar quadratic frame potential, so the result is not a mere reparameterization or known-table calculation. The optimized metric and full equality set are mathematically useful even without a separate downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
