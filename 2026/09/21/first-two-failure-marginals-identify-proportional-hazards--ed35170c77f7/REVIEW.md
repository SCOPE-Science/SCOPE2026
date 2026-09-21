# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For independent PHR components, the first-failure survival is the product of all component survivals, giving \(S_1=B^\Lambda\). The event \(T_2>t\) means that at most one component has failed by time \(t\); expanding this event gives
\[
S_2=\sum_i B^{\Lambda-\lambda_i}-(n-1)B^\Lambda.
\]
Substituting \(u=S_1=B^\Lambda\) removes the unknown baseline exactly and yields a finite signed exponential sum after \(u=e^{-x}\).

The uniqueness argument is elementary and handles repeated hazards: group equal exponents, order the distinct exponents, multiply an assumed zero sum by the slowest exponential factor, and take \(x\to\infty\) recursively. Because all normalized hazards are strictly positive, all positive-term exponents \(1-q_i\) lie strictly below the negative-term exponent 1, so the coefficient \(-(n-1)\) cannot cancel with a component term. This identifies \(n\) and the normalized hazard multiset.

The converse model characterization follows by setting \(q_i=1-\alpha_i\), using \(\sum\alpha_i=n-1\), and choosing the normalized baseline \(B=S_1\). For known \(n\), differentiating the exponential sum at zero yields the first \(n\) power sums of \(1-q_i\); Newton identities reconstruct the root polynomial even with repeated roots.

The two single-marginal impossibility statements were checked separately. The first marginal can always be absorbed into the unknown baseline. For the second marginal, \(\Phi_q'(z)>0\) on \((0,1)\), with endpoints 0 and 1, so every admissible second-failure survival can be represented using any chosen positive hazard profile and component count by changing the baseline. The numerical artifact independently checks the main identity, Newton reconstruction, monotonicity, and a different-component-count reproduction of the same second-failure marginal.

Hidden-hypothesis checks included repeated hazard multipliers, unknown component count, the unavoidable common scale equivalence, survival support endpoints, and the distinction between marginal and joint observation. The theorem intentionally excludes zero multipliers, which would collide with the exponent-1 term.

## Originality

PASS, to the best of our knowledge, with a clearly stated residual literature risk.

The heterogeneous-PHR order-statistic literature is extensive, but the checked primary and review sources center on stochastic order, dependence, skewness, reliability bounds, or parametric inference. Pledger and Proschan (1971) initiated heterogeneous order-statistic and spacing comparisons. Kochar's 2012 review describes this lineage. Zhao, Li and Balakrishnan (2009) give likelihood-ratio comparisons for the second order statistic in heterogeneous exponential samples. Kochar (2022) proves dependence comparisons and extends them to the PHR model through a monotone cumulative-hazard transformation. These results do not state the two-marginal baseline-free identification theorem claimed here.

Parametric black-box reliability inference was also checked as a possible equivalent formulation. Tan (2007) estimates exponential component reliabilities from uncertain series/parallel system-life data under different information assumptions. Current `kofn` documentation demonstrates that heterogeneous exponential rates can be estimated from black-box system lifetimes in fixed parametric models, and explicitly notes permutation symmetry. Accordingly, identifiability in a known exponential baseline is not treated as a new contribution here.

Navarro and Spizzichino (2010) study the relation between order-statistic copulas and heterogeneous parent marginals. Broader searches covered masked-failure data, k-out-of-n system inference, heterogeneous exponential samples, order-statistic characterizations, semiparametric proportional hazards, unknown baselines, and identifiability from first/second failure times. No checked source supplied the exact transform
\[
S_2(S_1^{-1}(u))=\sum_i u^{1-q_i}-(n-1)u
\]
as a device for recovering an unknown component count and all relative hazards from two unlabeled marginal laws, nor the sharp result that either marginal alone is completely nonidentifying under an unrestricted common baseline.

The strongest residual originality risk is older reliability/inverse-problem literature under different terminology. The full 1971 Pledger--Proschan chapter was not inspected theorem by theorem. Older masked-data literature may also contain a semiparametric specialization not surfaced by the searches. This is residual uncertainty, not evidence of coverage.

## Value

PASS.

The result isolates an unexpectedly sharp information boundary for heterogeneous reliability systems with an unknown baseline. A series-system lifetime marginal and a fail-safe second-failure marginal can be collected from separate system populations and require no component labels or paired trajectories, yet together recover the entire relative hazard spectrum and even the component count. In contrast, either system-lifetime marginal by itself is compatible with every positive hazard profile after changing the nuisance baseline.

The theorem also supplies an exact model-class diagnostic and a constructive finite-derivative inversion when the component count is known. These statements separate structural identification from parametric likelihood fitting and make clear which information comes from combining system configurations rather than from specifying a baseline family.

## Scientific limitations

The statement assumes mutually independent components with a single common PHR baseline and strictly positive multipliers. It concerns exact population distributions. It does not provide statistical rates, robustness guarantees, confidence sets, or a stable numerical estimator. Finite exponential inversion is known to become ill-conditioned when exponents nearly collide. Component labels remain unidentified, and the absolute hazard scale is inseparable from the baseline without normalization. Censoring, dependent components, ties, zero multipliers, baseline misspecification, and approximate proportionality are outside the result. Older reliability literature remains a residual originality risk as described above.
