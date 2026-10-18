# Scientific review

## Correctness
PASS. The fully quantified claim concerns unweighted Cartesian products of simple cycles with both periods at least three and the dimensionless combinatorial-Laplacian Crank–Nicolson step. Positivity reduces exactly to the resolvent diagonal. A geometric Fourier-series identity proves strict monotonicity under *each* period increment, the three-by-three spectrum gives the maximal threshold, and a wrapped random-walk argument plus a uniform eigenvalue-derivative bound proves exponential convergence to the square-lattice elliptic constant. The infinite-grid constant's numerical interval is certified by a rational binomial-series tail bound. Finite rational matrix checks, Fourier bisections, and AGM evaluations independently test the stated formulas, without being mistaken for an infinite proof.

## Originality
PASS, subject to the expressly stated material literature risk. The general finite-generator return-resolvent criterion is prior work and already implies a unique crossing for each fixed torus. The infinite-lattice elliptic Green function is prior work (Guttmann 2010) and is expressly attributed; the elliptic constant alone is not claimed as new. The compared new statements are exact all-period strict ordering, the finite-grid extremum, and a quantitative exponential discrepancy bound. Higueras–Roldán 2023 works with one-dimensional Dirichlet boundaries. The published filtered-lattice result concerns a different integrator and one dimension. A Higueras–Roldán 2022 periodic-diffusion manuscript is cited in that 2023 paper but could not be inspected; its possible overlap is a nontrivial residual risk rather than a verified exclusion.

## Value
PASS. Determining the sharp positivity timestep—not merely linear stability—is relevant to nonnegative periodic heat diffusion. Strict ordering across all rectangular grid sizes, including nonmultiples, and an explicit finite-to-infinite correction answer a natural mesh-comparison question on an infinite class. The exponential bound gives practical control of the finite-size effect. The result is not claimed for anisotropic grids, variable weights, accuracy, or stagewise positivity.

## Closest sources and limitations
Guttmann, *Lattice Green functions in all dimensions*, arXiv:1004.1435v1; Higueras and Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066v1; the published *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*; and the published *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson*. Those sources provide known formulas or closely neighboring settings rather than the compared two-dimensional finite-torus size theorem. Equivalent older or unindexed work is possible. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
