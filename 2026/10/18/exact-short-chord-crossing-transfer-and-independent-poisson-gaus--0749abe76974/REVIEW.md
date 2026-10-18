# Scientific review

## Correctness — PASS

The exact transfer identity follows by counting ordered disjoint edges of the boundary cycle and conditioning on their occurrence in the uniform perfect matching. Every selected simple chord crosses no other chord; deletion preserves alternation of residual endpoints and leaves a uniform residual matching. This proves the coefficientwise generating-function identity for all stated \(n,k\), including \(k=n\). Substituting the classical mean and variance for crossing count produces the finite-moment consistency formulas. The joint characteristic-function argument relies explicitly on the published marginal crossing central limit theorem, shows \(a_{n,k}\le2\), and applies dominated convergence before invoking Lévy's theorem. Direct exact enumeration of every matching through seven chords passed 487 assertions. The program is corroboration, not an infinite certificate.

## Originality — PASS, with historical-priority risk

Acan (arXiv:1501.01489), Section 3, proves Poisson marginal short-chord behavior by counting compatible prescribed chords; it does not assert the bivariate transfer with a crossing variable. Flajolet–Noy (2000), Theorem 3, gives the crossing marginal moments and Gaussian limit, not the joint marked-simple-chord law. Paguyo (arXiv:2104.01134) studies separate marginal approximation rates. The known exact finite covariance is explicitly excluded from the novelty claim. A complete joint generating polynomial and joint independent Poisson–Gaussian fluctuations are strictly more informative than those separate marginal or covariance statements. The elementary deletion mechanism creates a real risk that an unlocated multivariate generating function already implies this identity; this remains a residual priority risk rather than evidence of a covering result.

## Mathematical value — PASS

Simple chords are the local isolated structures in a random chord diagram, while crossing pairs are a global intersection-graph statistic. The theorem gives the exact crossing distribution in every fixed-simple-chord stratum, notably diagrams with no simple chords, via a finite transform of known crossing enumerators. Its joint weak limit resolves the probabilistically meaningful question whether a Poisson local statistic and a Gaussian global statistic decouple—not something established by their separate marginal limits or by a vanishing correlation.

## Sources and limits

Primary material inspected: Flajolet–Noy (2000), crossings theorem and component discussion; Acan (arXiv:1501.01489), Sections 1, 3, 4; Paguyo (arXiv:2104.01134), introduction, stated marginal theorems and supporting arguments; Pilaud–Rué (arXiv:1307.6440), introduction and stated enumerative scope. No comprehensive historical-priority certificate or independently reproduced mathematical audit has been provided. The complete proof and reproducibility steps appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
