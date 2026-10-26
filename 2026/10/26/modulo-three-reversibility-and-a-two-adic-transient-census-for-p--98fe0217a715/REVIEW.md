# Assessment of the circular-prism parity census

## Correctness — PASS

The claim is an all-parameter theorem on the two-row finite cyclic binary state space, with exact boundary \(n\ge3\). The invertible row-coordinate change gives the triangular polynomial matrix \(J\); the only singular divisor is \(z^2+z+1\), whose multiplicity in \(z^n+1\) is exactly \(2^{\nu_2(n)}\) when three divides \(n\). Its nilpotent Jordan part gives the sharp entry time, exact cumulative counts, and equal-size basins. A direct Smith-factor computation independently gives fixed-point counts for every iterate; Möbius inversion then yields primitive-cycle counts. The separate matrix and polynomial implementations agree on 726 rank checks, and explicit state enumeration verifies 87,360 trajectories. These finite checks are corroboration and are not used to extrapolate to arbitrary \(n\).

## Originality — PASS, bounded

The accessible historical linear-cellular-automaton sources explain polynomial superposition, general orbit frameworks, and reversibility criteria on other graphs. The most relevant accessible broader work (Byszewski–Cornelissen, arXiv:2211.02866) describes multiband linear automata and algebraic periodic-point machinery, but does not supply the present graph-dependent modulus-three criterion, two-adic nilpotent depth, complete entry-time distribution, uniform basin size or exact finite-circumference gcd census. Chang–Su (arXiv:1603.01679) studies Cayley-tree boundary conditions and cannot directly furnish prism classifications. published-finding corpus comparisons with parity automata on multipartite graphs and Hamming cubes concern different adjacency operators. No statement-equivalent result was identified in the accessed material. The Ganguly–Sikdar–Chaudhuri 2008 paper is a residual risk: the full text was not accessible, so its possible implicit special cases cannot be excluded. Unindexed equivalences remain possible.

## Mathematical value — PASS

The circular prism is a natural infinite family of connected cubic graphs. The same degree-three XOR rule is invertible at all circumferences not divisible by three but produces increasingly long transient chains when divisible by larger powers of two. The exact fraction \(15/16\) attaining the maximum transient at every multiple of six is independent of circumference. Explicit recurrence, basin and all-period formulas strengthen a mere determinant test into a complete finite-family orbit census. This is an exact graph-dependent dynamical classification rather than a recomputation of a finite list or a generic linear-algebra statement.

## Closest literature and limits

Moore (1997, arXiv:adap-org/9701001), Ganguly–Sikdar–Chaudhuri (2008, DOI 10.3233/FUN-2008-87202), Chang–Su (arXiv:1603.01679), and Byszewski–Cornelissen (arXiv:2211.02866) are the main comparisons. Accessible full texts were read for the three arXiv works; only an abstract was accessible for the 2008 article. The claim is confined to \(C_n\square K_2\) with the specified XOR rule and does not assert a simplified classification of the set of possible primitive periods.

Self-review: passed. Independent audit: not yet performed.
