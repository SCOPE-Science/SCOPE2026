# Scientific review

## Correctness

**PASS.** The specified eight-state continuous-time generator is irreducible for positive boundary rates. The explicit eight positive stationary weights sum to the normalizer and solve all eight generator balance equations identically as polynomials in the nonnegative resetting rate. Exact algebra yields the three covariances. Descartes' rule of signs together with signs at resetting rates 0, 1 and 3 establishes exactly two positive distal-covariance zeros. Exact rational intervals isolate them. Explicit inequalities establish strictly negative neighboring covariances at every resetting rate at least 1. Perturbation persistence follows from continuity of the unique finite-chain invariant law. The included standalone checker reproduces the algebra and separately solves rational finite-state systems. The universal proof does not rely on a finite numerical scan.

## Originality

**PASS, conditional on the inspected literature.** Pelizzola and Pretti's *Totally asymmetric simple exclusion process with local resetting and open boundary conditions* (Journal of Physics A **55**, 454001, published November 11, 2022; DOI 10.1088/1751-8121/ac9d72; OA preprint arXiv:2402.13698) defines the self-review, develops a continuum mean-field approximation, and discusses nearest-neighbor covariances from simulation, not an exact three-site distal covariance or its two sign reversals. Pelizzola, Pretti and Zamparo (arXiv:2012.10993) study periodic boundaries and particle-number conservation rather than these open-boundary rates. Miron and Reuveni (arXiv:2011.08241) study symmetric hopping and provide a mean-field/simulation analysis; their abstract was inspected, not their complete article. Indexed literature and related published research-record searches did not expose a statement entailing the present exact finite-chain phase diagram. Solvability of a finite generator by general linear algebra is a method, not in itself a previously stated sign theorem. An unindexed exact finite-state specialization remains a priority risk, and search absence does not certify global novelty.

## Value

**PASS.** The nonadjacent pair is the minimal-distance witness to nonlocal resetting correlations in a three-site chain. The exact positive–negative–positive return is a robust qualitative effect, not a small coefficient improvement or an arbitrary choice of numerical cutoff. It contradicts the tempting extrapolation that distal correlations must share neighboring-pair signs: on the whole reentrant tail, neighboring pairs remain anticorrelated. The open-neighborhood persistence makes this a non-isolated counterexample relevant to evaluating finite-size correlation closure in driven interacting-particle models. It does not assert a bulk phase transition or resolve all boundary-rate regimes.

## Literature limits and verification

Compared statements and mechanisms, not merely titles: the 2022 open-boundary work's mean-field closure suppresses covariance, the 2020 periodic model differs in conservation and boundaries, and the 2020 symmetric-reset work differs in transport direction. The exact finite-size covariance polynomial is fully reproduced from the stated transition generator. The algebraic checker uses exact rational arithmetic, and its finite parameter examples are corroboration rather than proof.

Self-review: passed. Independent audit: not yet performed.
