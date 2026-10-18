# Scientific review

## Correctness — PASS

**Object and quantifiers.** The graph is the categorical product \(K_2\times K_3\times K_3\) with 18 lexicographically labeled vertices and 36 edges. The complex at integer degree \(d\ge0\) has a face exactly when its **induced** graph is acyclic of maximum degree at most \(d\). Because the graph has maximum degree four, enumeration through degree four is complete. Exactly \(2^{18}=262144\) subsets are considered in each independently implemented enumerator; no sampling or timeout supports the claim.

**Integral homology.** The primary program computes all simplicial faces, constructs codimension-one matchings, checks absence of closed gradient paths by complete topological sorting, and calculates signed integral Morse boundaries. The sole nonzero Morse boundaries, in degrees \(d=2,4\), reduce entirely with 16 and 3 unit integer pivots respectively; all other matrices vanish. Hence all Smith factors are units, proving both the listed free Betti groups and the absence of torsion. The independent reversed-order implementation counts components and edges and computes exact Smith normal forms using another implementation; all five stages agree.

**Rational persistence.** For every source Morse generator in homological degree 8 or 9 in degree-2 and degree-3 stages, a genuine signed full-chain cycle is constructed and checked by its complete simplicial boundary. Its target Morse image gives ranks \((36,6)\) for \(2\to3\) and \((199,6)\) for \(3\to4\), verified by nonzero modular minors in two characteristics. Because target boundary ranks were proved integrally with unit pivots, these minor tests certify the stated ranks over \(\mathbb Q\). Other maps are zero by homological dimension. Seven interval types follow. No integer persistence splitting or full homotopy wedge is inferred.

## Originality — PASS

The July 25, 2023 public preprint of Andrés Carnero Bravo, *The Forest Filtration of a Graph*, defines the construction; its complete publicly accessible revised text gives \(K_2\times K_2\times K_n\) cases and **Question 44** asking for positive-degree forest filtration of \(K_2\times K_m\times K_n\). Here both latter parameters are three, so the established two-factor-order-two theorem cannot imply these results. The July 23, 2023 public work of Omar Antolín Camarena and Carnero Bravo determines independence complexes of categorical products, equivalent here only to forest degree zero; it does not provide the positive-degree Betti numbers or persistence maps. Additional nearby published database findings treat independence complexes, categorical-product Rips complexes, or Morse complexes of different objects, not the present induced-forest filtration. Queries in the research record explicitly check aliases and the numerical invariants. The remaining risk is an unindexed or unpublished computation.

## Mathematical value — PASS

Question 44 directly motivates studying positive-degree forest filtrations of three complete-graph factors. The 18-vertex product is the first symmetric case with both variable factors larger than two. Its degree-two complex exhibits nonzero homology in three consecutive dimensions, while six top-degree rational classes persist across two filtration transitions. The rational barcode, torsion-free groups, and exact inclusion ranks reveal behavior not available from the known degree-zero independence classification or the published \(K_2\times K_2\times K_n\) subfamily. This is a natural finite instance rather than an arbitrary labeled sample. It does not claim resolution of the entire open family.

## Primary-source inspections, scope, and risks

* Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, 25 July 2023 initial submission, revised full public arXiv HTML v3, Theorem 42, Corollary 43, and Question 44: studied and compared the objects, parameters, and stated open extension.
* Antolín Camarena and Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, 23 July 2023 initial submission, public HTML v2 §4: compared the independence-complex specialization \(d=0\), not positive-degree forest filtrations.
* Related full-text and indexed-results comparisons are documented in `AUDIT.json`. An unpublished or unindexed matching calculation remains possible; indexed absence alone never proves priority.

Limitations: exact finite claim only, and computational proofs require rerunning the provided standalone programs. All stated checks are same-model; no independent outside audit, external mathematical certification, or integral persistence-module classification is claimed.

Self-review: passed. Independent audit: not yet performed.
