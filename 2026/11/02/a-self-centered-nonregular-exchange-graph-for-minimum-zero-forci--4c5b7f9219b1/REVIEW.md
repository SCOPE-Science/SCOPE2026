# Scientific assessment

## Correctness — PASS

The finite universe is exactly the \(\binom{16}{8}\) eight-subsets of the graph with edges defined by single-bit cube-coordinate changes. Both implementations independently establish the minimum size by exact forcing predicates, enumerate all 2360 minimum sets and all 22848 one-exchange edges, and compute graph distances by exhaustive breadth-first searches. One computes source-distance profiles for eleven automorphism orbits whose sizes sum to 2360; the other computes all 2360 source-distance profiles independently. Both reconstruct the degree distribution, every ordered-pair distance count and the Johnson-distance excess. No infinite extrapolation is asserted. Remaining risk: programming errors shared through the mathematical model; contrasting predicates and all-source verification mitigate but do not replace independent review.

## Originality — PASS, with residual risk

The earlier ordinary zero-forcing theory proves only the minimum size. General zero-forcing reconfiguration work provides the exchange operation but no implication establishing this particular 16-vertex graph's all-pairs distances. Recent hypercube work concerns forts and forcing/propagation, not the new graph metric. Importantly, a pre-existing finite census includes 2360 minimum sets, eleven symmetry orbits, and their propagation-time counts: this research does not claim those as new and relies on them only as checks. The new proposition is the exact edge/degree/metric geometry and its Johnson-distortion distribution. Searches for four-cube minimum-forcing-set swaps, token jumping, reconfiguration diameter and Johnson-distance distortion did not identify covering statements. The risk of an unindexed equivalent computation or unstated specialization remains.

## Value — PASS

The reconfiguration metric quantifies how constrained minimum zero-forcing configurations can be exchanged without losing feasibility, rather than merely how many such sets exist. Exact diameter \(8\), the unexpected common eccentricity despite nonregularity, and exactly 5808 ordered pairs suffering two extra moves beyond Johnson distance are structured, nontrivial benchmarks at the first four-cube level. Complete source/target distance counts support future comparison with higher-dimensional hypercubes and other constrained token-jumping spaces, without claiming such an extension here.

## Closest literature and scientific limits

AIM Minimum Rank–Special Graphs Work Group (2008) introduces the forcing setting; Peters (2012) gives the hypercube minimum size; Geneson–Haas–Hogben (2020) develops zero-forcing reconfiguration; Brimkov–Cameron–Grubbs (2025) analyzes hypercube forts and propagation. The degree and distance statements are specific to the stated operation and the four-cube. No uniqueness or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
