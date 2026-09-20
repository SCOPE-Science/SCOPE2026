# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The lower bound is the Erdős--Faudree--Ordman cut inequality, and a self-contained pointwise proof is included. For the upper bound, a proper edge-colouring of H decomposes E(H) into q=chi'(H) matchings. The hypothesis min(a,b)>=q guarantees distinct partner copies for all colour classes. Matching edges paired across corresponding copies give edge-disjoint K4s; internal edges of excess copies are placed in triangles whose fixed apex depends on the colour class. The matching property and the use of distinct apex copies prevent repeated crossing edges. All residual crossing edges are K2s. The resulting count exactly equals the cut lower bound.

Boundary checks include edgeless H (where the formula reduces to the complete-bipartite edge count), k=2 in the complete-cluster specialization, and odd complete graphs where chi'(K_k)=k rather than k-1. A standalone verifier checks representative noncomplete and complete H and confirms exact edge coverage and clique counts. Computation is supplementary rather than part of the proof.

## Originality

PASS, to the best of our knowledge. The directly relevant 2026 preprint by Bo Ning was inspected at the theorem/proof level. Its Proposition 3.1 treats only the balanced family (hK_k)∨(hK_k), with even k and h>=k-1, and explicitly invokes a one-factorization of K_k. The present theorem allows arbitrary H, unequal numbers a,b of copies, and replaces the parity-specific one-factorization hypothesis by min(a,b)>=chi'(H).

The classical Erdős--Faudree--Ordman paper was checked for the cut lower bound. Rohatgi--Urschel--Wellens (2021) was also checked because its Lemma 13 gives the related one-sided formula for joining a graph to a sufficiently large independent set; that result does not state or imply the two-sided repeated-copy equality without the additional K4 packing argument. Searches for exact formulas and synonymous descriptions involving joins of cluster graphs, joins of disjoint copies, edge-clique partitions, chromatic index, and complements of multipartite components did not locate the theorem above.

No particularly likely inaccessible source was identified. The main residual originality risk is an unindexed older observation about clique partitions of graph joins or very recent parallel work using different notation.

## Value

PASS. The result extracts a general exact mechanism from a construction that is central to a recent extremal clique-partition/covering theorem. It identifies chromatic index as the parameter that forces equality in the cut lower bound for joins of repeated arbitrary graphs, and it yields a concrete three-parameter exact family for both clique partition and spread that strictly extends the published balanced even-k calculation.

## Limitations

The chromatic-index threshold is only asserted to be sufficient, not necessary. The theorem determines cp for arbitrary H but determines cc only in the complete-cluster corollary. It does not by itself improve the asymptotic n^{4/3} order of the global spread deficit. Originality is to the best of our knowledge, and no independent audit is claimed.
