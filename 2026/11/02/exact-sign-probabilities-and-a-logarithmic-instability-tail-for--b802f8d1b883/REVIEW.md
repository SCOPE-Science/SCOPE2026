# Scientific review

## Correctness — PASS

The uniquely determined Lagrange quadrature weights have explicitly integrated cardinal-polynomial numerators. The affine normalization to ordered centered nodes makes their signs transparent; the mutually exclusive negative-weight events and their two-dimensional integrals give the exact sign probabilities. The tail proof isolates both adjacent node gaps, controls the complementary one-small-gap region by an explicit inverse-gap bound, and applies an exact hyperbola-area formula with matching upper and lower bounds. Letting the collision-square cutoff shrink proves the coefficient \(2\), and layer cake yields the strict moment frontier \(q=1\). The standalone exact-fraction checker verifies 560 finite cases, the independent probability integrals, and the tail constant, but finite evidence is not used as an infinite proof.

## Originality — PASS, qualified

Van den Bos et al. (arXiv:1809.09842) construct positive-weight rules by selecting from additional samples, not by accepting three independent uniform nodes without changing them. Van den Bos and Sanderse (arXiv:1902.07477) characterize deterministic positivity regions for node addition, not the probability law or sharp operator-norm tail. Yu and Townsend (arXiv:2202.04722) bound absolute trigonometric quadrature weights under separated periodic grid perturbations, unlike free uniform-node collisions. Neumayer, Schäfer, and Ullrich (arXiv:2610.32699) give high-probability positive rules after using many independent candidates and adapting the weights; this does not imply the sign distribution or tail of the uniquely determined unadjusted rule from exactly three draws. Related fixed-node Newton–Cotes work controls different sign configurations. A published degree-two random-node interpolation moment theorem already yields the order-one moment threshold through a Lebesgue-constant upper bound, but does not provide this quadrature-specific sign distribution or the precise logarithmic tail coefficient. Searches of direct expressions, sign laws, aliases, quadrature condition measures, published mathematical records, and relevant source texts did not identify an implication strong enough to give the full stated theorem. Failure to find coverage is not proof of absolute priority; specialized legacy sources are a residual risk.

## Value — PASS

Absolute quadrature weight sum is the exact amplification of bounded independent sample-value perturbations. A common design strategy is to keep nodes that were sampled at random rather than optimize their positions. This theorem quantifies the smallest nontrivial quadratic-exact case: fully positive weights occur with probability only \(\frac12\log3-\frac13\), and a logarithmically enhanced double-collision mechanism forces infinite mean amplification. The exact probability and leading coefficient are not consequences of merely knowing that negative weights sometimes occur or that a related interpolation norm has an infinite mean. They provide sharp benchmarks for random-node quadrature stability and for evaluating node-selection strategies. Nothing is claimed for arbitrary integrands, higher node counts or floating-point computations.

## Residual scientific limits

Independent examination and exhaustive historical publication-priority checks remain outstanding. The result assumes independent uniform draws, precisely three nodes, exact arithmetic and standard polynomial moments. The simulation and finite rational checks are diagnostics, not proof substitutes.

Self-review: passed. Independent audit: not yet performed.
