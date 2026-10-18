# Review of minimum zero-forcing-set exchange on circular ladders

## Correctness: PASS

The asserted domain is every integer \(n\ge6\), ordinary zero forcing on the vertex-distinguished graph \(C_n\square K_2\), with unrestricted one-vertex replacements. The cubic triangle-free first-force argument excludes three initially black vertices. Exhausting four-vertex row splits yields five disjoint families, each with an explicitly demonstrated complete forcing sequence. Template intersection counts establish the fixed type-to-type adjacency table, whence exactly \(13n\) vertices, \(48n\) edges, and degrees \(5,8,12\) with multiplicities \(4n,8n,n\). Explicit paths between shifted/aligned configurations give connectivity.

Two independently structured scripts have been run from their packaged paths: `verify_direct.py` exhaustively checks all three-/four-sets and exact exchange adjacency for \(5\le n\le13\); `verify_templates.py` compares symbolic pattern types for \(6\le n\le50\). Their state digests agree on common sample sizes, and both give the formula. Finite computations independently corroborate but are not substituted for the parameter-uniform proof. Main risk is an undetected mistake in the finite template overlap reduction; the complete representative table and short-cycle boundary checks mitigate it.

## Originality: PASS, with residual literature risk

Chilakamarri–Dean–Kang–Yi, arXiv:1105.1492v1 (2011), already give the zero-forcing number \(4\) for this Cartesian product. This is not treated as novel. Geneson–Haas–Hogben, arXiv:2009.00220v1 (2020), define the minimum-zero-forcing reconfiguration graph and prove several results for other graph families and forests. The closest relevant sections were inspected, and neither source implies the proposed all-size minimum-set classification, \(13n\) count, connected \(48n\)-edge exchange graph, or degree polynomial. Searches also considered equivalent base/exchange terminology and stronger coverage; recorded mathematical search results concerned different graph families or different invariants. No identical assertion was recovered among accessible historical claims. Negative retrieval is not a novelty proof; unindexed archival tables, inaccessible manuscripts and prior unpublished classifications remain specific risks.

## Mathematical value: PASS

Knowing the optimal number of initially blue vertices does not describe the choices of optimal seeds or whether one can move among them without enlarging the set. The exact five-type classification, uniform local-degree profile and constructive exchange connectivity resolve those two natural gaps throughout an infinite graph family. The exceptional five-column profile is supplied as a useful boundary, not folded into the general statement. No shortest exchange-distance, mixing-time, or alternate forcing-rule result is claimed.

Self-review: passed. Independent audit: not yet performed.
