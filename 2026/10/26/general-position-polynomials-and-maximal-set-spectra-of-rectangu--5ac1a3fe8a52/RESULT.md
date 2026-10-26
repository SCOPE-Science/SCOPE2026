# General-position polynomials and maximal-set spectra of rectangular rook graphs

## Finding

For integers \(p,q\ge 2\), let \(R_{p,q}=K_p\square K_q\) be the rook graph on the \(p\)-by-\(q\) board. A vertex subset is in general position when no three of its vertices lie on a shortest path. Write \(\Psi_{p,q}(z)=\sum_{S\text{ general position}}z^{|S|}\) and \(\mathcal M_{p,q}(z)=\sum_{S\text{ inclusion-maximal general position}}z^{|S|}\).

**Structural classification.** Under the natural identification of board cells with edges of the complete bipartite graph \(K_{p,q}\), general-position sets are **exactly** the edge sets whose nonisolated components are stars. An inclusion-maximal such set is exactly one of:

1. A star forest covering every vertex of \(K_{p,q}\) (a spanning star forest with no isolates).
2. A star forest with at least one isolated left vertex, no isolated right vertices, and every nontrivial component a star with its center on the left and at least two edges.
3. The left–right transpose of case 2.

The three cases are disjoint, even when a component is a single edge: such a component is permitted only in case 1.

**All-set enumerator.** As a formal series, with coefficient extraction in \(x,y\),
\[
\boxed{\Psi_{p,q}(z)=p!q!\,[x^py^q]\exp\!\left(xe^{zy}+ye^{zx}-xyz\right).}
\]

**Maximal-set enumerator.** Define
\[
B(x,y;z)=xyz+x(e^{zy}-1-zy)+y(e^{zx}-1-zx).
\]
Then
\[
\boxed{\begin{aligned}
\mathcal M_{p,q}(z)=p!q!\,[x^py^q]\bigl(&e^{B(x,y;z)}\\
&+(e^x-1)e^{x(e^{zy}-1-zy)}\\
&+(e^y-1)e^{y(e^{zx}-1-zx)}\bigr).
\end{aligned}}
\]

**Exact maximal-cardinality spectrum.** The cardinalities of all inclusion-maximal general-position sets are precisely
\[
\boxed{\{p,q\}\ \cup\ \{p+q-k:2\le k\le\min(p,q)\}.}
\]
Thus their minimum size is \(\min(p,q)\), their maximum size is \(p+q-2\), and the spectrum need not be an interval. For the two-row family, for every \(q\ge2\),
\[
\boxed{\Psi_{2,q}(z)=(1+2z)^q+qz^2,\qquad
\mathcal M_{2,q}(z)=qz^2+2^qz^q.}
\]
In particular, when \(q\ge4\), all intermediate sizes strictly between \(2\) and \(q\) are absent: the gap length is unbounded.

## Assumptions and scope

Graphs are finite, simple, and undirected; \(p\) and \(q\) are arbitrary integers at least two, with no requirement that they be equal. The empty vertex set is included in \(\Psi_{p,q}\), but not in \(\mathcal M_{p,q}\). All maximality statements refer to inclusion, not maximum cardinality. A star includes a one-edge \(K_{1,1}\); a **nontrivial star** in the exceptional maximal families has at least two edges. Isolated vertices of the bipartite incidence graph are not edges, hence do not contribute to the powers of \(z\).

In the bivariate exponential generating functions, \([x^py^q]\) extracts the indicated coefficient, with the left and right original vertices independently labeled. Equality holds as a polynomial identity in \(z\), for each fixed \(p,q\ge2\). No convergence assertion for the formal series is needed.

## Proof

**Step 1: Geodesics and an edge-set obstruction.** Each rook-graph vertex is a cell \((i,j)\). Distinct cells in the same row or column are adjacent. For cells \((i,j)\), \((k,\ell)\) in different rows and columns, the distance is exactly two, and the **only** internal vertices on shortest paths between them are \((i,\ell)\) and \((k,j)\). Therefore a chosen set fails general position if and only if it contains three corners of some two-by-two subrectangle. Identifying \((i,j)\) with the edge between left vertex \(i\) and right vertex \(j\) in \(K_{p,q}\), those three cells are exactly the edges of a three-edge simple path \(P_4\). Hence a chosen set is in general position if and only if its incidence subgraph contains no \(P_4\) as a (not necessarily induced) subgraph.

