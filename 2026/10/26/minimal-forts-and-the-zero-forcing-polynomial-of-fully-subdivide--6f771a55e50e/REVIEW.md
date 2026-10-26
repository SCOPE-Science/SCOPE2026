# Scientific review: minimal forts and zero forcing polynomial of fully subdivided complete graphs

## Correctness

PASS. The fort proof uses an exhaustive disjoint partition by original vertices in a candidate fort; its two local conditions are necessary and sufficient. Mixed-origin forts necessarily contain a cycle-only fort except for the one omitted-original star case. Obstruction transversals give exact forcing sets, and the graphic-matroid forest expansion plus explicit star exception count gives the claimed generating polynomial. Cayley's tree formula gives the exact number of minimum forcing sets. Direct-process brute force, complete literal fort enumeration and coefficient comparison check orders 3–5; randomized n=6 checks supplement the infinite proof. The scalar minimum was known previously.

## Originality

PASS with residual literature-priority risk. The inspected 2014 complete-subdivision study determines the minimum forcing number, which is not claimed as new. The inspected 2018 zero forcing polynomial, 2023 forts, and 2024 graph-operation manuscripts supply context and methodology but do not state the full minimal-fort hypergraph, forest/singleton equivalence, or this explicit Tutte specialization for the fully subdivided clique. Searches for equivalent subdivision, forest and minimum-set formulations in published mathematical records found nearby work on distinct graph classes. A more general unindexed subdivision theorem could cover the result, so absence in these searches is not treated as proof of uniqueness.

## Mathematical value

PASS. The theorem identifies every inclusion-minimal obstruction in a natural classical graph family and connects a difficult-to-enumerate dynamical coloring invariant to spanning forests of a clique. The full polynomial simultaneously determines every forcing-set coefficient, all minimum-set counts, and random-seeding probabilities; this strictly improves on the previously known minimum size, providing a structural tool for further questions. It is not a relabeling of a known polynomial table or a finite numerical slice.

## Closest literature and limits

Barrett et al. (Electronic Journal of Linear Algebra 27, 2014) already obtain the minimum zero forcing number for complete subdivisions. Boyer et al. (arxiv:1801.08910), Cameron et al. (arxiv:2310.17904) and Menon–Singh (arxiv:2405.01423) provide the relevant polynomial, fort and graph-operation frameworks. The result applies to the complete single-edge subdivision, not arbitrary base graphs or generalized forcing variants. Its all-order proof is mathematical; finite computer tests are corroboration. Unindexed graph-subdivision and matroid formulations remain priority risks.

Self-review: passed. Independent audit: not yet performed.
