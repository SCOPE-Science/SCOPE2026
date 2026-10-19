# Self-review

## Correctness — PASS
For deterministic nonzero real matrices, the proof explicitly conditions on the common left Gaussian, derives an independent chi-square multiplier for the iid right draws, and proves the exact origin coefficients and three-case convolution asymptotics. All prefactors, singular-value normalization, the critical logarithm, the strict moment cutoff, and the infinite-probe strong-law limit follow from the written argument. The reproducibility script numerically evaluates exact finite-dimensional integrals and tests stated isotropic prefactors, without using numerical experiments as an infinite-dimensional proof.

## Originality — PASS
The nearest literature is Bujanović et al. (2024), Theorems 3 and 5, whose columns comprise independently sampled Gaussian factors, and Bujanović–Kressner (2020) on independent random rank-one vectors. Güttel et al. (2022) also use independent bilinear Gaussian probes. The shared-left construction violates that crucial premise, producing a rank-limited exponent absent from the corresponding independent-law calculation. Completed semantic mathematical-record searches using shared-factor, factor reuse, chi-square product and rank/probe aliases found no equivalent covering statement. The elementary convolution lemma is acknowledged as standard in method. Risks include unindexed equivalent formulations and the limited literature coverage, not a claim of exhaustive novelty certification.

## Value — PASS
The result makes the rank cost of factor reuse explicit. In ordinary independent-factor tensor sketching, adding probes improves lower-tail power; a shared factor leaves an irreducible nondegenerate error even with infinitely many right probes. The exact constants, logarithmic equality case, and moment threshold make the obstruction precise for sketch-norm validation and dependent structured random projections. This is a motivated mathematical comparison of two genuinely different sketch distributions.

## Limitations
No claim is made for the independent-column algorithms of the cited papers or matrices chosen adaptively from sketch data; the coefficient limits fix the rank, probe count and positive singular values. The self-review is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
