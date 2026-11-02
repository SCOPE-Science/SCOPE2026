# Review of weak-flux monitored quantum-triangle detection

## Correctness — PASS

The exact three-state Hamiltonian is compressed onto the two-dimensional no-detection subspace in the symmetric/antisymmetric basis. The resulting exact matrix yields a simple isolated dark eigenvalue for fixed non-revival sampling intervals and a first-order split double eigenvalue at each positive full revival. The corresponding expansions give squared-modulus losses \(9t^2\alpha^2/2\) and \(t^2\alpha^2\). Uniformly bounded two-dimensional spectral projections establish limiting survival exponentials and exponential tails, thereby covering every moment. The supplied independent full-Hamiltonian matrix-exponential check and Lyapunov-mean computations passed 49 checks. The mathematical argument, not finite numerical tests, proves the infinite-attempt result.

## Originality — PASS (qualified)

The closest source is Wang et al., *First Hitting Times on a Quantum Computer* (arXiv:2402.15843), particularly its dark-state sections and on-site survival-operator appendix. It already gives the three-site Hamiltonian, zero-flux dark state, phase-factor coincidence conditions, and qualitative near-resonance slow decay. The present claim adds a parameter-specific singular-limit law for the *initial antisymmetric dark state*: an explicit non-revival decay coefficient, a different full-revival coefficient, an exponential limiting attempt distribution and moment limits. These are not stated in the inspected source sections. Friedman et al. (arXiv:1611.05676) provide first-detection renewal relations, while Thiel et al. (Phys. Rev. Research 2, 043107) classify dark/bright detection probability. Neither checked statement implies these two weak-flux coefficients. No matching result was identified in targeted research-record searches. Priority beyond the inspected records and primary literature remains a residual risk; independent validation has not occurred.

## Mathematical value — PASS

The main source emphasizes finite observation windows and slowly escaping states near phase coincidences; the exact \(\alpha^{-2}\) clock, full limiting distribution, and sampling-resonance change in rate quantify a natural unresolved detection-efficiency scale. The rate discontinuity describes noncommuting small-flux and exact-revival limits and supplies directly testable finite-window detection predictions. This is not a rephrasing of the known zero-flux darkness or total eventual detection probability.

## Limitations

Fixed strictly positive sampling interval, near-zero but nonzero magnetic phase, ideal on-site projective measurements, noiseless three-state coherent dynamics, one coherent antisymmetric initial state. No statement about the crossover when sampling time approaches revival simultaneously with flux, and no independence/priority certification.

Self-review: passed. Independent audit: not yet performed.
