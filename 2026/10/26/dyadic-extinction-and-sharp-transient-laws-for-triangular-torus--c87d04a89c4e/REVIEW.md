# Review of triangular-torus parity dynamics

## Correctness — PASS

The factorization of the six-neighbour symbol, exact local group-algebra primary decomposition, root-set inclusion-exclusion, each nilpotency index including the repeated central root, and dyadic penultimate ideal ranks provide an all-size proof. Exact binary Gaussian elimination verified 256 size pairs, 102,912 direct labelled states and nine penultimate ranks. The tests are corroboration, not a substitute for the proof.

Proof boundaries: all integers \(m,n\ge3\), with the six diagonally oriented neighbours defined precisely; the central dyadic cases, asymmetric powers of two, and odd-part gcd root intersections are separately handled. The text proves the full infinite family; finite rank tests are supplementary. A phase preimage means \(F^T\)-preimage, not an entire orbit basin.

## Originality — PASS (bounded literature comparison)

The arXiv full text of Zaidenberg (2006) provides convolution/Fourier machinery and examples, but not the exact triangular six-neighbour symbol classification, local central nilpotence or sharp last-step rank. The inspected four-page Uguz–Siap–Akin (2013) full text works with ternary-field periodic hexagonal automata and reversible matrices; Bhavadharani–Christy (2025) uses ternary Moore neighbourhoods with null boundaries. The earlier four-neighbour square-grid parity recurrence uses a distinct symbol and does not imply this six-neighbour claim. published-finding corpus targeted searches returned no exact or stronger triangular-torus finding. The 2011 hexagonal paper remains a stated full-text access risk.

Closest primary sources: M. G. Zaidenberg, Convolution equations on lattices: periodic solutions with values in a prime characteristic field, arXiv:math-ph/0606070v1 (first posted 2006-06-29), https://arxiv.org/abs/math-ph/0606070; S. Uguz, I. Siap, H. Akin, 2-Dimensional Reversible Hexagonal Cellular Automata with Periodic Boundary, Acta Physica Polonica A 123 (2013), 480–483, doi:10.12693/APhysPolA.123.480, https://doi.org/10.12693/APhysPolA.123.480; Bhavadharani and Christy, Algebraic Structure of Moore Cellular Automata - Finite Triangular Lattice (2025), doi:10.18280/mmep.120726, https://doi.org/10.18280/mmep.120726. The earlier possibly related 2011 paper is named explicitly: I. Siap, H. Akin, S. Uguz, Structure and reversibility of 2D hexagonal cellular automata (2011), doi:10.1016/j.camwa.2011.09.066, https://doi.org/10.1016/j.camwa.2011.09.066. A full-text check of the plausibly relevant 2011 Siap–Akin–Uguz hexagonal-automata paper was unavailable (the discoverable abstract concerns reversibility); some unindexed same-operator result could exist. The 2013 follow-on was fully inspected and works over a different finite field.

## Mathematical value — PASS

A natural infinite family of six-regular triangular lattice quotients has a complete arithmetic attractor/extinction classification: an odd-part gcd controls recurrent dimension, powers of two control exact transient depth, and square versus rectangular dyadic geometry changes sharp last-step rank from 3m/2 to n-2m+2. Global extinction even on arbitrarily large such graphs and exact worst-case proportions supply structural dynamical information beyond a routine finite enumeration.

## Verification boundary

The source identities and dated public preprint establish historical scope, not independent verification. The bundled exact-rank computation is reproducible with standard Python 3. The review is internal to the submitted scientific work; no independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
