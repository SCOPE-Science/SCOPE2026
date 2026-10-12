# Scientific review

## Correctness — PASS

The graph isomorphism \(R_{m,n}=L(K_{m,n})\) converts connected domination to a connected occupied-edge support covering all vertices of at least one bipartition class. Deleting a cycle edge keeps that support connected and dominating; a tree occupying both full classes has a removable leaf. The sole surviving minimal structures are one-sided-spanning trees without degree-one vertices on their proper-support side. This implies the exact Stirling-number formula by the weighted matrix-tree identity, whose Schur-complement determinant is explicitly evaluated. Labeled exponential decomposition yields the full connected polynomial. All boundary cases \(m,n\ge2\) and both orientation choices are covered. Direct exhaustive verification on eleven boards confirms every coefficient and minimality classification but is not used as an infinite proof.

## Originality — PASS, with bounded literature risk

The closest same-object treatment is Stephan Mertens, arXiv:2401.00716 (2024), which computes the ordinary domination polynomial of rook graphs and uses the complete-bipartite incidence representation. Its theorem has no connectedness refinement, no classification of minimal connected supports, and no two-interval minimal cardinality spectrum. Kanté et al., arXiv:1407.2053 (2014), and Abu-Khzam et al., arXiv:2205.00086 (2022), address generic minimal connected-domination enumeration complexity, not these family-specific counts; Kanté et al., arXiv:1404.3501 (2014), concerns ordinary minimal edge domination of line graphs, with no connectedness requirement. Checks for equivalent formulations as *connected edge domination of complete bipartite graphs*, stronger coverage and data-table equivalence revealed no decisive covering formula. Earlier work under poorly indexed variant terminology remains a residual risk. This review does not establish absolute novelty or independent priority.

## Value — PASS

Minimal connected domination is structurally and algorithmically different from ordinary domination. The complete classification gives an explicit exact count for every inclusion-minimal set size, the exact upper inclusion-minimal parameter \(m+n-2\), and a natural sharp and potentially arbitrarily long forbidden size interval when \(n\ge2m\). The full connected-domination polynomial is an additional complete enumeration for the same natural graph family. These statements go beyond a scalar bound, a renamed standard identity, or a tiny numerical improvement; the gap and entire spectrum are intrinsically motivated by the set family.

## Scientific limitations

The special bipartite exponential and tree-enumerator identities are standard tools and not new discoveries in isolation. A conceivable earlier specialization under an unfamiliar name is not excluded. The verifier is finite corroboration; the universal proof is combinatorial. No external assessment or audit is represented.

Self-review: passed. Independent audit: not yet performed.
