# Self-review

## Correctness — PASS

The exact scalar specialization is obtained from the paper's unrelaxed last-sweep equations rather than a surrogate scheme. Eliminating the relaxed inner pressure variable yields the fourth-degree characteristic polynomial in RESULT.md; independent direct-matrix and symbolic factorization calculations reproduce it. At zero flow the polynomial factors into \((\zeta-1)(\zeta-1/3)(\zeta^2+2a_K\zeta-a_K)\). Classical strict Schur inequalities give exactly \(-1<a_K<1/3\); the perturbation of the physical root has rigorously negative first derivative. The claimed implication is only for sufficiently small **positive** flow and avoids unproved equality cases. Finite numerical checks do not stand in for the proof.

## Originality — PASS, with residual priority risks

The closest source is Altmann--Deiml, arXiv:2403.12699: Proposition 4.1 proves \(3\omega^K<(2+\omega)^{K-1}\) as a sufficient bound, and Section 5.1 already **observes** that even sweep counts can be more stable. Those findings are prior art, not recharacterized as new. The new claim is the exact open necessary/sufficient scalar *second-order spectral* threshold for each parity and the physical-root asymptotic, notably \(K=2\) permitting couplings strictly between \(1\) and \(2\). The first-order Euler result arXiv:2304.12224 happens to yield the even parity inequality but has a different update and cannot imply this BDF2 spectral classification. The fixed-stress higher-order work arXiv:2311.14400 uses a distinct stabilized iteration. No covering statement was identified in the checked primary texts, mathematical search results, or the known published records. Older spectral analyses or a later uninspected revision might contain an equivalent result; novelty is not certified independently.

## Value — PASS

The original method's published experiments document a sizable unexplained even-versus-odd stability difference. A sharp modal threshold is a natural diagnostic of whether its general sufficient inner-iteration requirement is conservative, and the \(K=2\) window \(1<\kappa<2\) gives a material (not tiny) improvement for small-positive-flow instances. The claim does not generalize this advantage to arbitrary spatial discretizations and does not assert new high-dimensional error theory.

## Limitations and closest literature

Primary comparison: Altmann--Deiml (2024), arXiv:2403.12699, Sections 3.6, 4 and 5.1; earlier first-order iteration, arXiv:2304.12224, Sections 3--4; related higher-order fixed-stress scheme, arXiv:2311.14400, Sections 2--4; one-pass BDF2, arXiv:2203.16664. Strict parameter inequalities exclude marginal points. The mathematical finding is self-reviewed only.

Self-review: passed. Independent audit: not yet performed.