Every nontrivial connected bipartite graph without a three-edge path is a star. Indeed, if a spanning tree were not a star then that tree would have diameter at least three and contain such a path. If a spanning tree is a star, the bipartition forces any extra edge between its already-spanned vertices to run between its center and one of its leaves, hence that edge is already in the tree. Thus the connected graph itself is a star. Conversely every star is \(P_4\)-free. This proves the all-set classification without relying on a mere maximum-cardinality argument.

**Step 2: Enumerating all sets.** A bipartite star forest has isolated left vertices (EGF contribution \(x\)), isolated right vertices (\(y\)), one-edge components (\(xyz\)), left-centered stars with \(k\ge2\) edges (\(xz^ky^k/k!\)), and right-centered stars with \(k\ge2\) edges (\(yz^kx^k/k!\)). The exponential formula for sets of labeled connected components therefore gives
\[
\exp\left(x+y+xyz+x\sum_{k\ge2}\frac{z^ky^k}{k!}+y\sum_{k\ge2}\frac{z^kx^k}{k!}\right)
=\exp(xe^{zy}+ye^{zx}-xyz).
\]
The one-edge component is counted once rather than once from each center orientation. Multiplication by \(p!q!\) extracts labeled incidence graphs on the fixed bipartition. This proves the displayed formula for \(\Psi_{p,q}\).

**Step 3: Characterizing inclusion-maximal sets.** A star forest with no isolates is inclusion-maximal: any new bipartite edge must join two different nonisolated components, and their union then contains a three-edge path. No new edge exists within a star component.

If there are isolates on both sides, an edge joining opposite isolates can be added, so the forest is not maximal. Suppose therefore that the only isolates are on the left. A one-edge component can be extended by attaching an isolated left vertex to its right endpoint. A star with center on the right can also be extended by attaching such an isolated left vertex. Hence every component must instead be a left-centered star with at least two edges. In this case all right vertices are leaves of these stars, and adding any new edge from an isolated left vertex to a right leaf creates a \(P_4\), using a second leaf of the same star. Edges between existing components likewise create a \(P_4\). The forest is therefore maximal. Exchanging the parts gives case 3. These are exhaustive and mutually exclusive.

**Step 4: Enumerating inclusion-maximal sets.** No-isolate components are precisely the one-edge components and the stars with at least two edges, whose connected-component EGF is \(B(x,y;z)\). This gives \(e^B\). For case 2, \(e^x-1\) supplies one or more isolated left vertices; the remaining components are only left-centered stars of at least two edges, contributing \(\exp(x(e^{zy}-1-zy))\). This factor contains no isolated right vertices. The third term is its transpose. Their disjoint sum proves \(\mathcal M_{p,q}\).

For a purely integer alternative, write \(T(n,h)\) for the number of partitions of \(n\) labeled elements into \(h\) unlabeled blocks of size at least two. Then \(T(0,0)=1\), and for positive indices
\[
T(n,h)=hT(n-1,h)+(n-1)T(n-2,h-1),
\]
with all impossible boundary values zero. The nonspanning maximal-family contribution with left isolates is exactly
\[
z^q\sum_{h=1}^{\min(p-1,\lfloor q/2\rfloor)}\frac{p!}{(p-h)!}\,T(q,h),
\]
and the transposed family has the analogous contribution \(z^p\sum_h q!T(p,h)/(q-h)!\). Together with the spanning-star-forest EGF \(e^B\), these give an executable finite formula.

**Step 5: Cardinality spectrum.** A spanning star forest with \(k\) nonisolated components uses \(p+q-k\) edges. Because \(p,q\ge2\), it cannot be one spanning star, so \(2\le k\le\min(p,q)\). Every such \(k\) occurs: use \(k-2\) disjoint one-edge components, and on the remaining at least two vertices of each bipartition choose one star centered left and another centered right, joining each center to every noncenter vertex on the opposite side. This leaves no isolates and creates exactly \(k\) components. A nonspanning maximal forest with isolated left vertices covers each of the \(q\) right vertices exactly once, hence has exactly \(q\) edges; its transposed version has \(p\) edges. Both types exist, by a single star of degree \(q\) centered left or degree \(p\) centered right with the other vertices of the center side isolated. This proves the displayed support and its extrema.

