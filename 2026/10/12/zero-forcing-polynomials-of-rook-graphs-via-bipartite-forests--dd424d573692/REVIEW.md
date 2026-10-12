# Scientific review

## Correctness — PASS

A cell of the rook graph corresponds to an edge of a bipartite incidence graph. The count of its currently white rook-neighbors is exactly the sum of the two endpoint degrees in the current white incidence graph. Consequently a valid first force exists exactly with an isolate on one side and a leaf on the other. A completely white bipartite cycle cannot lose its first edge by a force, and a leaf-accessible forest can be peeled to empty after one move creates isolates on both sides. These facts establish the full if-and-only-if criterion, including the all-blue and singleton-side boundaries. The standard two-word bipartite Prüfer code and labeled-component exponential formula then determine every polynomial coefficient. Tree counts with a forbidden leaf side yield the exact minimum-set multiplicity. Direct finite checks cover 70,502 colorings, 5,140 bipartite spanning-tree instances and 25 larger parameters. These checks are corroboration, not a proof over infinitely many parameter pairs.

## Originality — PASS, with residual risk

Boyer et al., *The zero forcing polynomial of a graph* (arXiv:1801.08910v1), introduce the polynomial and study general coefficients and selected graph families; its inspected full-text sections do not give the rook-graph characterization or enumeration. Montazeri and Soltankhah, *k-Forcing number for Cartesian product of some graphs* (2021), Theorem 2.1, prove the previously known minimum rook-graph zero-forcing number, but not a classification and count of all forcing sets. The current complete-set characterization and two-sort component enumerator are strictly more informative than either scalar minimum and are not consequences of a same-polynomial formula from those two papers. A related 2020 path-cover article and a 2024 Cartesian-product forcing-number article could not be compared in full, and an equivalent bipartite-forest enumeration under another name remains possible. These access risks limit priority confidence; they do not negate the specific comparison established with the inspected sources.

## Value — PASS

The theorem gives a complete natural graph-counting invariant on an unrestricted, two-parameter family of classical Cartesian products. It replaces a known minimum-size value with a necessary-and-sufficient structural description for **every** set and all-size exact counts, and it derives a nontrivial Stirling-number expression for the number of extremal sets. The bipartite-forest bijection and leaf restrictions explain the forcing dynamics and make the answer reusable for counting related configurations. No broad theorem for arbitrary Cartesian products is claimed.

## Closest sources and limitations

Boyer et al. (2018), arXiv:1801.08910v1; Montazeri and Soltankhah (2021), DOI:10.55016/ojs/cdm.v16i1.68557, Theorem 2.1. Related but not fully inspected: Montazeri and Soltankhah (2020), DOI:10.1007/s41980-019-00290-8; Montazeri and Soltankhah (2024), DOI:10.22049/cco.2023.28177.1471. Finite verification is not infinite proof; the parameter domain is restricted to finite rook graphs.

Self-review: passed. Independent audit: not yet performed.
