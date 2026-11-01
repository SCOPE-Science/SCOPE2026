# The 96-symmetry magnitude-homology character of the Möbius–Kantor graph

## Finding
Let \(M=GP(8,3)\) be the Möbius–Kantor graph and \(G=\operatorname{Aut}(M)\), of order \(96\). On rational graph-magnitude homology in bidegree \((3,4)\), the **complete** character \(\chi(g)=\operatorname{tr}(g\mid\operatorname{MH}_{3,4}(M;\mathbb Q))\) has values \(304\) on the identity, \(4\) on exactly eight elements, \(-4\) on exactly twelve elements, and \(0\) on the remaining seventy-five elements. Equivalently, every automorphism with four fixed graph vertices and no edges among them has character \(4\); every automorphism with four fixed vertices spanning two disjoint edges has character \(-4\); all fixed-vertex-free automorphisms have character \(0\). The identity has character \(304\).

Consequently, \[\dim_{\mathbb Q}\operatorname{MH}_{3,4}(M;\mathbb Q)^G=\frac{304+8\cdot4-12\cdot4}{96}=3.\] The total Betti number \(304\) was already reported by Hepworth and Willerton; it is not the new result. The new result determines how every one of the \(96\) automorphisms acts on this rational homology and hence the three-dimensional fixed subspace.

## Assumptions and scope
Label the sixteen vertices \(u_i=i\), \(v_i=8+i\) for \(0\le i\le7\), with subscripts interpreted modulo eight. The unordered edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\) for \(0\le i\le7\), and \(d\) is their shortest-path metric. The graph has \(24\) edges, every vertex has degree three, diameter four, and girth six.

For \(k\ge1\), the integral magnitude chain group \(C_k\) at total length four has basis all tuples \((x_0,\ldots,x_k)\) with consecutive vertices distinct and \(\sum_{i=0}^{k-1}d(x_i,x_{i+1})=4\). For an internal vertex \(x_i\), the magnitude boundary deletes \(x_i\) with sign \((-1)^i\) precisely when \(d(x_{i-1},x_i)+d(x_i,x_{i+1})=d(x_{i-1},x_{i+1})\). Otherwise its contribution is zero. All chain groups with \(k>4\), as well as \(C_0\) at positive length, are zero. Graph automorphisms act on chains by componentwise permutation, with no orientation sign.

## Proof
**Exact chain ranks.** Enumerating all tuples by their integer shortest-path distances gives \[(\operatorname{rank}C_1,\operatorname{rank}C_2,\operatorname{rank}C_3,\operatorname{rank}C_4)=(16,1056,2592,1296).\] Each length-four endpoint pair has an intermediate point on a shortest path, hence \(\partial_2:C_2\to C_1\) is surjective, with rank \(16\) over \(\mathbb Q\).

Binary Gaussian elimination on the **complete** boundary matrices gives \[\operatorname{rank}_{\mathbb F_2}(\partial_3)=1040,\qquad \operatorname{rank}_{\mathbb F_2}(\partial_4)=1248.\] A nonzero minor modulo two remains nonzero over \(\mathbb Q\). The chain identity \(\partial_2\partial_3=0\) bounds the rational rank of \(\partial_3\) above by \(1056-16=1040\), so it is exactly \(1040\). There are \(48\) distinct integral cycles \((a,b,a,b,a)\), one for each **oriented** edge \(a\sim b\); they are distinct basis vectors of \(C_4\) and have zero boundary. Thus \(\operatorname{rank}_{\mathbb Q}\partial_4\le1296-48=1248\), and the binary lower bound makes this an equality. The required chain identity \(\partial_3\partial_4=0\) was also checked exhaustively with integer signs. Therefore \[\dim_{\mathbb Q}\operatorname{MH}_{1,4}=\dim_{\mathbb Q}\operatorname{MH}_{2,4}=0,\quad\dim_{\mathbb Q}\operatorname{MH}_{3,4}=2592-1040-1248=304,\quad\dim_{\mathbb Q}\operatorname{MH}_{4,4}=48.\] The \(48\) alternating-edge cycles are a basis of the latter rational group. This establishes all rational ranks used below without assuming the published numerical table.

