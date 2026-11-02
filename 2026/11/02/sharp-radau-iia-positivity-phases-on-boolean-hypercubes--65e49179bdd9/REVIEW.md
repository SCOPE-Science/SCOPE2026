# Scientific review of sharp Radau IIA positivity phases on Boolean hypercubes

## Correctness

**PASS.** The graph convention, stability rational function and endpoint notion of positivity are explicit. Walsh diagonalization proves the finite shell identity at every dimension. Exact polynomial cross-multiplication establishes all rational shell formulas for dimensions one through five. The displayed low-dimensional numerator sign arguments show universal positivity through dimension three and reduce four- and five-dimensional positivity to the two diagonal and one antipodal polynomials. Two Descartes-sign-change certificates, rational sign witnesses, and the monotonic antipodal polynomial give exactly the asserted roots and their ordering. A shortest-path/Taylor argument proves the distance-five obstruction in all higher dimensions; a binomial monotonicity argument establishes negativity at the fixed intermediate step, and the zero-mode limit establishes eventual positivity. These are analytic arguments; finite checks only test their algebra and implementation.

The independent exact-arithmetic matrix implementation in `verify.py` gave `VERIFY_OK 12593 exact assertions`, comparing rationally inverted endpoint matrices with their Walsh decompositions in dimensions one through five. All stated polynomial identities were reconstructed coefficientwise, rather than only compared at sample points. No intermediate Runge--Kutta stage-positivity assertion is made.

## Originality

**PASS on checked evidence, with documented historical risk.** The 2013 rational absolute-monotonicity study by Lóczi and Ketcheson [1] concerns method-class monotonicity radii rather than graph-specific matrices and step-set reconnection. The 2015 work of Higueras, Ketcheson and Kocsis [2] changes the integrator by perturbation, unlike the unmodified two-stage Radau IIA matrix studied here. Blanes, Iserles and Macnamara [3] develop positive methods for general graph-Laplacian systems and discuss general order barriers, but not exact Hamming-shell Radau positivity domains. The historical Radau survey [4] is a method-development source, not a hypercube positivity classification. The nearest published analogous numerical results use other stability functions or other graph families. An unindexed older paper specialized to the same graph and method might nonetheless cover a portion of the claim.

The claimed new scope is deliberately precise: exact dimension-four and dimension-five phase intervals, the sharp dimension-three universal positivity cutoff, and the coefficient \(-10/9\) of the first distance-five obstruction. Generic RK positivity failure and the known Walsh spectrum are background facts, not novelty claims.

## Mathematical value

**PASS.** A stable third-order implicit integrator can produce negative mass even for arbitrarily short timesteps on a symmetric Markov diffusion network; the appearance of this defect is controlled by the graph's dimension and shortest-path distance. This is a natural numerical-design boundary, not an arbitrary parameter slice: Boolean hypercubes are Cartesian products of the simplest symmetric two-state graph, and the fifth-distance obstruction arises from the method's first non-exponential Taylor coefficient with the wrong sign. The exact disconnected safe intervals in dimensions four and five provide usable positive-step rules and distinguish endpoint positivity from global SSP bounds. No inference about other integration schemes or all intermediate intervals above dimension five is asserted.

## Literature and limitations

[1] Lóczi–Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, https://arxiv.org/abs/1303.6651 (2013).

[2] Higueras–Ketcheson–Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, https://arxiv.org/abs/1505.04024 (2015).

[3] Blanes–Iserles–Macnamara, *Positivity-preserving methods for ordinary differential equations*, https://arxiv.org/abs/2102.08242.

[4] Hairer–Wanner, *Stiff differential equations solved by Radau methods*, https://doi.org/10.1016/S0377-0427(99)00134-X (1999).

The complete positivity domain is proved only for dimensions at most five; for greater dimensions the theorem states small-step failure, one fixed negative intermediate step, and eventual positive recovery. Independently checked novelty is not a statement that all historical results have been indexed or read. No independent mathematical validation or certification has occurred.

Self-review: passed. Independent audit: not yet performed.
