# Review: two covariance reversals from one pendant edge

## Correctness — PASS

The all-parameter identity follows pointwise from \(B=M-LZ\), with \(Z\) indicating that the sole cycle is fully retained. Computing each edge/isolated-vertex and cycle/isolated-vertex covariance gives the exact unicyclic formula, and specializing to the single-leaf host yields the polynomial \(\Phi_L\). Its transformed coefficients show at most two positive roots. The four small cases are disposed of by strict negative quadratic discriminants, and an exact witness for \(L=7\), with a uniform lower bound for \(L\ge8\), establishes two simple roots in every larger case. Endpoint signs then force the complete three-phase classification. The standalone code passed 212 independent exact-rational checks, including exhaustive configurations for cycles and lollipops up to cycle length eight. Its checks corroborate rather than substitute for the unbounded proof.

## Originality — PASS, with residual risk

The closest published bridge studies are Elçi–Weigel–Fytas (random-cluster bridge densities and bridge fluctuations, arXiv:1509.00668), Bonneau–Biham–Kühn–Katzav (configuration-network bridge frequencies and **endpoint-degree** covariances, arXiv:2009.03682), and Lanchier–La Salle (percolation cluster moments and isolated vertices, arXiv:2111.01982). An accessible published published-finding corpus result gives component-count/triangle-count covariance, not bridge-count/isolate-count covariance. The examined statements and their proved implications do not provide the sharp cycle-length-seven two-root classification. Relevant published work could still encode it implicitly in general percolation generating functions; complete priority cannot be guaranteed. Existing edge-level and component-level identities are acknowledged rather than claimed as new.

## Value — PASS

Bridge vulnerability and isolated-node fragmentation are two natural network-resilience diagnostics. Their joint covariance is not sign-determined by monotonicity because creating cycles can destroy bridges. The exact one-leaf family demonstrates the resulting *reentrant* negative–positive–negative dependence at a sharp natural graph-size threshold, while the leafless cycle gives a contrasting single switch. This is a complete infinite-family classification, not a parameter chosen for a favorable calculation.

## Scope and limitations

Independent homogeneous Bernoulli bond retention only; cycle length at least three; no claim about arbitrary unicyclic hosts, multiple cycles, or stochastic independence at covariance zeros. The critical probabilities are uniquely defined as roots, without closed-form expressions. There has been no independent validation.

Self-review: passed. Independent audit: not yet performed.
