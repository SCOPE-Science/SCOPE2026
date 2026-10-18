# Sharp spread and Euclidean incenter freedom for triangular-graph Lipschitz-free spaces

## Finding
Let \(n\ge5\), let \(J(n,2)\) be the graph of two-element subsets of \([n]\), with adjacency when two subsets intersect, and use its unit-edge shortest-path metric. Set \(N=\binom n2\). On the zero-sum Euclidean space \(H=\{x\in\mathbb R^N:\sum_Ax_A=0\}\), equip \(H\) with the real Lipschitz-free transportation norm of that metric; write \(P_n\) for its unit ball.

**Theorem.** The exact Euclidean inradius of \(P_n\) is
\[
r_n=\left(\frac{n-2}{n}\left\lfloor\frac{n^2}{4}\right\rfloor\right)^{-1/2}.
\]
Exactly
\[
T_n=\begin{cases}\binom{n}{n/2},&n\text{ even},\\2\binom{n}{(n-1)/2},&n\text{ odd}\end{cases}
\]
facets touch the Euclidean ball \(r_n B_2\) centered at zero. Their centered supporting normals are **precisely** the distinct functions
\[
f^{S}_{\{i,j\}}=\mathbf1_S(i)+\mathbf1_S(j)-\frac{2|S|}{n},
\qquad |S|\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}.
\]
The complete set of centers of Euclidean balls of maximal radius in \(P_n\) has affine dimension
\[
\boxed{N-n=\frac{n(n-3)}2}.
\]
Equivalently, if a uniformly selected vertex \(A\) of the graph is used to define graph spread, the sharp variance over all real \(1\)-Lipschitz graph functions is
\[
\operatorname{spread}(J(n,2))
=\frac{2(n-2)\lfloor n^2/4\rfloor}{n^2(n-1)}.
\]
All variance maximizers, up to adding constants, are exactly the functions \(f^S\) in the displayed class. Thus their counts and equality cases are determined, not just the extremal value.

## Assumptions and scope
All scalars are real. The Euclidean structure is the **canonical zero-sum coordinate** inner product on signed masses indexed by unordered pairs, not the basepoint coordinate structure and not a Banach–Mazur-optimized ellipsoid. An edge of \(J(n,2)\) has metric length one; disjoint pairs of vertices have distance two. The result applies to every integer \(n\ge5\), with no asymptotic qualification.

If \(Q_n=\{f\in H:|f_A-f_B|\le1\text{ when }A,B\text{ intersect}\}\), then \(Q_n=P_n^\circ\) relative to \(H\). Accordingly the origin-centered inradius is the reciprocal of \(\max_{f\in Q_n}\|f\|_2\). Central symmetry shows that an origin-centered ball attains the globally largest Euclidean radius: averaging any contained balls of radius \(r\) centered at \(c\) and \(-c\) gives the same-radius ball centered at zero.

## Proof
**1. Reduction to integer Lipschitz potentials.** Pin one graph vertex's potential to zero. The graph-edge difference constraints have an oriented incidence matrix, which is totally unimodular, and integer right-hand sides. Hence every vertex of the bounded Lipschitz polytope has integral coordinates. The squared norm of the centered potential, \(\sum_A(f_A-\overline f)^2\), is strictly convex modulo constants. Therefore every maximizer is an integral polytope vertex. Since \(J(n,2)\) has diameter two, subtracting its minimum makes such a potential take its values in \(\{0,1,2\}\). If it uses only \(0\) and \(1\), its squared centered norm is at most \(N/4\), strictly below the value claimed for \(n\ge5\).

**2. Separating the low and high edges.** Suppose both levels zero and two occur. Regard graph vertices as edges of \(K_n\). Let \(a\) be the number of edges assigned zero and \(b\) the number assigned two. No zero-edge can meet a two-edge, by the Lipschitz condition. Thus the unions of their endpoints are disjoint subsets of \([n]\). Let their sizes be \(s,t\ge2\); after reversing the potential assume \(s\ge t\). Then \(s+t\le n\), \(a\le A=\binom s2\), and \(b\le B=\binom t2\). The squared centered norm depends only on \(a,b\):
\[
V(a,b)=a+b-\frac{(a-b)^2}{N}.
\]

