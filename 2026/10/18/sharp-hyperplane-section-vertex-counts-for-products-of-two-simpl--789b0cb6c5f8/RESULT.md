# Sharp hyperplane-section vertex counts for products of two simplices

## Finding

For integers \(m,n\geq 2\), let \(P_{m,n}=\Delta_{m-1}\times\Delta_{n-1}\) be a Cartesian product of standard simplices, of dimension \(m+n-2\) and with \(mn\) vertices. Among **all affine hyperplanes** \(H\) in the affine hull of \(P_{m,n}\), the maximum number of vertices in the section \(P_{m,n}\cap H\) is
\[
\boxed{\nu(m,n)=\sum_{i=1}^{r}(T-i)(U-i)},\qquad
r=\min\{m,n\},\quad
T=\left\lfloor\frac{m+n+1}{2}\right\rfloor,\quad
U=\left\lceil\frac{m+n+1}{2}\right\rceil.
\]
In particular \(\nu(q,q)=q(q^2-1)/3\) for every integer \(q\ge2\), and \(\nu(2,3)=5\) for a triangular prism.

There is also a complete characterization of **generic** maximizing sections (hyperplanes through no vertex): sort the two sets of simplex-vertex functional values in decreasing order; the \(m\)-by-\(n\) sign matrix of values on product vertices must have positive entries at every index pair \((i,j)\) satisfying \(i+j<(m+n+2)/2\), negative entries at every pair satisfying \(i+j>(m+n+2)/2\), and arbitrary signs at the zero-weight antidiagonal \(i+j=(m+n+2)/2\). Every such sign pattern is realized by a generic affine hyperplane. After independently fixing the decreasing row and column orders, there is one maximizing pattern when \(m+n\) is odd, and exactly \(2^r\) when \(m+n\) is even.

The sharp asymptotic cost of geometric realizability can be seen when \(m=n=q\): the unrestricted graph maximum cut of the product's rook-graph skeleton has \(2q\lfloor q^2/4\rfloor\) crossing edges, whereas the best hyperplane-induced cut has only \(q(q^2-1)/3\). The ratio tends to \(2/3\).

## Assumptions and scope

Write \(\Delta_{m-1}=\operatorname{conv}\{e_1,\ldots,e_m\}\) in its affine hull, and analogously for \(\Delta_{n-1}\). All hyperplanes are affine codimension-one subsets of the \((m+n-2)\)-dimensional affine hull; neither centrality nor a special metric is assumed. A section vertex is a zero-dimensional face of the intersection. A hyperplane is *generic* if its affine functional is nonzero at each of the \(mn\) product vertices. The maximum includes supporting and nongeneric sections.

## Proof

**1. Generic sections reduce to graph cuts.** The vertices of \(P_{m,n}\) are \((e_i,e_j)\). Two of these are joined by an edge precisely when they share one index. Thus its graph is the rook graph \(K_m\square K_n\). For a generic intersecting hyperplane \(H=\{L=0\}\), each vertex of \(P_{m,n}\cap H\) occurs at the unique interior crossing of an edge with endpoint signs opposite. Indeed, a vertex of an intersection with a hyperplane is the intersection with a minimal face of dimension at most one; genericity rules out zero-dimensional old vertices. Distinct edges do not share interior points. Therefore the section's vertex count equals the number of cut edges of the rook graph.

