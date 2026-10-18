# Scientific review: triangular Johnson graph projection constants

## Correctness

**PASS (same-model).** The claim concerns real unweighted \(J(n,2)\) for each integer \(n\ge5\). The proof classifies **every equivariant edge-to-cut map** from the two-dimensional anti-invariant potential space and shows that it is symmetric. This forces equivariant cut projections to be orthogonal; taking the transpose of the difference of two cycle projections proves the same rigidity for the cycle space. Group averaging then establishes optimality among all projections for every edge \(\ell_p\). The graph Laplacian is explicitly diagonalized using unsigned pair incidence; five exhaustive classes of potential differences give the two endpoint formulas. Exact rational computation passed 24,980 assertions over \(4\le n\le8\), including grounded-inverse cross-checks for \(4\le n\le7\). Those checks do not replace the infinite-family proof.

## Originality

**PASS (qualified scientific comparison).** The directly relevant 2023 open preprint by Dilworth–Kutzarova–Ostrovskii provides the general invariant-projection framework and studies tori and Hamming graphs, not exact \(J(n,2)\) cut/cycle projection constants. The earlier 2020 Laakso/diamond analysis concerns different graphs. Related published Johnson spherical projectors act on functions of subsets, not on the oriented graph-edge cut/cycle spaces here. The known \(J(4,2)\cong K_{2,2,2}\) case and \(J(3,2)\cong K_3\) case are excluded from the new range. Targeted record and primary-literature comparisons found no dominating result for \(n\ge5\), but indexing and alternative formulations leave residual bibliographic uncertainty.

## Value

**PASS.** Projection constants are natural quantitative invariants of the complementability of graph cut and cycle spaces in real \(\ell_1\) edge spaces. The result settles both constants for an infinite and independently natural family of Johnson/triangular graphs, proves global rather than merely invariant optimality, and yields distinct sharp limiting values \(3\) and \(4\). The calculation is a nontrivial new family beyond tori, Hamming graphs, complete multipartite boundary cases, and ordinary complete graphs, rather than a single isolated numeric example.

## Limitations and closest sources

The formulas apply to the endpoint norms only; intermediate exponent optimality is qualitative. Neither weighted nor higher-rank Johnson graph claims are made. The closest primary source is arXiv:2305.12582v1 (Sections 1.5 and 2.6–2.7), with arXiv:2007.07949 for related recursive graph work; the graph identification \(T_n=L(K_n)=J(n,2)\) is standard. An indexed published Johnson spherical projector record could be assessed only from its mathematical summary, not its complete repository contents, so an equivalent alternate development remains a bibliographic risk.

Self-review: passed. Independent audit: not yet performed.
