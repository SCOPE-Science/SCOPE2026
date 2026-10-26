# Edge-general-position polynomials of quadrilateral books

## Finding
Let \(r\ge 2\), and let \(B_r\) be the graph obtained by gluing \(r\) four-cycles along one common edge. Its vertices are \(u,v,x_1,\ldots,x_r,y_1,\ldots,y_r\), and its edges are the spine \(h=uv\) and the page edges \(a_i=ux_i\), \(b_i=vy_i\), and \(c_i=x_i y_i\), for \(1\le i\le r\). Let \(P_r(z)=\sum_{S}z^{|S|}\), summed over all subsets \(S\subseteq E(B_r)\) such that every shortest path contains at most two edges of \(S\).

Define
\[
U_r(z)=\sum_{a=2}^r\binom{r}{a}z^a(1+z)^{r-a}
\]
and
\[
V_r(z)=\sum_{a=2}^r\sum_{b=2}^r\sum_{t=\max(0,a+b-r)}^{\min(a,b)}
\binom{r}{a}\binom{a}{t}\binom{r-a}{b-t}
 z^{a+b}(1+z)^{r-a-b+t}.
\]
Then the **complete edge-general-position polynomial** is
\[
\boxed{P_r(z)=(1+z)^r(1+rz)^2+2(1+rz)U_r(z)+V_r(z)
+z\bigl((1+z)^r(1+2rz+rz^2)+2U_r(z)\bigr).}
\]
In particular, the number of admissible edge subsets, including the empty subset, is
\[
\boxed{P_r(1)=5^r+(2r+6)3^{r-1}+(r^2+9r-4)2^{r-2}.}
\]
The maximum size and number of labeled maximum subsets are, respectively,
\[
\operatorname{gp}_{\mathrm e}(B_r)=\max\{2r,r+3\},\qquad
\#\{S:|S|=\operatorname{gp}_{\mathrm e}(B_r)\}=
\begin{cases}2,&r=2,\\4,&r=3,\\1,&r\ge4.\end{cases}
\]
For \(r\ge4\), the unique maximum set consists of the \(r\) edges incident to \(u\) other than the spine together with the \(r\) edges incident to \(v\) other than the spine (that is, all \(a_i\) and \(b_i\)). At \(r=3\), the three other maximum sets consist of \(h\), all \(c_i\), and the pair \(a_j,b_j\) for one fixed page \(j\). At \(r=2\), just those latter two page-indexed sets are maximum.

## Assumptions and scope
All graphs are finite, undirected, and simple, and the pages have distinct internal vertices. The edge subsets are distinguished by their edges in the fixed graph, not counted up to automorphisms. A geodesic means a shortest path between its endpoints. The polynomial identity is for every integer \(r\ge2\) and every indeterminate \(z\); the total-count formula, maximum formula, and extremizer classification have the same range. In the exceptional case \(r=1\), the graph is a four-cycle, every edge subset is admissible, and \(P_1(z)=(1+z)^4\).

## Proof
Every vertex pair in \(B_r\) has distance at most three. The distance-three pairs are precisely \(x_i,y_j\) with \(i\ne j\). Indeed, all other pairs are adjacent or linked by an evident path of length two, whereas \(x_i\) and \(y_j\) for distinct pages have no common neighbor. The three length-three geodesics between such a pair have edge sequences
\[
(a_i,h,b_j),\qquad (a_i,a_j,c_j),\qquad(c_i,b_i,b_j).
\]
No other geodesic can contain three edges. Thus these three families, over all ordered pairs \(i\ne j\), are the *entire* list of forbidden selected triples.

For \(S\subseteq E(B_r)\), put \(A=\{i:a_i\in S\}\), \(B=\{i:b_i\in S\}\), and \(C=\{i:c_i\in S\}\). The forbidden triples give the following necessary and sufficient conditions:

1. If \(|A|\ge2\), then \(A\cap C=\varnothing\).
2. If \(|B|\ge2\), then \(B\cap C=\varnothing\).
3. If \(h\in S\), then \(A=\varnothing\), or \(B=\varnothing\), or \(A=B=\{j\}\) for one \(j\).

First count subsets not containing \(h\). If \(|A|,|B|\le1\), the choices contribute \((1+rz)^2(1+z)^r\). If exactly one of \(|A|,|B|\) is at least two, first choose that larger set, then freely select \(C\) off it; the other set is empty or a singleton. This gives \(2(1+rz)U_r(z)\). If both sizes are at least two, choose \(A\) of size \(a\), choose \(t=|A\cap B|\) of its elements for \(B\), then the remaining \(b-t\) from the complement; the allowable \(C\) are precisely subsets outside \(A\cup B\). This gives \(V_r(z)\). All these classes are disjoint and exhaustive.

