# A single deleted hypercube edge increases sharp gradient-reconstruction sensitivity from dimension four

## Finding

Write \(Q_d\) for the unweighted graph with vertices \(\{0,1\}^d\), with \(d\geq2\), and edges between vertices differing in one coordinate. Orient each edge in its varying coordinate from bit zero to bit one. Let \(h\) be the edge from \(0\) to the first coordinate unit vector; delete \(h\), obtaining the connected graph \(G_d=Q_d\setminus\{h\}\). Let \(\Pi_d\) and \(\Pi'_d\) denote the Euclidean orthogonal projections from edge data onto the respective spaces of vertex gradients on \(Q_d\) and \(G_d\). All norms below are induced by the maximum absolute edge coordinate.

The intact cube satisfies \(\|\Pi_d\|_{\infty\to\infty}=(d+1)/2\). For the edge \(e\) parallel to \(h\) and one unit transverse step away, the **exact absolute row sum** of \(\Pi'_d\) is

\[
R_d=\frac{d+1}{2}+\frac{d-3}{2}\,\alpha_d,
\qquad
\alpha_d=\frac{2^d-d-1}{(d-1)((d-2)2^{d-1}+1)}.
\]

Thus deletion of a single edge strictly increases the worst-case coordinatewise sensitivity for **every** \(d\geq4\):

\[
\|\Pi'_d\|_{\infty\to\infty}\geq R_d>
\|\Pi_d\|_{\infty\to\infty}=\frac{d+1}{2}.
\]

The dimension threshold is sharp. At \(d=2\), \(\|\Pi'_2\|=1<3/2\); at \(d=3\), \(\|\Pi'_3\|=2=\|\Pi_3\|\). At \(d=4\), the **full sharp norm** is

\[
\boxed{\|\Pi'_4\|_{\infty\to\infty}=\frac{133}{51}=
\frac52+\frac{11}{102}}.
\]

The norming rows in dimension four are exactly the three remaining edges parallel to \(h\) at transverse Hamming distance one; selecting their row signs attains the norm. Moreover, \(\lim_{d\to\infty}d(R_d-(d+1)/2)=1\). No exact formula for the **global** deleted-cube norm in every dimension \(d\ge5\) is asserted.

## Assumptions and scope

The graph is finite, simple, unweighted and connected; the edge inner product is ordinary counting measure. Vertices are indexed by binary vectors and a coordinate is oriented from zero to one. For a graph \(G\) write \(D_G\) for the oriented edge-by-vertex incidence matrix, \((D_Gu)_{(i,x)}=u(x)-u(x\oplus 2^i)\), where the \(i\)-th bit of \(x\) is zero. The projection is \(\Pi_G=D_G(D_G^TD_G)^+D_G^T\), with the Moore–Penrose inverse. The induced norm is \(\|\Pi_G\|_{\infty\to\infty}=\max_e\sum_f|\Pi_G(e,f)|\). All claims are for integers \(d\ge2\); formulas involving \(h\) refer to the fixed edge in coordinate zero, and symmetry handles any other deleted edge. The intact and deleted operators act on different edge spaces, each with its own maximum norm. No identification of their domains is required to compare the numerical operator norms.

## Proof

**1. Signs and row masses for the intact cube.** The cube Laplacian is the sum of \(d\) commuting two-point Laplacians. Its continuous-time heat kernel is

\[
H_t(x,y)=\prod_{k=0}^{d-1}\frac{1+(-1)^{x_k+y_k}q}{2},
\qquad q=e^{-2t}.
\]

Because incidence annihilates constants, the gradient projector equals \(\int_0^\infty D H_tD^T\,dt\). For edges \((i,x)\) and \((j,y)\), with the displayed base points having bit \(i\) or \(j\) zero, this yields, when \(i=j\),

\[
\Pi_d((i,x),(i,y))=\int_0^\infty 2q
\prod_{k\ne i}\frac{1+(-1)^{x_k+y_k}q}{2}\,dt>0;
\]

and, when \(i\ne j\),

\[
\Pi_d((i,x),(j,y))=(-1)^{x_j+y_i}
\int_0^\infty q^2\prod_{k\notin\{i,j\}}
\frac{1+(-1)^{x_k+y_k}q}{2}\,dt.
\]

The integrands determining magnitudes are positive. Summing each fixed row over all edges of its own direction gives exactly \(1\), and summing absolute values over each different direction gives exactly \(1/2\), by independently summing the factors in the product and integrating \(2q\) or \(q^2\) over \(t\). Hence every intact-cube row has absolute sum \(1+(d-1)/2=(d+1)/2\).

**2. The deleted-edge projector.** Put \(L=D^TD\), \(b=D_h^T\), and \(S=E(Q_d)\setminus\{h\}\). Removing \(h\) replaces \(L\) by \(L-bb^T\). Both graphs are connected, so invert the latter on the mean-zero vertex subspace. By the rank-one inverse identity,

\[
\Pi'_d(f,g)=\Pi_d(f,g)+\frac{\Pi_d(f,h)\Pi_d(h,g)}{1-\Pi_d(h,h)},
\qquad f,g\in S.
\]

The denominator is positive because \(h\) is not a bridge. For the parallel edge \(e=(0,2)\) in bitmask notation, integration of the preceding heat kernels gives

\[
q_d:=\Pi_d(h,h)=\frac{2^d-1}{d2^{d-1}},\qquad
 a_d:=\Pi_d(e,h)=\frac{2^d-d-1}{d(d-1)2^{d-1}}.
\]

For example, these follow from \(q_d=\int_0^1((1+u)/2)^{d-1}\,du\) and
\(a_d=\int_0^1((1-u)/2)((1+u)/2)^{d-2}\,du\), by substituting \(u=e^{-2t}\). Set \(\alpha_d=a_d/(1-q_d)\), which simplifies to the rational expression in the finding. Direct subtraction shows \(0<\alpha_d\le1\), with equality only at \(d=2\).

**3. Exact damaged row.** In the row of \(e\), every same-direction entry \(\Pi_d(e,f)\), \(\Pi_d(h,f)\) is positive. Its damaged same-direction absolute sum is

\[
(1-a_d)+\alpha_d(1-q_d)=1.
\]

For the transverse direction \(j=1\), the intact entries satisfy \(\Pi_d(e,f)=-\Pi_d(h,f)\) term by term, so their damaged sum is \((1-\alpha_d)/2\). For each other transverse direction \(j\ge2\), the corresponding entries for \(e\) and \(h\) have the same sign, by the heat-kernel sign formula; their damaged sum is \((1+\alpha_d)/2\). Adding all \(d\) direction sums yields

\[
R_d=1+\frac{1-\alpha_d}{2}+
(d-2)\frac{1+\alpha_d}{2}
=\frac{d+1}{2}+\frac{d-3}{2}\alpha_d.
\]

For \(d\ge4\) this strictly exceeds the intact norm. Also \(d^2\alpha_d\to2\), giving \(d(R_d-(d+1)/2)\to1\).

**4. Sharpness of the dimension threshold.** For \(d=2\), deletion leaves a tree; every edge-data vector is a gradient, so \(\Pi'_2=I\). To check \(d=3\) and \(d=4\) exhaustively, a second representation of the full cube projector follows by diagonalizing the vertex Laplacian in the binary Walsh characters:

\[
\Pi_d((i,x),(j,y))=2^{1-d}
\sum_{\substack{\emptyset\ne T\subseteq\{0,\ldots,d-1\}\\i,j\in T}}
\frac{(-1)^{\sum_{k\in T}(x_k+y_k)}}{|T|}.
\]

Combining this finite rational sum with the rank-one update in step 2 yields all remaining-edge row sums exactly. The complete multiplicity table at \(d=3\) is \(2\) (twice), \(9/5\) (once), \(15/8\) (four times), and \(39/20\) (four times); its maximum is \(2\). At \(d=4\), the table is \(133/51\) (three times), \(125/51\) (three times), \(41/17\) (once), \(22/9\) (six times), \(42/17\) (twelve times), and \(127/51\) (six times). Its maximum is \(133/51\), with precisely the stated three norming edges. These are exhaustive because the checker independently enumerates every remaining edge, all matrix coefficients and all absolute row sums. For any row, taking input edge values equal to the signs of that row gives an attaining vector; hence the computed row maximum is the induced operator norm, not just an upper estimate.

## Verification

Execute `python3 CHECK.py` with Python 3 and no external dependencies. The verifier constructs grounded vertex-Laplacian inverses in exact rational arithmetic and independently constructs the full-cube projection by Walsh spectral sums. For dimensions \(2,3,4\) it compares the two matrices, verifies the rank-one deletion identity coefficient-by-coefficient, verifies the formulas for \(q_d\), \(a_d\), \(\alpha_d\), and \(R_d\), checks all complete deleted-cube row-sum histograms, and reconstructs exact maximizing sign vectors. It does **not** try to enumerate arbitrarily large cube dimensions; those are covered by the analytic heat-kernel proof.

## Relationship to prior work

Jiang–Lim–Yao–Ye formulate incomplete pairwise ranking as orthogonal projection of edge flows onto graph gradients, using combinatorial Hodge decomposition; this supplies the natural least-squares interpretation of the operator. Burton–Pemantle develop transfer impedances and Green-function methods, including high-dimensional cube asymptotics; those general methods do not state the exact single-edge-deletion maximum-norm threshold or the dimension-four sharp constant. Schild–Rao–Srivastava prove logarithmic bounds on average electrical-flow localization, rather than the present exact worst-row outage sensitivity. Gurel-Gurevich–Nachmias–Sachdeva sharpen general localization estimates but do not state the hypercube deletion result. The intact-cube norm follows directly from the heat-kernel sign structure and is used only as a comparison baseline, not as a new discovery.

## Limitations

The closed formula \(R_d\) is the exact norm of one particular remaining-edge evaluation functional, not necessarily the global operator norm for \(d\ge5\). The graph must be a unit-weight binary hypercube with precisely one missing edge; arbitrary failures, unequal conductances, other Cartesian products, and non-Euclidean fitting objectives are not classified. The first-order asymptotic concerns \(R_d\) minus the intact norm, not an asserted expansion of the full deleted norm. Prior unpublished or unindexed calculations may contain equivalent formulas; originality is subject to that risk.

## References

- R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability **21** (1993), 1329–1371; open full text at https://arxiv.org/abs/math/0404048.
- X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067v1 (public 7 November 2008), https://arxiv.org/abs/0811.1067.
- A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632 (2017), https://arxiv.org/abs/1708.01632.
- O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130 (2026), https://arxiv.org/abs/2605.24130.
