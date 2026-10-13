# Scientific review

## Correctness — PASS

For any \(2<x<y\) the proof handles the whole interval by reducing its absolute quadratic maximum to the endpoint minimum and a possible positive vertex maximum. Strict monotonicity of these two envelopes in the corrective step proves existence and uniqueness; their crossing gives two explicit formulas separated at \(x_c=1+(\sqrt2-1)(y-1)\). Substitution independently checks the threshold, the exact \(4+2\sqrt2\) stability boundary, the normalized bandwidth limit, and the slow-mode nonexpansion implication. The checker tests exact rational endpoint identities and numerical uniform-interval suprema, but finite tests are not used as infinite proofs.

## Originality — PASS, with residual risk

The closest primary paper, Eriksson–Johnson–Logg (2003), analyzes stabilizing small-step packets after large explicit Euler steps, typically for an individual stiff scalar mode and more generally via multistage spectral polynomials. It does not state the unique single-correction minimax law on an uncertain continuous high-frequency interval or its two-case transition. Van Leer–Tai–Powell (1989) optimize different multistage Fourier smoothing polynomials, with a complex stability spectrum and freely selected stage coefficients. A closely related published safe-Richardson note insists that both factors are individually nonexpansive, excluding the required unstable first stage. The exact fixed-root interval problem may nonetheless have an equivalent historical treatment not found in the inspected sources; no exhaustive-priority or independent certification is claimed.

## Value — PASS

This is a motivated sharp design question arising directly from the stiff-mode rescue mechanism in the primary paper, not an arbitrary small-parameter polynomial exercise. It produces the unique optimal correction over an entire uncertainty interval, an exact geometry transition, a universal large-band stability barrier, a limiting normalized bandwidth law for arbitrarily high frequencies, and an additional slow-spectrum safety guarantee. The result does not assert general high-order integration accuracy or universal speedups.

Self-review: passed. Independent audit: not yet performed.
