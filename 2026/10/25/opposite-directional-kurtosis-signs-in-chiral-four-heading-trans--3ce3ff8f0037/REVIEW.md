# Scientific self-review

## Correctness — PASS

For strictly positive Poisson clockwise and anticlockwise quarter-turn rates, the four-state generator has simple stationary eigenvalue zero and the other eigenvalues have negative real parts. A direct characteristic-polynomial computation supplies all long-time cumulant coefficients, while fourfold invariance provides the exact radial fourth-moment contraction. The inequalities are proved algebraically for all positive rates, including the nonzero diagonal gap and the exclusion of the one-directional endpoints. An independent exact Poisson-equation recursion in `CHECKER.py` agrees on 18 rational parameter-direction cases (236 overall assertions). The sign result applies to long-time cumulant rates, not all finite times.

## Originality — PASS (same mathematical model literature comparison)

The closest 2023 source, Loewe–Kozhukhov–Shendruk, contains four-heading transport and fourth-order anisotropy with balanced clockwise/counterclockwise turning, whereas the present chiral left/right rate imbalance produces the explicit positive-versus-negative directional fourth-rate regions. Its Appendix C concerns unequal horizontal/vertical turn relaxation and therefore does not itself give a clockwise/counterclockwise bias sign theorem. Sevilla's arbitrary angular-scattering formulation has rotationally uniform initial headings and does not single out a square-oriented laboratory direction. Villa-Torrealba et al. supply partial-turning transport and non-Gaussian frameworks without this discrete handed-turn threshold. Existing records on continuous-heading drift/reorientation concern a different state process. Published-index searches returned no exact formula, but absence of an indexed result is not proof of uniqueness. The main risk is that a broader four-state Markov additive-functional result may implicitly contain the coefficient or classification, requiring independent scholarly priority review.

## Scientific value — PASS

The result resolves a physically natural question raised by fourth-gradient anisotropy studies: can opposite handed turning rates change the *sign* of projected non-Gaussian correction while leaving diffusive transport isotropic? The exact criterion \(|a-b|/(a+b)>1/\sqrt3\), complete angular sectors, and simultaneously negative radial deficit separate laboratory-axis diagnostics from rotationally aggregated statistics. They provide precise observable benchmarks and avoid misclassifying positive axial fourth cumulants from a global radial measurement. This is a constrained, finite-state, long-time result, not a general claim about all active Brownian particles.

## Closest sources and residual risks

Loewe et al. arXiv:2305.03663, full sections on four-heading propagation and higher gradients and Appendix C; Sevilla arXiv:1905.07090, angular turning kernels and radial observables; Villa-Torrealba et al. arXiv:2002.02872, partial-angle reorientations. The literature comparisons are qualified by residual priority risk from equivalent spectral and perturbative results for chiral finite-state walks. An independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
