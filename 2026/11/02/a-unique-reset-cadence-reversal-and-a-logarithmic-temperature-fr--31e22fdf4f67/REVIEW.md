# Scientific review: Gaussian reset-clock crossing

## Correctness — PASS

For the precisely stated Gaussian redraw model, the endpoint symmetrized KL per cycle reduces to \(F_b(t)=\tfrac12(q_b+q_b^{-1}-2)\). The strictly single-inflection curvature and the explicit exponential-versus-deterministic convex-order kernel produce a rigorous unique-crossing proof: its kernel scale family has a strict monotone-likelihood-ratio property, derived using \(2\sinh(v/2)>v\). Independent endpoint asymptotics give the required sign on both sides. The large-reset-contrast scaling uses a uniform rational-kernel approximation and the classical exponential integral. All quantifiers require \(b>0\), with reset times strictly positive; the claim does not include the degenerate width-zero process. The standalone checker passed 197 bounded computations, including independent integration. Finite checks are corroboration, not the proof.

## Originality — PASS, with stated comparison limits

Farago (2026, arXiv:2605.28445) gives the same endpoint Gaussian KL observable and periodic/Poisson formulas **in a singular-width approximation**; the exact finite-width ordering reversal and its unique root are not stated in its inspected full text. The 2024 Olsen–Gupta–Mori–Krishnamurthy finite-time-trap study and 2025 Gupta–Olsen–Krishnamurthy erasure study address physical work rather than this specific endpoint divergence. Mori–Olsen–Krishnamurthy (2023) treats physical entropy production under random resets. Neri (2025) treats random-time protocol information costs. These observations do not eliminate the possibility that an abstract variation-diminishing theorem would imply the single-crossing structure, nor do search results establish mathematical uniqueness of the work in the literature. Specific general-source priority risk remains.

## Value — PASS

The result resolves a natural and potentially experimentally relevant question left open by a model in which both named reset clocks were already analyzed: which equally frequent clock has the larger *coarse-grained endpoint divergence* when the reset width is finite? The exact answer changes once, and the critical frequency diverges with a nontrivial power combined with a logarithmic correction as the reset width shrinks. This singular-layer classification explains why the standard width-zero calculation predicts the wrong ordering at sufficiently high but finite rates. Neither the distinction nor the threshold is a mere parameter renaming or numerical table entry.

## Limitations and evidence

The endpoint divergence is a lower-bound-style coarse-grained information benchmark, not measured physical dissipation or implementation work. Harmonic Gaussian dynamics and independent complete reset redraws are required. The most relevant cited full text was read; some adjacent works were inspected only in available abstract or selected full-text portions, so external priority remains provisional. Exact analytical steps and reproducible bounded calculations are provided separately. No independent audit or experimental validation has been performed.

Self-review: passed. Independent audit: not yet performed.
