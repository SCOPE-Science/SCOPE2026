# Sharp endpoint cut–cycle norms on categorical products of complete graphs

## Finding
For every pair of integers \(a,b\ge3\), let \(G=K_a\times K_b\) be the **categorical** graph product: its vertices are pairs \((i,j)\), and two vertices are adjacent precisely when both coordinates differ. Orient edges arbitrarily, equip the real edge space with its standard Euclidean inner product, let \(Q\) be the orthogonal projection onto gradients (the cut space), and let \(P=I-Q\) be its cycle-space complement. Put
\[
B_{a,b}=\frac{2(a^2b^2-a^2-b^2-6ab+5a+5b-3)}{ab(a-1)(b-1)},\qquad
R_{a,b}=\frac{2|a-b|(2ab-4a-4b+9)}{ab(a-1)(b-1)(ab-a-b)}.
\]
Then the exact induced endpoint operator norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=B_{a,b}+R_{a,b}},
\qquad
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=B_{a,b}+R_{a,b}+1-\frac{4(ab-1)}{ab(a-1)(b-1)}}.
\]
Every edge column attains the relevant norm. The imbalance term \(R_{a,b}\) is strictly positive exactly when \(a\ne b\); it comes from a reversal of electrical-current signs when the coordinate sizes cross.

There are also sharp **global** bounds, with suprema over integer \(a,b\ge3\):
\[
\sup_{a,b}\|Q\|_{1\to1}=\frac83,\qquad
\sup_{a,b}\|P\|_{1\to1}=\frac{11}3.
\]
Neither supremum is attained by a finite graph. Both are approached as \(a=3\) and \(b\to\infty\). For any fixed integer \(a\ge3\),
\[
\lim_{b\to\infty}\|Q\|_{1\to1}=2+\frac2a,\qquad
\lim_{b\to\infty}\|P\|_{1\to1}=3+\frac2a.
\]
If \(\min\{a,b\}\to\infty\), the two norms tend to \(2\) and \(3\), respectively.

## Assumptions and scope
All graphs are finite, simple, connected, unweighted and undirected; \(a,b\) are arbitrary integers at least three. The edge Hilbert space is \(\mathbb R^{E(G)}\) with counting measure, not normalized counting measure. The incidence operator \(\partial:\mathbb R^{E(G)}\to\mathbb R^{V(G)}\) sends a positively oriented edge \(uv\) to \(\delta_u-\delta_v\). Thus \(L=\partial\partial^*\), \(Q=\partial^*L^+\partial\), and \(P=I-Q\). Reversing an edge orientation only conjugates these matrices by diagonal signs; all claimed endpoint norms are orientation-independent. Graph connectivity follows because any two vertices sharing a coordinate have a common neighbor when \(a,b\ge3\).

## Proof
**1. Electrical potential.** By edge transitivity, fix the source edge \(e=((0,0),(1,1))\) and solve \(Lf=\delta_{(0,0)}-\delta_{(1,1)}\). Set \(D=ab-a-b>0\), \(p=1/[a(b-1)]\), \(q=1/[b(a-1)]\). A solution (with mean zero) is
\[
f(i,j)=\frac1D\left[\mathbf1_{(i,j)=(0,0)}-\mathbf1_{(i,j)=(1,1)}-p(\mathbf1_{i=0}-\mathbf1_{i=1})-q(\mathbf1_{j=0}-\mathbf1_{j=1})\right].
\]
To reconstruct it, write the adjacency matrix as \((J_a-I_a)\otimes(J_b-I_b)\). The Laplacian has eigenvalues \(0\) on constants, \(a(b-1)\) on first-coordinate mean-zero functions, \(b(a-1)\) on second-coordinate mean-zero functions, and \(D\) on the tensor interaction space. Decomposing the source into these four orthogonal subspaces and dividing by the three nonzero eigenvalues gives the displayed \(f\). In particular the transfer-current column of \(Q\) at \(e\) consists exactly of all oriented edge gradients of \(f\).

**2. Absolute gradients by level cuts.** After multiplying \(f\) by \(D\), its nine constant-value vertex classes, indexed by \(00,11,01,10,0*,1*,*0,*1,**\) (where each star denotes a coordinate outside \(\{0,1\}\)), have heights
\[
1-p-q,\quad -1+p+q,\quad q-p,\quad p-q,\quad -p,\quad p,\quad -q,\quad q,\quad0.
\]
Suppose \(a\ge b\). Then \(p\ge q>0\), \(p<2q\), and \(2p+q<1\). Hence increasing heights occur in the order
\[
11,\ 0*,\ *0,\ 01,\ **,\ 10,\ *1,\ 1*,\ 00.
\]
Coincident heights when \(a=b\) cause zero gaps and do not affect the following computation. Write \(d=(a-1)(b-1)\), the graph degree. The boundaries after adding the first one, two, three and four height classes have respectively
\[
C_1=d,\quad C_2=(b-1)d-2(b-2),\quad C_3=(a+b-3)d-2D,\quad C_4=(a+b-2)d-2(D+a-2)
\]
edges. Indeed each boundary is \(d\) times the size of the lower-level vertex set, minus twice its internal-edge count; the first four internal-edge counts are \(0,b-2,D,D+a-2\). The remaining four boundary sizes are \(C_4,C_3,C_2,C_1\) by the order-two symmetry exchanging source and sink. The corresponding successive height gaps are
\[
1-2p-q,\quad p-q,\quad 2q-p,\quad p-q,\quad p-q,\quad 2q-p,\quad p-q,\quad1-2p-q.
\]
For any real vertex function, the coarea identity says the sum of absolute gradients over all edges is the sum of its successive height gaps times the cardinalities of the associated edge cuts. Consequently
\[
\sum_{uv\in E(G)}|f(u)-f(v)|
=\frac2D\bigl[(1-2p-q)C_1+(p-q)C_2+(2q-p)C_3+(p-q)C_4\bigr].
\]
Expansion yields \(B_{a,b}+R_{a,b}\) for \(a\ge b\). Interchanging coordinate axes handles \(a\le b\), changing \(a-b\) into \(b-a\) and producing the absolute value. The entire calculation is algebraic; it is valid for every admissible pair. Edge transitivity then makes this the \(\ell_1\) norm of \(Q\). Since \(Q\) is symmetric, its \(\ell_\infty\) norm agrees.

