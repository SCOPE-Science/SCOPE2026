# Scientific review: optimum domination configurations of the five-cube

## Correctness

**PASS.** Bipartition coverage forces at least four selected vertices in each parity class. The explicit cosets of ten two-dimensional even subspaces give exactly forty feasible four-sets on each side; the weight-three-neighbor argument proves completeness. This implies 1600 optimum total dominating configurations, and the affine-plane intersection property proves that no two configurations differ by a single swap. A 48-element stabilizer partitions the remaining forty odd-parity cosets into complete orbits of sizes 1, 3, 12, 12, 12, and matching existence is invariant within each orbit. Its five representatives establish 1120 paired and 480 nonpaired configurations. Independent direct bitmask enumeration of all 10,518,300 eight-vertex subsets, full symmetry action, and perfect-matching checks are implemented in `verify.py` and completed successfully.

## Originality

**PASS, subject to the stated residual risk.** Haynes--Slater (1998) introduced the parameter, and Brešar--Henning--Rall (2007) obtained general Cartesian-product bounds. The inspected full hypercube subsection of Gorzkowska--Henning--Pilśniak--Tumidajewicz (2023) tabulates the already-known \(\gamma_{\mathrm{pr}}(Q_5)=8\), and studies vertex-deletion stability. The numerical optimum is explicitly not new. Neither its hypercube analysis nor the accessible material of the other sources gives the complete parity-block census, five orbit types, paired-versus-total split, or isolated exchange classification. Searches under paired/total domination, five-cube, eight selected vertices, exact counts and token exchanges found no stronger coverage. The 1998 and 2007 full texts were not available, and an unindexed equivalent theorem cannot be excluded.

## Value

**PASS.** Minimum paired domination models guards requiring adjacent backup partners. Even when the optimum size is known, the geometry of all optimal guard placements matters: here there are 1600 minimum total guard deployments, exactly 480 fail the pairing requirement, and no minimum placement permits even a single safe guard relocation without temporarily losing feasibility. Five explicit symmetry types expose distinct local matching obstructions, rather than merely recomputing the known optimum cardinality. This is a complete, motivated finite classification of a canonical Cartesian-product graph, not a selected arbitrary statistic.

## Limits

The theorem concerns exactly the 32-vertex five-cube and the strict one-removed/one-added model at optimum cardinality. The proof includes a finite group-enumeration component; no inference about all higher cubes is made. Only the 2023 primary source was materially available as full text in the most relevant hypercube sections. Publication priority beyond inspected sources is not independently guaranteed.

Self-review: passed. Independent audit: not yet performed.