**Group and character.** Every distance-preserving permutation of the sixteen vertices is enumerated by an exhaustive injective backtrack, retaining a candidate image of a vertex only when all pairwise distances to previously assigned vertices agree. It produces exactly \(96\) complete permutations; since the graph is connected and distance one means adjacency, these are precisely the full graph automorphism group. Each automorphism acts by permuting the basis tuples of \(C_k\), so \(\operatorname{tr}(g\mid C_k)\) equals the number of those tuples whose entries are all fixed by \(g\). On \(\operatorname{MH}_{4,4}\), it is the number of oriented edges both of whose endpoints are fixed. Additivity of the trace across finite chain complexes yields the exact identity
\[\operatorname{tr}(g\mid\operatorname{MH}_{3,4})=\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2)+\operatorname{tr}(g\mid C_3)-\operatorname{tr}(g\mid C_4)+\operatorname{tr}(g\mid\operatorname{MH}_{4,4}).\]

The exhaustive fixed-tuple calculation gives four rows, expressed as (fixed vertices; fixed oriented edges; traces in degrees one through four; resulting third-homology trace):

| Number of group elements | Fixed vertices | Fixed oriented edges | \(\operatorname{tr}C_1,\operatorname{tr}C_2,\operatorname{tr}C_3,\operatorname{tr}C_4\) | \(\chi\) |
| ---: | ---: | ---: | --- | ---: |
| 1 | 16 | 48 | \(16,1056,2592,1296\) | 304 |
| 8 | 4 | 0 | \(4,0,0,0\) | 4 |
| 12 | 4 | 4 | \(4,8,0,4\) | -4 |
| 75 | 0 | 0 | \(0,0,0,0\) | 0 |

The full ninety-six-row indexed table in `character_table.csv` supplies the permutation and trace of every individual group element; hence the classification is more precise than the four value frequencies alone. Averaging the character over the group gives the three-dimensional invariant subspace claimed.

## Verification
Run `python3 magnitude_verify.py` in the same directory as `character_table.csv`. This standalone Python 3 verifier uses only the standard library. It reconstructs the exact shortest-path metric and chain bases, exhaustively verifies both signed chain identities, computes both binary boundary ranks by full pivot elimination, checks all \(48\) alternating cycles, exhaustively enumerates all graph automorphisms without knowing their order in advance, compares the exact complete character table, and checks the invariant average. The expected terminal line is `MAGNITUDE_VERIFY_OK`. The actual output is included in `verification_output.txt`.

Binary ranks are used as rigorous lower bounds on rational boundary ranks and paired with independent rational upper bounds; they are not treated as equality by assumption. No claim is made about integral torsion in the third magnitude-homology group.

## Relationship to prior work
Hepworth and Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125, Appendix A.3.4, already give the Möbius–Kantor graph's \(96\)-element automorphism group and numerical Betti number \(304\) in bidegree \((3,4)\). Their Appendix A.3 introduction explicitly discusses possible symmetry actions but supplies neither the individual character traces nor the invariant dimension calculated here. The present character therefore refines rather than repeats their ranks.

Gu, *Graph magnitude homology via algebraic Morse theory*, arXiv:1809.07240, studies trees, pawful graphs, the icosahedral graph and cycles, not this graph's automorphism character. Asao–Hiraoka–Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044, Theorem 1.3, gives near-diagonal vanishing under sufficient girth, not a character in this bidegree for a girth-six graph. Asao–Wakatsuki, *Minimal projective resolution and magnitude homology of geodetic metric spaces*, arXiv:2408.12147, Theorem 1.1, gives a stronger basis theorem **under a geodeticity hypothesis**. The Möbius–Kantor metric fails that hypothesis: the two different shortest paths \(0\to1\to2\to3\) and \(0\to8\to11\to3\) both have length three.

## Limitations
The theorem applies only to the standard sixteen-vertex Möbius–Kantor graph, the graph metric, rational homology in the one bidegree \((3,4)\), and the natural full graph automorphism group. The integral third-homology lattice and possible torsion are not determined; neither are actions on other bidegrees. The literature comparisons were directed at relevant primary texts and indexed results, and cannot exclude an equivalent unindexed calculation. No independently performed mathematical audit is asserted.

## References
- R. Hepworth and S. Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125 (first public submission 2015-05-15), Appendix A.3.4; https://arxiv.org/pdf/1505.04125.
- Y. Gu, *Graph magnitude homology via algebraic Morse theory*, arXiv:1809.07240 (2018), Sections 1–4; https://arxiv.org/pdf/1809.07240.
- Y. Asao, Y. Hiraoka and S. Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044 (2021), Theorem 1.3; https://arxiv.org/pdf/2101.09044.
- Y. Asao and S. Wakatsuki, *Minimal projective resolution and magnitude homology of geodetic metric spaces*, arXiv:2408.12147 (2024), Theorem 1.1; https://arxiv.org/pdf/2408.12147.
