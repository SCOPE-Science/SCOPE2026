# Sharp rank budgets and extremal packings in trace-norm matrix spaces

## Finding

**Theorem (maximally separated trace-class matrix families).** Fix integers \(p,q\ge1\) and a finite indexed family of **nonzero** matrices \(A_1,\ldots,A_m\in M_{p,q}(\mathbb C)\). The trace norm \(\|A\|_1=\operatorname{Tr}|A|\) is the sum of the singular values; \(\operatorname{rank}A\) is the dimension of the initial support of its polar factor. Suppose every pair is maximally separated:

\[
\|A_i-A_j\|_1=\|A_i\|_1+\|A_j\|_1 \qquad (i\ne j).
\]

Then the **sharp rank budget** is

\[
\boxed{\sum_{i=1}^{m}\operatorname{rank}(A_i)\le 2\min\{p,q\}.}
\]

More precisely, write \(A_i=U_i|A_i|\) with polar partial isometry \(U_i:\mathbb C^q\to\mathbb C^p\) and support \(Q_i=(\ker A_i)^\perp\). The pairwise maximal-distance condition holds **if and only if** the subspaces

\[
G_i=\{(x,U_ix):x\in Q_i\}\subset\mathbb C^q\oplus\mathbb C^p
\]

are pairwise orthogonal. The rank budget is attained by \(2\min\{p,q\}\) signed coordinate matrix units \(\{E_{jj},-E_{jj}\}\) on a common rectangular diagonal.

**Saturated square-case rigidity.** For \(p=q=d\) and \(m=2d\), if additionally \(\|A_i\|_1=1\), then each \(A_i\) has rank one, so it has a representation \(A_i=u_iv_i^*\) with unit vectors \(u_i,v_i\in\mathbb C^d\). Exactly the extremizers are those for which

\[
\left\{\frac1{\sqrt2}(v_i,u_i):1\le i\le2d\right\}
\]

is an orthonormal basis of \(\mathbb C^{2d}\). Conversely, any orthonormal basis of \(\mathbb C^{2d}\) whose vectors have equal squared norms \(1/2\) in the first and second \(d\)-coordinate blocks determines such an extremal family by the preceding formula. Every saturated family satisfies \(\sum_i A_i=0\).

**Finite metric corollary.** A star with \(m\ge1\) leaves, each edge of length one and leaf-to-leaf distance two, admits an isometric embedding (not assumed linear, positive, self-adjoint, or normal) into \((M_d(\mathbb C),\|\cdot\|_1)\) if and only if \(m\le2d\). Hence its exact minimal target matrix size is \(\lceil m/2\rceil\).

## Assumptions and scope

All vector spaces are over \(\mathbb C\), all matrix dimensions are positive integers, and families are finite with every member nonzero. No equality of member ranks, positive-semidefiniteness, or common polar factor is assumed. Pairwise maximal distance means equality in the triangle inequality for the difference, not just an arbitrary equilateral set. The rank budget applies to rectangular matrices; the balanced-basis classification as stated applies to square matrices of maximal cardinality. An additional zero matrix could be included without consuming rank, so the nonzero qualification is necessary for the cardinality corollary.

## Proof

**1. A polar-factor saturation lemma.** For any nonzero \(A=U|A|\in M_{p,q}(\mathbb C)\), put \(Q=(\ker A)^\perp\). If \(Z\in M_{p,q}(\mathbb C)\) is a contraction for the operator norm, then

\[
\operatorname{Re}\operatorname{Tr}(Z^*A)\le\|A\|_1,
\]

and equality holds exactly when \(Zx=Ux\) for all \(x\in Q\). Indeed, choose an orthonormal eigenbasis \(e_j\) of \(|A|\) on \(Q\) with positive singular values \(s_j\). The trace is \(\sum_j s_j\langle Ze_j,Ue_j\rangle\) (up to the conventional inner-product orientation), and every real summand is at most \(s_j\). Equality forces each \(Ze_j=Ue_j\) by Cauchy--Schwarz and the contraction bound, and linearity yields the assertion. The converse is immediate.

**2. Exact pairwise criterion.** For distinct \(i,j\), the dual formula

\[
\|A_i-A_j\|_1=\max_{\|Z\|_{\mathrm{op}}\le1}\operatorname{Re}\operatorname{Tr}(Z^*(A_i-A_j))
\]

has a maximizer in finite dimension. If the maximum equals \(\|A_i\|_1+\|A_j\|_1\), the contraction saturates both trace inequalities and therefore satisfies \(Zx=U_ix\) on \(Q_i\) and \(Zy=-U_jy\) on \(Q_j\). Because \(\|Zx\|=\|x\|\) on these subspaces and \(I-Z^*Z\) is positive semidefinite, it annihilates both \(Q_i\) and \(Q_j\). Hence for every \(x\in Q_i\), \(y\in Q_j\),

\[
\langle U_ix,U_jy\rangle=-\langle x,y\rangle.
\]

Equivalently, \(\langle(x,U_ix),(y,U_jy)\rangle=0\); thus \(G_i\perp G_j\).

Conversely, assume \(G_i\perp G_j\), hence the preceding mixed-inner-product identity. On \(Q_i+Q_j\), define \(Z(x+y)=U_ix-U_jy\). If \(x+y=0\), the identity implies \(\|U_ix-U_jy\|=\|x+y\|=0\), so the map is well-defined. Expanding squared norms and applying the mixed-inner-product identity gives

\[
\|U_ix-U_jy\|^2=\|x+y\|^2.
\]

Thus \(Z\) is an isometry on \(Q_i+Q_j\). Extend it by zero on the orthogonal complement. The extension is a contraction and simultaneously norms \(A_i\) and \(-A_j\), proving the maximal-distance equality. No assumption on intersections between \(Q_i\) and \(Q_j\) was used.

