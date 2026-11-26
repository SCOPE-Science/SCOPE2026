# The two eight-vertex exceptions for parameter-independent optimal site protection on trees

## Finding

Let the vertices of a fixed unweighted tree survive independently with common probability \(p\in(0,1)\), except that one chosen vertex is made certain to survive. Let \(C\) count ordered pairs of surviving vertices in the same surviving connected component, including the diagonal. Among the 23 unlabelled trees on eight vertices, exactly 21 have a protected vertex maximizing \(\mathbb E[C]\) simultaneously for all \(p\). The two exceptions, with labels \(0,\ldots,7\), are:

- \(A=\{01,05,12,23,24,56,67\}\). Vertex 2 is the unique optimum below the root \(\alpha\in(0,1)\) of \(p^2+p^3=1\), vertex 1 is the unique optimum above it, and exactly those two tie at \(\alpha\). This crossover was already covered by an equivalent deletion optimization [1, 2].
- \(B=\{01,05,12,23,24,56,57\}\). Exactly vertices 2 and 5 are optimal below \(1/\sqrt2\), exactly 0 and 1 are optimal above it, and precisely those four tie at \(1/\sqrt2\).

The contribution is the complete order-eight exceptional layer, in particular the second obstruction and its full optimum sets. The tree-order cutoff and the first crossover are not claimed as new.

## Assumptions and scope

All sites have unit weight. The surviving graph is the induced subgraph; the edges do not fail separately. Fixing the survival of the protected site does not change any other site's probability. The budget allows exactly one protection. No empirical intervention claim or classification beyond order eight is made.

## Exact objective and comparison with deletion

For the unique path \(P_{ab}\) from \(a\) to \(b\), let \(d(a,b)\) be the number of its edges. The contribution of \((a,b)\) to the expected gain from protecting \(v\) vanishes unless \(v\in P_{ab}\). Otherwise it is \((1-p)p^{d(a,b)}\), including the gain \(1-p\) when \(a=b=v\). Thus the protected sites maximizing the gain are precisely the maximizers of
\[
F_v(p)=\sum_{a,b:\,v\in P_{ab}}p^{d(a,b)}.
\]
Put \(W_T(p)=\sum_{a,b}p^{d(a,b)}\) and let \(S_v(p)\) count unordered distinct pairs in the same component of \(T-v\), weighting each by \(p^{d(a,b)}\). Then
\[
F_v(p)=W_T(p)-(n-1)-2S_v(p).
\]
Indeed the paths avoiding \(v\) consist of \(n-1\) diagonals and the two orientations of each residual pair. Therefore the optimal protected vertices are exactly the minimizers of \(S_v\), with identical ties, for every tree and every \(p\) in scope. The known lower-order guarantee for \(2\le n\le7\) and the switching spider \(A\) in [1, 2] apply through this identity; order one is immediate. The model interpretations are distinct, but the vertex optimization is not.

## Exhausting order eight

The companion `vertex_criticality_verify.py` enumerates all labelled eight-vertex trees via the bijection with Prüfer words of length six on \(\{0,\ldots,7\}\). It retains one tree per canonical code: center the tree, encode each rooted branch by a parenthesized sorted list of child codes, and for a central edge use the sorted pair of the two rooted half codes. Balanced words distinguish a single rooted tree from a concatenation of two rooted half trees. Induction on rooted tree order and preservation of the center under isomorphism justify the reduction to exactly 23 shapes. For each, summing unique paths gives all integer coefficient vectors of \(F_v\).

Let \(Q=F_u-F_v\) and set \(d=7\). For \(t=p/(1-p)>0\) one has the identity
\[
(1+t)^d Q\left(\frac{t}{1+t}\right)
=\sum_{j=0}^d t^j\sum_{k=0}^j [p^k]Q\binom{d-k}{j-k}.
\]
Nonnegative coefficients certify dominance on the whole interval; at least one strictly positive coefficient gives strict dominance there. At 21 representatives the checker finds a vertex with such nonnegative certificates against every other vertex. At the two others it verifies disjoint exact maximizer sets at \(1/2\) and \(9/10\), which suffices to exclude any common maximizer. The displayed trees are nonisomorphic (they have different degree multisets), and their codes are the two exceptional codes.

For \(A\), the path counts give \(F_2-F_1=2p(1-p^2-p^3)\). All vertices 3–7 are strictly dominated by 2, and vertex 0 by 1. For \(B\), the two three-valent vertices are interchanged by a tree automorphism, which also interchanges the internal path vertices 0 and 1; the four leaves are all strictly dominated by vertex 2. Here the two competing vectors, in ascending degree order, are \((1,6,8,6,8,8,0,0)\) for vertex 2 and \((1,4,8,10,8,8,0,0)\) for vertex 0. Their difference is \(2p(1-2p^2)\), so it has just the stated interior root. The strict comparisons follow from the above coefficient transform on the exact witness vectors. One can also infer strictness from the weak certificates and the strict inequalities at a sample where the dominating vertex is the unique winner or belongs only to the claimed tied optimum set: a certified coefficient list then cannot consist entirely of zeros.

## Reproduction and limitations

Run `python3 vertex_criticality_verify.py` (Python 3.9+). The exact integer certificates and rational nonuniversality checks, not the script's independent spot-check of survival configurations, establish the continuum result. The script also rechecks the already-covered lower orders. The exhaustive conclusion is specific to the eight-vertex layer, unit weights, uniform independent survival, and the ordered-pair objective. The deterministic objective \(C=\sum_i|K_i|^2\) is an existing component-coincidence measure, not a new index [3].

## References

1. [Sharp eight-vertex onset of transmissibility-dependent optimal vaccination on contact trees](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-sharp-eight-vertex-onset-of-transmissibility-dependent-optimal-v--639f57a81324/RESULT.md), Finding and Exact objective.
2. [Eight vertices are sharp for a transmissibility-dependent vaccination target on trees](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-eight-vertices-are-sharp-for-a-transmissibility-dependent-vaccin--9ba80a93d3d8/RESULT.md), Finding and Sharp eight-vertex witness.
3. S. Saura, *Measuring Connectivity in Habitat Mosaics: The Equivalence of Two Existing Network Indices and Progress Beyond Them*, Community Ecology 11 (2010), 217–222. DOI: 10.1556/ComEc.11.2010.2.10.
