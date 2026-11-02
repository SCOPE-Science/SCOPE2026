# Scientific review: arithmetic renewal limit cycles

## Correctness — PASS

The hypotheses make the renewal-age distribution exact: \(\Pr(A_t=a)=u(t-a)\Pr(L>a)\). The lattice renewal theorem with the rescaled aperiodic interarrival \(K=L/d\) and summable renewal tails proves full total-variation convergence on each phase, which bounds matrix trace norm. The Fourier multiplier is zero-free because an expectation of unit complex numbers equals one only when every one is one; the gcd-one condition then forces unit frequency. Matrix-element comparison proves the exact phase-gap equality and strict criterion. Independently implemented exact rational finite-horizon and spectral computations passed 1212 diagnostics. Neither simulation nor partial enumeration is used to justify the infinite-time claim.

## Originality — PASS with residual risk

Wald et al., arXiv:2410.11497v1 and the later v3, establish the discrete quantum resetting dynamics, the age recursion, constant-probability stationary states, and deterministic periodic nonconvergence. Section IV and appendices do not state the span-gcd classification for **all proper finite-mean random clocks**, the explicit trace-norm residue limits, or the zero-free Fourier criterion for noncollapse. Sevilla and Valdés-Hernández, arXiv:2209.05643v1, provide the continuous-time arbitrary-renewal model and conditional steady-state analysis; their conclusions do not cover integer-arithmetic limit cycles. The new assertion is neither a renamed deterministic example nor a claim that renewal theory is new. Residual risk: an unindexed general operator-valued arithmetic renewal theorem might subsume this result; a broader published result has not been excluded by exhaustive external search.

## Mathematical value — PASS

The infinite family of all finite-mean lattice clocks permits a complete, sharp classification of late-time quantum state behavior without restricting to a particular hazard family, a qubit, or a second moment. It distinguishes nearly sure eventual resetting from actual equilibration, supplies the exact observable phase gap, and determines precisely when gate-state commutation suppresses coherent limit cycles. It is a natural structural answer to the non-Poisson convergence question in the motivating literature, rather than a parameter-specific numerical increment.

## Boundaries and literature

A proper finite-mean clock is essential; partial resets, infinite-mean processes, other gate channels, and pathwise state convergence remain outside the theorem. The arithmetic renewal theorem and deterministic-reset examples are established prior mathematics; independent literature and scientific review remain necessary.

Self-review: passed. Independent audit: not yet performed.
