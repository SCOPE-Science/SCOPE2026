# Minimum mitre count over the 14 anti-Pasch KTS(21)

## Context
A Steiner triple system of order 21 (STS(21)) is a set of 70 triples on 21 points with each pair in exactly one triple. The Pasch configuration is the (6,4) configuration; the mitre is the (7,5) configuration on points {a,b,c,d,e,f,g} with triples abe, acf, adg, bcd, efg. An STS(21) is 5-sparse iff it is anti-Pasch (zero Pasch configurations) and anti-mitre (zero mitres). Kokkala and Ostergard ("Sparse Steiner triple systems of order 21", J. Combin. Des. 29 (2021), 75-83; dataset DOI 10.5281/zenodo.3899950) classified the 83,003,869 anti-Pasch STS(21)s and found exactly 14 that are resolvable (Kirkman triple systems, KTS(21)), published as file kts-21-antipasch.txt.

## Definitions
- Parallel class: 7 pairwise-disjoint triples covering all 21 points. A resolution is 10 parallel classes partitioning the 70 blocks.
- T_min: minimum mitre count over the 14 resolvable anti-Pasch systems.
- Systems indexed 0-13 in file order of kts-21-antipasch.txt.

## Result
T_min = 21. All 14 systems are anti-Pasch (Pasch count 0). Mitre counts by file index are [45,51,39,39,27,42,45,35,21,21,42,44,46,45]. The minimum 21 is attained by systems 8 and 9 (both automorphism order 3). Hence none of the 14 resolvable anti-Pasch KTS(21)s is 5-sparse: the certified positive lower bound 21 rules out a 5-sparse KTS(21) in this set.

## Proof / evidence
Each system was decoded from its 21 rows of 10 symbols in {0..6}: column j is parallel class j, with points sharing a digit forming a triple. Verified: every column partitions the 21 points into 7 triples (140 columns), each system has 70 blocks, and all 210 pairs occur exactly once. Pasch counts were computed by two independent methods: (A) 6-set brute force with structural degree-2 test; (B) intersecting-pair completion with division by 6. Both give 0 on all 14. Mitre counts were computed by two independent methods: (A) 7-set brute force with structural test (degree sequence [2,2,2,2,2,2,3], unique root, three pairwise-disjoint legs, two transversal blocks); (B) root-based triple-of-blocks completion counting each mitre once at its unique degree-3 root. Both give the vector above. Counters were cross-validated on the Fano plane (7 Pasch, 0 mitres) and the cyclic STS(13) (13 Pasch, 0 mitres). All 42 witnesses on the two minimum systems were matched to the literal abe/acf/adg/bcd/efg triple pattern by exhaustive permutation search, and every witness block verified present in the decoded systems. Stored automorphism orders spot re-verified for systems 0, 1, 4, 8.

## Limitations
Result is relative to the published 14-system dataset, taken as the complete resolvable subset; no independent re-enumeration of the 83M anti-Pasch STS(21)s was attempted. Counts are machine-certified, not hand-proved. Automorphism orders re-verified for 4 of 14 systems only; remaining stored values are not load-bearing for T_min.

## Reproducibility
Decode columns of kts-21-antipasch.txt, then call count_pasch_A/B and count_mitre_A/B in counters.py. Decoded blocks plus resolutions are in decoded_14_systems.json; minimum witnesses in mitre_witnesses_sys8_sys9.json; raw counts in counts_raw.txt.

## References
- J. I. Kokkala, P. R. J. Ostergard, Sparse Steiner triple systems of order 21, J. Combin. Des. 29 (2021), 75-83. https://doi.org/10.1002/jcd.21757
- Dataset: https://doi.org/10.5281/zenodo.3899950 (file kts-21-antipasch.txt)
- G. Erskine, T. S. Griggs, Properties of Steiner triple systems of order 21, arXiv:2401.13356.
