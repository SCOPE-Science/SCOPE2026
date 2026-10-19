# Self-review

## Correctness — PASS

The claim is conditional on a finite-dimensional Hermitian Hamiltonian, a strictly positive Poisson reset rate, and the explicit power-biased historical-time kernel. The matrix-unit Volterra equation and its Kummer reduction are derived directly. The nonzero Gamma coefficient is established using the positive real part of its argument. The next-order term is checked by substitution into the equation, giving the first-order logarithmic-time ratio uniformly across finitely many frequencies. The proposed limit has an explicit Poisson convex mixture of unitary channels, so its complete positivity does not rest on a numerical test. The qubit diamond coefficient follows from matching upper and lower norm bounds; the coherence threshold follows from an exact nonzero Hilbert-Schmidt asymptotic. The locally executed finite verification returned `VERIFY_OK 215`.

## Originality — PASS, with priority limitation

The general scalar Kummer equation for power-biased **classical diffusion** is already in Boyer, Evans and Majumdar, arXiv:2411.00641, Section 5.1, equations (44)–(50). Substituting an imaginary quantum Bohr frequency gives the scalar formula; **that transfer alone is not counted as original**. The uniform-memory quantum result is already in de Mauro, Kulkarni and Majumdar, arXiv:2608.02297, including its nonzero-frequency algebraic exponent and logarithmic oscillations. What remains assessed is the structural characterization of the **nonuniform quantum** normalized propagator: its uniform diamond-norm convergence to a fully CPTP compound-Poisson semigroup, the strictly positive and explicitly sharp qubit first-order diamond constant, and the state-dependent integrated-coherence boundary. The examined prior sources do not state this package of quantum-channel consequences. A prior implicit consequence of established scalar formulas plus known quantum-channel facts remains possible, and priority is not independently certified.

Additional comparison: Siudzińska and Chruściński, arXiv:1706.10041, analyze generalized Pauli channels with time-translation-invariant convolution kernels. Their master equation is not the historical-state two-time sampling equation considered here. Other quantum resetting work, arXiv:2601.13367, employs a fixed reset state and waiting-time renewal. Searches for aliases, Poisson subordination, normalized logarithmic-time propagators and memory-kernel decoherence did not identify an equivalent statement.

## Value — PASS

The measurable distinction is between persistent finite-time memory and an emergent CP-divisible **logarithmic-time limit**; the statement gives a diamond-norm error relevant to reference-entangled inputs and an exact positive sharp coefficient for a qubit, not just a formal limiting scalar exponent. The associated bias threshold identifies when the time-integrated Hilbert-Schmidt residual coherence is finite, a natural accumulated nonstationarity criterion. The semigroup can be simulated by a compound-Poisson waiting-time clock. These results make the model's long-time quantum-channel structure and its precision quantitatively explicit.

## Limitations and closest literature

Only finite dimensions and the stated kernel are proved. Finite-time normalized propagators need not be quantum channels. The qubit sharp coefficient does not imply a dimension-independent sharp coefficient. The coherence threshold is for Hilbert-Schmidt residual energy coherence. The scalar kernel solution and the uniform-memory limit are established prior mathematics, rather than separate new claims. Particularly important is the possibility of an overlooked earlier implicit CP-semigroup derivation from the classical Kummer solution.

Self-review: passed. Independent audit: not yet performed.
