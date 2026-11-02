# Scientific review: paired sketched Rayleigh ranking

## Correctness — PASS

The algebraic sign factorization is exact; the \(2\times2\) Gram matrix of the sketched orthonormal eigenvectors has a real Wishart distribution. The trace-normalized disk density is correctly normalized for every integer \(k\ge2\). Conditional beta integration, Tonelli expansion and gamma-function simplification yield the finite-row formula. A separate circle argument handles \(k=1\), and an integration-by-parts argument gives the \(k=2\) elliptic form. Gamma duplication and dominated convergence prove the fixed-overlap asymptotic. The extracted standalone verifier passed 700,113 symbolic, numerical, and sampled checks. These checks corroborate, but do not replace, the proof. The candidate equality endpoint is explicitly excluded.

## Originality — PASS, qualified

The closest directly inspected primary references were Nakatsukasa--Tropp, arXiv:2111.00113 (2021), and Balabanov--Grigori, arXiv:2111.14641 (2021). Their relevant full-text sections describe sketched eigenvalue projections, sketched Rayleigh quotients, and embedding-based comparisons, but do not give the exact strict ranking-inversion law for two coupled fixed trial vectors and one common Gaussian sketch. A checked earlier one-quotient spectral-escape result integrates an entirely different event; it does not imply this paired ordering probability. Separate searches for equivalent Wishart-disk and Gaussian-ratio expressions produced no directly covering statement. The Wishart density and special-function identities are recognized as classical. The principal residual risk is an unindexed specialist distribution identity or an uninspected publication that implies the same formula; independent publication priority remains unverified.

## Mathematical value — PASS

A sketched quotient can be individually accurate or bounded while a pairwise ranking still fails. The result gives an exact benchmark for that **joint decision**, in terms of sketch dimension and candidate overlap, with a sharp \((\rho/2)^k/\sqrt{k}\) rare-event law rather than a loose generic subspace-embedding guarantee. The eigenvalue-gap cancellation and two-row elliptic expression identify nontrivial structure. This is a motivated exact benchmark for numerical eigenvalue estimation, not a general proof of convergence or preservation of ordering for arbitrary candidate sets.

## Limitations and literature comparison

The analysis assumes a symmetric matrix, two orthonormal eigenmodes, swapped trial coefficients, and shared real i.i.d. Gaussian sketch rows. It covers two **separate one-dimensional sketched quotients**, not an eigenvalue ordering of one joint projected matrix. At equal candidate vectors, strict inversion is impossible even though the interior probability has a nonzero limiting value. No independent audit or independent publication-priority assessment has been performed. Full-text material inspected: the relevant eigenvalue/symmetry sections of Nakatsukasa--Tropp (https://ar5iv.labs.arxiv.org/html/2111.00113) and the eigenvalue/supplemental-quotient sections of Balabanov--Grigori (https://arxiv.org/pdf/2111.14641). A later Gaussian eigenvalue sketching paper was compared only by abstract and not claimed to be excluded by whole-document inspection.

Self-review: passed. Independent audit: not yet performed.
