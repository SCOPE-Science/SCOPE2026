# Scientific review: two-heavy-part balance reversal

## Correctness — PASS

The claim fixes \(r\ge3\), \(u\ge4\), \(a,b\ge1\), and \(a+b=u\). Distances, the negative-type quadratic form, the critical endpoint, and the comparison parameter \(ab\) are explicitly defined. Expanding the powered distance matrix yields an exact identity on zero-sum vertex measures. Cauchy–Schwarz is sharp for constant weights on each graph part, converting the problem into a finite generalized Rayleigh quotient. Its two-dimensional characteristic polynomial is \(rv\mu^2-((r-1)u+2v)\mu+(u+r-2)\). A test vector locates its larger root above \(2/r\); substituting \(2/r\) in the polynomial and differentiating the smaller root proves the strict/flat sign trichotomy. The endpoint is included and every larger exponent fails by a uniform-on-part zero-sum witness. An independent full-matrix eigenvalue comparison and exact-rational checks support the calculations. The finite computations are explicitly not used as proofs of unrestricted statements.

## Originality — PASS, with disclosed residual risk

Sánchez, arXiv:1108.0451 (2011), supplies the general finite-distance-matrix framework and a closed result for complete bipartite graphs. Deza and Grishukhin (2000) discuss general two-distance spectral/Euclidean embedding methods and multipartite-related constructions. These are important prior mathematical tools, not newly discovered methods. The narrowly assessed result is the **fixed-budget inversion of the strict ordering under splitting two parts, with precise equality line \(u=r\)**; it is neither the already-known bipartite formula nor a claim that two-distance matrices were previously unstudied. The primary materials inspected did not state that comparison. Search coverage included equivalent generalized-roundness, conditionally negative-distance, and Hilbert-snowflake terminology, and semantically related published records. An equivalent hidden in older two-distance literature remains possible. Full text of Deza and Maehara (1990) was inaccessible; no conclusion of noncoverage is drawn from an abstract alone.

## Value — PASS

A fixed vertex and partition budget poses a natural extremal question for the largest Hilbert-snowflake exponent. The direction of the extremum *reverses* as the number of singleton parts passes the total variable-part budget, and an entire family of distinct part profiles collides at the same exponent on the exact equality line. These are structural constraints on metric embeddings, rather than arbitrary small-graph constants or direct restatements of an available table. The proof gives an exact formula and unique balancing optimizers away from the transition. The classification is limited to two variable parts, and it makes no assertion about arbitrary multipartite graphs.

## Sources, comparison, and limitations

The most relevant primary sources are Sánchez, “On the supremal \(p\)-negative type of a finite metric space” (2011), Theorem 3.1 and its full finite-metric criterion; Deza and Grishukhin, “Hypermetric two-distance spaces” (2000), its two-distance spectral approach; and Deza–Maehara, “Metric transforms and Euclidean embeddings” (1990), an inaccessible historical comparator. Exact source identifiers and residual originality risks are recorded in `AUDIT.json`. The attached `verify.py` performs finite reproducibility tests but is not an independent infinite-proof certificate.

Self-review: passed. Independent audit: not yet performed.
