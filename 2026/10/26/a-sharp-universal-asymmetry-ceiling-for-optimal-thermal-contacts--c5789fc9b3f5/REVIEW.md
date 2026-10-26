# Scientific review: optimal contacts of a Langevin dimer

## Correctness (PASS)
The autonomous relative-coordinate and velocity process is a Hurwitz-stable Ornstein–Uhlenbeck system: mechanical energy decreases strictly outside the largest invariant set at the origin. Stationary second-moment equations give the stated exact current, checked by an independent symbolic Lyapunov residual and by 340 numerical covariance solutions. At fixed total damping, current is strictly increasing in an explicit one-variable fraction \(F_r(p)\); its logarithm is strictly concave on \((0,1)\). The polynomial stationarity relation and two exact resultants identify the unique global extremal mass ratios. Sign and endpoint arguments complete the sharp bound. The included program corroborates, but does not replace, the proof.

## Originality (PASS, qualified)
The exact heat flow of coupled Langevin oscillators is established prior work. Morgado–Duarte Queirós, arXiv:1207.6044, calculate equal-mass, equal-friction transport, not allocation over unequal masses. Falasco et al., arXiv:1505.05088, analyze uniform damping and mode-energy distributions. Henkel, doi:10.1002/andp.202100089, gives a general oscillator spectral heat-flux formula that encompasses the underlying physics but does not derive the fixed-sum optimum or the sharp universal \(\sqrt7/28\) bound. Barton, doi:10.1088/0953-8984/27/21/214005, considers dynamically identical oscillators; only its abstract was accessible. Classical harmonic chains of Zürcher–Talkner (1990) concern general transport, not this extremal law in the accessible abstract. A related pinned, unit-mass two-oscillator friction-allocation result involves different constraints and does not imply the unpinned unequal-mass theorem. The full specialized literature is not exhausted; an equivalent older optimization remains possible. These are priority limitations, not correctness evidence.

## Mathematical value (PASS)
The theorem resolves a natural fixed-contact-budget thermal design question for all positive mass ratios, proves the unusual invariance with respect to spring and friction scales, and obtains a globally sharp and surprisingly small universal allocation shift with exact reciprocal equality cases. This is a nontrivial constrained transport classification, not a restatement of the known two-oscillator conduction formula.

## Limitations and outstanding risks
The conclusion is confined to classical, Gaussian white-noise, Markovian reservoirs; positive damping; one unpinned Hooke spring; and long-time mean flux. The center-of-mass position is not stationary. It does not apply automatically to frequency-dependent baths, onsite pins, quantum fluctuations, or finite-time transport. Barton (2015) and Zürcher–Talkner (1990) could not be checked in full, leaving a finite historical-priority risk. No external independent audit is represented.

Self-review: passed. Independent audit: not yet performed.
