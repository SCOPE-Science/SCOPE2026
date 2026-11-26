# Independent mathematical audit

## correctness

PASS

The original five-graph numerical classification is confirmed but four substantially overlapping rows are excluded from the final claim. Independent replay /workspace/audit-work/3-replay.py with the frozen power_certificate.json and graph codes H MK P D T rebuilds the five edge sets, exhausts seeds from size zero through the first successful size using queued unmarked-neighbor counts, and constructs all jump adjacencies by bucketing common (k−1)-subsets before filtering slide moves by base adjacency. All minimum masks and transitions matched the certificate after decoding stored indices into masks. Unweighted shortest paths from every source, grouped into batches, agreed with the table and all three connected slide eccentricity histograms. Independent two-coloring verified the opposite-part pair condition in the two frozen cases; the half-label side profile in the supplied Python code is not a substitute for this check in the generalized Petersen labeling. The replay also recovered 16 Tutte–Coxeter placement orbits. The repaired RESULT.md narrows to GP(8,3) and characterizes all minima: the displayed rotations, reflection and u_i↦v_{3i}, v_i↦u_{3i} reduce the empty/singleton/pair check to the stated table and the empty case. Parallel forces have the same saturated set as arbitrary legal forcing, since every enabled force either remains enabled or already has its target marked. No singleton works, and the successful pairs are precisely opposite-color nonedges, so the jump graph is the line graph of a 5-regular bipartite complement on 8+8 vertices. Slides flip one color, so none survive. Any two disjoint complement edges are at distance at most three using a common neighbor of their same-side endpoints. For every complement edge ab, pick an original neighbor c of b and an original neighbor d of a not adjacent to c: such a d exists because b is outside N_G(a) and already uses one of c's three adjacencies. The cross-edges ad and cb are both absent from the complement, so cd is at distance exactly three from ab. A fresh stdlib replay of repairs/3/check_mobius.py passed, checking all 16 singletons and 120 pairs without symmetry reduction, the closure table, all exchanges and all jump eccentricities. Corrected RESULT.md and VERIFICATION.md plus the checker are in /workspace/repairs/3; frozen code was inspected, not executed, and frozen evidence was not modified.

## originality

PASS

Pass only the repaired Möbius–Kantor claim: its complete minimum power-dominating-pair characterization and exact jump and slide structure. The original five-graph table is not passed as a distinct classification: separate indexed claims cover substantially the Heawood, Pappus, Desargues and Tutte–Coxeter results. Their later path dates do not prove scientific priority or provenance. The strongest indexed comparison for GP(8,3) itself treats ordinary zero forcing, not power domination. The structurally analogous Heawood result concerns projective-plane incidence graphs and does not establish this graph's eligible seeds. No novelty is claimed for the scalar minimum or for reconfiguration definitions.

## value

PASS

The repaired graph is a standard cubic symmetric configuration, not an arbitrary slice. The classification answers exactly which optimal sensors are admissible and explains why one-token motion along graph edges is totally frozen despite a short, connected unrestricted exchange graph. A researcher comparing local and nonlocal sensor reconfiguration can reuse the bipartite-complement state model and its line-graph distance proof; the value is not the scalar minimum, a bare repeat of four tabulated cases, or a universal inference from one example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
