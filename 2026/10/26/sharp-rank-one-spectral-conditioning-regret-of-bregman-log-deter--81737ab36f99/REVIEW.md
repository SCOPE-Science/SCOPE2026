# Scientific review

## Correctness — PASS

The theorem quantifies over every \(M>1\), \(0<\varepsilon<1\), and every positive-definite Hermitian rank-one correction to the identity. The BLD minimizer is derived independently from the determinant lemma and a one-variable derivative test. The global spectral comparison requires a separate min–max proof over both signs of the rank-one correction; restricting to commuting candidates would be insufficient. Boundary ties and the exponentially sharp fixed-\(M\) ratio follow from monotonicity of \(z-\log z-1\). Exact symbolic identities and finite numerical checks in `verify.py` agree with the proof.

## Originality — PASS, with residual risk

The closest source, Bock–Andersen arXiv:2312.06417, already proves the low-rank BLD selection principle and compares selected numerical preconditioners. It does not furnish the global spectral-condition optimum over all signed Hermitian rank-one corrections or the exact mismatch wedge. The earlier arXiv:2304.12162 concerns nonnegative correction error and therefore does not cover the signed instance. Foundational Bregman matrix-nearness and low-rank factorization-error works address different aims. Searches by title, exact spectrum, aliases, and implication yielded no decisive equivalent. An unindexed equivalent counterexample or an implicit extension of other general rank-one approximation theory remains possible; originality is not a claim of exhaustive coverage.

## Value — PASS

Divergence minimization and spectral-conditioning optimization are competing, natural design criteria for the *same* constrained preconditioner family. A complete disagreement region and an exponentially large sharp regret demonstrate that one criterion does not provide any dimension-free or spectrum-independent multiplicative surrogate guarantee for the other. This is a motivated boundary result, not merely a renamed BLD minimizer or an arbitrary finite calculation. It does not prove a CG iteration-count penalty.

## Scientific limitations and literature

The domain is a three-eigenvalue SPD system with an indefinite normalized factorization error, fixed baseline identity, exact arithmetic, and rank one. The 2023 Bock–Andersen BLD minimizer is prior art, and the broader arbitrary-rank and real-world solver behaviors are unproved. Later studies of Kaporin conditioning optimize a different functional. Source access was strongest for the full Bock–Andersen matrix-truncation text and the relevant positive-error predecessor; other background papers were compared at abstract/metadata level and do not justify exhaustive negative-coverage claims.

Self-review: passed. Independent audit: not yet performed.
