# Independent mathematical audit

## correctness

PASS

The 3 constant necklaces and 8 triple necklaces partition all 27 three-mers into eleven disjoint directed cycles; thus a minimum hitting set needs at least eleven vertices and every equality candidate is exactly one transversal of these classes. This reduces the entire finite problem to 3^8=6561 candidates. An independent Python implementation enumerated all transversals, tested residual DAGs via Kahn topological elimination, computed longest paths, independently enumerated 3 two-cycles and 18 four-cycles, verified the exact 5436/1041/84 rejection/acceptance partition, and split 84 acyclic masks 60/24; it separately reconstructed all seven symmetry orbits of size 12. The character-length translation is exact: h residual vertices correspond to an avoiding word of length h+2, next length h+3 forced. Exhaustiveness rests on necklace partition, not truncation.

## originality

PASS

Marçais, DeBlasio and Kingsford give the general de Bruijn MDS and window-guarantee framework and tables emphasizing binary and four-letter alphabets; their published full HTML Tables 1–2 do not list the requested ternary sigma=3,k=3 census, latency classes, or the exact 21-short-cycle criterion. Published Resultary searches for ternary order-three MDS did not identify the same complete values. Overlap in unindexed code/supplementary computations remains possible, but the exact three-mer classification is not mechanically implied by the previous general algorithms.

## value

PASS

For sequence-sketch design, the precise minimum footprint (eleven patterns) and optimal guaranteed coverage length (nine letters) are natural competing invariants. A full 84-element census, latency split, seven symmetry classes, and compact 21-cycle obstruction supply concrete reusable classification rather than an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