**Step 6: The two-row identities.** When \(p=2\), a star forest either chooses at most one cell in each column or is exactly the two cells in one column. The first class contributes \((1+2z)^q\); the second contributes \(qz^2\). In a maximal set, choosing at most one cell in each column requires choosing exactly one in every column, giving \(2^qz^q\). The other maximal sets consist of both cells of a single column, giving \(qz^2\). At \(q=2\), these two terms correctly combine because their degrees coincide.

## Verification

The standalone file `verify_gp_rook.py` implements the original geodesic condition by directly testing all shortest-path middle vertices for every chosen nonadjacent pair. A separate function builds the bipartite incidence graph and tests its component shapes. For each of nine boards up to \(4\times4\) and also \(3\times5\), all vertex subsets were independently tested for general position, inclusion-maximality, the classification, and the two polynomial counts. The enumerated sample \(R_{3,5}\) satisfies
\[
\Psi_{3,5}(z)=1+15z+105z^2+335z^3+495z^4+303z^5+15z^6,
\]
\[
\mathcal M_{3,5}(z)=5z^3+213z^5+15z^6.
\]
The \(z^4\) coefficient of the second polynomial vanishes, as predicted by the spectrum theorem. The verifier reports 120,656 exhaustively checked masks, and further exact-integer recurrence checks for \(2\le p\le8\), \(p\le q\le12\). Execute it using `python3 verify_gp_rook.py`; expected text output is in `verification_output.txt`. The finite tests support but do not replace the arguments in Steps 1–6.

## Relationship to prior work

Iršič, Klavžar, Rus, and Tuite introduced general-position polynomials in their 11 January 2024 preprint (arXiv:2401.05696; published in *Results in Mathematics*, 2024). Their full article computes them for several graph classes and operations, including rectangular **path** grids, but does not give the rook-graph bivariate star-forest formula or its maximal-set polynomial. Theorem 5.3 of Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero (arXiv:2306.09965, first released 16 June 2023) already gives the lower general-position number \(\min(p,q)\) for rook graphs, without classifying and counting all maximal sets. The previously known maximum value \(p+q-2\) is also not claimed as new; it is stated in the earlier literature on general position in Cartesian products. The novelty claimed here is the simultaneous all-set classification, both exact enumerators, the full inclusion-maximal spectrum, and the explicit unbounded cardinality gaps.

These comparisons concern the specific statements and implications, not title matching. They do not establish global publication priority: a mathematically equivalent unindexed star-forest enumeration could exist.

## Limitations

The proof concerns two factors \(K_p\square K_q\) and ordinary undirected graph geodesics. It does not establish the formulas for three or more Hamming factors, arbitrary Cartesian products, mutual-visibility variants, root geometry, or unimodality of the resulting polynomials. Previously published extreme cardinalities are treated only as known boundary cases. The structural and enumeration claims have not received independent mathematical review, and bibliographic equivalences outside the inspected sources remain a residual risk.

## References

1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first publicly posted 2024-01-11); *Results in Mathematics* 79 (2024), article 110, DOI 10.1007/s00025-024-02133-3. https://arxiv.org/abs/2401.05696
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first publicly posted 2023-06-16), Theorem 5.3; *Discussiones Mathematicae Graph Theory* 45 (2025), 509–531. https://arxiv.org/abs/2306.09965
3. S. Klavžar, B. Patkós, G. Rus, I. G. Yero, *On General Position Sets in Cartesian Products*, *Results in Mathematics* 76 (2021), article 123, DOI 10.1007/s00025-021-01438-x. https://link.springer.com/article/10.1007/s00025-021-01438-x
4. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. Rahimi Mahid, G. Rus, *The General Position Problem on Kneser Graphs and on Some Graph Operations*, *Discussiones Mathematicae Graph Theory*, published paper and Section 3. https://bibliotekanauki.pl/articles/32222714.pdf
