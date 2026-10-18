# General-position and maximal-set polynomials of rectangular rook graphs

## Finding
For all integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\), and let \(\Psi_{m,n}(z)=\sum_{S\in\operatorname{GP}(R_{m,n})}z^{|S|}\), where a general-position (GP) set contains no three vertices on a common shortest path. The **complete GP polynomial** is determined by
\[
\sum_{m,n\ge0}\Psi_{m,n}(z)\frac{u^m v^n}{m!n!}
=\exp\!\bigl(u+v+zuv+u(e^{zv}-1-zv)+v(e^{zu}-1-zu)\bigr).
\]
Here the terms with a zero-sized factor are defined by the same exponential formula.

Let \(\mathcal M_{m,n}(z)\) count *inclusion-maximal* GP sets by cardinality. Define \(\bigl\{\!\bigl\{\begin{smallmatrix}n\\p\end{smallmatrix}\bigr\}\!\bigr\}_{\ge2}\) to count partitions of an \(n\)-element labeled set into \(p\) nonempty, unlabeled blocks, each of size at least two, and let \((m)_p=m(m-1)\cdots(m-p+1)\). Put
\[
 A_{m,n}=\sum_{p=1}^{\min(m-1,\lfloor n/2\rfloor)} (m)_p
 \Bigl\{\!\Bigl\{\begin{smallmatrix}n\\p\end{smallmatrix}\Bigr\}\!\Bigr\}_{\ge2}.
\]
Then the **complete inclusion-maximal GP polynomial** is
\[
\mathcal M_{m,n}(z)=
\sum_{a=0}^{m}\sum_{b=0}^{n}(-1)^{a+b}\binom ma\binom nb\Psi_{m-a,n-b}(z)
+A_{m,n}z^n+A_{n,m}z^m.
\]
Moreover, if \(2\le m\le n\), the exact support of this polynomial is
\[
\{k:[z^k]\mathcal M_{m,n}(z)>0\}
=\{m\}\cup\{n,n+1,\ldots,m+n-2\}.
\]
Thus for \(n\ge m+2\), the interior cardinalities \(m+1,\ldots,n-1\) (a run of \(n-m-1\) integers) **never** occur as sizes of inclusion-maximal GP sets, while every size from \(n\) through \(m+n-2\) does occur. The counts of every admissible cardinality, not merely minimum and maximum sizes, are given by the two formulas above.

## Assumptions and scope
All graphs are finite, simple, undirected. The rook graph has vertex set \([m]\times[n]\) with distinct vertices adjacent if they share one coordinate. An inclusion-maximal set cannot be enlarged while retaining the GP property; maximal does not mean maximum cardinality. A \(\Psi_{a,b}\) term in the inclusion-exclusion formula with \(a=0\) or \(b=0\) is the constant \(1\). All displayed identities concern every pair of integers \(m,n\ge2\), not only square boards.

## Proof
**Step 1 (geodesic/forest dictionary).** Identify a square \((i,j)\) with edge \(i\!\! -\!\! j\) of the labeled complete bipartite graph \(K_{m,n}\). The rook graph is its line graph. A geodesic containing three selected squares has length two, so corresponds to three selected bipartite edges \(e_1,e_2,e_3\) in which \(e_1\) and \(e_3\) are disjoint and each meets \(e_2\). These edges form a (not necessarily induced) three-edge path. Conversely, any selected three-edge path has disjoint end edges, giving a rook-graph geodesic. Hence a set is GP if and only if its selected bipartite edges contain no three-edge path. Any connected simple bipartite graph that contains no three-edge path is a star or a single vertex: a cyclic connected graph contains such a path; a tree of diameter at least three also contains one. Therefore GP sets correspond bijectively to bipartite star forests, including isolated vertices.

**Step 2 (all-set generating function).** Each star-forest component is uniquely one of: an isolated left vertex (weight \(u\)); an isolated right vertex (\(v\)); one isolated edge (\(zuv\)); a left-centered star with \(d\ge2\) edges (\(uz^dv^d/d!\)); or a right-centered star with \(d\ge2\) edges (\(vz^du^d/d!\)). There are no overlapping component types because only stars of degree at least two have a distinguished center, and a single edge is counted separately. The labeled exponential formula yields exactly the displayed bivariate EGF; extracting \(m!n![u^mv^n]\) gives \(\Psi_{m,n}(z)\).

**Step 3 (maximality criterion).** A star forest with no isolated vertices of either bipartition is inclusion-maximal, because adding any missing edge necessarily joins two positive-edge components and makes a three-edge path: take an existing edge at each endpoint of the new edge; those together with the new edge give a path. (A missing edge cannot lie within a star component, because that component already contains every center–leaf pair and its two leaves have the same bipartition.) If isolated vertices occur on *both* sides, their joining edge extends the forest. If there is an isolated left vertex and at least one right-centered component of degree at least two, adding the edge from that isolated left vertex to the right center preserves a star. If there is an isolated left vertex and a single-edge component, adding an edge to its right endpoint also preserves a star. Consequently, a maximal forest with an isolated left vertex has no single-edge or right-centered components. Further, it has no isolated right vertices. It therefore consists exclusively of left-centered stars of degree at least two, plus at least one isolated left vertex, with every right vertex a leaf of one such star. Conversely, all such forests are maximal: connecting an isolated left vertex to a right leaf makes a three-edge path, since that leaf's star center has at least one other right leaf. The case of isolated right vertices is symmetric. The three types (no isolates; left isolates only; right isolates only) are disjoint and exhaustive.

