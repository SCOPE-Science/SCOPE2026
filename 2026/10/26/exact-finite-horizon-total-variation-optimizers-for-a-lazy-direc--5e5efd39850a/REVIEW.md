# Scientific assessment

## Correctness: PASS

The exact Fourier inversion reduces three-state total variation to a single trigonometric maximum. A phase coordinate maps the full admissible parameter interval bijectively to \([-\pi/3,\pi/3]\). In the outer region a sharp lower bound forces the two candidate phases; in the inner region the logarithmic derivative \(h(\tan x-\tan(hx))\) is strictly negative for \(h\ge2\). Boundary probabilities, the one-step exception, the spectral comparison, and the asymptotic constant are all covered. The standalone test script passed 60978 finite numerical comparisons. There is no dependence on numerical evidence to establish the theorem.

## Originality: PASS with residual priority risk

Compared the finite-horizon exact total-variation optimizer, not only the shared topic of cycle walks, with available primary results. Boyd–Diaconis–Xiao optimize symmetric-chain eigenvalues; Gerencsér–Hendrickx–Van Dooren optimize cycle spectral gaps; Gerencsér (arXiv:1905.03223) analyzes mixing on a cycle with an additional random edge; and Olesker-Taylor–Zanetti give general geometric mixing bounds. None of the inspected portions supplies the two finite-horizon optimizers or the nonvanishing limiting relative improvement. A related earlier study of mixing times on cycles was not obtained in full, leaving possible historical priority risk. A literature search cannot establish absolute novelty.

## Value: PASS

This is the complete finite-horizon minimax problem for the minimal nontrivial oriented cyclic walk, with exact optimizers for every horizon. It separates finite-time total variation from its standard spectral proxy by a persistent \(13.397\ldots\%\) limiting relative gap and identifies the precise \(h^{-1}\) bias detuning that realizes the improvement. This is a parameter-free boundary phenomenon, not a tuned isolated numerical example.

## Scope and limits

No claim is made about globally optimal arbitrary three-state kernels, mixing-time threshold optimization, or independent external validation. The previous literature comparison is subject to the identified inaccessible-source priority risk.

Self-review: passed. Independent audit: not yet performed.
