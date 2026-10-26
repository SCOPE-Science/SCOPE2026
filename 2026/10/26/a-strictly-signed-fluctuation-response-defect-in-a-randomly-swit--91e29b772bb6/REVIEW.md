# Scientific review: fluctuation–response defect in a switching harmonic trap

## Correctness — PASS

The stationary second-moment vector solves \((2K-Q)u=2Dp\). The position autocovariance and additive-drift impulse response are represented by distinct initial vectors propagated by the *same* substochastic generator \(Q-K\). Their initial fluctuation–response difference is zero, its right derivative is \(Dab(k_1-k_0)^2/[(a+b)(ak_0+bk_1+2k_0k_1)]\), and the two distinct negative spectral modes uniquely fix its entire positive-time profile. Positivity of the eigenvalues, the unique peak, the integrated sum rule, and cancellation of the nonzero stiffness when \(k_0=0\) follow algebraically. The companion program checked 960 matrix-exponential comparisons, 160 integrated identities and peak locations, and two event-driven numerical simulations. These checks do not establish independent verification and are not used as substitutes for proof.

## Originality — PASS, subject to documented residual risk

Santra–Das–Nath (arXiv:2104.00609) derive unforced intermittently trapped dynamics and variance behavior; Alston–Cocconi–Bertrand (arXiv:2202.02630) derive entropy production for Markov-switching confining potentials; and Frydel (arXiv:2407.12213) derives stationary distributions and moments for fluctuating harmonic traps. The pertinent primary material was inspected for a matching forced drift response and an explicitly evaluated, strictly signed all-lag fluctuation–response defect. The combination of the sign-definite response defect, its unique peak, and the stiffness-independent area in an on/off trap was not identified in these inspected materials or the targeted mathematical-literature comparison. The underlying Markov-modulated Ornstein–Uhlenbeck formulas are established machinery, not new. An equivalent theorem may exist in broader response or Markov-modulated diffusion literature; no definitive global priority claim is made.

## Mathematical value — PASS

The all-lag sign law provides a testable nonequilibrium discriminator that relates two distinct measurements, passive spontaneous relaxation and forced susceptibility. Its nontrivial parameter-wide positivity and the exact cancellation of trap strength in the fully intermittent integrated response distinguish this result from mere moment tabulation. It gives a measurable protocol for a natural optically-switching confinement model, including asymmetric switching and a completely unconfined switching state.

## Scope and residual risks

The theorem requires two-state continuous-time Markov switching independent of Brownian noise, scalar harmonic confinement with at least one positive stiffness, stationary preparation, and an additive drift perturbation that does not change the environment. The normalization does not cover other FDT conventions by default. The later semi-Markovian-trap literature and broad Markov-modulated linear response literature were not exhaustively inspected. Independent technical assessment and bibliographic priority checking remain necessary.

Self-review: passed. Independent audit: not yet performed.
