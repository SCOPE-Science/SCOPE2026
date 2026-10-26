# Sharp edge-space stability of Hodge projections on complete multipartite graphs

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be an unweighted complete multipartite graph, with \(r\ge2\) nonempty parts, positive integer part sizes, and \(N=\sum_i a_i\). Orient its edges arbitrarily and form the edge-to-vertex incidence matrix \(B\), the combinatorial vertex Laplacian \(L=BB^\top\), and the Euclidean edge-space projections
\[
P=B^\top L^\dagger B,\qquad Q=I-P.
\]
Thus \(P\) projects edge data onto gradients and \(Q\) onto divergence-free flows. Measure both as maps on the real coordinatewise maximum-norm edge space. Define, for integers \(1\le s<N\),
\[
F_{\kappa,N}(s)=\frac{s}{N}-\frac{\kappa(N-1)}{N(N-s)}.
\]
For an output edge connecting parts of sizes \(a\) and \(b\), **every absolute row sum is exact**:
\[
\sum_f|P_{ef}|=2+F_{2,N}(a)+F_{2,N}(b),\qquad
\sum_f|Q_{ef}|=3+F_{4,N}(a)+F_{4,N}(b).
\tag{1}
\]
Writing \(a_{(1)}\ge a_{(2)}\) for the two largest part sizes gives the sharp operator norms
\[
\boxed{\|P\|_{\infty\to\infty}=2+F_{2,N}(a_{(1)})+F_{2,N}(a_{(2)})},
\tag{2}
\]
\[
\boxed{\|Q\|_{\infty\to\infty}=3+\max_{i<j}\{F_{4,N}(a_i)+F_{4,N}(a_j)\}}.
\tag{3}
\]
The maximizing edge for \(P\) joins two largest parts; the maximizing edge for \(Q\) joins two parts with the largest **scores** \(F_{4,N}(a_i)\), which may instead be the smallest parts.

For every fixed \(2\le r\le N\), the unique part-size multiset maximizing \(\|P\|_{\infty\to\infty}\) is
\[
\left\{\left\lfloor\frac{N-r+2}{2}\right\rfloor,
\left\lceil\frac{N-r+2}{2}\right\rceil,
\underbrace{1,\ldots,1}_{r-2\ \mathrm{parts}}\right\}.
\tag{4}
\]
The corresponding exact maximum is (2) evaluated at the two displayed large parts, and for fixed \(r\) as \(N\to\infty\),
\[
\max\|P\|_{\infty\to\infty}=3-\frac{r+6}{N}+O_r(N^{-2}).
\tag{5}
\]
Always \(\|P\|_{\infty\to\infty}<3\) and \(\|Q\|_{\infty\to\infty}<4\), with both upper bounds asymptotically sharp. For the balanced bipartite graph \(K_{m,m}\),
\[
\|P\|_{\infty\to\infty}=3-\frac4m+\frac2{m^2},\qquad
\|Q\|_{\infty\to\infty}=4-\frac8m+\frac4{m^2}.
\tag{6}
\]
For the tripartite graph \(K_{N-2,1,1}\), \(N\ge4\),
\[
\|P\|_{\infty\to\infty}=2-\frac2N,\qquad
\|Q\|_{\infty\to\infty}=3-\frac6N,
\tag{7}
\]
and the \(Q\)-extremizing edge connects the **two singleton parts**, rather than the dominant part.

## Assumptions and scope
All graph edges have unit weight, each part is nonempty, \(r\ge2\), and all vector spaces and induced norms are real. Either edge orientation is allowed: changing orientation only changes the signs of rows and columns and leaves absolute row sums and operator norms unchanged. Here \(L^\dagger\) denotes the Moore–Penrose inverse, the usual graph gradient orientation is specified by \(B\), and \(\|A\|_{\infty\to\infty}=\max_e\sum_f|A_{ef}|\) for a finite real matrix. Each stated inequality concerns these particular orthogonal projections, not the optimal norm over all projections onto the same subspace. Part-size optimization holds for a fixed number of vertices \(N\) and parts \(r\), with \(2\le r\le N\).