**3. Complementary projection.** The diagonal of the source column is the effective resistance across an edge:
\[
Q_{ee}=f(0,0)-f(1,1)=\frac{2(ab-1)}{ab(a-1)(b-1)}\in(0,1).
\]
Thus the absolute column sum of \(I-Q\) is the column sum of \(Q\), plus \(1-2Q_{ee}\). All columns are equivalent under graph automorphisms, and \(P\) is symmetric. This establishes the two endpoint formulas.

**4. Sharp global bounds and limits.** By symmetry assume \(a\le b\), and write \(u=a-3\ge0\), \(v=b-a\ge0\). Define
\[
\begin{aligned}
H_0(u)&=u^6+8u^5+29u^4+82u^3+186u^2+234u+108,\\
H_1(u)&=3u^5+20u^4+58u^3+117u^2+174u+108,\\
H_2(u)&=3u^4+16u^3+33u^2+35u+24,\\
H_3(u)&=u(u+2)^2.
\end{aligned}
\]
Direct substitution in the established exact formula gives
\[
\frac83-\|Q\|_{1\to1}
=\frac{2[H_0(u)+vH_1(u)+v^2H_2(u)+v^3H_3(u)]}{3(u+2)(u+3)(u+v+2)(u+v+3)(u^2+uv+4u+2v+3)}>0.
\]
Every displayed coefficient is nonnegative and the constant polynomial is strictly positive; hence the inequality is strict at every finite size. Since \(\|P\|=\|Q\|+1-2Q_{ee}<\|Q\|+1\), the cycle bound follows. At \(a=3\) and \(b\ge3\), the cut formula simplifies to \(\|Q\|=4(2b-3)/[3(b-1)]\), tending to \(8/3\); the diagonal resistance tends to zero, so \(\|P\|\to11/3\). The remaining limits follow by dividing the rational formula by the leading powers of the parameters; for \(\min\{a,b\}\to\infty\), both correction fractions vanish.

## Verification
Run `python verify_categorical.py` with Python 3 and SymPy installed. The standalone checker performs exact rational Laplacian-residual, transfer-current, and complementary-column checks on every one of the 100 pairs with \(3\le a,b\le12\), encompassing 162,450 individual edge-current comparisons. Independently, it reconstructs complete grounded-Laplacian inverses and all 126 edge columns of the cases \((3,3),(3,4),(4,4)\). It also verifies symbolically the coarea expansion, diagonal formula and positive-polynomial global-bound identity. Successful output is `CATEGORICAL_COMPLETE_GRAPH_EXACT_OK configurations=100 edge_current_checks=162450 grounded_projection_columns=126 symbolic_identities=PASS`. These finite computations and symbolic manipulations corroborate the proof but do not replace its all-parameter sign and coarea arguments.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) study invariant cycle projections and endpoint norms, including Cartesian Hamming graphs whose edges change exactly one coordinate. The present categorical product has edges changing both coordinates, so that class does not contain the graphs here. Their results furnish the functional-analytic motivation but not the displayed two-parameter classification. Foster-Greenwood and Uhl (2024) identify direct products of complete graphs as generalized Hamming graphs while studying metric dimension; their stated invariants and methods do not provide edge projection norms. The equal-factor special case belongs to the strongly regular graph regime, whereas unequal factors have distinct row and column Laplacian eigenvalues and require the separate imbalance analysis. No claim of minimality among all possible projections is made.

## Limitations
Only canonical Euclidean-orthogonal cut and cycle projections on real, unweighted, two-factor categorical products are treated. The result does not address nonorthogonal minimum projections, weighted factors, arbitrary tensor products or intermediate \(\ell_p\) norms. The public-source comparison is necessarily nonexhaustive; an alternative electrical-flow derivation in less-indexed literature remains a bibliographic uncertainty. The automated symbolic and finite checks are reproducibility aids, not independent mathematical certification.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first submitted 21 May 2023; https://arxiv.org/abs/2305.12582 .
2. B. Foster-Greenwood, C. Uhl, *Metric Dimension of a Direct Product of Three Complete Graphs*, Electronic Journal of Combinatorics 31(2) (2024), #P2.13, DOI:10.37236/12399; https://doi.org/10.37236/12399 .
