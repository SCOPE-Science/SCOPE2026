# Scientific review

## Correctness — PASS

The triangular martingale decomposition is an exact identity. Its conditional covariance has positive cross term because attachment to the root and attachment to a leaf are disjoint categories; the off-diagonal sign was checked directly. An exact variance recursion bounds leaf fluctuations uniformly, supporting the probabilistic replacement of conditional leaf probability by its deterministic mean. The predictable quadratic variation is a Riemann sum and converges for every \(\theta_n/n\to c\in(0,\infty)\). Bounded increments establish Lindeberg; Cramér--Wold and the martingale CLT establish the joint limit. Explicit integration and positive definiteness are verified. The exact finite covariance and its proof are separately checked, and a standalone rational enumerator replays the finite moments. The normal limit is not asserted on the basis of finite experiments.

## Originality — PASS, with residual priority risk

Leckey--Neininger, arXiv:1202.2439, studies *fixed* \(\theta\), derives the exact leaf mean and a marginal leaf CLT. Hiesmayr--Işlak, arXiv:1712.03572, establishes marginal results for weighted recursive trees and a separate branch-count CLT; the paper's statements and relevant proof sections do not give this triangular-parameter joint limit. Previously established fixed-weight scalar CLTs and the mean-induced finite covariance are expressly excluded from the novelty claim. The asserted contribution is the bivariate Gaussian limit with explicit covariance at \(\theta_n/n\to c>0\), not merely reparameterizing fixed-weight asymptotics. An unlocated more general multivariate theorem remains a historical-priority risk.

## Value — PASS

This critical scale makes root attraction compete with the aggregate weight of other vertices. Both branch and leaf counts fluctuate on a square-root scale, with a strictly positive, nontrivial correlation. Determining their joint covariance matrix answers a natural dependence question that marginal CLTs cannot settle and distinguishes the linear-attraction regime from fixed root weight. The theorem provides a reusable probabilistic description for counts of root-founded families and terminal nodes in growing weighted trees.

## Closest literature and limits

Leckey--Neininger (2012, arXiv:1202.2439), Theorem 2.5 and its proof: fixed root weight and marginal leaf count. Hiesmayr--Işlak (2017, arXiv:1712.03572), Sections 3 and 6: weighted-tree marginals and branch count, not the stated joint linear-weight regime. The result has no established uniform version at \(c=0\) or \(c=\infty\), and independent priority assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
