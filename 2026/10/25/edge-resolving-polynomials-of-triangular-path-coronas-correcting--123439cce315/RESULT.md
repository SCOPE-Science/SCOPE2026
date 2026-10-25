# Edge-resolving polynomials of triangular path coronas: correcting a constant-dimension claim

## Finding
For each integer \(n\ge2\), start with the path \(u_0u_1\cdots u_{n-1}\), and for each path edge \(u_iu_{i+1}\) add a new vertex \(w_i\) adjacent to both endpoints, keeping the original edge. Write \(H_n=P_n\diamond K_1\). An edge-resolving set is a set \(S\subseteq V(H_n)\) for which distinct edges \(e,f\) have different distance vectors \((d(s,e))_{s\in S}\), where \(d(s,xy)=\min\{d(s,x),d(s,y)\}\). Let \(E_n(z)=\sum_{S\text{ edge-resolving}}z^{|S|}\).

For \(n\ge4\), define \(m=n-1\) and the auxiliary graph \(F_n\) with vertex set \(\{u_0,u_m,w_0,\ldots,w_{m-1}\}\), the path edges \(w_iw_{i+1}\) for \(0\le i\le m-2\), and two terminal triangles \(\{u_0,w_0,w_1\}\) and \(\{u_m,w_{m-2},w_{m-1}\}\). **The complete structural criterion** is
\[
\boxed{S\text{ resolves every edge of }H_n\iff S\cap V(F_n)\text{ is a vertex cover of }F_n.}
\]
The \(n-2\) interior original-path vertices are optional and contribute a factor \((1+z)^{n-2}\). Define path independence polynomials \(P_{-1}(t)=P_0(t)=1\), \(P_1(t)=1+t\), and \(P_j(t)=P_{j-1}(t)+tP_{j-2}(t)\) for \(j\ge2\). Then, for every \(n\ge4\),
\[
\boxed{E_n(z)=(1+z)^{n-2}z^{n+1}\left[P_{n-1}(1/z)+\frac{2}{z}P_{n-3}(1/z)+\frac1{z^2}P_{n-5}(1/z)\right].}
\]
The negative index \(-1\) in the last term when \(n=4\) is defined above. The small cases are \(E_2(z)=3z^2+z^3\) and \(E_3(z)=(1+z)z^3(4+z)\). In particular,
\[
\boxed{\operatorname{edim}(H_n)=\left\lceil\frac n2\right\rceil+1\quad(n\ge3),}
\]
and the number of smallest edge-resolving sets is \(2(n-1)\) for odd \(n\ge3\), and \(4\) for even \(n\ge4\); for \(n=2\), the minimum size is two and there are three minimum sets.

This corrects the assertion \(\operatorname{edim}(P_n\diamond K_1)=2\) for \(n\ge3\) in Theorem 3.4 of Korivand, Khashyarmanesh and Tavakoli (2023); already \(\operatorname{edim}(H_3)=3\), while the error grows linearly in \(n\). The previously stated mixed metric dimension is not contested or claimed new.

## Assumptions and scope
All graphs are finite, simple and labeled by the displayed vertices. The index \(i\) ranges through \(0,\ldots,m-1\); denote the three edges in triangle \(i\) by \(A_i=u_iu_{i+1}\), \(L_i=u_iw_i\), and \(R_i=u_{i+1}w_i\). End vertices of the path are \(u_0,u_m\). An independent set of \(F_n\) is the complement of an ordinary vertex cover. The theorem concerns **edge** metric dimension, not ordinary vertex metric dimension or mixed metric dimension.

## Proof
**1. Explicit distance calculation.** For any tip landmark \(w_j\), with \(0\le i,j<m\), direct shortest-path inspection gives
\[
\begin{array}{c|ccc}
 &j<i&j=i&j>i\\\hline
 d(w_j,A_i)&i-j&1&j-i\\
 d(w_j,L_i)&i-j&0&j-i+1\\
 d(w_j,R_i)&i-j+1&0&j-i
\end{array}
\]
Also the two endpoint landmarks have profiles
\[
\begin{array}{c|ccc}
&A_i&L_i&R_i\\\hline
 d(u_0,\cdot)&i&i&i+1\\
 d(u_m,\cdot)&m-1-i&m-i&m-1-i
\end{array}.
\]
Every profile follows from the fact that all movement between blocks follows the original path; every off-path tip is one edge from its incident path endpoints.

