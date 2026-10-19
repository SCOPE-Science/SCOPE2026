# Scientific assessment

## Correctness — PASS

The claim is proved for \(n\ge3\), \(K>1\), and \(1<t<K\), without restricting arbitrary admissible rank-one preconditioners to diagonal form. Sherman–Morrison and Rayleigh optimization establish both global Bregman minimizers; one-rank interlacing bounds the entire competing class for the spectral condition number. The logarithmic-mean inequalities and one-variable monotonic ratios establish the precise thresholds and the sharp unattained supremum. The standalone verifier passed 9,093 seeded finite checks, independently supporting but not replacing the algebraic proof.

## Originality — PASS with residual risk

The spectral scores are explicitly inherited from Bock and Andersen's 2023/2025 matrix-truncation work and are not themselves claimed as new. The independently proved contribution is the full all-rank-one sharp spectral comparator, two logarithmic-mean switches, four-region phase diagram, and the same unbounded exact fixed-\(K\) competitive gap for both divergence orientations. The 2023 positive-semidefinite relative-error condition-number theorem excludes the indefinite situation. The 2025 Kaporin article uses a different condition measure, although only its abstract could be inspected; an overlooked equivalence in prior spectral-preconditioning literature remains possible.

## Mathematical value — PASS

The result addresses a natural decision question for low-rank preconditioner design: whether minimizing either asymmetric Bregman divergence controls the extreme-eigenvalue condition number relative to the best correction under the same rank budget. It gives sharp quantitative divergence from that optimization goal, even after allowing every real symmetric rank-one correction; the family is the smallest dimension in which a fixed middle eigenvalue supplies a nontrivial obstruction. It does not assert that worse spectral conditioning necessarily means slower realized Krylov convergence.

## Closest literature and limitations

* Bock and Andersen, *A New Matrix Truncation Method for Improving Approximate Factorisation Preconditioners*, arXiv:2312.06417 (2023), DOI:10.1002/nla.70012 (2025): divergence objectives and mode scores, numerical spectral comparisons.
* Bock and Andersen, *Preconditioner Design via the Bregman Divergence*, arXiv:2304.12162 (2023): condition-number optimality for positive-semidefinite relative corrections with a nontrivial kernel, not mixed-sign defects.
* Bock and Andersen, *Connecting Kaporin's condition number and the Bregman log determinant divergence*, arXiv:2503.22286 (2025): abstract-only comparison; determinant/trace-type conditioning not proven equivalent to the spectral quantity here.

Scope: exact positive-definite diagonal family, all positive-definite real rank-one updates, \(n\ge3\), exact arithmetic, unique divergence minimizers away from ties. Literature indexing is incomplete, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
