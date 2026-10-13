# Self-review

## Correctness
PASS. The claim is restricted to cardinality-optimal binary length-eight \((2,1)\)-separating systems with the secondary condition of maximum possible minimum Hamming distance. The distance-sum argument gives the upper bound \(d_H\le4\) for every ten-word binary code, the displayed representatives attain \(4\), and the exact verifier enumerates every distance-four equality case containing zero. Translation incidence yields the global labeled count, while exact stabilizer enumeration and orbit-stabilizer give three disjoint orbits whose sizes exhaust the census.

## Originality
PASS. The closest exact published record proves the known value \(m_2(8,2)=10\), but its statement and verifier do not count maximum codes, optimize their minimum Hamming distance, or classify distance-four equality cases. The 2023 hypercube paper gives only a lower bound of \(10\) at dimension eight, and the 2010 separating-system source is asymptotic. Exact-parameter, alias, table, and implication searches found no source that entails the new census or three-orbit decomposition. Residual risk remains for an unindexed historical computation.

## Value
PASS. The finding identifies the strongest Hamming separation compatible with the known cardinality optimum and gives the complete equality structure under the natural cube isometry group. This is a motivated structural invariant of optimal separating/frameproof codes, not a routine renaming or arbitrary parameter slice.

## Closest literature and limitations
The closest result is `2026/9/21/SCOPE-exact-length-eight-binary-21-separating-systems--bbbd20b813f0`, which supplies the cardinality-ten theorem. Korže--Vesel, DOI:10.1007/s00009-023-02416-z, supplies the primary hypercube formulation and earlier finite table. Randriambololona, arXiv:1010.5764v1, supplies the archive-era separating-system formulation. The new equality census is computer-assisted but finite, exhaustive, and replayable.

Self-review: passed. Independent audit: not yet performed.
