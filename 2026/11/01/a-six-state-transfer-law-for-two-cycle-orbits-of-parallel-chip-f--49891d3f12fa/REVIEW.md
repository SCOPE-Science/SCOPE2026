# Scientific review: two-cycle enumeration on open chip-firing ladders

## Correctness — PASS

The theorem concerns the actual synchronous degree-threshold chip-firing map on labelled undirected open ladders, with nonnegative integer chips, and counts only primitive two-cycle *orbits*. Summing two steps imposes a harmonic total firing-count function; connectedness forces all vertices to fire once per period. This yields the exact phase-dependent chip intervals, each of length equal to the number of opposite-phase neighbours. The converse explicitly reconstructs both states from any positive-weight phase pattern, making the weighted cut sum an exact bijection rather than a bound. The factor of two comes from the two actual states per primitive orbit.

For the rung transfer, all sixteen ordered rung-pair states reduce under bit complementation and row exchange to six symmetry classes; the quotient matrix, initial vector and terminal vector are explicitly reconstructed by the included independent Python checker. Direct exact matrix arithmetic gives the rational generating function and the order-four annihilator. The executable checks the six-dimensional characteristic identity and six scalar residual seeds to establish the recurrence for *all* lengths algebraically; the finite enumerations are separate corroboration. The claimed asymptotic follows from the strict dominance of the positive root. Boundary condition \(n=2\), count normalization and no horizontal wraparound are explicitly handled.

Reproducibility: `python3 verify.py` finishes with `LADDER_CHIPFIRE_EXACT_VERIFY_OK`. The actual recorded run checked 87,376 complete firing-phase patterns for lengths 2–8 and 341,248 bounded chip configurations for lengths 2–4, besides transfer identities. General claims are not based on finite extrapolation.

## Originality — PASS, subject to indexed-literature limitations

The phase-cut sum is not claimed as a new characterization of graph-wide period-two chip firing. The claim is the ladder-specific exact six-state evaluation, explicit rational generating function, fourth-order recurrence, all-length coefficients and sharp exponential rate. Literature examined includes Dall'Asta's one-dimensional *ring* model [1], Jiang's graph-period theorem [2], Fey–Levine–Wilson's ladder sandpile *density* calculation [3], and Jiang–Scully–Zhang's general motor and firing-pattern framework [4]. None of the inspected relevant statements asserts or logically implies the exact number of primitive two-cycles on open ladders; [3] has the same spatial graph but a distinct observable and evolution setup. These comparisons are to implications, not simply matching titles.

Accessible earlier counts for paths, complete binary trees and complete bipartite graphs concern graph families not equivalent to the open ladder under relabelling or duality; their formulas do not determine this ladder evaluation. The online mathematical-record searches located no exact ladder formula or stronger matching census, but a failed search cannot certify universal uniqueness. Broader unindexed transfer enumerations and inaccessible historical literature remain explicit originality risks.

## Mathematical value — PASS

An open ladder is the canonical width-two strip: it is the smallest genuinely cyclic family lying between path/tree structures and wider planar strips. Computing **the complete primitive two-cycle orbit population at every length** is a natural dynamical invariant, not an arbitrary finite slice. The unexpectedly small rational denominator and the Perron rate \(6+\sqrt{35}\), as well as the exact alternating finite-size term, distinguish its recurrent-state growth from path and branching-tree counts. It provides a tractable test case for systematic width growth and exact orbit enumeration beyond trees. No theorem about broader attractor periods or transient basin sizes is asserted.

## Scope and residual risks

Originality is based on the four inspected source texts and targeted mathematical-record/literature searches; neither indexing nor access can rule out every historical equivalent. The phase-cut criterion itself and general transfer-matrix counting ideas are prior technique, not asserted inventions. Computational reproduction is a consistency check and does not replace the complete mathematical proof. Independent external validation has not been performed.

## References

[1] L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267 (2006-01-12).
[2] T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (2010-03-04).
[3] A. Fey, L. Levine, D. B. Wilson, *The approach to criticality in sandpiles*, arXiv:1001.3401 (2010).
[4] T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (2012-11-29).

Self-review: passed. Independent audit: not yet performed.
