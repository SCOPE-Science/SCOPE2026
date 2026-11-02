# Scientific review

**Correctness (C) — PASS.** For the extreme-eigenvector plane the bilinear denominator is governed by the explicitly computed symmetric \(2\times2\) matrix with determinant \(ab c_{11}c_{22}-(a+b)^2c_{12}^2/4\). The exact sample-correlation beta distribution gives the event probability. The deterministic threshold follows from the proved sharp lower cosine bound and an SPD Householder-reflector witness. Full-space probabilities are not asserted for \(N>2\). The local verifier passed 5,612 diagnostic checks with 480,000 random sketches; no finite sample is used as proof.

**Originality (O) — PASS under available evidence.** Related randomized Arnoldi work discusses sketched harmonic Ritz values and positivity under embedding assumptions; the complete original paper was not accessible here and is a residual priority risk. The closest earlier fixed-vector result (identifier `16336c9a-1e80-4709-ae3a-89d629a714c3`) determines the probability at any one vector chosen *before* sketching, including its optimal worst-case vector. That statement does not imply the *probability that there exists a vector after sketching*. The new beta law is a uniform event for one common Gaussian sketch, and the sharp embedding radius pertains to simultaneous positivity. Related published searches found no exact uniform statement; negative search results do not prove uniqueness.

**Value (V) — PASS.** Uniform post-sketch positivity is an algorithmically meaningful distinction when bases, candidate directions, or Rayleigh minimizers are selected from already-sketched information. The exact two-mode beta risk gives a sharp safety benchmark even though full-space adaptive risk can be larger; the simultaneous embedding guarantee has an optimal achievable cutoff. These are nontrivial sharp quantitative results, not a reformulation of a fixed-vector tail.

The main limitations are two-mode restriction for the exact probability, real Gaussian sketch, exact arithmetic, and incomplete access to the original full manuscript. Independent specialist review and comprehensive historical priority checks remain outstanding.

Self-review: passed. Independent audit: not yet performed.
