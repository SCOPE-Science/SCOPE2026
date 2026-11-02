# Self-review — cubic Walsh lattice phase

## Correctness — PASS
The exact third Walsh kernel is \((S_N^3-(3N-2)S_N)/6\); finite-difference telescoping yields the stated boundary-binomial formula. The large-dimensional expansion applies the standard fourth-cumulant local binomial correction, evaluates the two continuum Gaussian terms exactly, and adds the derivative-jump Bernoulli terms at zero and both moving nonzero roots. Uniform error control makes the remainder \(O(1)\). The density of the fractional phases along each parity yields the sharp limsup and liminf. Complete rational finite checks through dimension 400 and finite log-binomial phase comparisons support, but cannot replace, the analytic proof.

## Originality — PASS (best-knowledge assessment)
Defant et al. (arXiv:2208.06467; arXiv:2302.00233) already prove the general invariant-projection formula and first-order asymptotics. A public degree-two Walsh result supplies a separate one-root order-one phase law; its inspected full statement expressly does not cover degree three. Relevant searches for third Krawtchouk absolute moments, exact projection constants, equivalent sign-sum formulations and stronger coverage did not reveal the present two-root correction. Pointwise Krawtchouk WKB is not an L1 averaged phase theorem. An uncatalogued equivalent result is still a bibliographic risk; the novelty conclusion is not externally certified.

## Value — PASS
The cubic chaos projection constant is a natural geometric invariant. Identifying the sharp order-\(\sqrt N\) parity/lattice correction and its exact extremal subsequences significantly refines the previously established \(N^{3/2}\) growth; a universal second coefficient does not exist. The result gives a general structural explanation of the oscillation, not an arbitrary finite computation.

## Limits
Real homogeneous degree three only. Neither higher degrees nor all-order asymptotics are established. Originality remains subject to independent bibliographic review.

Self-review: passed. Independent audit: not yet performed.
