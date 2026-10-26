# The exact \(P_3\)-convexity polynomial of antiprism graphs

## Finding

For every integer \(n\ge3\), let \(A_n\) be the antiprism graph with vertices \(a_i,b_i\), indexed modulo \(n\), and with edges \(a_i a_{i+1}\), \(b_i b_{i+1}\), \(a_i b_i\), and \(a_i b_{i-1}\). A subset of vertices is \(P_3\)-convex if every vertex outside the subset has at most one neighbour inside it. Define its cardinality polynomial by
\[
C_n(z)=\sum_{S\subseteq V(A_n),\ S\ P_3\text{-convex}}z^{|S|}.
\]
Then the following bivariate generating identity holds as a formal power series in \(t\) with coefficients in \(\mathbb Z[z]\):
\[
\boxed{\sum_{n\ge3}\bigl(C_n(z)-1-z^{2n}\bigr)t^n=
\frac{2zt^3(3-2t)+z^2t^5(5-4t)}{(1-t)(1-t-2zt^3-z^2t^5)}.}
\]
Every nonempty proper \(P_3\)-convex set is exactly a distance-two packing (its distinct vertices have graph distance at least three), and the largest proper convex sets have cardinality exactly \(\lfloor2n/5\rfloor\). The exceptional summands \(1\) and \(z^{2n}\) count the empty set and the whole vertex set.

## Assumptions and scope

Graphs are undirected and simple; indices are taken modulo \(n\). In particular \(A_3\) is the octahedral graph. A distance-two packing is a set with no two selected vertices joined by a walk of length at most two. All parameters and enumerators count labelled vertex subsets, not automorphism orbits. The generating function is exact for every integer \(n\ge3\), with no asymptotic restrictions. The independent variable \(z\) marks the number of selected vertices.

## Proof

**Step 1: Convexity collapses to distance-two packing.** The antiprism has the triangles \((a_i,a_{i+1},b_i)\) and \((a_i,b_i,b_{i-1})\) for every \(i\). Each edge is in at least one of these triangles, and their edge-sharing adjacency graph is connected: consecutive upper triangles communicate through intervening lower triangles, and likewise around the ring. If two selected vertices are adjacent, they belong to one triangle, whose third vertex must also be selected in any convex set. Since any two vertices of a fully selected triangle are selected, convexity forces all vertices of each neighbouring triangle, propagating through the entire connected triangle family. If two selected vertices instead have distance exactly two, their common middle vertex is either already selected (giving an adjacent selected pair) or is forced into the convex set, again giving an adjacent pair. Thus any convex set other than the entire graph has all selected vertices mutually at distance at least three. Conversely, a distance-two packing has at most one selected neighbour at each outside vertex and hence is convex. This includes the empty packing.

**Step 2: Local gap criterion.** A packing chooses at most one of \(a_i,b_i\) at each cyclic index, since these two vertices are adjacent. Encode the positions as a cyclic ternary word on \(0,A,B\). For successive occupied indices in cyclic order, write \(d\) for the positive gap in indices. Gaps \(d=1\) are forbidden because every vertex in column \(i\) is at distance at most two from every vertex in column \(i+1\). For a gap \(d=2\), the only possible ordered pair is \((A,B)\): among the four pairs \((a_i,a_{i+2})\), \((a_i,b_{i+2})\), \((b_i,a_{i+2})\), \((b_i,b_{i+2})\), only \((a_i,b_{i+2})\) has distance at least three along that forward arc. If \(d\ge3\), no forbidden pair is created along the arc (every edge changes the cyclic index by at most one); any wrap-around short route appears in the *other* successive gap and is checked there. Since a graph walk of length at most two changes its index through at most two consecutive steps, every forbidden pair in an occupied word is detected by one of its successive cyclic gaps. This also handles two occupied sites, whose two directed gaps must *both* satisfy the criterion. A singleton occupancy gives both possible colours at any index. Therefore the criterion is necessary and sufficient: every successive gap is at least two, and a gap of exactly two is permitted only from \(A\) to \(B\).

