# Scientific review

**Correctness — PASS.** The claim applies to real SPD matrices and deterministic squared-norm embeddings on each current two-vector span. The analytical argument reduces the true residual to an oblique-projection angle, proves the sharp \(\varepsilon/\sqrt{1-\varepsilon^2}\) coefficient by the two-dimensional Gram inequality, and proves the sharp SPD residual-angle bound using the positive quadratic operator polynomial. The explicit two-dimensional Gram and endpoint-eigenvector constructions achieve both bounds simultaneously. At the critical distortion the normal-equation numerator vanishes, giving an actual stalled algorithm. The accompanying checker tests exact arithmetic only; it does not replace proof.

**Originality — PASS, with residual bibliographic risk.** Nakatsukasa–Tropp's generic quasi-optimal sketch bound, Burke–Güttel–Soodhalter's sketched projection/angle results and Güttel–Liu–Nyman's restarted harmonic framework were inspected. Earlier indexed findings include a different exact spectral-sign threshold and a general tangent-oblique-projection norm, but neither states the sharp true-residual factor for SPD sGMRES(1) together with the all-restarts convergence/critical stagnation dichotomy. Elementary ingredients and a plausible specialized prior derivation remain risks; no exhaustive novelty certification is claimed.

**Mathematical value — PASS.** The exact safety range supplies a direct design criterion for one-vector sketched Krylov cycles, improves upon loose generic residual factors and shows a structural failure at the precise endpoint even with a valid norm embedding. It is a natural complete classification of one-cycle SPD residual robustness, not a claim about practical sketch success probabilities or longer restarted methods.

**Limitations.** Exact arithmetic, real SPD matrices, one-vector Krylov cycles and norm-embedding assumptions on each current residual subspace. No random-embedding probability, floating-point reliability or multi-vector factor is established.

Self-review: passed. Independent audit: not yet performed.