**2. Hyperplane-induced cuts are Ferrers diagrams.** On product vertices any affine functional has additive values \(L(e_i,e_j)=a_i+b_j\). Independently reorder the values so \(a_1\ge\cdots\ge a_m\) and \(b_1\ge\cdots\ge b_n\). Let \(D\) be the positive-sign cells. Its row lengths \(\lambda_1\ge\cdots\ge\lambda_m\) lie in \(\{0,\ldots,n\}\), and the height of column \(j\) is \(k_j=\#\{i:\lambda_i\ge j\}\). So \(D\) is a Ferrers order ideal. Conversely, any such integer sequence is realizable by \(a_i=\lambda_i\), \(b_j=-j+\tfrac12\), which gives strictly positive values exactly when \(j\le\lambda_i\). Hence maximizing over generic hyperplanes is exactly maximizing over Ferrers diagrams.

**3. Exact weighted-cell identity.** In a row with \(\lambda_i\) positive and \(n-\lambda_i\) negative vertices, there are \(\lambda_i(n-\lambda_i)\) crossing edges; column \(j\) gives \(k_j(m-k_j)\). Thus
\[
V(D)=\sum_{i=1}^m\lambda_i(n-\lambda_i)
+\sum_{j=1}^n k_j(m-k_j).
\]
Expanding the squares by \(s^2=\sum_{j=1}^s(2j-1)\), and using \(\sum_i\lambda_i=\sum_j k_j=|D|\), gives the **exact identity**
\[
V(D)=\sum_{(i,j)\in D}\bigl(m+n+2-2i-2j\bigr).
\]
This also follows directly by the marginal effect of adjoining a corner cell of a Ferrers diagram. The weights strictly decrease along either index. Therefore the diagram of all positive-weight cells is itself an order ideal and maximizes the sum. Equality forces inclusion of every positive-weight cell and exclusion of every negative-weight cell, with completely free choices among zero-weight cells.

**4. Evaluate and classify.** By symmetry assume \(m\le n\). Put \(s=m+n+1\), \(T=\lfloor s/2\rfloor\), \(U=\lceil s/2\rceil\). In row \(i\), positive-weight cells have column indices \(1\le j\le T-i\); note \(T-i\ge0\) for \(i\le m\le n\), apart from the harmless zero case. Summing their weights yields
\[
\sum_{j=1}^{T-i}(m+n+2-2i-2j)
=(T-i)(U-i).
\]
Adding over \(i=1,\ldots,m\) proves the stated formula. The zero-weight cells satisfy \(i+j=(m+n+2)/2\). They are absent when \(m+n\) is odd; when it is even there are exactly \(r\) such cells, which are mutually incomparable in the product partial order. Every subset therefore yields a distinct maximizing Ferrers diagram, all representable by the explicit additive functional of Step 2.

**5. Nongeneric sections cannot beat the bound.** If \(H\) is disjoint from \(P_{m,n}\), there is nothing to show. Otherwise choose an affine functional \(L\) vanishing on \(H\). If the polytope has vertices on both strict sides of \(H\), each old polytope vertex on \(H\) has an incident edge leading to the positive side: a vertex at which no edge increases \(L\) would be a global maximizer of \(L\) on the polytope, contradicting the existence of positive values. Translate \(H\) a sufficiently small distance toward the positive side, and make a further tiny generic perturbation. Every old section vertex arising from a strictly crossed edge persists; each old vertex lying in \(H\) yields an additional distinct section vertex on an incident positive edge. These distinct points account for all old section vertices, so a generic section has at least as many. For a supporting section with no strictly crossed edges, an infinitesimal inward translate yields at least one edge crossing at every vertex of its supporting face, by the same local-edge argument. Therefore **every** section is bounded above by a generic one. The maximum already has a generic realization, completing the proof.

**6. Unrestricted-cut comparison.** Each of the \(2q\) row and column copies of \(K_q\) has at most \(\lfloor q^2/4\rfloor\) cut edges. A checkerboard coloring simultaneously attains every one of those clique bounds, so the unconstrained cut is \(2q\lfloor q^2/4\rfloor\). The proven formula gives \(\nu(q,q)=q(q^2-1)/3\), yielding the asserted ratio.

## Verification

The standalone Python 3 checker `check_simplotopes.py` independently enumerates 76,792 Ferrers diagrams across \(2\le m\le8\) and \(m\le n\le9\), verifying the exact maxima and number of generic maximizing sign diagrams. It constructs 823 exact-rational hyperplane sections and compares their distinct crossing-edge intersection vertices to the graph-cut count, including explicit maximizers. Nine square rook-graph comparisons confirm the strict unconstrained-cut gap. Run with `python3 check_simplotopes.py`; the final line should read `SIMPLOTOPE_SECTION_THEOREM_CHECKS_OK`. These are finite checks, not the proof for all dimensions.

## Relationship to prior work

Seacrest and Su [1] introduce simplotopes and study lower bounds for their triangulations; this determines neither maximum section vertex counts nor the maximizing Ferrers patterns. Hibi and Li [2] study *separating* hyperplanes that cut a polytope into two polytopes without creating new vertices, a different task from counting the crossed-edge vertices in a section. Padrol and Pfeifle [3] study economical higher-dimensional realizations of prescribed polygonal sections, rather than extremal sections of a fixed product. De Loera, Lopez-Campos, and Torres [4] study general hyperplane-section vertex bounds and specific families including cubes; their general bounds do not give the product-specific exact maximum or equality classification proved here.

The proof uses elementary, established polytope graph and Ferrers-diagram facts. The claimed contribution is the *joint* sharp all-parameter section count, complete generic equality classification, and quantitative gap from unrestricted cuts; not discovery of the rook graph or Ferrers diagrams.

## Limitations

The result treats **two factors**, with each simplex positive-dimensional. The equality classification is for hyperplanes avoiding every original vertex; the maximum upper bound also holds for nongeneric and supporting sections. No claim is made about all possible intermediate section vertex counts, higher-codimension slices, volume-maximizing sections, or more than two simplex factors. Related extremal cut identities could exist under other terminology; historical priority beyond the inspected sources remains unconfirmed. No independent mathematical audit has been performed.

## References

[1] T. Seacrest and F. E. Su, *A lower bound technique for triangulations of simplotopes*, arXiv:0910.1134 (first public 6 October 2009), https://arxiv.org/abs/0910.1134.

[2] T. Hibi and N. Li, *Cutting convex polytopes by hyperplanes*, arXiv:1402.3805 (2014), https://arxiv.org/abs/1402.3805.

[3] A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443 (2014), https://arxiv.org/abs/1404.2443.

[4] J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (2024), https://arxiv.org/abs/2412.12419.
