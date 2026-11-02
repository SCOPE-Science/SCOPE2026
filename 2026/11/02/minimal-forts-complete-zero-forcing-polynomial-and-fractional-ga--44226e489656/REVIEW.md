# Self-review

## Correctness — PASS

The exact neighborhood counts for a fort with left/right index sets are reconstructed in the proof. Cases with each shore size at most two are exhaustive, yielding exactly the two types of small minimal forts and ruling out every other type; any fort having three left or right vertices contains a listed triple. The zero-forcing polynomial then follows through the established fort-transversal equivalence. The disjoint-fort upper bound uses the proved minimum cardinality three, and the matching lower construction handles all three residue classes of the parameter. The fractional value has an explicit feasible primal assignment and an explicit dual packing with matching objectives, including the \(n=3\) boundary. Standard-library verification directly checked forts and zero forcing from graph adjacency for orders three through eight and returned `VERIFY_OK`. Computation does not certify untested orders; the infinite claims use the general proofs.

## Originality — PASS, with bounded priority risk

The foundational 2023 fort-cover/LP article and 2024 minimal-fort enumeration establish the corresponding complete-bipartite problem, where a shore pair is a fort. This does **not** survive deletion of a perfect matching and does not imply this crown-graph theorem. The 2025 computational-IP paper gives generic methods rather than this all-orders specialization. The 2025 hypercube paper overlaps at the single isomorphic case \(\operatorname{Cr}_4\cong Q_3\) but is not a family covering all parameters. Semantic research-record searches for crown-graph minimal forts, fractional parameters, equivalent direct-product formulations, and complete-bipartite matching deletion returned results on distinct invariants, or on complete multipartite graphs with different edge sets. Other indexed crown invariants and unrelated fort-family statements do not imply this claim. Search does not establish absolute priority, and obscure unpublished formulas remain a residual risk.

## Mathematical value — PASS

Deleting one perfect matching from a biclique changes the minimal-fort hypergraph from a union of shore-pair systems to a nonuniform rank-three/rank-four system. Determining **all** its minimal forts gives an exact global zero-forcing polynomial, not merely one optimum, and yields both a sharp disjoint-fort packing formula and a fractional LP value. The limiting integrality ratio of three differs from the near-two behavior for complete bipartite graphs in the foundational paper, making this a structural example relevant to fort relaxations and extremal graph zero forcing. It is a natural infinite graph family, not a parameter-selected finite table.

## Limitations and evidence

Scientific novelty is conditional on the specified inspected literature and indexed research records, not a declaration of independent priority certification. Enumeration by direct Python search was performed only through \(n=8\), and maximum disjoint-fort packing directly through \(n=7\). The independent audit channel is not performed.

Self-review: passed. Independent audit: not yet performed.
