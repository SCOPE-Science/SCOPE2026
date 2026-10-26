# Scientific assessment

## Correctness — PASS

The exact Markov generator closes the position variance and position–orientation covariance as a two-dimensional inhomogeneous ODE. Its integral representation gives a nonnegative causal response kernel and a control-uniform \(O(\varepsilon^2)\) remainder. Exact differentiation proves unimodality, including the resonant case \(k=a\); an exchange argument yields the unique bang-bang optimal window and the sharp horizon/dose transition. Independent integration and quadrature comparisons passed as described in `VERIFICATION.md`. Numerical tests do not stand in for universal proof.

## Originality — PASS, with risk

Baldovin–Manacorda (arXiv:2602.04560v1), inspected in its model, control, conclusion and appendix portions, studies the underlying harmonic particle and slow-protocol work/distribution-level control; it does not state this fixed-dose first-order variance scheduling phase diagram. Frim–DeWeese (arXiv:2304.06023) treats different controlled parameters for exact shortcuts and minimal time. Davis–Proesmans–Fodor (arXiv:2305.11078) supplies broader active-matter linear-response principles for thermodynamic dissipation, so the general mathematical principles are not claimed as new. Searches for fixed tumbling dose, impulse-response maxima, and exact bang-bang timing returned no equivalent model-specific claim. General response and optimal allocation theory may implicitly subsume the result; no priority beyond accessible comparisons is certified.

## Value — PASS

A fixed budget of elevated tumble rate is a natural experimentally constrained intervention, and final position spread is a directly observable control target. The theorem resolves *when* to spend that finite dose at first order: early intervention below a sharp horizon, delayed interior intervention in the other regime, and an exact dose-dependent transition. This is not a generic assertion that more activity reduces variance; the competing correlation and confinement time scales create a nonobvious best lag. The exact \(\varepsilon^2\) bound controls how the linear-response optimization approximates the actual stochastic model.

## Limitations

The theorem addresses endpoint variance under stationary initialization, not full-distribution shortcuts, work optimization or finite-amplitude global optimality. Implicit coverage by general constrained linear-response control theory is the main originality risk.

Self-review: passed. Independent audit: not yet performed.