**3. Sharp bound for the large and small endpoint sets.** If \(t\ge n/4\), the partial derivatives of the concave quadratic \(V\) at \((A,B)\) obey
\[
\partial_aV(A,B)=1-\frac{2(A-B)}N\ge0,
\qquad\partial_bV(A,B)=1+\frac{2(A-B)}N>0.
\]
By the supporting-plane inequality for a concave function, \(V(a,b)\le V(A,B)\). Put \(A'=\binom{n-t}{2}\). Since \(s\le n-t\), and \(\partial_aV(A',B)=4t/n-1\ge0\), monotonicity on \([A,A']\) yields
\[
V(a,b)\le V(A,B)\le V(A',B)
=\frac{n-2}{n}t(n-t)
\le\frac{n-2}{n}\left\lfloor\frac{n^2}4\right\rfloor.
\]
Each inequality is strict unless all zero and two edges within their respective endpoint sets occur, their endpoint sets partition \([n]\), and their sizes are as balanced as possible. (Even if a displayed derivative vanishes at its upper endpoint, the negative definite quadratic change along that coordinate makes a proper decrease strict.)

If \(t<n/4\), then \(n\ge9\). Writing \(d=a-b\), completing the square gives
\[
V(a,b)=2b+d-\frac{d^2}N\le2b+\frac N4
\le t(t-1)+\frac N4
<\frac{n^2}{16}+\frac{n(n-1)}8
<\frac{n-2}{n}\left\lfloor\frac{n^2}4\right\rfloor.
\]
The final strict inequality holds for every integer \(n\ge9\), by \(\lfloor n^2/4\rfloor\ge(n^2-1)/4\). Hence an optimizer necessarily falls into the balanced equality case of the previous paragraph.

**4. Construction and uniqueness of maximizers.** Conversely, let \(S\sqcup S^c=[n]\) be a balanced partition. Assign the value two to a pair contained in \(S\), zero to a pair contained in \(S^c\), and one to a crossing pair. Adjacent pairs cannot differ in value by two, so this is a \(1\)-Lipschitz function. Its squared centered norm is precisely \(\frac{n-2}{n}|S|(n-|S|)\). The analysis above proves these and only these functions maximize. Centering their entries produces exactly \(f^S\). The strict convexity in step 1 also implies that each maximizer is a vertex of \(Q_n\), so each indexes a genuine distinct facet of \(P_n\); distinct choices \(S\) give distinct centered vectors.

**5. Contact count and the dimension of all optimal centers.** For even \(n\), the balanced choices are precisely the \(\binom n{n/2}\) subsets of half size. For odd \(n\), both complementary sizes occur, giving \(2\binom n{(n-1)/2}\) distinct choices. This establishes \(T_n\).

Let \(W\) be the span in \(H\) of all \(f^S\). The operator mapping \(h\in\mathbb R^n\) to \(((h_i+h_j)/2)_{i<j}\), followed by removal of the mean, maps each centered indicator \(\mathbf1_S-(|S|/n)\mathbf1\) to a scalar multiple of \(f^S\). For any fixed balanced cardinality \(k\), differences of indicators of size-\(k\) subsets obtained by exchanging one element span the \((n-1)\)-dimensional zero-sum subspace in \(\mathbb R^n\). The displayed operator is injective on it: if \(h_i+h_j=0\) for every pair, all \(h_i\) vanish (\(n\ge3\)). Hence \(\dim W=n-1\).

An optimal-radius ball with center \(c\) must satisfy both antipodal inequalities at every maximally long normal, forcing \(\langle c,f^S\rangle=0\); thus \(c\in W^\perp\cap H\). Conversely, there are only finitely many other vertex normals and each has strictly smaller norm. Their inward-shifted inequalities consequently have positive slack at \(c=0\). Therefore a small relative Euclidean neighborhood of zero in \(W^\perp\cap H\) consists of optimal-radius centers. Its affine dimension is \((N-1)-(n-1)=N-n\).

## Verification
A self-contained Python 3 standard-library program, `verify_triangular_inballs.py`, exhaustively checks all integral admissible potential classes for \(n=4,5,6\), including their exact maximizer sets; it also checks every balanced contact normal and its exact rational span rank for \(n=4,5,6,7,8\). Reproduction: `python verify_triangular_inballs.py`. Its expected final message is `ALL EXACT TRIANGULAR-GRAPH TESTS PASSED`. The infinite statements are proved in steps 1–5; the finite enumerations are independent checks, not a substitute for those steps.

For example, the theorem gives \(r_5=\sqrt{5/18}\) with \(20\) tangent facets and a five-dimensional center locus; \(r_6=1/\sqrt6\), \(20\) tangent facets, and a nine-dimensional center locus; \(r_7=\sqrt{7/60}\), \(70\) tangent facets, and a fourteen-dimensional center locus.

## Relationship to prior work
The representation of a finite transportation unit ball as the convex hull of normalized molecules and its polarity with the Lipschitz ball are established facts, discussed by Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, first public 2019-11-24). Ostrovska and Ostrovskii (arXiv:2112.02689, first public 2021-12-05) study the isometric Banach-space structure of finite transportation cost spaces and graph-cycle quotients. The graph-spread statistic as a maximum Lipschitz-function variance predates both papers (e.g. Addario-Berry, Janson and McDiarmid, arXiv:0902.1156).

None of these general constructions supplies the explicit triangular-graph extremal inequality or its complete equality and incenter classification. The classical complete-multipartite inradius formulas also do not apply to \(J(n,2)\) once \(n\ge5\).

## Limitations
This theorem treats the precise canonical Euclidean inner product, not an optimal affine ellipsoid or arbitrary weighted Johnson graphs. It determines the dimension and necessary linear equations of the full maximal-center set, but does not give its complete face lattice or volume. No claim of an exhaustive worldwide novelty search or independent external audit is made. The case \(n=4\) is included in the checker as a boundary case but not claimed as the new infinite-family result: that graph is complete tripartite and has other descriptions.

## References
1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public 2019-11-24. https://arxiv.org/abs/1911.10642
2. S. Ostrovska and M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689, first public 2021-12-05, primary MSC 46B04. https://arxiv.org/abs/2112.02689
3. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first public 2009-02-06. https://arxiv.org/abs/0902.1156
