# Minimum total Roman \(\{2\}\)-domination configurations of square rook graphs: forest classification and exact census

## Finding
For each integer \(n\ge2\), let \(R_n=K_n\square K_n\), with labeled rows and columns. Let \(\gamma_{t\{R2\}}(R_n)\) be its total Roman \(\{2\}\)-domination number. Then
\[
\gamma_{t\{R2\}}(R_n)=\left\lceil\frac{4n}{3}\right\rceil.
\]
Every minimum-weight function takes **only** values zero and one. Under the incidence identification \(V(R_n)=E(K_{n,n})\), its one-labeled positions form precisely the spanning forests on the labeled \(2n\)-vertex complete bipartite graph with \(c=\lfloor2n/3\rfloor\) components, **every component of order at least three**. Conversely, every such forest gives a minimum function.

The exact number \(M_n\) of labeled minimum functions is as follows. Put \(B_k(n)=(n!)^2/(4^k(k!)^2)\). For integers \(k\ge1\),
\[
\begin{aligned}
M_{3k}&=B_k(3k),\\
M_{3k+1}&=B_k(3k+1)\,\frac{k(64k^2+107k+49)}{18(k+1)},\\
M_{3k+2}&=B_k(3k+2)\,\frac{4k+3}{3(k+1)}.
\end{aligned}
\]
The last formula also holds at \(k=0\), giving \(M_2=4\). Counts distinguish all labeled subsets and do not divide by row-column permutations or any automorphism.

The general rectangular value, included to establish the sharp square case, is
\[
\gamma_{t\{R2\}}(K_p\square K_q)=\min\left\{2p,\left\lceil\frac{2(p+q)}3\right\rceil\right\}\quad(2\le p\le q).
\]

## Assumptions and scope
For a finite simple graph \(G\), a total Roman \(\{2\}\)-dominating function is \(f:V(G)\to\{0,1,2\}\) such that each vertex with label zero has sum of neighbor labels at least two, and each vertex with positive label has at least one positively labeled neighbor. Its weight is \(\sum_{v\in V(G)}f(v)\). In \(K_p\square K_q\), distinct squares are adjacent exactly when they share a row or a column. All rows and columns are labeled and \(p,q\ge2\).

## Proof
**1. Empty row or column.** If a column is completely zero, the square in that column within each row has no contribution from its column. Its row must therefore have weight at least two. The total weight is at least \(2p\). If a row is completely zero, the same argument gives at least \(2q\ge2p\). The lower bound \(2p\) is attained by putting a two in each of the \(p\) squares of one column, leaving all other squares zero: the positive squares have positive column-neighbors because \(p\ge2\), while every other square has row-neighbor weight two.

**2. All rows and columns represented.** Suppose instead that every row and column contains a positive square. A zero square has one positive neighbor in its row and one in its column, and these are distinct, hence its zero-condition holds even if every label two is lowered to one. Lowering twos does not change the positive support or the condition on positive squares. Thus no minimum function in this regime uses twos: otherwise its weight could be decreased.

View the positive squares as edges of a bipartite incidence graph \(H\) on the \(p\) row-vertices and \(q\) column-vertices. All \(p+q\) vertices are incident with edges. A positive square has a positive neighbor exactly when the corresponding edge of \(H\) belongs to a component with at least two edges; equivalently, \(H\) has no component consisting of a single edge. Hence each component of \(H\) has at least three vertices. If \(c(H)\) is the number of components, then
\[
c(H)\le\min\left\{p,\left\lfloor\frac{p+q}{3}\right\rfloor\right\},
\qquad
|E(H)|\ge p+q-c(H).
\]
Both inequalities can hold simultaneously. Set \(c=\min\{p,\lfloor(p+q)/3\rfloor\}\). Partition the row-vertices and column-vertices into \(c\) disjoint groups, each with at least one vertex from each side and a total of at least three vertices. This is possible because \(p,q\ge c\) and \(p+q\ge3c\): start with one row and one column per group, distribute an extra vertex to each group, then distribute any remaining vertices. Within every group take a spanning tree of its complete bipartite graph. The resulting graph \(H\) has \(p+q-c\) edges and all required properties. Therefore the optimum in the fully represented regime is \(p+q-c\). Combining with Step 1 gives
\[
\min\left\{2p,\,p+q-\min\left(p,\lfloor(p+q)/3\rfloor\right)\right\}
=\min\left\{2p,\left\lceil 2(p+q)/3\right\rceil\right\}.
\]
The equality follows by considering \(p+q\ge3p\) and \(p+q<3p\) separately.

