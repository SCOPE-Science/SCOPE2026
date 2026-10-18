# Scientific review: arctangent volume law

## Correctness — PASS
The domain is the anchored real dual Lipschitz ball of the squared path; the unit-molecule duality and graph-edge inequalities give precisely the increment constraints. The unimodular alternating-coordinate change preserves the claimed Lebesgue volume. The symmetric integral operator represents the whole polytope volume by Fubini; its resolvent solves an elementary differential boundary-value problem. Direct differentiation of its closed formula checks both boundary conditions and the ODE. An absolutely convergent cotangent difference supplies the exact lattice coefficients; the term with smallest pole modulus supplies the infinite-dimensional asymptotic. The standalone checker independently computes rational volumes for dimension up to five and compares two exact symbolic expansions. These finite computations supplement rather than replace the all-dimensional proof.

## Originality — PASS (subject to residual bibliographic risk)
The closest checked primary works concern poset Lipschitz polytopes (arXiv:1703.10586v1), finite-metric Lipschitz-free geometry (arXiv:1807.03814v1) and general Lipschitz-free ball geometry and volume products (arXiv:1911.10642v1). The first concerns asymmetric poset inequalities and descent enumerators; the others do not evaluate the full squared-path dual-ball volume sequence. A previously circulated result computes the *facet count* for the same squared path, which does not imply the continuous Lebesgue volumes. Searches using graph-power, dual-ball, integral-kernel, generating-function and arctangent-formula terminology identified no evaluated equivalent, but this cannot exclude unindexed work or an equivalent formula framed differently. The claim is restricted to the evaluated resolvent, exact volumes, and dominant asymptotic, not the generic transfer-integral representation.

## Mathematical value — PASS
A path and its square differ by one natural locality extension: the added unit-length distance-two edges. The exact volume loss under this graph operation is otherwise not determined by the known facet sequence. The theorem evaluates the *entire* volume generating function, an absolutely convergent closed form for every dimension, and the sharp exponential rate with a controlled second-pole error. It provides a reusable resolved-kernel approach to dual-ball volume problems for finite-metric Banach spaces, with a motivated and dimension-uniform invariant rather than an isolated calculation.

## Scientific limitations
The result concerns real dual balls and anchored-coordinate volumes only. It neither computes primal transportation-ball volumes nor establishes broader graph-power analogues. The asymptotic follows from the analytic proof; computations verify only finitely many dimensions. Bibliographic coverage is not exhaustive, and no independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
