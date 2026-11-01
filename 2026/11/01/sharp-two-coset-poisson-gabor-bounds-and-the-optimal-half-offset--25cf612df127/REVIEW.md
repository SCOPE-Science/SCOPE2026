# Scientific review

## Correctness — PASS
The proof constructs the exact \(L^2\) frame multiplier under a normalized unitary Zak transform and checks the window normalization from its Fourier transform. Its positive derivative with respect to \(\cos(2\pi x)\) reduces global frame extrema to two position fibers. On the minimum fiber, a hyperbolic-cosine identity handles both frequency-wrap intervals and supplies the minimum of the two values. On the maximum fiber, strict convexity of the frequency function shows every maximum occurs at a gluing endpoint. A direct fiber-concentration argument justifies sharp, not merely valid, bounds. The quadratic degeneration follows from Taylor's theorem. The pure-Python spot checker independently exercises the spatial series. The proof does not rely on those spot checks to establish the all-parameter statement.

## Originality — PASS under inspected evidence
The closest 2026 Poisson result (Belov–Semenov, arXiv:2610.30037v1) supplies a qualitative criterion for the same orientation and covers existence, but its inspected statement and proof do not determine sharp bounds for two frequency cosets or optimal offset. The 2013 Kloos–Stöckler paper provides the Zak formalism and qualitative/bound results for exponential B-spline windows, which covers the method but not this Poisson two-coset formula. The 2022 Cauchy-kernel operator article concerns a different window and rectangular time-frequency lattices (abstract and introduction inspected only). Indexed comparison records for sharp tent-spline and hat-spline bounds concern different generators and geometry. An inspected previous Poisson Gabor bounds statement concerns two *translation* cosets, not two *modulation* cosets; the latter does not follow by a modulation relabeling of the former because the Fourier-transformed generator is exponential rather than Poisson. Historical implicit equivalent formulas are a residual priority risk.

## Value — PASS
This is a natural two-coset nonlattice subfamily of the recently studied semi-regular Poisson Gabor systems. The exact global constants, strict offset optimizer, and sharp quadratic rate of loss of stability refine the available qualitative criterion and provide an explicit conditioning benchmark for periodic nonlattice frequency sampling. The result makes no claim of resolving the general semi-regular frame set.

## Closest literature and limits
Belov–Semenov (2026), Kloos–Stöckler (2013), and Belov–Kulikov–Lyubarskii (2022) as cited in RESULT.md. The result concerns exactly two frequency cosets at integer translation spacing; extension to arbitrary irregular sets is unproved. Priority against every historical periodic Gabor frame-bound formula remains open.

Self-review: passed. Independent audit: not yet performed.
