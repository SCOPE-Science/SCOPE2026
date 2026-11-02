# Scientific review: three-color CCA on wheels

## Correctness — PASS

The wheel dynamics admit a direct exhaustive logical dichotomy: the existence of a rainbow triangle involving the hub forces the hub to rotate at every time, and each rim color difference locks by the second update; in the absence of such a triangle, every site becomes monochromatic within two updates. Both directions are proved for every labelled wheel with at least three rim vertices. Four explicit finite transfer matrices classify each of the six time-by-attractor classes. Their characteristic polynomials follow from exact integer matrix identities and rational rank certificates. The self-contained standard-library checker independently evaluates the identities, and directly simulates every one of 265680 configurations for rim lengths three through ten. The finite simulation is only a cross-check; the infinite-family statements follow from the symbolic dynamics and finite-matrix identities.

## Originality — PASS with stated residual risks

Gravner–Lyu–Sivakoff (arXiv:1610.07320, Theorem 3 and Section 4) already characterize synchronization on general finite graphs using cycle circulations and bound the synchronization time by graph diameter; neither assertion is presented as new. Their general theorem gives a qualitative criterion and an upper bound for the *synchronizing* part of wheel dynamics. It does not give the fixed-versus-period-three first-entry census, the universal time-two bound for *oscillatory* wheel states, the four spectral polynomials, or the exact 81-state-to-six-dimensional trace reduction. The inspected 2021 Bello thesis treats a different randomized finite-graph voting process and deterministic systems on infinite trees. Published mathematical-record queries for wheel CCA, greenberg-hastings cones, and finite graph automaton periodicity did not locate this combined enumeration. Search absence does not certify uniqueness; an unindexed account or a stronger graph-wide counting theorem may still cover parts of it.

## Mathematical value — PASS

A full labelled first-periodic-entry census across an infinite family of dense, highly cyclic excitable networks is a natural quantitative refinement of qualitative synchronization criteria. The proof separates immediate period-three waves from configurations which retain their waves only after two updates, and establishes the striking asymptotic that almost every uniformly chosen initial state first enters a primitive three-cycle at exactly the second update. The primitive-cycle orbit count and exact fixed-basin size are further intrinsic dynamical invariants, not arbitrary parameter slices.

## Sources and limitations

Primary source checked: J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (original public submission October 24, 2016), model definitions, Theorem 3 and its proof, and finite-graph sections. A relevant later comparison is J. Bello's 2021 Ohio State dissertation, whose abstract and table of contents distinguish its finite-graph stochastic voting problem from the present synchronous CCA. This contribution makes no assertion about four or more colors, other thresholds, irregular wheel variants, or independent verification. The exact transfer computation is reproducible by running the packaged checker.

Self-review: passed. Independent audit: not yet performed.
