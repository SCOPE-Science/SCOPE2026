# Independent mathematical audit

## correctness

PASS

The 90 multiset permutations of 001122 give a finite compatibility graph with 2745 undirected edges for minimum Hamming distance >=4. A fresh bit-mask Bron-Kerbosch maximal-clique implementation fully enumerated 90,627 maximal cliques, with counts by sizes 6:38895, 7:20160, 8:20520, 9:10320, 11:720, 15:12. Thus maximum size is 15 and precisely twelve labeled maxima exist. Every maximum meets the Hamming distance condition; source orbit calculation gives one S6 x S3 orbit (order4320, stabilizer360), a balanced five-of-each-symbol coordinate distribution and distance-pair counts 90 at4 and 15 at6. Finite enumeration exhausts every feasible code, not just a heuristic optimizer.

## originality

PASS

Huczynska and Mullen define the minimum-distance frequency permutation array framework and general bounds/constructions, but no inspected statement determines this parameter-specific twelve-maxima orbit. Related exact-distance equidistant FPAs require all distances equal to four; each claimed maximum here contains fifteen distance-six pairs, so EFPA examples or bounds do not directly imply this census. Resultary index exact-parameter search produced other permutation metrics, not a covering classification. An unindexed constant-composition table is a genuine risk.

## value

PASS

The natural smallest ternary repeated-symbol frequency-permutation setting with an existing distance-four literature question has a complete extremal classification: exact maximum, all twelve labeled optima, unique coordinate/symbol symmetry orbit and distance spectra. This exact dataset is a structural benchmark for constant-composition-code bounds and constructions, not an arbitrary enumeration without object motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