**Step 4 (enumerating the three maximal types).** Inclusion–exclusion over the left and right isolated vertices counts forests of the first type as
\[
\sum_{a=0}^{m}\sum_{b=0}^{n}(-1)^{a+b}\binom ma\binom nb\Psi_{m-a,n-b}(z).
\]
For the second type, use \(p\) chosen distinct left centers (ordered as labeled targets for the \(p\) leaf blocks), partition all \(n\) right vertices into \(p\) blocks of size at least two, and insist \(p\le m-1\), leaving a left isolated vertex. This gives \((m)_p\Bigl\{\!\Bigl\{\begin{smallmatrix}n\\p\end{smallmatrix}\Bigr\}\!\Bigr\}_{\ge2}\) forests, each with exactly \(n\) edges. Sum over \(p\) for \(A_{m,n}z^n\); the symmetric type contributes \(A_{n,m}z^m\). The polynomial formula follows.

**Step 5 (spectrum and gap).** Assume \(m\le n\). A maximal forest with left isolates has exactly \(n\) edges, while the symmetric case has \(m\) edges. A forest of the first type spans all \(m+n\) bipartite vertices and, because \(m,n\ge2\), consists of \(c\) positive-edge star components with \(2\le c\le m\) (each component touches at least one left vertex). It therefore has exactly \(m+n-c\) edges, belonging to \(\{n,n+1,\ldots,m+n-2\}\). Conversely, for every \(c\in\{2,\ldots,m\}\) build one right-centered star with \(m-c+1\) left leaves (possibly one) and \(c-1\) left-centered stars whose centers are the remaining left vertices and whose right leaves partition the remaining \(n-1\) right vertices into \(c-1\) nonempty blocks. This is possible because \(n\ge m\ge c\). It spans all bipartite vertices, uses \(c\) positive-edge star components, hence is maximal and has \(m+n-c\) edges. The size \(m\) comes from the right-centered star incident to every left vertex, leaving \(n-1\) right vertices isolated; it is maximal. These constructions prove the exact stated support.

## Verification
The accompanying standard-library-only program `verify.py` independently constructs shortest-path distances in rook graphs and exhaustively decides the geodesic triple condition and inclusion-maximality for all vertex subsets on ten rectangular boards. It computes the proposed polynomials by a different component recurrence and the restricted-set-partition correction and compares every coefficient to direct enumeration. The ten boards comprise 370,512 vertex subsets, and a further 42 boards are checked symbolically for support and boundary coefficients. Run `python3 verify.py` in the directory containing the extracted program. Recorded output is `verification_output.txt`, concluding `VERIFICATION_OK direct_boards=10 direct_subsets=370512 symbolic_boards=42`. These finite checks test, but do not replace, the quantified proof above.

## Relationship to prior work
Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero (arXiv:2306.09965, v1 of 16 June 2023) establish the *lower* general-position number for products of complete graphs (Theorem 5.3), yielding the already known \(\operatorname{gp}^{-}(K_m\square K_n)=\min(m,n)\). Iršič, Klavžar, Rus, and Tuite (arXiv:2401.05696, v1 of 11 January 2024) introduce the general-position polynomial and general identities but do not tabulate these two rectangular-rook-graph polynomials. Earlier work on general-position sets in Cartesian products establishes the known largest cardinality \(m+n-2\). The present complete bivariate family enumeration and the inclusion-maximal spectrum refine the known scalar extrema. The result also has a different statement from the mutual-visibility polynomial: GP forbids *any* occupied intermediate geodesic vertex, whereas mutual visibility only requires *some* unoccupied shortest path for each pair.

## Limitations
The theorem covers two Cartesian complete-graph factors of orders at least two, not arbitrary graph products or products with three or more factors. Independence of discovery or priority in unindexed literature is not established; equivalences under bipartite star-forest counting should be checked in subsequent external review. All proof and program assessments accompanying this package are self-review; independent scientific audit has not been performed.

## References
1. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first submitted 16 June 2023); https://arxiv.org/abs/2306.09965.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first submitted 11 January 2024); https://arxiv.org/abs/2401.05696.
3. S. Klavžar, B. Patkós, G. Rus, I. G. Yero, *On General Position Sets in Cartesian Products*, arXiv:1907.04535 (first submitted 10 July 2019), later Results in Mathematics 76, 123 (2021); https://arxiv.org/abs/1907.04535.