## Proof
**1. A two-source Green potential.** Fix an output edge \(e=(u,v)\) joining distinct parts \(A\), \(C\) of sizes \(a,b\). Put
\[
p=\frac1{N(N-a)},\quad q=\frac1{N(N-b)},\quad
U=\frac1N+(a-1)p,\quad V=\frac1N+(b-1)q.
\]
Define a vertex potential \(\phi\) by \(\phi_u=U\), \(\phi_x=-p\) at the other \(a-1\) vertices of \(A\), \(\phi_v=-V\), \(\phi_y=q\) at the other \(b-1\) vertices of \(C\), and \(\phi=0\) outside \(A\cup C\). Its sum on \(A\) is \(1/N\), its sum on \(C\) is \(-1/N\), and its total sum is zero. For a zero-mean potential on a complete multipartite graph, at a vertex \(z\) in a part of size \(s\),
\[
(L\phi)_z=(N-s)\phi_z+\sum_{y\text{ in the same part}}\phi_y.
\]
Substituting the displayed values gives \(L\phi=\delta_u-\delta_v\). Connectivity and mean zero therefore imply \(\phi=L^\dagger(\delta_u-\delta_v)\). For every input edge \(f=(x,y)\), the projection-matrix entry is \(P_{ef}=\phi_x-\phi_y\), with the chosen edge orientations.

**2. Exact absolute row counts.** Let \(c=N-a-b\) be the number of vertices outside the two selected parts. Since \(q\le1/N\le U\) and \(p\le1/N\le V\), every absolute value is resolved by the potential's explicit ordering. Separate edges linking (i) \(u\) and \(v\), (ii) \(u\) to the other \(b-1\) vertices of \(C\), (iii) the other \(a-1\) vertices of \(A\) to \(v\), (iv) the remaining \((a-1)(b-1)\) cross edges, and (v) edges from \(A\cup C\) to the \(c\) outside vertices. Edges between two outside parts contribute zero. The absolute \(P\)-row sum is exactly
\[
\begin{aligned}
S_P={}&(U+V)+(b-1)(U-q)+(a-1)(V-p)\\
 &+(a-1)(b-1)(p+q)\\
 &+c\,[U+(a-1)p+V+(b-1)q].
\end{aligned}
\]
Elementary simplification yields
\[
S_P=2+\frac{a+b}{N}-2R,
\qquad
R=P_{ee}=U+V=\frac{N-1}{N}\left(\frac1{N-a}+\frac1{N-b}\right).
\tag{8}
\]
The edge resistance \(R\) is between zero and one: \(P\) is an orthogonal projection, and \(R=\langle P\delta_e,\delta_e\rangle\in[0,1]\). For \(f\ne e\), \(Q_{ef}=-P_{ef}\); on the diagonal \(Q_{ee}=1-R\). Thus
\[
S_Q=S_P+1-2R.
\]
Inserting (8) establishes both identities in (1). Maximizing an absolute row sum gives (3) immediately.

**3. Largest parts optimize the gradient projection.** For \(a\ge b\), a direct factorization shows
\[
F_{2,N}(a)-F_{2,N}(b)=
\frac{(a-b)[(N-a)(N-b)-2(N-1)]}{N(N-a)(N-b)}.
\tag{9}
\]
When \(r\ge3\), any two distinct parts satisfy \(a+b\le N-1\), so \((N-a)(N-b)\ge 2(N-1)\). Hence the sign in (9) is nonnegative, and part sizes and their \(F_{2,N}\)-scores have the same weak order. For \(r=2\) there is only one pair. This proves (2), including the attaining edge.

