# Gap-slack isometry and exact token-sliding distances for mutually visible triples on cycles

## Finding
Let \(C_n\) be the simple cycle on \(\mathbb Z_n\), and let \(F_k(C_n)\) be its \(k\)-token graph. For \(2\le k<n\) and an integer \(U\ge2\), write \(\mathcal G_{n,k,U}\) for the induced subgraph of \(F_k(C_n)\) on configurations whose \(k\) positive clockwise gaps between consecutive occupied vertices are all at most \(U\).

**Gap-slack isometry theorem.** If \(k<n<kU\), then \(\mathcal G_{n,k,U}\) is isometric in \(F_k(C_n)\): every two admissible configurations admit a shortest token-sliding path that remains admissible throughout. More precisely, for admissible \(S,T\), with \(s_j=\sum_{i=0}^{j}(\mathbf 1_S(i)-\mathbf 1_T(i))\),
\[
 d_{\mathcal G_{n,k,U}}(S,T)=d_{F_k(C_n)}(S,T)
 =\min_{c\in\mathbb Z}\sum_{j=0}^{n-1}|s_j-c|.
\]
An integer median of the \(n\) values \(s_j\) achieves the minimum; thus the distance can be found by one cumulative scan and selection of a median.

A triple of distinct vertices of \(C_n\) is mutually visible exactly when all three clockwise gaps are at most \(\lfloor n/2\rfloor\). Consequently, for **every \(n\ge3\)**, its three-token mutual-visibility reconfiguration layer \(\mathcal R_{\mathcal M}^3(C_n)\) is an isometric induced subgraph of \(F_3(C_n)\) with the same exact median-flow distance formula. This strengthens connectivity to exact preservation of all pairwise token-sliding distances.

The strict slack condition has a genuine boundary: \(\mathcal G_{6,3,2}\) has two isolated vertices, \(\{0,2,4\}\) and \(\{1,3,5\}\), which have distance three in \(F_3(C_6)\). Isometry does **not** mean every ambient geodesic is admissible: for \(C_5\), the visible triples \(\{0,2,4\}\) and \(\{0,1,3\}\) have an ambient length-two path through the nonvisible triple \(\{0,1,4\}\), but they also have a visible length-two path through \(\{0,2,3\}\).

## Assumptions and scope
All graphs are simple and unweighted. A token move replaces an occupied vertex with an adjacent unoccupied vertex. In \(F_k(C_n)\), vertices are all \(k\)-subsets of \(\mathbb Z_n\), with an edge precisely when one legal token move relates them. For \(S=\{x_1,\ldots,x_k\}\), list the occupied vertices clockwise and put \(g_i=x_{i+1}-x_i\) in positive cyclic integers, with \(x_{k+1}=x_1+n\). Then \(g_i\ge1\) and \(\sum_i g_i=n\). Membership in \(\mathcal G_{n,k,U}\) means \(g_i\le U\) for all \(i\). The theorem requires \(2\le k<n<kU\), not merely nonemptiness. A mutual-visibility set permits a shortest path between every two of its vertices whose internal vertices avoid the set. The visibility-layer corollary also includes the small case \(n=3\), where the triple layer has just one configuration.

## Proof
**1. Feasible lifted configurations.** Fix a clockwise labelling of the tokens. A lifted configuration is an increasing integer vector \(x=(x_1,\ldots,x_k)\) such that
\[
1\le x_{i+1}-x_i\le U\quad(1\le i<k),\qquad
1\le x_1+n-x_k\le U.
\]
Write \(\mathcal F\) for the set of such vectors. Coordinatewise minima and maxima of any two vectors in \(\mathcal F\) also belong to \(\mathcal F\). Indeed, each difference constraint is preserved by coordinatewise minimum and maximum: if both \(a-b\) and \(a'-b'\) lie in \([1,U]\), then the corresponding difference for \(\min(a,a')\), \(\min(b,b')\), or for the coordinatewise maxima, remains in \([1,U]\). The cyclic constraint is treated identically, since \(\min(a+n,b+n)=\min(a,b)+n\).

**2. Monotone interpolation.** If \(p,q\in\mathcal F\) satisfy \(p_i\le q_i\) for every \(i\), there is a path from \(p\) to \(q\) increasing one coordinate by one at each step, of length \(\sum_i(q_i-p_i)\). To prove this, suppose \(p\ne q\), put \(\delta_i=q_i-p_i\), let \(M=\max_i\delta_i>0\), and consider indices \(i\) with \(\delta_i=M\). Increasing \(p_i\) is illegal only if its preceding gap already equals \(U\) or its succeeding gap equals \(1\). At a preceding saturated gap, the feasibility of \(q\) forces \(\delta_{i-1}\ge\delta_i=M\); at a succeeding gap of length one, it forces \(\delta_{i+1}\ge\delta_i=M\). Thus, if no maximal-deficit coordinate can increase, direct an arrow from each maximal-deficit index to such a neighboring maximal-deficit index. A directed cycle results. On the ring, reversing direction across one gap would require that gap to equal both \(1\) and \(U\), impossible since \(U\ge2\). Any directed cycle without such a reversal traverses the entire ring uniformly; it would force **all** gaps of \(p\) to equal \(1\), or **all** to equal \(U\). Their sums would give \(n=k\) or \(n=kU\), contradicting \(k<n<kU\). (For \(k=2\), the two oppositely oriented gaps are treated separately and the same alternatives result.) Hence a legal increase exists. Repetition proves the assertion.

