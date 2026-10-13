# Scientific review: distance-conditioned leaf count in Cayley trees

## Correctness — PASS
For a fixed labelled path of length \(k\), rooted-forest completions are enumerated by \(\det(nI-J)=s n^{n-s-1}\), including the empty-forest boundary separately. The leaf indicators of an off-path vertex and of either path endpoint are counted by deleting that vertex and comparing exact forest counts. Their sum proves the conditional mean for every admissible parameter; substitution gives the exact difference, including the last transition and the \(n=2,3\) cases. Strict monotonicity of \((k^2+1)(k+2)\) proves the modal location and all ties. Uniform expansion at \(k=O(n^{1/3})\) yields the asymptotic peak and nonzero gain. The standalone exact enumeration of \(280{,}392\) trees supports but does not replace these steps.

## Originality — PASS
Janson (2003, full text, DOI 10.1002/rsa.10074) develops the Wiener index and internal path length of random simply generated trees, including Cayley trees, without the distance-conditioned global leaf-count regression. Berzunza Ojeda and Janson (2021, full article, DOI 10.1017/S0963548321000304) analyze the distance profile and leaf-size-biased trees, but give asymptotic profile results rather than this finite path-conditioned mean and sharp cubic threshold. Wagner (2014, DOI 10.1017/S0963548314000443) treats additive tree parameters including leaves, without a located distance-conditioned assertion. Searches under leaf/path/degree/metric aliases found no equivalent formula. The closest previous mixed-degree/Wiener moment on uniform trees does not determine conditional means at each distance. The residual risk is an older joint degree-distance generating function or path-forest enumerator encoding the regression implicitly.

## Value — PASS
Leaf count is the basic branching/extremity statistic; fixed-pair distance is a canonical metric observable. Conditioning on every distance reveals an unexpected exact nonmonotone relationship with a cubic-root optimum, unlike the square-root order of typical pair distances. The formula, boundary cases, tie sizes, and constant-height advantage form a natural all-size dependence law, not an arbitrary finite slice or a marginal moment recalculation. Its effect on expected leaves is bounded (not a large-order perturbation), which is a material scientific limitation rather than a reason to call the scale transition uninteresting.

## Scope and residual limitations
The classification \(60C05\) is supported by the directly relevant random-tree distance-profile literature. The historical anchor is Janson's verifiable first-online publication date, 2003-03-03. No independent literature audit, external certification or inference about full conditional distributions is claimed.

Self-review: passed. Independent audit: not yet performed.
