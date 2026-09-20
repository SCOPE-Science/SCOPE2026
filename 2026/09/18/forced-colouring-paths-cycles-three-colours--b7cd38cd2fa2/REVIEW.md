# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked from the forcing definition rather than inferred from numerical data. On a path or cycle with three available colours, any ultimately forceable uncoloured vertex must have both neighbours already coloured with two distinct colours. This forces the initially uncoloured set to be independent (and excludes path endpoints), while the converse is immediate when all omitted vertices are tight in the final proper colouring.

The counting reduction was checked in two independent forms. For paths, a proper 3-colouring is encoded by a starting colour and \(\pm1\) edge increments in \(\mathbb Z_3\); each selected tight internal vertex imposes one independent equality of adjacent increments. For cycles, the same encoding adds the closure constraint, and contracting the disjoint equality pairs reduces the count to \(\pm1\) sequences whose sum is \(0\pmod3\), giving \((2^m+2(-1)^m)/3\) by a roots-of-unity filter. Standard independent-set counts then yield the stated coefficients.

Boundary cases were checked: \(P_2\), \(P_3\), \(C_3\), even and odd cycles, and the endpoint \(p=1/3\). The formulas reproduce the known \(P_4\) and \(C_4\) examples. A standalone exhaustive verifier enumerated all partial 3-assignments for paths through order 8 and cycles through order 8 and matched every coefficient exactly.

The all-colour corollary is also sound. The \(\lambda=2\) path/even-cycle case is the established connected-bipartite formula, odd cycles admit no 2-colouring, and for \(\lambda\ge4\) the maximum degree 2 prevents any uncoloured vertex from being forced because forcing would require at least three distinct colours among its neighbours.

## Originality

The principal directly related sources were inspected. Farr's 2026 arXiv paper develops the forced colouring function, gives the connected-bipartite formula for \(\lambda=2\), and lists small examples, but no general \(\lambda=3\) formula for paths or cycles was found. The earlier Farr--Morgan arXiv preprint introducing the polynomial was searched for path/cycle family results and likewise contains no such formula; it does contain the correct \(K_{1,2}\) example.

Exact and synonymous web searches included combinations of “forced colouring”, “forced coloring function”, “forced 3-colouring polynomial”, paths, cycles, and graph polynomials. No equivalent family formula, stronger theorem implying it, or competing parameterization was identified. Zero-forcing polynomials and the forcing chromatic number are distinct notions and do not imply these formulas.

The closest residual coverage risk is the final 2025 Springer version of the Farr--Morgan chapter (DOI 10.1007/978-3-031-86319-6_18). Its arXiv version and search-visible publication material were inspected, but the final typeset chapter was not checked page-by-page. It is therefore possible, though not evidenced by the searches, that the final chapter contains an added calculation absent from the preprint. Very recent unindexed parallel work is a further residual risk. Originality is assessed only to the best of our knowledge.

The currently posted 2026 v1 lists \(6p^2(1-2p)\) for \(K_{1,2}\), whereas the older Farr--Morgan source gives \(6p^2(1-p)\). The latter is also forced by direct counting and the general endpoint identity at \(p=1/3\). This review treats the 2026 entry as a small typographical regression, not as a new contribution of the present result.

## Value

The result supplies exact formulas for two canonical infinite graph families at the first nontrivial colour count not covered by degree or bipartite simplifications. The structural lemma explains the formulas through independent sets of tight vertices, the path formula gives a short linear recurrence, and the cycle formula exhibits an additional mod-3 closure term. Combining these formulas with the known \(\lambda=2\) case and the elementary \(\lambda\ge4\) regime completely determines the forced colouring function of every path and cycle for all positive integer colour counts.

## Limitations

The independent-set characterization is special to maximum degree 2 and is not claimed for general graphs. The result does not provide a general-purpose evaluation algorithm for broader graph classes. The computational verification supports but does not replace the general proof. No independent audit is asserted.
