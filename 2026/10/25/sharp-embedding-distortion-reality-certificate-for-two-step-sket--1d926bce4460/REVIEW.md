# Scientific review

**Correctness — PASS.** The reduction to the three-dimensional sketch Gram matrix is exact for all real symmetric matrices after two Lanczos steps. The scalar two-by-two compression proof establishes the sharp metric cross-term constant \(\varepsilon/\sqrt{1-\varepsilon^2}\), and the reduced discriminant implies the full bound. The explicit positive-definite tridiagonal witness attains equality and a defective boundary. The included verifier checks symbolic identities and 1000 randomized instances, but those finite checks are not the universal proof.

**Originality — PASS, best-knowledge assessment.** Nakatsukasa--Tropp (arXiv:2111.00113, section 6.8) already state that symmetric sketched Ritz values can be nonreal. De Damas--Grigori (arXiv:2407.03208v1) provide the modern sketched Arnoldi/Petrov--Galerkin formulation. Liu--Liu (arXiv:2610.22261v1) provide a real-Schur remedy. A previously recorded Gaussian-sketch result (identifier `7cd7cbdb-20aa-4dae-820a-6537f0baf613`) quantifies a probability of nonreality on a tridiagonal class. These statements do not imply the sharp *uniform distortion* certificate and its exact worst-case imaginary-part formula. The inspected literature and searches did not identify coverage, but an undiscovered general perturbation theorem remains possible.

**Value — PASS.** A directly usable reality certificate for sketched eigensolvers now depends on measurable consecutive Lanczos couplings and a norm-embedding tolerance. Sharpness makes the threshold meaningful rather than a loose gap argument; a defective boundary identifies the transition mechanism. The proof is exact and does not require infinite enumeration.

**Limits.** The sketch must be an embedding for both trial vectors and the next residual; the bound is worst-case over admissible systems with fixed couplings, not the necessary threshold for every fixed matrix. No large-iteration convergence, sketch-probability guarantee, or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