**2. Necessity of the cover constraints.** For each consecutive tip pair \(w_i,w_{i+1}\), the edges \(R_i\) and \(L_{i+1}\) are separated *only* by the landmarks \(w_i,w_{i+1}\). Moreover, \(A_0,R_0\) are separated only by \(u_0,w_0\), and \(A_0,L_1\) only by \(u_0,w_1\). Reflecting the path yields the symmetric constraints \(u_mw_{m-1}\) and \(u_mw_{m-2}\). Thus every edge resolver meets every auxiliary edge. When \(n=3\), direct use of the same profiles shows the six pairs of vertices in \(\{u_0,u_2,w_0,w_1\}\) are compulsory witness pairs; they form \(K_4\). When \(n=2\), the three graph edges enforce the three vertex-cover constraints of \(K_3\).

**3. Sufficiency via all distinguishing sets.** For two distinct edges \(e,f\) of \(H_n\), let \(W(e,f)=\{v:d(v,e)\ne d(v,f)\}\). A set that covers \(F_n\) necessarily intersects \(W(e,f)\) whenever \(W(e,f)\) contains both endpoints of an edge of \(F_n\). The distance table proves this containment for every edge pair, as follows.

If among \(w_0,\ldots,w_{m-1}\) there are two **consecutive** distinguishing tips, their path edge in \(F_n\) proves the assertion. It remains to compare pairs for which the distinguishing-tip indices contain no consecutive integers. For \(m\ge5\), substitution of the three piecewise affine rows in step 1, splitting according to whether the tip index lies left of, at, between, or right of the blocks of \(e,f\), yields exactly the following six unordered edge pairs:
\[
\begin{array}{c|c|c}
\{e,f\}&\{j:w_j\in W(e,f)\}&\text{additional witness}\\\hline
\{A_0,R_0\}&\{0\}&u_0\\
\{A_0,L_1\}&\{1\}&u_0\\
\{A_1,L_2\}&\{0,2\}&u_0\\
\{R_{m-3},A_{m-2}\}&\{m-3,m-1\}&u_m\\
\{R_{m-2},A_{m-1}\}&\{m-2\}&u_m\\
\{A_{m-1},L_{m-1}\}&\{m-1\}&u_m
\end{array}.
\]
In each row the indicated endpoint and one of the displayed tips form an edge of \(F_n\). To verify that the table is exhaustive, fix the edge types in \(\{A,L,R\}^2\), suppose their block indices satisfy \(i\le k\), and substitute each of the five ranges \(j<i\), \(j=i\), \(i<j<k\), \(j=k\), \(j>k\). Within each open range the difference of the two distances is affine in \(j\). If its nonzero support has length at least two, that range supplies consecutive witnesses; otherwise its nonzero entries are confined to the displayed adjacent-block boundary configurations. For \(m\ge5\), these resolve to exactly the six table rows. Thus no unlisted pair can evade a path witness edge.

For the finite overlapping-boundary cases \(m=2,3,4\), substitute the same formulas and check all \(3m\choose2\) pairs directly. The resulting distinguishing sets either contain an auxiliary edge or, for \(m=2\), contain an edge of \(K_4\) on the four relevant vertices. The standalone exact verifier enumerates **every** vertex subset in these cases and independently checks the criterion against the original distance definition. This proves sufficiency and completes the necessary-and-sufficient characterization for all \(n\ge2\).

