# Review: bidirected \(K_{3,3}\) multipath homotopy

## Correctness — PASS

The claim concerns the actual directed linear forest complex of the 18 arcs, with directed cycles and duplicate source/target incidences excluded. The standalone certificate enumerates the complete 715-face augmented poset in two structurally distinct ways. It checks all 2,394 Hasse incidences and all 341 ordinary matching pairs, verifies topological acyclicity, and performs exact integer boundary cancellations at \(\pm1\) pivots. The resulting 0/3/4-dimensional CW complex has zero integral four-to-three differential; \(\pi_3(\bigvee^{19}S^3)\to H_3\) is an isomorphism, so the four-cell attaching maps are nullhomotopic. Original mod-two boundary ranks independently reproduce the claimed Betti numbers. Finite enumeration is exhaustive here because the object has exactly eighteen arcs.

## Originality — PASS, with stated bibliographic risk

The closest primary source is Caputi–Collari–Di Trani–Smith (arXiv:2208.04656), whose §3.2 defines one-way complete bipartite arcs and computes an Euler characteristic, not the homotopy of the fully bidirected case. The older Caputi–Collari–Di Trani path-poset article (arXiv:2110.11206) gives oriented graph examples but does not cover this specific graph. The later Deshpande–Sawant article (arXiv:2602.14936) proves equivalent **definitions** under the name directed linear forest complex and gives conflict-hypergraph methods, but the inspected results do not supply the stated mixed homotopy type. Searches of published indexed findings identified only the different bidirected double-star (tree) family and the different \(K_{3,3}\) discrete Morse/vector-field complex; their conclusions do not imply this claim. The possibility of unindexed equivalent prior work remains.

## Value — PASS

This is the first balanced complete bipartite example beyond the cycle case with three vertices in each part and both directions allowed, and it has rich overlap between directed path constraints and directed cycles. An exact mixed-dimensional **homotopy classification** is not determined by the pre-existing alternating-orientation Euler formulas. The contrast with the one-way orientation's four-circle wedge supplies natural motivation, while the self-contained integral computation provides a reproducible test example for general theories of multipath and directed-linear-forest complexes. No downstream theorem or general family is claimed.

## Limitations and sources

The finding is finite and only concerns this exact six-vertex digraph. The strongest excluded-overlap risk is an equivalent computation outside indexed collections; searches do not certify universal uniqueness. Primary material inspected: Caputi–Collari–Di Trani–Smith (arXiv:2208.04656), Caputi–Collari–Di Trani (arXiv:2110.11206), and Deshpande–Sawant (arXiv:2602.14936). All verification consists of standalone self-checks; an independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