If \(h\in S\), the third condition leaves either \(A=B=\varnothing\), exactly one of \(A,B\) nonempty, or both equal to one singleton. Counting these yields
\[
z\bigl((1+z)^r(1+2rz+rz^2)+2U_r(z)\bigr).
\]
The two counts combine to prove the polynomial formula.

For the total count, \(U_r(1)=3^r-2^r-r2^{r-1}\). To evaluate \(V_r(1)\), give each page one of five statuses: empty, \(c\), \(a\), \(b\), or both \(a\) and \(b\). These are exactly the states allowed when both \(|A|\) and \(|B|\) are unrestricted but \(C\cap(A\cup B)=\varnothing\). Inclusion-exclusion for \(|A|\le1\) and \(|B|\le1\) gives
\[
V_r(1)=5^r-2(3^r+2r3^{r-1})+2^r+3r2^{r-1}+r(r-1)2^{r-2}.
\]
Substitution in the polynomial formula at \(z=1\), followed by collecting the powers of \(5\), \(3\), and \(2\), gives the displayed formula for \(P_r(1)\).

For maximal cardinality without \(h\), the two small-size cases obey \(|S|\le r+2\) and \(|S|\le r+1\), respectively. If \(|A|,|B|\ge2\), then \(C\subseteq[r]\setminus(A\cup B)\) and consequently
\[
|S|\le|A|+|B|+r-|A\cup B|=r+|A\cap B|\le2r.
\]
Equality there forces \(A=B=[r]\) and \(C=\varnothing\). For \(r\ge3\), the other no-spine cases have fewer than \(2r\) edges. With \(h\), the cases with one of \(A,B\) empty have \(|S|\le r+2\), whereas \(A=B=\{j\}\) gives \(|S|\le r+3\), with equality if and only if \(C=[r]\). Comparing \(2r\) and \(r+3\) proves the maximum formula and the stated exact classification, including the small ties and exceptions. For \(r=2\), a no-spine set never reaches five.

## Verification
The standalone `verify.py` uses two different counting procedures: a direct enumeration of shortest paths in the explicit graph and admissible edge subsets, and the closed binomial-sum formula above. For \(1\le r\le5\) these methods agree coefficient-by-coefficient; the geodesic enumeration finds respectively \(0,6,18,36,60\) distinct forbidden triples, as predicted by the proof. A separate construction from the three combinatorial conditions agrees with the formula through \(r=6\); the total-count identity, maximum size, and extremizer multiplicities are also checked in those cases. The exact output is included in `verify_output.txt`. These finite checks corroborate, but do not replace, the proof for all \(r\).

## Relationship to prior work
Manuel, Prabha, and Klavžar introduced edge general position in arXiv:2105.04292 (first public version, 2021-05-10). Their Theorem 4.1 covers the numerical \(r=2\) instance because \(B_2\cong P_3\square P_2\); it does not state a square-book polynomial or the result for \(r\ge3\). Tian, Klavžar, and Tan, arXiv:2302.01587, treat certain extremal graph classes and block graphs, not the two-connected, nonclique square-page books \(B_r\) with \(r\ge2\). Manuel, Prabha, and Klavžar's generalized edge-position work, arXiv:2207.07357, develops the \(k\)-variant and exact results for torus, hypercube, and Benes networks, not a book-graph edge-subset census. The fact that a graph is a partial cube does not by itself determine its full edge-general-position polynomial. Results about *vertex* general-position variants of books and *edge* general position of spider trees address different objects or predicates. No general theorem in the inspected sources implies the displayed enumerator.

## Limitations
Originality is assessed against the identified sources and publicly searchable related results, not established as exhaustive priority. The existence of unindexed work on short geodesic avoidance in books or tree prisms remains a risk. Only the square-page books, with all pages sharing an edge, are handled here; no result is asserted for general prisms of trees, higher polygonal books, or arbitrary graph products. The exact numerical case \(r=2\) is a known consequence of the grid result; the proposed contribution is the full enumerator and structural classification for the entire family, especially \(r\ge3\).

## References
1. P. Manuel, R. Prabha, S. Klavžar, *Edge General Position Problem*, arXiv:2105.04292v1, first public 2021-05-10, https://arxiv.org/abs/2105.04292.
2. J. Tian, S. Klavžar, E. Tan, *Extremal edge general position sets in some graphs*, arXiv:2302.01587 (first public 2023-02-03), https://arxiv.org/abs/2302.01587.
3. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (2022-07-15), published in Art of Discrete and Applied Mathematics 8 (2025), https://doi.org/10.26493/2590-9770.1745.5f4.
4. Y. Cao, S. Ji, L. Wang, *The edge general position number of some graphs*, Bull. Malaysian Math. Sci. Soc. (2025), https://doi.org/10.1007/s40840-025-01873-x.