For general \(x,y\in\mathcal F\), their coordinatewise minimum \(z\) belongs to \(\mathcal F\); monotone paths \(z\to x\) and \(z\to y\) yield, after reversing the first one, an \(x\)-to-\(y\) path of exact length \(\sum_i|x_i-y_i|\). Each unit coordinate change is a legal token slide; no ordering or gap constraint is violated.

**3. Isometry.** A token-sliding path on a cycle cannot reverse the cyclic order of individually labelled tokens. Starting from a chosen lift \(x\) of \(S\), follow any ambient path to \(T\) and label its endpoint tokens by this conserved cyclic order. Their lifted terminal positions form some \(y\in\mathcal F\), obtained from a cyclic listing of \(T\) with an integer winding number. The path has at least \(\sum_i|x_i-y_i|\) moves. By Step 2, a path of exactly that length exists through admissible configurations. Replacing the original path proves \(d_{\mathcal G}(S,T)\le d_{F_k(C_n)}(S,T)\). The reverse inequality holds because \(\mathcal G\) is an induced subgraph, completing the isometry proof.

**4. Median-flow distance.** For any two \(k\)-subsets \(S,T\), orient cycle edge \(e_j\) clockwise from \(j\) to \(j+1\). If \(f_j\) denotes the net number of clockwise traversals of this edge in a token motion, conservation at each vertex gives \(f_j-f_{j-1}=\mathbf1_S(j)-\mathbf1_T(j)\), hence \(f_j=s_j-c\) for some integer \(c\). Every motion has at least \(\sum_j|f_j|\) steps. Choose \(c\) to be one of the observed median values of the \(s_j\) (for example, the lower middle order statistic); at least one edge then has zero net flow. Cut the cycle at such an edge. On the resulting path, match the \(k\) initially occupied positions and the \(k\) target positions in increasing order. Moving rightward targets from right to left and then leftward targets from left to right realizes that ordered matching without collisions, with exactly \(\sum_j|s_j-c|\) moves; the zero-flow cut edge is not used. Thus the minimum over \(c\) equals the ambient token-graph distance. Step 3 transfers this formula to \(\mathcal G\).

**5. Mutual visibility.** If a triple is listed clockwise with consecutive gap \(g_i\), the arc of length \(g_i\) between that consecutive pair has no other selected vertex internally, while the complementary arc contains the third selected vertex. Thus the pair has an avoiding geodesic precisely when \(g_i\le n-g_i\), that is, \(g_i\le\lfloor n/2\rfloor\). For \(n\ge4\), \(3\lfloor n/2\rfloor>n>3\), so Steps 1–4 apply with \(k=3\). For \(n=3\) the triple layer is a singleton and the metric identity is immediate. The boundary and nonconvexity examples follow by directly checking the specified triples and moves.

## Verification
Run `python verify_mv_isometry.py` (standard Python library only). This standalone verifier independently tests mutual visibility via both shortest clockwise and anticlockwise paths, rather than assuming the gap criterion. It constructs the full three-token graph and the visibility-induced graph, checks all ordered pairs of visible triples against independent breadth-first distances in both graphs, and checks the cumulative-median formula for every \(3\le n\le17\). It verifies 162,372 ordered pairs and separately checks the sharp saturation obstruction. It does not serve as an infinite proof; Steps 1–5 do.

## Relationship to prior work
Fresán-Figueroa, Goldfeder, and Lozano-Piña (arXiv:2610.24324v1, first posted 2026-10-16), Section 6, characterize mutually visible triples of cycles by their three gaps and prove that the associated token-sliding layer is connected. They do not provide isometric embedding into the ambient token graph or exact pairwise distances. The present result uses their natural configuration family and upgrades connectivity to metric preservation, with a general bounded-gap theorem.

Fabila-Monroy and coauthors, *Token Graphs* (arXiv:0910.4774v1, 2009; journal 2012), introduce token graphs and prove general connectivity/diameter bounds. Their results do not include this gap-constrained isometry theorem. The median-flow metric is a one-dimensional transport identity; the asserted new content is its guaranteed realization while every intermediate configuration remains gap-bounded. Equivalent older descriptions of constrained exclusion processes remain a historical-priority risk.

## Limitations
This is an existence theorem for a shortest admissible path, not a statement that **all** ambient shortest paths remain admissible. It concerns cycles and uniform upper bounds on clockwise gaps, not arbitrary graph hosts or heterogeneous gaps. The strict slack hypothesis is necessary in general, as shown by the two isolated saturated configurations. The finite verifier tests only the stated finite range. An independent mathematical audit and exhaustive historical-priority determination have not been performed.

## References
1. J. A. Fresán-Figueroa, I. A. Goldfeder, A. Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets*, arXiv:2610.24324v1, 2026-10-16, https://arxiv.org/abs/2610.24324 (especially Section 6).
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, arXiv:0910.4774v1, 2009-10-25; *Graphs and Combinatorics* 28 (2012), 365–380, https://arxiv.org/abs/0910.4774 (especially Sections 2–3).
3. S. Di Stefano, *Mutual visibility in graphs*, 2022, cited for the standard mutual-visibility definition and cycle maximum in reference 1.
