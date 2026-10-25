# Perfect discrete-Morse matchings for five three-row grid matching complexes

## Finding

Let \(G_n=P_3\square P_n\) be the Cartesian product of simple paths having three and \(n\) vertices, and let \(\mathcal M(G_n)\) be the ordinary matching complex: its vertices are graph edges and its simplices are collections of pairwise vertex-disjoint edges. For every integer \(n\in\{3,4,5,6,7\}\), there exists an explicitly specified acyclic matching of the **ordinary** face poset with exactly one critical vertex and \(b_n\) critical \((n-1)\)-simplices and no other critical simplices, where

\[
(b_3,b_4,b_5,b_6,b_7)=(5,9,16,31,55).
\]

These are perfect discrete-Morse matchings. In particular, they establish the integral homotopy equivalences

\[
\begin{aligned}
\mathcal M(G_3)&\simeq\bigvee^{5} S^2,\\
\mathcal M(G_4)&\simeq\bigvee^{9} S^3,\\
\mathcal M(G_5)&\simeq\bigvee^{16} S^4,\\
\mathcal M(G_6)&\simeq\bigvee^{31} S^5,\\
\mathcal M(G_7)&\simeq\bigvee^{55} S^6.
\end{aligned}
\]

The asserted new structural property is the existence of these complete, perfect **acyclic face-poset matchings** and explicit reproducible witnesses. The five numerical homotopy statements were asserted in a 2021 article's table, but that article was subsequently retracted; they are not presented as previously unmentioned numerical predictions.

## Assumptions and scope

The graph is the ordinary, nonperiodic three-by-\(n\) rectangular lattice, with vertices \((i,j)\) for \(0\le i<3\), \(0\le j<n\), adjacent precisely when their Manhattan distance is one. The matching complex is not a perfect-matching complex, a categorical-product matching complex, or a three-cut complex. The statement concerns exactly five finite values \(3\le n\le7\), not arbitrary larger \(n\).

## Proof

For fixed \(n\), order the \(5n-3\) graph edges by scanning \((i,j)\) lexicographically in row-major order, adding the downward grid edge, if present, followed by the rightward grid edge, if present. Encode each face of \(\mathcal M(G_n)\) as a bitmask of graph-edge indices. Its edge set and **all** faces, including the empty face, are generated with the independent recurrence in `grid_matching_certificate.py`: starting with the empty set, add each graph edge to every previously constructed matching that does not already occupy either endpoint of that edge. This produces each allowable edge subset exactly once; conversely every matching arises by the recurrence.

Fix the five explicit pivot permutations `PIVOTS` in that file. Beginning with all faces unpaired, process each pivot edge index \(e\) in its listed order. Pair each remaining face \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever the latter is also remaining, and delete both from the remaining set. For a fixed pivot, each upper face has a unique lower face, so this is a well-defined disjoint matching of incident faces. Each step removes exactly one Hasse-cover pair.

The certificate constructs the **complete augmented Hasse diagram** of the matching complex for each of the five orders. Orient every unmatched cover downward and every matched cover upward. A full indegree topological elimination visits every face in each case; therefore this orientation is a directed acyclic graph and the matching is an acyclic discrete-Morse matching. Independently, the certificate checks that the unmatched masks number exactly \(b_n\), all have dimension \(n-1\), and checks the signed augmented Euler characteristic. The complete verified counts are:

| \(n\) | Graph edges | Faces, including empty | Hasse covers | Matched pairs | Unmatched \((n-1)\)-faces |
|---:|---:|---:|---:|---:|---:|
| \(3\) | 12 | 131 | 340 | 63 | 5 |
| \(4\) | 17 | 823 | 2911 | 407 | 9 |
| \(5\) | 22 | 5096 | 22688 | 2540 | 16 |
| \(6\) | 27 | 31687 | 170374 | 15828 | 31 |
| \(7\) | 32 | 196785 | 1239360 | 98365 | 55 |

Since the augmented empty face is paired, delete that one pair and omit the empty face to obtain an acyclic matching of the ordinary nonempty face poset. Acyclicity is inherited by the induced directed diagram on nonempty faces. Precisely one previously paired vertex becomes critical. All other critical faces remain the \(b_n\) faces of dimension \(n-1\). Forman's finite simplicial discrete-Morse theorem now produces a CW model with one zero-cell and only \(b_n\) cells in dimension \(n-1\). Because \(n-1\ge2\), each higher cell attaches to the sole zero-cell; the resulting CW space is the displayed wedge of spheres. This proves an *integral homotopy equivalence*, not just a field-homology calculation, for each stated value.

## Verification

Run `python3 grid_matching_certificate.py` with standard Python \(3\) and no external packages. The certificate computes graph edges, all matchings, all matched covering pairs, a Kahn topological-sort check on every oriented Hasse cover, the critical dimensions, and augmented Euler characteristics. `CERTIFICATE_OUTPUT.txt` records the exact observed output, ending `CERTIFICATE_OK`. The largest test enumerates 196785 faces and 1239360 Hasse covers, and verifies all of them; the script does not infer acyclicity from a sample or a probabilistic test.

## Relationship to prior work

Chauhan, Sharma, and Shukla (arXiv:2609.27366, initially submitted 2026-09-23) establish homological vanishing/connectivity for three-row grid matching complexes; their abstract does not state an infinite homotopy classification. A previous article by Goyal, Shukla, and Singh, *Matching complexes of \(3\times n\) grid graphs*, explicitly listed exactly the five wedge homotopy types above (Table 1, 2021), but was subsequently **retracted**, with a 2025 corrigendum explaining that indispensable purported inclusion maps arose from non-induced subgraphs. Thus the numerical answers themselves have prior history. The present finding supplies a separately checkable **perfect discrete-Morse realization** of those finite statements, a combinatorial certificate not implied by the former numerical assertions. Matsushita's 2019 theorem concerns two-row grids and a related family, not these three-row complexes. Public mathematical records inspected for overlap included a four-by-four grid matching-complex classification, which is a different graph and has mixed-dimensional homology.

## Limitations

No claim is made for \(n=8\), \(n=9\), or any unbounded range, and the results do not revalidate any discarded recurrence from the retracted paper. Computer execution verifies finite witnesses under the explicit bitmask encodings; there is no independent external audit or formal machine-checked proof. The current 2026 preprint could be inspected at abstract/indexed-statement level rather than from its full text, leaving some literature-overlap uncertainty for a **perfect Morse certificate**, though its public abstract is compatible with the distinction drawn here.

## References

- P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (first public 2026-09-23), https://arxiv.org/abs/2609.27366.
- S. Goyal, S. Shukla, A. Singh, *Matching complexes of \(3\times n\) grid graphs*, *Electron. J. Combin.* 28(4), P4.16 (2021); **retracted**, 2025 corrigendum appended to https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p16/pdf/.
- T. Matsushita, *Matching complexes of small grids*, *Electron. J. Combin.* 26(3), P3.1 (2019), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i3p1/pdf.
- R. Forman, *Morse theory for cell complexes*, *Adv. Math.* 134 (1998), 90–145; finite CW discrete-Morse theorem.
