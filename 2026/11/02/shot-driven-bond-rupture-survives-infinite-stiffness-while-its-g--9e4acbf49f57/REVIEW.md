# Self-review

## Correctness — PASS

The relative-coordinate OU reduction gives drift \(a=\lambda+2k\), total jump rate \(2\omega\), Gaussian jump marks \(N(0,\sigma^2)\), and Gaussian diffusion rate \(4D\). The Brownian convolution converges uniformly to zero on every compact interval almost surely by pathwise integration by parts and the Brownian modulus of continuity. Since each bounded time horizon contains finitely many jumps and continuous marks avoid the threshold exactly, the rupture stopping time is eventually exactly the first over-threshold jump time, on a common-noise coupling. A first mark larger than \(2L\) forces rupture regardless of any pre-jump value in \((-L,L)\), giving a uniform exponential upper domination and all positive moment limits. The Gaussian surrogate's mean exit solves the displayed backward equation, and its integral and endpoint asymptotic have been rederived. Exact symbolic checks and illustrative finite simulations passed from the package's standalone verifier.

A finite sample is not the proof of an almost-sure statement. The proof covers every real stiffness above a random finite bound; it does not require a discretization of stiffness. All parameter quantifiers and cases \(D=0\) and \(D>0\) are explicit.

## Originality — PASS (qualified best-knowledge)

The motivating paper, Goel–Marathe arXiv:2610.26316v1/v2, addresses well-to-well and center-of-mass escape in a nonlinear dimer and uses a Gaussian small-kick approximation for its analytical MFPT. It does not state the strong-stiffness fixed-relative-bond threshold law. Masoliver's 1987 full-text sections III, V, VI provide first-passage equations and solvable one-sided exponential/fixed-shot models; his general framework is acknowledged but does not give this two-sided Gaussian-marked all-moment limit explicitly. Borovkov–Novikov 2007 (full text, sections 1–3) concerns martingale identities and, for explicit transforms, exponential positive jumps; its exponential limit takes a distant boundary, not stiffness to infinity at fixed boundary. Related small-amplitude Lévy metastability is a different scaling. Searches of related published records and comparison with available earlier mathematical claims found no matching stated claim or stronger applicable theorem.

The residual priority risk is that general existing shot-noise first-passage methods could imply the present sharp limit after a nontrivial specialization, or that an uncatalogued dimer-rupture study already proves it. This qualified check does not claim global uniqueness or independent priority validation.

## Value — PASS

The source studies how bond strength affects escape, making the fate of relative-bond failure under stiff coupling a natural, motivated observable. The theorem identifies an exact nonzero stiffness-independent rupture-rate floor, not a small numeric correction. It explains a severe failure of the widely used effective-diffusion approximation: equal instantaneous variance but an asymptotically finite mean versus an exponentially divergent mean. The theorem includes the entire limiting rupture-time law and all positive moments, with the strong samplewise coupling result supplying a structural mechanism. Its value is confined to the specified harmonic idealization and fixed shot amplitudes.

## Scientific limitations and related material

Harmonic localization and instantaneous unbounded Gaussian kicks are assumptions, not properties proved for Morse or nonlinear double-well dynamics. The shot-noise and Gaussian diffusion models are not interchangeable for this exit observable at fixed amplitude. The 1987 Masoliver and 2007 Borovkov–Novikov full texts are acknowledged as broad precursors; possible implicit consequences remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
