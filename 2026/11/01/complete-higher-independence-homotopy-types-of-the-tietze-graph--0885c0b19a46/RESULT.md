# Complete higher-independence homotopy types of the Tietze graph

## Finding
Let \(T\) be the twelve-vertex Tietze graph, defined below. For each integer \(r\ge1\), let \(\operatorname{Ind}_{r}(T)\) be the abstract simplicial complex whose faces are the vertex subsets inducing only connected components of size at most \(r\). The complete homotopy classification is:

\[
\operatorname{Ind}_{r}(T)\simeq
\begin{cases}
\bigvee^{2}S^{2}, &r=1,\\
\bigvee^{3}S^{4}, &r=2,\\
S^{5}, &r=3,4,\\
\bigvee^{6}S^{4}\vee S^{5}, &r=5,\\
\bigvee^{89}S^{5}, &r=6,\\
\bigvee^{193}S^{6}, &r=7,\\
\bigvee^{149}S^{7}, &r=8,\\
\bigvee^{55}S^{8}, &r=9,\\
\bigvee^{11}S^{9}, &r=10,\\
S^{10}, &r=11,\\
\{\mathrm{point}\}, &r\ge 12.
\end{cases}
\]

These are integral homotopy equivalences, not merely field-homology coincidences. The mixed-dimensional stage at \(r=5\) is notable: it has six four-spheres and one five-sphere. The larger counts at \(r=6,7\) are genuine integral wedge multiplicities. Statements for \(r\ge12\) are the usual full-simplex limit and are included only to close the classification.

## Assumptions and scope
The graph is constructed by deleting a vertex from a standard Petersen graph and replacing it with a triangle, each triangle vertex inheriting one of the deleted vertex's three external neighbors. For an entirely unambiguous independent definition, label the vertices \(1,\ldots,12\) and take the following eighteen edges:

```text
(1,2) (1,6) (1,10) (2,3) (2,7) (3,4)
(3,8) (4,9) (4,11) (5,7) (5,8) (5,12)
(6,8) (6,9) (7,9) (10,11) (10,12) (11,12)
```

All vertices have degree three. A face is a nonempty subset \(\sigma\subseteq\{1,\ldots,12\}\) for which the largest induced connected component has size at most \(r\). The empty face is implicit; the combinatorial verifier enumerates nonempty faces. There are twelve nontrivial integer cutoff inputs \(1\le r\le12\); for all larger \(r\) the complex is unchanged. The theorem concerns ordinary (nonequivariant) homotopy types.

## Proof
**Complete face enumeration.** Represent a vertex subset by the integer bitmask with bit \(i-1\) for vertex \(i\). Two independently implemented induced-component searches, one breadth-first and the other iterative neighborhood closure, agree on all \(2^{12}\) masks. For each cutoff, select exactly the masks satisfying the stated component-size condition. Closure under deleting vertices is then checked through all codimension-one faces.

**Integral Morse certificate.** In increasing vertex order, greedily match a live face \(\sigma\) with \(\sigma\cup\{v\}\) when both are present, deleting the pair from the unmatched set. Every resulting matching pair is recorded explicitly in the accompanying JSON certificate. Give each Hasse incidence \(\tau\subset\sigma\) with \(|\sigma\setminus\tau|=1\) the downward orientation except for matched incidences, which are reversed. Kahn's complete directed-graph topological-sort algorithm consumes all vertices for every cutoff, proving each gradient matching acyclic. Since every match pairs a simplex with a codimension-one coface, Forman's theorem gives a CW model with exactly the recorded critical cells.

**Signed attachment degrees.** Order the vertices increasingly and use the usual oriented simplicial boundary with deletion sign \((-1)^j\) in zero-based vertex order. Eliminate each matched lower face using its incident upper face: if \(\partial u=\varepsilon\ell+z\), replace \(\ell\) in all boundaries by \(-\varepsilon z\). Memoized recursion yields exact integer Morse differential matrices between critical cells. The certificates record these complete matrices, their rational ranks and explicit square minors of determinant \(+1\). The only nonzero differentials occur at the following cutoffs:

