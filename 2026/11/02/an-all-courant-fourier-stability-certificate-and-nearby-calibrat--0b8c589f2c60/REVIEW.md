# Scientific review

## Correctness — PASS

The scalar tableau exactly factors into a Crank--Nicolson multiplier times the cubic SSPRK stability polynomial. The stated upwind flux stencil has nonnegative real Fourier symbol \(16T^3/15\), so the implicit multiplier is contractive. For the prescribed calibration, its explicit effective Courant parameter never exceeds \(10/7\). The exact rational polynomial \(1-|P_3|^2=cT^2H(c,T)\) has a complete nonnegative Bernstein coefficient certificate on two rectangles; a standalone verifier constructs and checks all \(168\) coefficients. The separate rational instability witness at phase \(\pi/2\) gives genuine high-Courant instability for calibration \(69/100\). The theorem's finite-mesh conclusion follows from Parseval, not from sampling. Risks are limited to possible transcription error, addressed through independent numerical tableau comparison and exact symbolic construction.

## Originality — PASS (accessible-source comparison)

The closest source is te Winkel--Weller--Kühnlein--Kent (2026), equations (6), (16), (18) and their stability analysis: it uses a sampled numerical phase/Courant region rather than a mathematical guarantee for all continuous phases and unbounded Courant values. Classical splitting work may anticipate the factorization, which is not the novelty claim. The NEMO manual's numerical RK3/UP5 threshold near \(1.43498\) provides relevant antecedent numerical evidence, but not the method-specific all-Courant Bernstein proof or the calibration-failure rational witness. Searches of closely related published results and the accessible mathematical records did not identify a theorem covering the complete statement. This is a best-knowledge comparison, not exhaustive priority certification; a rigorous prior UP5 stability theorem could potentially shorten or imply part of the proof.

## Value — PASS

The motivating method is designed for locally very large Courant numbers, yet its published stability envelope rests on finitely sampled modes and Courant numbers up to \(100\). A global uniform-coefficient analytic guarantee closes a mathematically material reliability gap, and the \(0.69\) counter-calibration quantifies its near-boundary sensitivity. The exact positive-coefficient proof is fully reproducible and independently useful when choosing an implicitness rule. Its scope is deliberately restricted to spatially uniform blending; it is not a general variable-coefficient stability theorem.

## Related sources and limitations

The motivating arXiv:2610.08166v1 was inspected in accessible HTML across its method, spatial stencil, stability section, and conclusions. Related operator-splitting literature, the Weller--Lock--Wood IMEX abstract, and the NEMO RK3/UP5 numerical table were compared. An exhaustive search of older rigorous SSPRK3/UP5 CFL proofs was not feasible. No statement about variable blending, flux correction, positivity or general boundary conditions is reviewed as proved.

Self-review: passed. Independent audit: not yet performed.
