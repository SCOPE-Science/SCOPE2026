# Independent mathematical audit

## correctness

PASS

For tie-retaining synchronous majority on Q_n, n<=4, the transition is an exact bitmask map. Independent exhaustive recalculation of all 65,536 Q4 states with functional-digraph indegree pruning found exactly 702 fixed states, 885 primitive two-cycle orbits, and no cycles longer than 2; entry shells by period (0:702/1770, 1:9336/8000, 2:25344/9600, 3:8864/0, 4:1920/0) sum to 65536. It directly verified F^6=F^4 on every state and max entrance time 4. Source Python explicitly enumerates all 384 spatial affine automorphisms and partitions recurrent masks into 14 fixed and 16 two-cycle classes; source C++ independently exhausts all 65536 states. The finite enumeration is exhaustive, not induction to n>=5.

## originality

PASS

Goles–Olivos general period-at-most-two theorem is prior work; Benjamini–Chan–O’Donnell–Tamuz–Tan discuss unimodular/random graph majority convergence, not this exact sixteen-vertex state-orbit census. Resultary query surfaced a different parity automaton on a distance-two hypercube, not synchronous neighbor-majority. An earlier unindexed Q4 census is possible.

## value

PASS

Complete transient and recurrent classification for Q4 under its full 384-automorphism symmetry group, including the sharp first periodic entrance and exceptional two-cycle-basin cutoff, is a natural nonroutine finite dynamical invariant and a reproducible benchmark for majority dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
