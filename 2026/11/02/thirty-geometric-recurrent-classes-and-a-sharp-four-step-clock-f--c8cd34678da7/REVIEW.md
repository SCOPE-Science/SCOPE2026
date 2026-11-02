# Self-review

## Correctness — PASS

The finite state space is exactly \(2^{2^n}\) masks for each \(1\le n\le4\). The transition is explicitly specified by neighbor popcounts and persistent state on ties. The C++ enumerator directly computes all states, fixed points, two-periodic pairs, entrance layers and basins; the independently implemented Python code constructs the complete functional digraph by indegree pruning and reproduces every count. For \(Q_4\) it also verifies that all 702 fixed configurations and 885 primitive temporal two-cycles split without overlap into 14 and 16 orbits under all 384 spatial automorphisms. A time-four initial witness is \(1972\to1377\to276\to1\to0\). Exhaustive finite enumeration is conclusive for the stated dimensions only; it is not an infinite-dimensional proof.

## Originality — PASS, qualified

The nearest historical theorem, Goles–Olivos (1980), proves eventual periods of at most two but does not imply exact periodic populations, first-entry shells, or the 30 spatial classes for \(Q_4\). Benjamini et al. (2014) study unimodular/random graphs and the general period-two property; Kaaser et al. (2016) address voting-time bounds; their inspected accessible texts give no four-cube census. Zehmakan (2024) counts stable configurations on cycles, not the sixteen-vertex cube. Relevant indexed searches for “majority Q4”, “4x4 toroidal majority”, the exact counts, and equivalent descriptions identified no dominating statement. Close but noncovering research concerns neighbor-XOR or three-color excitation, which are not the present Boolean threshold update. Residual risk: an unpublished or unindexed cube computation may coincide with the exact numbers and symmetry classes. Search absence is not a uniqueness proof.

## Mathematical value — PASS

The four-cube is the first 4-regular Boolean cube and is isomorphic to a \(4\times4\) nearest-neighbor toroidal grid, so both exact geometric attractor types and temporal relaxation are naturally motivated invariants. The result gives a complete 30-class quotient description, exact attractor and basin populations, and a sharp jump in maximal entrance time from one on \(Q_3\) to four on \(Q_4\), with longer transients only in fixed-point basins. This is a complete natural finite cutoff rather than an arbitrary restricted enumeration. No general claim about all cubes is required for this value.

## Literature and scientific limits

Primary references: Goles–Olivos (1980), DOI 10.1016/0012-365X(80)90121-1; Benjamini et al., arXiv:1405.2486, first public 2014-05-11; Kaaser et al. (2016), DOI 10.4230/LIPIcs.MFCS.2016.55; Zehmakan (2024), DOI 10.1007/s10458-024-09651-y. The 1980 item was compared from bibliographic/abstract evidence rather than full text. The results are limited to exact finite-state computation on \(Q_1\)–\(Q_4\). No independent human audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
