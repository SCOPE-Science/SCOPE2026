# Scientific review

## Correctness — PASS
The signed saddle system is reconstructed from the Tikhonov normal equations, and the Type-II triangular factors give an exact block projector under the binary spectral mask. The proof reconstructs the Krylov-image dimension, minimum residual, reconstructed retained modes, and best full-range residual by per-frequency orthogonal projection. The strict condition-two SPD witness is exact. The packaged verification checks symbolic equalities, rational constants and 480 independent seeded Fourier examples; the proof, not finite testing, establishes the universal result.

## Originality — PASS
The main 2026 optical-Fourier preconditioner paper provides the binary pupil and Type-II block structure, but its mathematical and experimental sections do not state the exact projector, sharp one-step stalled residual, global retained-mode multiplier or strict range-versus-Krylov error gap. Brown and Walker (1997) and Sugihara and Hayami (2023) already cover generic singular-GMRES breakdown and range-symmetry principles, which are not claimed as new. Mathematical comparison thus concerns the specialized optical Tikhonov conclusion rather than the abstract fact that GMRES can stagnate. Older equivalent specialized analyses remain a residual bibliographic risk.

## Mathematical value — PASS
A binary aperture models a motivated, physically specified Fourier truncation; even perfect noiseless optics then changes the preconditioned problem rank. The theorem identifies a computable exact feasibility and failure boundary, with all-data squared residual and signal error, and isolates an extra Krylov restriction beyond loss of frequency information. The example uses an SPD forward matrix with condition number two, separating the mechanism from ill-conditioning artifacts.

## Sources, constraints and uncertainty
C. Drum et al., arXiv:2610.17275v1 (full relevant scientific sections read); P. N. Brown and H. F. Walker, DOI:10.1137/S0895479894262339 (original author-hosted manuscript, relevant theorem); K. Sugihara and K. Hayami, arXiv:2310.16442 (full relevant singular-GMRES theory). Scope is noiseless, fixed, unrestarted, conjugate-symmetric binary Fourier pupil and symmetric circulant operator. Neither hardware trials nor finite computational checks demonstrate general noisy practical performance. The conclusion has no independent validation.

Self-review: passed. Independent audit: not yet performed.