| Cutoff | Number of critical \(4\)-cells | Critical higher cells | Integral boundary rank | Primitive minor |
|---|---:|---:|---:|---:|
| \(r=3\) | 4 | Five \(5\)-cells | 4 | \(+1\) |
| \(r=4\) | 2 | Three \(5\)-cells | 2 | \(+1\) |
| \(r=5\) | 10 | Five \(5\)-cells | 4 | \(+1\) |
| \(r=6\) | 0 | 96 \(5\)-cells and seven \(6\)-cells | 7 | \(+1\) |

All other cutoffs have exactly one critical vertex and cells in one positive degree, or only one critical vertex at \(r=12\). A nonzero maximal-rank determinant-one minor proves that each displayed differential has only unit Smith invariant factors. Since the lowest positive critical dimension is at least two, the attaching maps in these two-level CW complexes are classified by their integer degrees; primitive integer row/column operations give elementary homotopy cancellations. In particular the \(r=5\) matrix has rank four between ten \(4\)-cells and five \(5\)-cells, leaving six \(4\)-spheres and one \(5\)-sphere; the \(r=6\) matrix has rank seven between 96 \(5\)-cells and seven \(6\)-cells, leaving 89 \(5\)-spheres. The remaining sphere multiplicities are the critical-cell counts. This proves the displayed integral homotopy equivalences.

**Independent finite check.** Independently of the discrete-Morse reduction, the verifier forms the complete simplicial boundary matrices over \(\mathbb F_2\) and computes their ranks by sparse bitset Gaussian elimination. For every cutoff, the resulting reduced Betti numbers match those obtained from the integral CW model. This is a corroboration, not a substitute for the integral proof.

## Verification
Run `python3 verify_tietze_higher_independence.py tietze_higher_independence_certificate.json` from the directory containing the two supplied files. No third-party Python packages are needed. The certificate contains every matched pair, every critical face, all signed Morse differential entries and the explicit unit minors. The verifier independently reconstructs all face sets, checks two component-size algorithms, exhaustively rechecks all matched pairs and directed-Hasse acyclicity, recomputes integral differentials and full mod-two simplicial boundary ranks, and compares all reconstructed data with the saved certificate.

Across the twelve cutoffs, 33,248 nonempty faces, 16,345 matched pairs and 184,650 Hasse incidences are checked (sums include the complete-simplex endpoint). The verifier prints `SAVED_CERTIFICATE_FULL_REPLAY_PASS` and `TIETZE_COMPLETE_HIGHER_INDEPENDENCE_HOMOTOPY_VERIFIED` upon success. The accompanying output is the actual saved replay record.

## Relationship to prior work
Deshpande and Singh introduced systematic integral homotopy calculations for higher-independence complexes, treating complete multipartite graphs, fully whiskered graphs, cycles and regular rooted trees [1]. Deshpande, Shukla and Singh established a chordal-graph wedge theorem and distance-domination bounds [2]. Abdelmalek and collaborators studied chordal and tree cases [3]. These family assumptions do not yield the stated sequence for the nonchordal Tietze graph. Related published calculations for the Petersen graph's second higher-independence complex concern a different graph: the Tietze triangle replacement is not a homotopy-preserving operation established by those results. The trivial full-simplex endpoint is not claimed as a discovery.

The result is a finite, exact classification for a specifically motivated cubic graph; it does not imply a general theorem for all cubic graphs or for arbitrary vertex-to-triangle expansions. Searches described in the accompanying review found no statement implying the full Tietze sequence, but absence from searched literature is not a proof of global priority.

## Limitations
No equivariant homotopy type, naturality of the inclusion maps between different cutoffs, persistent-homology barcode, or general formula for further graph families is asserted. The first-public date attached to this calculation identifies its motivating higher-independence construction, not publication of this new computation. All proof certificates use finite exhaustive checking; the general mathematical passage to homotopy equivalence uses Forman discrete Morse theory and elementary simply connected CW homotopy theory. An equivalent calculation absent from searched indexed sources remains possible.

## References
[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, version 1 first public 2020-01-15. https://arxiv.org/abs/2001.05448

[2] P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, arXiv:2001.06775, first public 2020-01-19. https://arxiv.org/abs/2001.06775

[3] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public 2021-06-21. https://arxiv.org/abs/2106.10863