**4. Unique fixed-size optimizer.** Consider \(F_{2,N}\) on \((0,N)\); direct differentiation gives \(F_{2,N}''(s)<0\), so the sum of its values at two positive integers with fixed sum is uniquely maximized (up to interchange) by the most balanced split. Let
\[
h_N(t)=F_{2,N}(\lfloor t/2\rfloor)+F_{2,N}(\lceil t/2\rceil).
\]
For \(2\le t<N\), its successive increments are increments of \(F_{2,N}\) at \(k=\lfloor t/2\rfloor\). Exactly,
\[
F_{2,N}(k+1)-F_{2,N}(k)
=\frac{(N-k)(N-k-1)-2(N-1)}{N(N-k)(N-k-1)}\ge0
\]
when \(k\le\lfloor(N-2)/2\rfloor\). These increments are strictly positive except at \(N=4,k=1\). If \(r\ge3\), the sum of the two largest parts is at most \(N-r+2\le N-1\); choosing all other parts singleton makes this sum maximal, and balancing the largest two makes the \(F_{2,N}\)-sum maximal. Uniqueness follows from strict concavity and the positive increments, including the exceptional \(N=4\) case where the fixed part-count constraint leaves only the displayed maximizing multiset. For \(r=2\) the two parts already sum to \(N\), and strict concavity gives the same balancing conclusion. The statement (4) follows. Expanding the two \(F_{2,N}\) terms at these balanced sizes for fixed \(r\) yields (5).

**5. Universal upper bounds and contrasting edges.** The fixed-\(r\) maximum in (4) is at most the balanced bipartite maximum at the same \(N\); inserting its even or odd balanced integer parts into (2) gives a quantity strictly below \(3\). Every \(P\)-row sum is therefore strictly below \(3\). Since \(R>0\), equation (8) gives \(S_Q=S_P+1-2R<4\). Formula (6) proves that both bounds are sharp as limiting supremums. For \(K_{N-2,1,1}\), the two part-score values for \(Q\) are \(F_{4,N}(N-2)=-1\) and \(F_{4,N}(1)=-3/N\); their pairwise comparison selects the singleton-to-singleton edge for \(N\ge4\), proving (7).

## Verification
The accompanying self-contained Python 3 script `verify.py` performs exact-rational grounded-Laplacian inversion and constructs both full projection matrices independently of the closed forms. For all integer multipartite part partitions of \(2\le N\le10\), it verifies the claimed entries, every absolute row sum, the sharp \(P\) and \(Q\) norms, symmetry, a projection-matrix identity, and the fixed-part-count upper bound. The completed run reported `MULTIPARTITE_GRADIENT_EXACT_OK 174858 configurations 128 edge_rows 2926`. Those finite computations corroborate, but do not replace, the all-size algebraic proof given above. Run `python3 verify.py` with only the Python standard library.

## Relationship to prior work
Jiang, Lim, Yao and Ye (2008) describe the orthogonal graph Hodge/gradient decomposition for ranking data, establishing the underlying \(L^2\) geometry. Kassel and Wu (2013) give the related transfer-current / Green-kernel representation. The new statement does not claim originality for the formula \(P=B^\top L^\dagger B\) or for Hilbert-space norm-one contractivity. Its subject is the **exact induced edge-coordinate maximum norm** for complete multipartite graphs, the two competing edge types for gradient and circulation projection, and the fixed-part-count sharp maximizers. No theorem implying these exact quantities was located in the sections of the two primary texts inspected.

Adjacent exact findings in finite metric geometry concern the Euclidean inradius of complete multipartite symmetric edge polytopes, the Euclidean distortion of complete bipartite transportation spaces, or optimized projections in clustered Lipschitz-free spaces. Those objects are different from the *canonical orthogonal edge-flow projector* here; their sharp constants do not algebraically determine (1)–(7). Previous exact computations on theta networks, wheels, and weighted Boolean cubes concern other graph classes, and the prior complete-multipartite biharmonic-heat result concerns an unrelated semigroup. This is a best-knowledge source comparison, not a proof of global bibliographic uniqueness.

## Limitations
The graph must be simple, finite, connected, complete multipartite, and unweighted. The theorem does not give these constants for arbitrary graphs or heterogeneous conductances. The maximum in (3) is a simple score comparison; no monotonicity in part size is asserted for the circulation projector. No independent mathematical review or complete historical-priority certification has occurred. Older electrical-transfer-impedance literature could express an equivalent computation using different terminology.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, first publicly posted 2008-11-07, https://arxiv.org/abs/0811.1067.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first publicly posted 2013-12-10, https://arxiv.org/abs/1312.2946.
