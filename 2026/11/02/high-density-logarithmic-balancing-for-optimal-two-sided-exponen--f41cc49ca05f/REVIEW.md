# Scientific assessment: high-density exponential Gabor optimization

## Correctness: PASS

The mathematical object is the standard rectangular Gabor system of the \(L^2\)-normalized window \(e^{-|t|}\), with integer density \(q\ge2\). The previously proved sharp frame-bound identities and unique optimizer are fully identified as inputs (Faulhuber–Shafkulovska, Equation (8.1), Theorem 2.7). Their theorem places the optimum in the logarithmic window needed for all subsequent expansions. The exact condition-number factorization is algebraically reconstructed, including positive denominator. A differentiated uniform expansion proves the optimizer scale \(e^{-\eta_q}\sim1/(4q^2)\), then the quantified remainder \(O((\log q)^2/q^2)\) in its location. Substitution proves all three displayed conditioning coefficients and the fourth-order denominator remainder. A high-precision checker of the exact equation supplies numerical corroboration, not the infinite proof.

## Originality: PASS with residual risk

The mathematically closest prior source is Faulhuber–Shafkulovska (arXiv:2204.02917), not merely a Gabor title match: it treats exactly the same normalized two-sided exponential, rectangular integer-density lattice, and sharp condition number. It already proves finite-\(q\) uniqueness and gives the full sharp bound formulas. These earlier results are excluded from the novel claim. Its stated optimizer localization is only \(\eta_q\in(\operatorname{arcosh}q,4\operatorname{arcosh}q)\), while its exact functions do not explicitly provide either the additive-sharp logarithmic center or the three-term high-density condition-number expansion. Deducing those requires a moving-optimum derivative analysis, not just evaluating a fixed prescribed lattice.

The 2026-08-05 totally-positive Gabor frame-set theorem gives qualitative existence for the entire window class but does not quantify this minimizing lattice. Other checked related sources concern different windows (Poisson, tent spline, Hermite), translation sampling rather than Gabor spectral conditioning, or different finite Fourier objects. The specialized 1996 Janssen source and incompletely indexed follow-up literature leave a small residual possibility of a prior unstated equivalent asymptotic.

## Value: PASS

When redundant sampling increases, choosing an optimal lattice aspect ratio is a concrete frame-design question, and knowing the correct vanishing condition-number excess quantifies how rapidly the frame becomes tight. The new additive optimizer localization is far stronger than the original order-of-magnitude interval. The full \(q^{-2}\) coefficient, including its logarithmic and constant pieces, distinguishes the optimal design from merely near-optimal choices and captures the balance of the lattice-frequency distortion and exponentially decaying tail. The result is an exact asymptotic structural characterization along the natural unbounded family of integer densities, not an arbitrary finite-parameter table or a minor numerical improvement.

## Limits and sources

The theorem uses, rather than reproves, sharp frame bounds and global uniqueness; it does not extend to general totally positive windows, nonrectangular lattices, or finite-sample approximations. Directly compared primary sources are:

- J. de Dios Pont et al., *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992 (2026-08-05), relevant framing and Theorem 1.1.
- M. Faulhuber and I. Shafkulovska, *Gabor Frame Bound Optimizations*, arXiv:2204.02917, particularly Section 2.4 and Section 8 (including exact Equation (8.1), Theorem 2.7, and condition-number analysis).
- T. Kloos and J. Stöckler, *Zak Transforms and Gabor Frames of Totally Positive Functions and Exponential B-Splines*, arXiv:1311.7359 (methodological predecessor).

Residual risks: a mathematically equivalent expansion might exist in an older unindexed appendix, supplement, or later work; these were not exhaustively ruled out. No external mathematical certification has been performed.

Self-review: passed. Independent audit: not yet performed.
