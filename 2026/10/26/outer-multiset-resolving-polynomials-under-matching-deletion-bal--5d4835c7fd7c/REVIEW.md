# Review of matching-deletion outer multiset resolving polynomials

## Correctness — PASS

For every \(3\le p\le q\) and \(0\le t\le p\), the proof first derives all graph distances, then represents each omitted vertex's multiset of distances by two integers: number of selected vertices on its own bipartition side and whether its deleted partner remains a landmark. Because the latter is binary, no side can contain three omitted vertices. Counting the remaining omission patterns \((2,0),(0,2),(1,1),(2,1),(1,2),(2,2)\) yields the four exact coefficients and rules out all higher terms. Boundary \(q=p+1\) is explicitly accounted for. The minimum values and missing crown layer then follow from positivity. A separate BFS-based enumeration tests all \(31{,}936\) subsets in 46 parameter trials, including balanced and unbalanced boundaries. This is a check, not proof of all cases.

## Originality — PASS, with residual priority risk

The 2019 Gil-Pons et al. foundation and full 2022/2023 Klavžar–Kuziak–Yero source establish the invariant and known complete-multipartite/diameter-two results; those cover the undeleted case but not the distance-three signatures of nonzero matching deletion. The 2026 Araujo-Pardo et al. paper on circulant classes and diameter bounds was also compared at its accessible full text. A record of an exact result for arbitrary complete multipartite graphs covers the \(t=0\) boundary, not any \(t>0\) graph here. Searches of scientific records for matching-deleted bipartite graphs found different parameters (CIS, edge metric dimension), neither implying the new polynomial. The novelty assessment is best-knowledge, not a guarantee against unindexed literature or the unread full text of a 2026 survey.

## Mathematical value — PASS

The exact full cardinality enumerator for a natural infinite near-complete bipartite family resolves both a robustness perturbation question and an unexpected non-upward-closed landmark property. The balanced crown-graph case has a whole impossible cardinality layer immediately above its minimum bases, whereas the unbalanced side of the aspect-ratio boundary admits four-omission sets. These transitions and exact optimum census are structural, not a trivial relabeling of the old \(t=0\) case.

## Limits and literature

The proof needs the smaller class of size at least three; for two-vertex classes deleted-edge distances can differ. For historical baselines see Gil-Pons et al., arXiv:1902.03017; Klavžar et al., DOI 10.1007/s00025-022-01829-8; Araujo-Pardo et al., DOI 10.1007/s40590-026-00973-3; and the published scientific record on complete multipartite outer multiset dimension. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
