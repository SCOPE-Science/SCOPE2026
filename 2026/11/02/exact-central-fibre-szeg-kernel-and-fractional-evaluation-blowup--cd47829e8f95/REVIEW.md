# Scientific assessment

## Correctness — PASS
The canonical unweighted boundary measure is explicitly specified, and the orthogonality proof uses both Haar-circle actions. The pure powers form the complete restriction-relevant orthogonal subspace because the remaining monomials vanish at the central fibre and evaluations are continuous. The Vandermonde moment, beta-integral resummation, arcsine identity and expansion prove all degrees and all fibre points analytically. The standard-library checker verifies finite sample identities separately; it does not purport to certify infinite assertions.

## Originality — PASS under inspected evidence
The 2026 primary paper [1] constructs the Hardy space and proves its abstract kernel projection and averaged radial growth; it does not state the explicit two-point fibre kernel or its fractional point-evaluation asymptotic. The 2024 pentablock operator paper [2] studies isometry models, not this canonical kernel. Searches for equivalent reciprocal-central-binomial, hypergeometric and arcsine formulations produced no covering indexed result. The exact evaluated invariant is more specific than the general projection formula and requires the additional moment computation. Historical implicit coverage is a remaining risk, especially because ingredients of the computation are classical.

## Value — PASS
This central slice is the nilpotent-matrix fibre and is singled out by the domain symmetries, not chosen for numerical convenience. The exact formula exhibits a fractional diagonal boundary singularity with sharp constants in a newly introduced several-variable Hardy space. This is a usable benchmark for sharp evaluation and interpolation analysis and a complementary local counterpart to the known averaged diagonal estimate.

## Scope and risks
Only the canonical unweighted Hardy space and the central fibre are classified. No full kernel formula, weighted-space statement, uniform boundary bound or external verification is claimed. The initial Hardy-space construction, bounded evaluations and abstract projected Szegő formula are credited to [1].

Self-review: passed. Independent audit: not yet performed.

References: [1] Guicong Su and Nitin Tomar, arXiv:2610.17729v1, Sections 2--3; [2] Abhay Jindal and Poornendu Kumar, arXiv:2406.05996v2.
