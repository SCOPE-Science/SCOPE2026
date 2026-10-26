# Scientific review

## Correctness — PASS
The update is the adjacency XOR operator of a specified finite simple cubic torus. Passing to \(\mathbb F_4\) decomposes the two-coordinate group algebra into nine local factors because \(3k\) has odd part exactly three. Exactly two root pairs make both off-diagonal Laurent symbols vanish; a nonzero local Jacobian makes those symbols independent truncated parameters. Computing the ranks of their successive products proves four blocks of each odd Jordan size, the recurrent dimension, all cumulative transient counts and the sharp last-step proportion. The proof is uniform in \(a\), and finite checks are corroboration rather than an extrapolation.

## Originality — PASS (bounded)
The closest directly inspected prior work is the honeycomb tight-binding calculation of Hasegawa et al., arxiv:cond-mat/0604433. Its complex zero modes are antecedents, but no characteristic-two Jordan or transient census is claimed there. Bulitko (arxiv:0812.0111) supplies a general additive automaton framework without this computation. The indexed 2011 hexagonal-automaton rule-matrix work treats ternary-state null-boundary hexagonal cells, not the binary cubic vertex-honeycomb torus. Previous exact XOR classifications of four- and six-neighbour toroidal grids likewise do not imply the bipartite result. The full text of Kirby–Mallion–Pollak (1993) was not accessible, so an overlooked historical counterpart remains possible; this is a bounded originality assessment, not a guarantee of first discovery.

## Mathematical value — PASS
A natural order-three honeycomb resonance combined with power-of-two thickening produces an infinite family with an explicit **odd Jordan ladder** and an unbounded, sharp transient length. The exactly \(15/16\) last-step law is independent of graph size. These are structural attractor and basin invariants, not just a small-grid count, and clarify how two-sublattice coupling differs from square and triangular parity rules.

## Verification and limitations
The packaged standalone checker reconstructs the undirected graph and verifies every predicted rank for \(k=1,2,4,8\), covering up to 1152 vertices. It exhaustively enumerates the 262144 configurations at \(k=1\). Those computations do not prove the all-\(a\) theorem; the local-algebra argument does. No statement about general non-square honeycomb quotients, other moduli, primitive orbit periods or independently certified mathematics is asserted.

Self-review: passed. Independent audit: not yet performed.
