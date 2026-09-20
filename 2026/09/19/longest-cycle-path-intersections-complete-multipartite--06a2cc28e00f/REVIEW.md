# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof reduces the problem to a single largest part \(B\) of size \(M\) and its complement \(O\) of size \(q=n-M\). A cycle contains at most as many vertices of \(B\) as of \(O\), while a path contains at most one more vertex of \(B\) than of \(O\). In the non-spanning regimes these bounds are attained by explicit alternating constructions, and equality forces every vertex of \(O\) to appear. In the spanning regimes, Dirac's theorem handles \(M\le q\), while the boundary case \(M=q+1\) for paths is handled by an explicit alternating Hamiltonian path.

The resulting longest-object vertex-set families are uniform subset layers of the unique largest part. Their pairwise intersection spectra follow from the exact intersection range of two \(k\)-subsets of an \(M\)-set. The connectivity identity \(\kappa(K_{n_1,\ldots,n_r})=n-\max_i n_i=q\) is checked directly by the deletion argument in the proof.

Adversarial checks included the Hamiltonian boundary \(M=q\), the traceable-only boundary \(M=q+1\), complete graphs, stars, complete bipartite graphs, tied largest parts, and the small case \(K_2\). No hidden assumption is needed beyond \(q\ge2\) for the longest-cycle statement.

A definition-level verifier independently enumerated all connected complete multipartite graph types of order \(2\) through \(9\). It used adjacency-based subset dynamic programming rather than the closed formulas. All 87 graph types passed; there were 166 longest-path/cycle checks and 44 non-spanning common-core/count checks.

## Originality

PASS, **to the best of our knowledge**.

The September 2026 paper of Ma, Ning and Zhao states Smith's conjecture and explicitly uses the complete bipartite graph \(K_{k,n-k}\), \(n\ge3k\), as a sharpness example. Its inspected text does not give the complete-multipartite classification, and a full-text search returned no occurrence of "multipartite".

The full arXiv text of Gutiérrez--Valqui (2024), which relates Smith's and Hippchen's conjectures, was inspected; searches returned no occurrence of "multipartite" or "bipartite". The 2013 Shabbir--Zamfirescu--Zamfirescu survey was inspected as a full PDF; a full-text search returned no occurrence of "multipartite". Broader searches used formulations involving complete multipartite graphs, longest cycles, longest paths, pairwise intersections, common vertices, Smith's conjecture, Hippchen's conjecture, and longest-object transversals. No exact description of the longest-object vertex-set families or their full intersection spectra was located.

Residual risk remains because the underlying Hamiltonicity facts for complete multipartite graphs are classical and the intersection formulas are elementary once the vertex-set description is recognized. Older work may therefore contain the same observation under different language.

The most relevant incompletely inspected sources are:

- T. Hippchen, *Intersections of Longest Paths and Cycles*, Ph.D. thesis, Georgia State University (2008). Bibliographic records and the abstract were found, but the full thesis was not inspected. It is relevant because it is the source of Hippchen's conjecture and may contain special-family examples.
- H. Wu, *Intersection of cycles and paths in k-connected graphs*, Discrete Applied Mathematics 378 (2026), 226--233, DOI 10.1016/j.dam.2025.07.013. Bibliographic records, keywords, and snippets were inspected; the full article was not inspected. Its title and Smith-conjecture keyword make it a plausible source of overlapping special cases.
- P. Kains, *On Intersections of Long Cycles and Paths in k-Connected Graphs*, Ph.D. dissertation, University of Mississippi (2023). The dissertation page and abstract were inspected, but the full dissertation was not inspected. The abstract describes general intersection bounds rather than complete multipartite classifications.

No inspected statement implied the present exact formulas.

## Value

PASS.

The result turns the current complete-bipartite sharpness example for Smith's conjecture into an exact structural theorem for the whole complete multipartite class. It is stronger than verifying the pairwise lower bounds: in every non-Hamiltonian or non-traceable case, all longest objects share the same minimum vertex cut of cardinality \(\kappa(G)\). It also gives the complete pairwise intersection spectrum and exact equality regimes for both Smith's and Hippchen's conjectures.

## Limitations

- The theorem concerns undirected simple complete multipartite graphs; it does not address semicomplete multipartite digraphs or incomplete multipartite graphs.
- The cycle statement assumes \(q\ge2\), since graphs with \(q=1\) need not contain a cycle.
- The finite verifier supports but does not replace the general proof.
- Full texts of the three sources listed above were not inspected, leaving residual originality uncertainty.
- No independent validation or independent audit has been performed.