**3. Rigidity at square-board optimum.** Set \(p=q=n\). The bound \(\lceil4n/3\rceil<2n\) excludes every function with an empty row or column. Step 2 excludes twos, and the minimum number of positive cells is \(2n-c\) with \(c=\lfloor2n/3\rfloor\). Any incidence graph with \(c'\) components has at least \(2n-c'\) edges. Since every component has at least three vertices, \(c'\le c\). At equality of edge number, both \(c'=c\) and the tree equality \(|E(H)|=2n-c'\) must hold. Thus \(H\) is a spanning forest with \(c\) components, each having at least three vertices. Conversely any such forest induces a valid optimal function, proving the bijection.

**4. Exact enumeration.** A bipartite tree on a prescribed set of \(a\ge1\) row vertices and \(b\ge1\) column vertices has \(a^{b-1}b^{a-1}\) choices. Define its exponential component generating function
\[
T(x,y)=\sum_{\substack{a,b\ge1\\a+b\ge3}}
\frac{a^{b-1}b^{a-1}}{a!b!}x^a y^b.
\]
The exponential formula for *unordered* components now gives the exact coefficient identity
\[
M_n=(n!)^2[x^ny^nu^{\lfloor2n/3\rfloor}]\exp\bigl(uT(x,y)\bigr).
\]
The smallest component contributions are
\[
T_3=(x^2y+xy^2)/2,
\quad T_4=x^3y/6+x^2y^2+xy^3/6,
\quad T_5=x^4y/24+x^3y^2+x^2y^3+xy^4/24.
\]
For \(n=3k\), the \(2k\) components all have order three; balancing equal row and column totals forces \(k\) of each of the two \(T_3\) types. Their generating coefficient is \(1/(4^k(k!)^2)\), yielding the first formula.

For \(n=3k+2\), the \(2k+1\) components have one extra vertex above the three-vertex baseline. Exactly one component has order four and the others order three; extracting \(x^{3k+2}y^{3k+2}\) from \(T_4T_3^{2k}/(2k)!\), with the factor corresponding to choosing which component has order four, reduces to
\[
\frac{M_{3k+2}}{((3k+2)!)^2}=
\frac{4^{-k}}{(k!)^2}\cdot\frac{4k+3}{3(k+1)}.
\]
For \(n=3k+1\), the \(2k\) components have two extra vertices. There is either one order-five component and \(2k-1\) order-three components, or two order-four components and \(2k-2\) order-three components. Hence
\[
\frac{M_{3k+1}}{((3k+1)!)^2}
=[x^{3k+1}y^{3k+1}]
\left(\frac{T_5T_3^{2k-1}}{(2k-1)!}+
\frac{T_4^2T_3^{2k-2}}{2(2k-2)!}\right)
=\frac{4^{-k}}{(k!)^2}\cdot\frac{k(64k^2+107k+49)}{18(k+1)}.
\]
These exhaust the possible positive component-size profiles, completing the enumeration for all integers \(n\ge2\).

## Verification
The standalone file `verify_rook_tr2.py` performs exhaustive independent all-label checks for five small rectangular boards, exhaustive binary-support checks for square boards of orders two through four, and a rational-arithmetic labeled bipartite-tree exponential-formula count for square orders two through ten. The checks agree with all three closed census cases and with the rectangular weight formula; they are finite consistency tests, not a substitute for the general argument above.

For \(n=2,3,4,5,6,7,8,9,10\), the calculated minimum-census values are respectively
\[
4,\ 9,\ 880,\ 4200,\ 8100,\ 7629300,\ 31046400,\ 57153600,\ 225280440000.
\]
Run `python3 verify_rook_tr2.py` in an ordinary Python 3 environment; only standard-library modules are needed. The program checks `ALL_TESTS_PASSED` or raises an assertion.

## Relationship to prior work
The defining total Roman \(\{2\}\)-domination paper [1] explicitly relates binary-valued functions to double dominating sets. This identification is used, not claimed as novel. The paper [2] likewise develops the general invariant. The rook-graph \(k\)-tuple domination study [3] treats the same underlying graph and the related double-domination parameter; its available abstract concerns bounds, and its full text was not available for decisive priority inspection. Carballosa--Wisby [4] give total \(k\)-domination results for rook graphs, but total two-domination requires **two open-neighborhood** defenders at every square, including occupied squares, whereas here one open-neighborhood defender suffices at an occupied square. Mertens [5] counts ordinary rook dominating sets, which satisfy a weaker rule at unoccupied squares. Neither of those theorems determines this minimum-configuration census directly. The structural bijection with forests and the three congruence-class formulas are the specific proposed contribution, rather than the standard double-domination reduction or a scalar parameter alone.

## Limitations
The priority comparison with the 2009 rook-graph \(k\)-tuple paper relies on bibliographic/abstract material because its full text was inaccessible; it may contain an equivalent enumeration in an appendix or special case. Likewise, unpublished or unindexed counts could overlap. The coefficient formula assumes conventional labeled bipartite tree enumeration; it does not classify configurations up to graph automorphisms. The program verifies finite instances only. No independent audit has been performed.

## References
1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira and I. G. Yero, *Total Roman \(\{2\}\)-domination in graphs*, arXiv:2101.02537 (first arXiv public version 2021-01-07), https://arxiv.org/abs/2101.02537.
2. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami and J. C. Valenzuela-Tripodoro, *Total Roman \(\{2\}\)-Dominating Functions in Graphs*, arXiv:2402.07968 (2024), https://arxiv.org/abs/2402.07968.
3. P. A. Burchett, D. Lane and J. A. Lachniet, *k-tuple and k-domination on the rook's graph and other results*, Congressus Numerantium 199 (2009), 187--204. Bibliographic abstract at https://www.researchgate.net/publication/265782870_k-tuple_and_k-domination_on_the_rook%27s_graph_and_other_results.
4. W. Carballosa and J. Wisby, *Total \(k\)-domination in Cartesian product of complete graphs*, arXiv:2001.07850 (first public version 2020-01-22), https://arxiv.org/html/2001.07850v4.
5. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), Article 24.3.7, arXiv:2401.00716, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.html.
