# Self-review

## Correctness — PASS

For every integer \(n\ge3\), the coarea identity gives \(\mathcal H^{n-1}(Q_n\cap H_t)=\sqrt n\,f_n(t)\). The opposite vertex is the farthest point of the cube from the section plane, so the exact pyramid volume is \((n/2+|t|)f_n(t)/n\). Log-concavity of the sum-of-uniforms density and the strictly concave logarithmic height give a unique optimal positive offset; its derivative at the origin is positive. Fourier inversion with the displayed characteristic-function expansion and uniform Gaussian tail control yields the two-term expansions, from which the stationary equation and gain follow. The exact three-dimensional calculation matches the established unrestricted maximum. All Gaussian moments and coefficient identities were independently checked using exact rational arithmetic; numerical quadrature confirms examples but cannot replace the proof.

## Originality — PASS (conditional on investigated public sources)

The nearest source, Nikolov (2026, arXiv:2610.14047v1), proves the unrestricted upper comparison, identifies the central maximizer, gives a strictly improving noncentral candidate, and determines the exact \(n=3\) maximum. It does not determine the optimizing diagonal offset in general dimension or its two-term expansion. Ambrus–Gárgyán (2025, arXiv:2412.12835) establish central Fourier/Laplace–Pólya asymptotics, not the offset-and-height optimization. Bartha–Fodor–González Merino (2020, arXiv:2005.08292) concern central diagonal sections. Pournin (arXiv:2203.15054v2) treats variation in normal direction at specified noncentral distances, not the maximizing offset times the apex height. Some portions of the latter secondary works were not comprehensively inspected; an older equivalent calculation could exist and is a documented priority risk. No absolute uniqueness-of-publication guarantee is asserted.

## Mathematical value — PASS

This is a natural exact optimization within the main-diagonal family singled out by the established central extremal theorem. The optimizer shifts by an order-one offset rather than remaining central and the optimal pyramid improves the central benchmark by an explicit positive \(1/(6n)\) relative leading term. The full second-order expansion supplies a reproducible benchmark for the still-unsettled unrestricted high-dimensional pyramid problem. The result does not purport to solve that unrestricted optimization.

## References and limits

N. Nikolov, *Maximal volumes of pyramids in the unit cube* (2026), arXiv:2610.14047v1, https://arxiv.org/html/2610.14047v1.

G. Ambrus and B. Gárgyán, *Estimates on the decay of the Laplace–Pólya integral* (2025), https://doi.org/10.1112/blms.70157, arXiv:2412.12835.

F. Bartha, F. Fodor, B. González Merino, *Central diagonal sections of the \(n\)-cube* (2020), arXiv:2005.08292.

L. Pournin, *Local extrema for hypercube sections*, arXiv:2203.15054v2.

Self-review: passed. Independent audit: not yet performed.