**4. Counting.** For \(n\ge4\), ignore the \(n-2\) free original vertices. To count independent sets in \(F_n\), first choose an independent subset of the tip path \(w_0\ldots w_{m-1}\) (generating function \(P_m(t)\)). Choosing the left endpoint \(u_0\) additionally forbids \(w_0,w_1\), giving \(tP_{m-2}(t)\); choosing \(u_m\) gives the same term. Choosing both forbids the first two and last two tips, giving \(t^2P_{m-4}(t)\) (for \(m=3\), the entire tip path is forbidden and \(P_{-1}=1\)). Hence the independence polynomial is \(J_m(t)=P_m(t)+2tP_{m-2}(t)+t^2P_{m-4}(t)\). Complementation converts independent sets into covers with polynomial \(z^{m+2}J_m(1/z)\); the free interior path vertices contribute \((1+z)^{m-1}\). The small cases follow similarly from \(F_2=K_3\) and \(F_3=K_4\).

Finally the standard path independent-set coefficient is \([t^r]P_k(t)=\binom{k-r+1}{r}\). Substituting it in \(J_m\) shows \(\deg J_m=\lfloor n/2\rfloor\), with leading coefficient \(4\) when \(n\ge4\) is even and \(2(n-1)\) when \(n\ge5\) is odd. The special \(n=3\) coefficient is four. Subtracting the independence number from \(|V(F_n)|=n+1\) proves the minimum cardinality and the basis counts; free interior vertices cannot belong to a minimum basis.

## Verification
Run `python3 verify_edge.py` from the extracted package. Its BFS distances are calculated directly from constructed adjacency lists; resolving sets are tested by comparing the complete list of edge-distance signatures, **not** by using the auxiliary cover lemma. Independently, the code constructs \(F_n\), tests every vertex subset for \(2\le n\le9\) (\(174{,}760\) subsets), and compares the full distribution with the formula. For \(4\le n\le14\), it independently identifies all pairs of edges whose set of distinguishing landmarks has cardinality two; precisely the auxiliary edges arise. Finally, \(61\) parameter values up to \(n=64\) independently check minimum degree and optimal multiplicity through exact coefficient arithmetic. Recorded output is `verify_edge.out`. These tests are finite; the general result depends on the explicit distance calculation and case analysis above.

## Relationship to prior work
Korivand, Khashyarmanesh and Tavakoli, *Mixed metric dimension over (edge) corona products*, published online 18 December 2023, Theorem 3.4, state \(\operatorname{edim}(P_n\diamond K_1)=2\) for \(n\ge3\) in addition to the separate mixed-dimension statement. Their proposed tip-endpoint pair does not always resolve edges. Already for \(n=3\), the two original path edges have the same edge distances from both tips; in fact no two landmarks suffice. The present finding proves the corrected dimension, classifies **all** edge-resolving sets, and enumerates them by cardinality. The earlier mixed-dimension result, also consistent with general block-graph literature, is not new here. The 2016 foundational edge metric dimension work sets the underlying definition, and existing calculations for unrelated lollipop, half, crown and multipartite graphs do not imply this classification on the path edge-corona family.

## Limitations
Only edge-coronas of paths with a single attached vertex per edge are treated. The claim does not concern general edge coronas, mixed resolving sets, or other snake graphs. Bibliographic and mathematical-record searches do not establish absolute novelty; an unindexed correction or an equivalent triangular-snake enumeration remains a priority risk. The algebraic boundary-case table is a finite comparison using the displayed formulas, corroborated computationally for multiple sizes; independent mathematical validation has not been performed.

## References
1. M. Korivand, K. Khashyarmanesh and M. Tavakoli, *Mixed metric dimension over (edge) corona products*, AKCE International Journal of Graphs and Combinatorics 21 (2024), 129–134, published online 18 December 2023, Theorem 3.4; DOI:10.1080/09728600.2023.2291465 (author-supplied full text and open journal full text inspected).
2. A. Ghalavand, S. Klavžar and M. Tavakoli, *Graphs whose mixed metric dimension is equal to their order*, arXiv:2305.19620 (2023), Corollary 3.2 (full PDF inspected; mixed, not edge, metric dimension).
3. A. Kelenc, N. Tratnik and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, Discrete Applied Mathematics 251 (2018), 204–220, arXiv:1601.05416 (foundational definition).
