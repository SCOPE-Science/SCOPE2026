# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `48beac4a5a0d12141392374f2c30b8eb1c1ad1a7`, verified unchanged before review.

## Correctness

I independently checked the Riccati interval induction with exact rationals. At `lambda=3/5`, the strong-bond image of `[1/2,11/10]` is exactly `[-231/50,-119/110]`, contained in `[-5,-1]`, and the weak-bond image of `[-5,-1]` is `[133/250,53/50]`, contained in `[1/2,11/10]`. The reflected intervals at `-3/5` follow by sign symmetry. Hence every denominator stays nonzero and the stated alternating Riccati signs are uniform over the whole coefficient box. With `p_0>0`, the Sturm sign-agreement convention indeed counts eigenvalues below `lambda` (checked against direct Jacobi determinants), giving 5 below each endpoint and therefore no spectrum in `[-3/5,3/5]`.

I also independently checked the easy baseline comparisons: each Gershgorin row interval covers the central window, the stated Brauer `(1,3)` oval inequality is comfortably satisfied throughout it, and direct interval optimization of the `T^2` row Gershgorin expressions reproduces the limiting lower edge `13/100`, strictly weaker than the Sturm certificate.

## Originality

Searches across finite Jacobi matrices, dimerized/SSH chains, disorder-uniform gaps, Sturm oscillation, Riccati interval methods, Gershgorin and Brauer comparison found extensive general spectral theory but no publication stating this exact interval box, rational invariant pair, and certified 5/5 finite-chain split. The record does not claim novelty of Sturm theory or of SSH physics; its claim is the concrete uniform finite-box certificate and quantitative comparison.

## Scientific value

Although the matrix size is small, the proof is not a numerical sample: it identifies a two-interval invariant under alternating Möbius/Riccati updates, yielding a continuum-uniform spectral exclusion and exact eigenvalue counts. This gives a transparent reusable certificate pattern and a controlled example where classical oval bounds miss a gap.

## Disposition

**PASSED unchanged.**
