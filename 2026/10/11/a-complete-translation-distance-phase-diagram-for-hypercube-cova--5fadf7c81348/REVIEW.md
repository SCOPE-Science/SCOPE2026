# Independent mathematical audit

## correctness

PASS

For Q=[-1,1]^d and h with |h|_2=2s, normalized overlap factors as product_i(1-x_i)_+, x_i=|h_i|/2 and sum x_i^2=s^2. Since s<sqrt(d), a positive all-coordinate competitor exists, excluding x_i>=1 at a maximizer. On any positive support face, let y_i=x_i^2 and f(y)=log(1-sqrt(y)); Lagrange stationarity requires x_i(1-x_i) equal, so positive x_i are either all equal or comprise complementary u,1-u. The latter has strictly positive two-coordinate second variation (1-2u)^2/[4u^3(1-u)^3], contradicting maximality. Hence the support-k candidates are exactly F_k(s)=(1-s/sqrt(k))^k for s<sqrt(k), and each is attainable. For real z>s^2, d(log F_z)/dz=H(s/sqrt(z)); H decreases to H(1/2)<0 then increases and crosses zero at unique rho~0.715331862959, making the candidate sequence strictly unimodal. For every k, log(F_k/F_{k+1}) starts zero with positive derivative, rises then tends to negative infinity before sqrt(k), so there is exactly one positive c_k. Sign and real-unimodality give rho sqrt(k)<c_k<rho sqrt(k+1), strict ordering and only adjacent ties. The algebra yields c1=2(sqrt(2)-1). All quantifiers and endpoint conventions are consistent. An independent numerical implementation validated the second variation at five u values, 50 ordered thresholds through k=50 and 48,620 deterministic random competitors in d=2..12; numerical tests corroborate but do not prove the general result.

## originality

PASS

Best-of-knowledge: searched the exact fixed-norm cube-overlap functional and its equivalent constrained-product formulation, queried the published Resultary corpus, and compared the primary covariogram reconstruction, translated symmetric-difference and shape-matching results at the level of the mathematical implications. None of the actually inspected statements yields the all-d formula, equality classes, and strictly ordered support-transition thresholds. This is a qualified, not exhaustive, priority assessment; earlier unindexed constrained-product inequalities remain a real risk.

## value

PASS

The radial maximum of an axis-aligned hypercube covariogram at a prescribed physical Euclidean displacement is a natural and interpretable geometric matching/autocorrelation statistic. Its exact all-dimensional profile, complete equality classification and d-1 sharp support activation transitions are not supplied by mere knowledge of the cube's separable overlap product or a generic Lipschitz inequality. The optimizer passes successively through all support sizes, a nontrivial structural phase diagram with useful benchmarks for constrained alignment. The universal scaled-threshold constant and first exact crossing add reusable quantitative detail. This is a self-contained nontrivial classification of a natural invariant, not an arbitrary slice or a routine single formula; no broad-body extension or paper-sized downstream theorem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
