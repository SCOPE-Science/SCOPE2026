# Acyclic polynomials and extremal induced forests of rook graphs

## Finding

Let \(R_{m,n}=K_m\square K_n\) be the graph on the \(m n\) labeled cells of an \(m\)-by-\(n\) rectangle, where two distinct cells are adjacent when they share a row or a column. For nonnegative integers \(m,n\), let \(A_{m,n}(z)\) count vertex subsets of \(R_{m,n}\) whose induced subgraph is a forest, with each subset weighted by \(z\) to the power of its cardinality. In the degenerate cases with an empty coordinate, take \(A_{m,0}(z)=A_{0,n}(z)=1\).

**Theorem (complete bivariate acyclic polynomial).** As a formal power series in \(x,y\) with polynomial coefficients in \(z\),

\[
\sum_{m,n\geq 0}\frac{A_{m,n}(z)}{m!n!}x^m y^n
=\exp\!\left(x+y+\frac{xy z+\frac12 xy(x+y)z^2}{1-xy z^2}\right).
\]

Consequently this identity determines every coefficient of the acyclic polynomial for every rook graph. If \(2\leq m\leq n\), its largest nonzero exponent is

\[
\deg A_{m,n}(z)=2m-\mathbf 1_{\{m=n\}}.
\]

The leading coefficient, counting all maximum induced forests and, by complementation, all minimum feedback vertex sets, is

\[
[z^{2m-1}]A_{m,m}(z)=(m!)^2
\qquad(m\geq 2),
\]

and, for \(2\leq m<n\) with \(c=n-m\),

\[
[z^{2m}]A_{m,n}(z)
=\frac{m!n!}{c!}
\sum_{j=1}^{\min(m,c)}\binom cj\binom{m-1}{j-1}\frac{1}{2^j}.
\]

For example,

\[
A_{3,3}(z)=1+9z+36z^2+78z^3+81z^4+36z^5,
\]

\[
A_{3,4}(z)=1+12z+66z^2+204z^3+342z^4+288z^5+72z^6.
\]

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. A vertex subset induces a forest if its induced graph contains no cycles; the empty induced graph counts as a forest. A feedback vertex set is a set whose deletion leaves an induced forest. The row and column labels are fixed; distinct labeled vertex subsets are not identified under graph automorphisms. The two-variable series is interpreted formally, so no analytic convergence assumptions are required. The explicit extremal counting formulas apply for every integer pair \(2\leq m\leq n\); swapping coordinates gives all pairs with both dimensions at least two.

## Proof

**1. The line-graph equivalence.** Identify each cell \((i,j)\) with the edge joining left vertex \(i\) and right vertex \(j\) in the complete bipartite graph \(K_{m,n}\). Two cells share a row or column exactly when the corresponding edges share an endpoint; hence \(R_{m,n}\) is its line graph. Given a selected set of cells \(S\), let \(F\) be the spanning edge subgraph of \(K_{m,n}\) consisting of the corresponding edges. Then \(R_{m,n}[S]=L(F)\), after ignoring isolated vertices of \(F\).

The line graph \(L(F)\) is a forest **if and only if** \(F\) is a linear forest (each component is a path, including isolated vertices). Indeed, a vertex of degree at least three in \(F\) creates a triangle in \(L(F)\). A cycle in \(F\) creates a cycle in \(L(F)\). Conversely, a forest of maximum degree at most two consists of paths, and the line graph of a disjoint union of paths is a disjoint union of paths. Thus counting acyclic vertex sets of \(R_{m,n}\) is equivalent, exactly and with weights preserved, to counting spanning labeled bipartite linear forests in \(K_{m,n}\), weighting every chosen edge by \(z\).

**2. Labeled path components.** Use \(x\) for vertices on the left shore and \(y\) for vertices on the right shore. A singleton component contributes \(x+y\). For a path having \(r\) vertices of each type (\(r\geq1\)), alternation forces \(2r-1\) edges; its labeled count is \((r!)^2\) and its bivariate exponential-generating contribution is \((xy)^r z^{2r-1}\). For a path with \(r+1\) vertices on one shore and \(r\) on the other (\(r\geq1\)), the labeled count is \((r+1)!r!/2\), because reversal identifies the two linear orderings. The two possible orientations of the shore imbalance contribute

\[
\tfrac12(x+y)(xy)^r z^{2r}.
\]

Every nontrivial connected bipartite linear-forest component has exactly one of these forms. Therefore their entire connected-component series is

\[
C(x,y;z)=x+y+
\sum_{r\geq1}(xy)^r z^{2r-1}
+\frac{x+y}{2}\sum_{r\geq1}(xy)^r z^{2r}
=x+y+\frac{xy z+\frac12xy(x+y)z^2}{1-xy z^2}.
\]

The labeled exponential formula for an unordered set of connected components gives the stated identity \(\exp(C(x,y;z))\). Extracting the coefficient of \(x^m y^n\) and multiplying by \(m!n!\) gives the complete polynomial, not just the extremal terms.

