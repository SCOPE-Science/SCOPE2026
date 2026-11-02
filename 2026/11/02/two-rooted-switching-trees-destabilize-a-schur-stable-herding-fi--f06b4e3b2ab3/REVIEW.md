# Scientific review

## Correctness
PASS. The two frozen rooted-tree matrices are exactly block triangular with duplicate follower spectrum. Schur reduction of the four-state characteristic polynomial yields a strict admissible interval. Rational block-determinant identities and the intermediate-value theorem prove a positive monodromy multiplier greater than one, independent of numerical sampling. Nine exact symbolic checks passed from the standalone artifact.

## Originality
PASS with residual priority risk. The 2026 PAT source derives the individual filter and conditional operator expansion but does not give the two-follower period-two determinant or the window \(75/32<\beta<25/8\). Classical switched-system work already contains examples where stable modes have unstable products; no novelty is claimed for that general observation. The 2018 Floquet multi-agent paper provides a general diagnostic method, not this evaluated PAT calculation. The inaccessible complete 2020/2021 Floquet paper remains a residual overlap risk.

## Value
PASS. The exact open parameter interval separates local/frozen-tree stability from unstable time-dependent operator dynamics for a natural two-follower specialization of a newly introduced four-stage filter. It clarifies why a remainder-decay or switching-compatibility hypothesis cannot be inferred from instantaneous rootedness and individual Schur stability alone. A parameter-specific, reproducible mathematical obstruction is more informative than a generic warning about switched matrices.

## Closest literature and limitations
Kamimoto (arXiv:2610.23992v1, 2026) specifies the PAT recurrence and rooted predecessor rules. Liberzon–Morse (1999) establish switching instability as a general possibility; Maadani–Butcher–Yucelen (2018) use Floquet stability on different multi-agent protocols. The current calculation does not prove that its alternating schedule occurs under Kamimoto's endogenous distance-based rule and does not fully classify the alternating system outside the stated window. An inaccessible plausible 2020/2021 source limits claims of historical priority.

Self-review: passed. Independent audit: not yet performed.