**3. Dimension bound and sharpness.** Fix orthonormal bases \(e_{i,1},\ldots,e_{i,r_i}\) of each \(Q_i\), where \(r_i=\operatorname{rank}(A_i)\). The vectors

\[
 w_{i,t}=\frac1{\sqrt2}(e_{i,t},U_ie_{i,t})\in\mathbb C^q\oplus\mathbb C^p
\]

form a single orthonormal set by the graph criterion and the polar isometry. Each has squared projection norm \(1/2\) onto \(\mathbb C^q\oplus\{0\}\), and likewise onto \(\{0\}\oplus\mathbb C^p\). Applying Bessel's inequality to either coordinate projection and summing yields

\[
\frac12\sum_i r_i\le q,\qquad \frac12\sum_i r_i\le p.
\]

This proves the bound \(\sum_i r_i\le2\min\{p,q\}\), stronger than the raw direct-sum dimension bound when the shape is rectangular. To attain it, take \(k=\min\{p,q\}\) and matrices \(A_{j,+}=E_{jj}\), \(A_{j,-}=-E_{jj}\) for \(1\le j\le k\), with zero-padding to the rectangular shape. Every matrix has rank one and trace norm one, and distinct matrices have trace-norm distance two (even within each signed pair).

**4. Equality classification for square matrices.** If \(p=q=d\) and \(m=2d\) nonzero members meet the separation hypothesis, the rank bound and \(r_i\ge1\) force \(r_i=1\) for every index. After normalizing to trace norm one, write \(A_i=u_iv_i^*\) with unit vectors. Its graph is spanned by \((v_i,u_i)\), so the pairwise criterion states precisely that the \(2d\) unit vectors \((v_i,u_i)/\sqrt2\) form an orthonormal basis in \(\mathbb C^{2d}\). Reversing the argument proves the converse. With \(V=(v_1\ \cdots\ v_{2d})\) and \(U=(u_1\ \cdots\ u_{2d})\), the block matrix \((V;U)/\sqrt2\) is unitary, so its off-diagonal block equation is \(VU^*=0\). Hence \(\sum_i A_i=UV^*=0\). For a non-diagonal construction, take the normalized Fourier matrix of size \(2d\): each column has half its squared mass in either block, so its columns give the required balanced orthonormal basis.

**5. Star classification.** Translate the image of a star's center to the zero matrix. Each leaf image is nonzero with trace norm one, and every pair of leaf images is at distance two. The rank budget forces \(m\le2d\). Conversely, any \(m\le2d\) of the signed diagonal matrix units in \(M_d(\mathbb C)\), together with the zero matrix for the center, give an isometric embedding. This proves the exact minimum size.

## Verification

The supporting `check.py` generates balanced Fourier rank-one families for every square size \(1\le d\le8\) and checks operator singular values, pairwise trace distances, orthogonality, and zero sum with floating-point tolerances. It also checks the rectangular signed-diagonal construction for \(1\le p,q\le5\), including every leaf pair. All universal quantifiers and the sharp rank bound are proved above; numerical instances are diagnostic and not evidence for an infinite-dimension or all-size assertion. Run `python check.py` with NumPy installed.

## Relationship to prior work

Jiao--Luo--Wu (2026, arXiv:2610.21445v1) prove an optimal-scaling metric-cotype inequality for the full Schatten trace class. Their theorem applies to arbitrary metric mappings but does not determine sharp finite matrix sizes for star isometries or a rank-budget classification of equality in matrix trace-norm triangles. Aziznejad--Unser (2020, arXiv:2009.07768v1) characterize Schatten norm duality mappings, including trace-norm Hölder saturation; the polar norming step above uses this standard type of duality, but their results do not assert the simultaneous graph-orthogonality rank budget for arbitrary maximally separated families. Chun (2019, arXiv:1908.05650v1) proves a sharp \(2n\) packing count in the real \(\ell_1\) cross-polytope; since the diagonal subspace does not exhaust arbitrary complex rectangular matrices, that theorem does not supply the present noncommutative upper bound or square-case equality family. Swanepoel--Villa (2011/2013, arXiv:1109.5063v1) study general maximal equilateral sets rather than maximally separated trace-class spheres. A known exact embedding threshold for unit-edge even cycles does not imply the star threshold, because cycles have maximal vertex degree two and cannot realize stars with three or more leaves as distance-preserving submetrics.

## Limitations

No assertion is made for approximately maximal separation, for general equilateral distances below the triangle-equality maximum, or for arbitrary infinite-rank trace-class operators. The saturated family classification describes square matrices only and requires the indicated normalization; different positive scalings preserve the general maximal-separation hypothesis. Standard duality and polar-graph reasoning might be implicit in older operator-ideal or metric-geometry literature not located here; historical priority remains a residual risk. No claim of independent verification is made.

## References

1. Y. Jiao, S. Luo, L. Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1 (first submitted 2026-10-15), https://arxiv.org/html/2610.21445v1.
2. S. Aziznejad, M. Unser, *Duality Mapping for Schatten Matrix Norms*, arXiv:2009.07768v1 (2020), https://arxiv.org/html/2009.07768v1.
3. J. H. Chun, *The maximum number of points in the cross-polytope that form a packing set of a scaled cross-polytope*, arXiv:1908.05650v1 (2019), https://arxiv.org/html/1908.05650v1.
4. K. J. Swanepoel, R. Villa, *Maximal Equilateral Sets*, arXiv:1109.5063 (2011), Discrete & Computational Geometry 50 (2013), 354--373.
5. R. Bhatia, *Matrix Analysis*, Springer (1997), standard singular-value and duality background.
