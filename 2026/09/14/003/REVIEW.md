# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: **PASS**. Independent enumeration finds exactly eight maximal independent sets, hence eight minimal vertex covers, all of size 5, with every vertex in five covers. Summing the cover inequalities gives \(5\deg(a)\ge 8m\), while diagonal exponent vectors attain ratio \(8/5\). Fresh composition search gives symbolic initial degrees \(2,4,5,7,8\) for \(m=1,\ldots,5\). For \(m=4\), exhaustive enumeration of the box \(\{0,\ldots,4\}^8\) gives 358134 symbolic candidates; there are 316 distinct three-edge load vectors, and every candidate dominates at least one load vector. Thus \(I^{(4)}\subset I^3\). The lower-bound sequence for resurgence follows by degree from the diagonal monomials.

Originality: **PASS**. Bocci et al. give the general linear-program description of Waldschmidt constants for squarefree monomial ideals, so the \(8/5\) value alone is a routine specialization of known machinery. However, the final claim also contains the exact first-five initial-degree data and the exhaustive containment \(I^{(4)}\subset I^3\). Nguyen–Pham–Vu compute regularities for all cubic circulant edge ideals, not these containment data, and Gu–Hà–O'Rourke–Skelton's explicit symbolic-power formulas are for unicyclic graphs, whereas the Wagner graph is not unicyclic. No exact prior containment/table row was located.

Scientific value: **PASS**. The Wagner graph is a canonical 8-vertex cubic circulant/Möbius ladder, and symbolic-versus-ordinary containment is a standard invariant question for edge ideals. The exact containment at a small nontrivial symbolic level, together with sharp initial-degree data, is a motivated benchmark rather than an arbitrary graph computation.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