**3. Maximum cardinalities.** Assume \(2\leq m\leq n\). Every left-shore vertex in a linear forest has degree at most two, so the number of selected edges is at most \(2m\). When \(m<n\), this bound is attained: choose \(m+1\) right vertices and link them by a path with each of the \(m\) left vertices inserted on a distinct path edge. The result is a path with \(2m\) edges. When \(m=n\), a spanning forest on \(2m\) vertices has at most \(2m-1\) edges, attained by an alternating Hamiltonian path. This proves the degree formula.

**4. Extremal multiplicities in the square case.** If \(m=n\), an optimal selected edge set has \(2m-1\) edges and uses all \(2m\) vertices, hence it is one alternating Hamiltonian path. Choose which shore starts (two possibilities), order the vertices within each shore (\((m!)^2\) possibilities), then divide by two for reversing the undirected path. This yields exactly \((m!)^2\) distinct optimal sets.

**5. Extremal multiplicities in the rectangular case.** Suppose \(m<n\). To have \(2m\) edges, every one of the \(m\) left vertices must have degree exactly two. Suppress each such degree-two vertex, replacing its two incident edges by an edge between the two neighboring right vertices. Acyclicity ensures that no parallel edge or cycle arises. This is a bijection between optimal selected-edge sets and a linear forest on the \(n\) labeled right vertices with exactly \(m\) edges, together with an assignment of the \(m\) distinct left labels to the \(m\) edges (\(m!\) choices).

A linear forest on \(n\) vertices with \(m\) edges has exactly \(c=n-m\) components, isolated vertices included. For an undirected path component on \(k\) labeled vertices there is one realization for \(k=1\), and \(k!/2\) realizations for \(k\geq2\). Its connected-component exponential generating function is therefore

\[
B(u)=u+\sum_{k\geq2}\frac{u^k}{2}
=u+\frac{u^2}{2(1-u)}.
\]

The number of such right-shore forests is \(n![u^n]B(u)^c/c!\). Because

\[
B(u)^c=u^c\left(1+\frac{u}{2(1-u)}\right)^c,
\]

and \(m\geq1\), the binomial expansion gives

\[
[u^{m}]\left(1+\frac{u}{2(1-u)}\right)^c
=\sum_{j=1}^{\min(m,c)}\binom cj\frac{1}{2^j}\binom{m-1}{j-1}.
\]

Multiplying by \(m!n!/c!\) proves the announced leading-coefficient formula. Each summand is counted with labeled edges and unoriented path components; there is no quotient by row/column automorphisms.

## Verification

The accompanying standalone standard-library Python file `verify_acyclic_rook.py` constructs rook-graph adjacency directly from shared row/column coordinates and tests all induced vertex subsets by union-find cycle detection for every checked parameter pair having at most sixteen graph vertices. The 14 checked parameter pairs range from \((1,1)\) through \((4,5)\), including the balanced \((4,4)\) graph. An independent recursion assembles labeled alternating bipartite path components, and a separate exact-rational expansion of the bivariate generating function checks every coefficient for eight parameter pairs, up to \((5,5)\). The script asserts the polynomial degree and leading-coefficient formulas in all fourteen cases, and prints `VERIFY_OK` and `EGF_VERIFY_OK` upon success. This is finite corroboration; the arbitrary-parameter claims follow from the proof above.

## Relationship to prior work

Barton, Brown, and Pike introduced the acyclic polynomial (in the vertex-induced-forest sense) and connected its degree with minimum feedback vertex sets. Their work establishes general properties, root behavior, and some other graph families, including a lexicographic-product identity; this does not imply the present Cartesian-product polynomial or extremal multiplicities. The corresponding scalar decycling number of rook graphs is available in graph-invariant tables and is not claimed as a new invariant. The new result is the complete coefficient enumeration and, in particular, the exact count and structure of all minimum feedback vertex sets. The equivalence with labeled bipartite linear forests explains both results. The same graph polynomial has also historically been called a *forest polynomial*, so that alias is included when comparing literature.

## Limitations

The result concerns two-dimensional rook graphs, not arbitrary line graphs, other Cartesian products, or induced trees that must be connected. The leading coefficient counts optimal vertex subsets, not numbers of distinct path orderings or their orbits under automorphisms. Literature comparison does not certify global publication priority; any previously overlooked enumeration of spanning bipartite linear forests could imply the stated generating function. No independent mathematical audit has been performed.

## References

1. C. Barton, J. I. Brown, and D. A. Pike, “Acyclic polynomials of graphs,” arXiv:2011.01735 (first publicly posted November 3, 2020), *Australasian Journal of Combinatorics* **82**(2) (2022), 146–181. https://arxiv.org/abs/2011.01735 ; https://ajc.maths.uq.edu.au/pdf/82/ajc_v82_p146.pdf .
2. S. L. Bau and L. W. Beineke, “The decycling number of graphs,” *Australasian Journal of Combinatorics* **25** (2002), 285–298; arXiv:math/0703544.
3. Wolfram MathWorld, “Feedback Vertex Set Number,” graph-invariant table including rook graphs. https://mathworld.wolfram.com/FeedbackVertexSetNumber.html .
4. Wolfram MathWorld, “Induced Forest,” terminology and interpretation of the induced-forest polynomial. https://mathworld.wolfram.com/InducedForest.html .
