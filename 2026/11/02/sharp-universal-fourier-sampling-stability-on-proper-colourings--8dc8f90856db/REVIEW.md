# Self-review

## Correctness — PASS

The claim concerns the probability-normalized Gram matrix of the constant and all degree-one additive characters restricted to proper colourings of a finite cycle. The transfer matrix \(T=J-I\) supplies the chromatic count \(Z=(q-1)^n+(q-1)(-1)^n\) and exact two-point probabilities. Full colour-permutation symmetry diagonalizes the colour sector; cyclic spatial symmetry diagonalizes the remaining covariance. Each Fourier eigenvalue, its multiplicity, the singular ternary triangle, and the nearest-neighbour-plus-rank-one precision formula follow algebraically. The sharp global inequality requires separate checks for even length, odd lengths at least seven, odd length five, and the small ternary cases. The decisive exceptional squared condition number \(\frac32(4+\sqrt5)\) at the ternary pentagon is obtained exactly. The included standalone checker performs twelve complete enumerations, 54 exact pair-moment comparisons, 900 exact colour-pair cell comparisons, 54 direct spatial DFT checks, and a finite grid of over 3,000 parameter cases. No universal inference is based on those finite tests.

## Originality — PASS under bounded primary-literature comparison

The related 1994 Borgs–Chayes Potts-covariance study gives spin-colour covariance decompositions, especially infinite-volume covariance and correlation length; the inspected text does not determine the spatial first-Fourier-band restriction eigenvalues of every finite proper-colouring cycle or the global maximizing pair. Salas–Sokal (2000) develops antiferromagnetic Potts transfer matrices for square-lattice strips and partition-function zero sets; no inspected theorem addresses sharp interpolation stability across all cyclic lengths and colour counts. The 2005 Chang–Shrock strip paper has relevant transfer-matrix methodology but only its abstract/bibliography were accessible. A related binary cycle independent-set covariance has a nearest-neighbour-plus-rank-one inverse; it samples a different constraint family and does not yield the ternary proper-colouring pentagon extremum. Public mathematical-record searches found related spectral frames for Hamming shells but not a stronger claim implying this uniform bound. Correlation or structure-factor formulations in older physical literature remain a real residual risk, and the bibliographic search cannot prove uniqueness.

## Mathematical value — PASS

This is a natural exact harmonic reconstruction problem on graph-colouring configuration spaces, not an arbitrary parameter slice. The classification covers every alphabet size at least three and every cycle length at least three, identifies the sole singular case, determines all singular values and an exceptionally sparse inverse covariance, and solves a nontrivial uniform worst-case stability optimization. In particular the worst nonsingular system is the ternary pentagon rather than the smallest admissible cycle or an asymptotic limit; this exception requires genuine finite-size optimization beyond the standard Potts partition function.

## Limits and outstanding checks

Higher coordinate Fourier degrees, other graph families, and the binary-colouring case are not part of the theorem. Independent audit and independent validation have not been performed. A finite-cycle Potts structure-factor paper using different terminology might contain an equivalent global optimization; this review does not claim to rule out all inaccessible literature.

Self-review: passed. Independent audit: not yet performed.
