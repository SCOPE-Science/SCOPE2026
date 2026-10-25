# Independent mathematical audit

## correctness

PASS

The weighted scalar p-mean has a unique root because the real p-energy is strictly convex, and implicit differentiation at nonzero residuals yields a positive sensitivity g_i=v_i|r_i|^{p-2}/sum(v_j g_j). For p>2, write the signed p-1 residual moments as two probability vectors; the dual test with d_i=(y_i-Cv_i)v_i^{q-1} has d_i+d_j<=0 on every pair and at most one positive entry, so concavity of the power sigma=(p-2)/(p-1) bounds each sign group and yields the pair maximum. Opposite-sign residuals on the winning pair realize its derivative; at other coordinates g=0. For 1<p<2, ||g||_q<=sum g and sum v_i g_i>=min(v_i) sum g give V/min(v_i); monotone smooth regularization of the p-mean passes the global bound through zero residuals. For k>=3, a balanced residual with one minimum-weight coordinate tending to zero has g_i diverge and realizes the bound. k=1 is a coordinate retraction, k=2 is an exact linear weighted mean, p=2 is orthogonal. Pair norm >=1 by retraction and Hölder equality forces equal weights for two active coordinates away from p=2. Independent constrained-residual gradient tests checked 3840 finite cases, supporting but not replacing the dual/sign and smoothing arguments.

## originality

PASS

The exact nonuniform all-weight formula and p-dependent support reduction survive close comparison. Earlier all-ones line constants and the weighted cross-polytope two-coordinate factor are covered ingredients, not novelties. The complete 2017 atomic-subspace article gives only finite/coarse constants, not the displayed sharp full-weight phase diagram.

## value

PASS

Quantitative sensitivity of a nonlinear best approximation is natural in Banach approximation; the sharp weighted k>=3 phase switch differs structurally above/below the Hilbert exponent and completely classifies nonexpansive lines. It resolves the exact constant beyond known coarse atomic-subspace bounds, not a mere parameter substitution or norm estimate. The closed-form weighted extremal structures matter even without an application to larger approximation spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