**Step 3: Exact cyclic generating function.** Put
\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
R(t)=t^2 E+\frac{t^3}{1-t}J.
\]
The entries of \(R\) count permitted consecutive occupied sites, the row and column indicating their respective \(A,B\) labels. A cyclic word with \(k\ge1\) occupied sites and total length \(n\) gives a closed walk of length \(k\) in this two-state weighted transition matrix. There are \(n\) choices for a marked first index, and exactly \(k\) choices for which occupied site was marked. Consequently, its exact labelled count is
\[
\frac{n}{k}[t^n]\operatorname{tr}\bigl((zR(t))^k\bigr).
\]
This identity also applies to singletons because \(\operatorname{tr}(E)=0\) and \(\operatorname{tr}(J)=2\). Summing over \(k\) and using the formal matrix identity \(-\log\det(I-X)=\sum_{k\ge1}\operatorname{tr}(X^k)/k\), the desired packing series is
\[
-t\frac{\partial}{\partial t}\log\det\bigl(I-zR(t)\bigr).
\]
A direct determinant calculation gives
\[
\det\bigl(I-zR(t)\bigr)
=1-\frac{2zt^3+z^2t^5}{1-t}.
\]
Differentiating and simplifying yields exactly the displayed rational function. Add back the empty and full sets to obtain \(C_n(z)\).

**Step 4: Sharp largest proper set.** In a cyclic word with \(k\ge2\) occupied indices, every gap contributes at least two, and every gap of length two must be an \(A\)-to-\(B\) transition. Such length-two gaps cannot be consecutive: after its terminal \(B\) another length-two gap would require it to be \(A\). Hence at most \(\lfloor k/2\rfloor\) gaps have length two, and the other gaps have length at least three. Necessarily
\[
n\ge 2\lfloor k/2\rfloor+3\lceil k/2\rceil
=\lceil5k/2\rceil,
\]
so \(k\le\lfloor2n/5\rfloor\). Conversely, for any \(k\ge2\) with \(\lceil5k/2\rceil\le n\), choose \(\lfloor k/2\rfloor\) nonconsecutive length-two gaps, label each of them \(A\)-to-\(B\), give all other gaps length three, and distribute the remaining \(n-\lceil5k/2\rceil\) units arbitrarily to a length-three gap. The resulting cyclic word is admissible, establishing equality at \(k=\lfloor2n/5\rfloor\). For \(n=3,4\) the maximal size is one, provided by any singleton. Therefore the formula holds for every \(n\ge3\).

## Verification

The reproducible standard-library checker `verify_antiprism.py` independently implements (i) the original outside-neighbour convexity test on all subsets of \(A_n\) for \(3\le n\le10\), (ii) distance-two packings via breadth-two neighbourhood exclusion, (iii) coefficient extraction from the rational generating function by recurrence, and (iv) direct enumeration of cyclic ternary words for \(3\le n\le12\). All these computations agree. Representative complete polynomials are
\[
C_5(z)=1+10z+5z^2+z^{10},\quad
C_8(z)=1+16z+56z^2+16z^3+z^{16},
\]
\[
C_{10}(z)=1+20z+110z^2+140z^3+5z^4+z^{20}.
\]
Run `python3 verify_antiprism.py` beside this file. The infinite result relies on the proof above, not on the finite checks.

## Relationship to prior work

Dourado, Grippo, Lin and Protti (2026) introduced a systematic counting framework for \(P_3\)-convex vertex sets, including complexity results and algorithms for general graphs and special graph classes. The theorem here determines a closed all-order, cardinality-refined enumerator on a distinct natural 4-regular planar graph family, together with a sharp proper-convex-set size formula. General algorithms for counting convex subsets do not themselves provide this rational bivariate expression or its two-colour gap classification. Standard distance-two packings are the independent sets of the square of a graph; the equivalence to nonfull convexity in this triangle-connected family is established explicitly here.

## Limitations

No claim is made about arbitrary maximal planar graphs, general circulant graphs or complete classifications beyond antiprisms. The result concerns vertex-labelled convex sets rather than automorphism orbit classes. Computations through bounded order are consistency tests, not substitutes for the proofs. Earlier work on graph-square independent sets or specialized convexity formulas not accessible to the searches might contain an equivalent expression; independent literature and mathematical verification have not been performed.

## References

1. M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first posted 2026-03-05), https://arxiv.org/abs/2603.04706.
2. R. Kuriakose, *Studies on Variations of Domination in Graphs* (2022), University of Calicut dissertation, Chapter 5 (related corona graph-convexity parameters), https://scholar.uoc.ac.in/bitstream/handle/20.500.12818/2412/1704_Reeja.pdf?sequence=1.
