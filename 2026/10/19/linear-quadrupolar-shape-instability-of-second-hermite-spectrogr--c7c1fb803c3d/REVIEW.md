# Scientific review

## Correctness — PASS
The normalized Hermite STFT produces the displayed Laguerre densities. Direct integration gives a triple leading eigenvalue \(1-5e^{-2}\); the exact all-index polynomial recurrence and sign of \(Q_m(2)\) yield gap \(2e^{-2}/3\). The operator derivative exists in trace norm because the phase-space rank-one projector is smooth in a fixed annulus. The compressed derivative has spectrum \(\{0,\pm\sqrt2 e^{-2}|\widehat b(2)|\}\), so standard isolated-spectrum perturbation gives the stated cusp. `CHECK.py` executed successfully using exact symbolic arithmetic. Remainder control requires the stated uniform \(C^1\) second-order boundary expansion.

## Originality — PASS, with residual risk
Material inspection of Abreu–Gröchenig's Eq. (2.4), Abreu–Gröchenig–Romero's definition and main results on accumulated spectrograms, Abreu–Dörfler's Gaussian inverse problem, and Nicola–Tilli's Gaussian Faber–Krahn theorem identified foundational machinery but not the specific threefold degeneracy plus shape-derivative theorem. Searches for equivalent second-Hermite ellipse spectral variation, higher Landau level shape instability, and radius-two disk splitting found no precise covering claim. An accessible earlier first-Hermite area-one disk calculation concerns another window and area and does not imply the new off-diagonal compression. An equivalent higher-Landau-level shape derivative embedded in another source remains possible; search absence does not establish uniqueness.

## Value — PASS
The theorem exposes a sharp obstruction to transferring Gaussian disk-optimality to non-Gaussian Hermite windows. It provides a dimension-three exact spectral crossing, a sharp nonzero first-order gain against equal-area ellipses, and a selection rule excluding every boundary mode except the quadrupole at first order. This is a motivated structural shape-optimization boundary, not a routine single numerical sample.

## Limits
Local smooth area-preserving variations only; no characterization of global maximizing domains and no independent external mathematical audit. An unidentified prior equivalent may exist.

Self-review: passed. Independent audit: not yet performed.
