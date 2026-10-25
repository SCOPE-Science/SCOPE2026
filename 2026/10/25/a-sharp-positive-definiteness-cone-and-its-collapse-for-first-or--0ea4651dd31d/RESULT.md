# A sharp positive-definiteness cone and its collapse for first-order exponential kernels on regular trees

## Finding
Let \(T_q\) be the infinite tree in which every vertex has degree \(q+1\), for any integer \(q\ge2\). Write \(d(x,y)\) for its graph distance. For real \(b\) and \(0<r<1\), the radial kernel
\[
K_{q,r,b}(x,y)=r^{d(x,y)}\bigl(1+b\,d(x,y)\bigr)
\]
is positive semidefinite on **every** finite set of vertices if and only if exactly the appropriate one of the following conditions holds:

- For \(0<r<q^{-1/2}\),
\[
-\frac{(1-\sqrt q\,r)(1-r^2)}{2r(\sqrt q-r)}\le b\le
\frac{(1+\sqrt q\,r)(1-r^2)}{2r(\sqrt q+r)}.
\]
- For \(r=q^{-1/2}\), \(0\le b\le(q-1)/(q+1)\).
- For \(q^{-1/2}<r<1\), \(b=0\).

All displayed boundaries are included. The nontrivial first-order perturbation cone therefore collapses exactly at the tree's \(\ell^2\) radial-decay threshold. For instance, for \(q=4\), the allowed \(b\)-interval at \(r=1/4\) is \([-15/28,5/4]\), at \(r=1/2\) it is \([0,3/5]\), and at \(r=3/4\) it is \(\{0\}\).

## Assumptions and scope
A kernel is positive semidefinite when \(\sum_{i,j=1}^N\overline{c_i}c_jK(x_i,x_j)\ge0\) for every \(N\ge1\), all vertices \(x_1,\ldots,x_N\), and all complex coefficients \(c_1,\ldots,c_N\). Repeated vertices are allowed. The graph is infinite, connected, acyclic, and \((q+1)\)-regular; \(q\) is a finite integer at least two. All distances are integral. No assertion is made about the bi-infinite path \(q=1\), irregular trees, or the endpoints \(r=0,1\).

## Proof
**1. Subcritical resolvent.** Let \(A\) be the adjacency operator on \(\ell^2(T_q)\). Orient edges toward a fixed end of the tree. The map carrying each basis vector to the sum of its \(q\) children is \(\sqrt q\) times an isometry, and \(A\) is this map plus its adjoint, so \(\|A\|\le2\sqrt q\). Conversely, distant finite radial-shell vectors approximate the recurrence with off-diagonal coefficient \(\sqrt q\), giving every \(t\in[-2\sqrt q,2\sqrt q]\) as an approximate spectral value. Thus
\[\sigma(A)=[-2\sqrt q,2\sqrt q].\]
For \(0<r<q^{-1/2}\), each column \(h_y(x)=r^{d(x,y)}\) belongs to \(\ell^2(T_q)\); direct evaluation at and away from \(y\) gives
\[
(I-rA+qr^2I)h_y=(1-r^2)\delta_y.
\]
Consequently the bounded operator with matrix kernel \(r^{d(x,y)}\) is
\[
F_r(A),\qquad F_r(t)=\frac{1-r^2}{1-rt+qr^2}.
\]
Differentiating in \(r\) within the subcritical interval shows that \(K_{q,r,b}\) is the matrix kernel of \(F_r(A)+br\,\partial_rF_r(A)\). Since \(F_r(t)>0\) throughout \(\sigma(A)\), positivity is equivalent to \(1+b g_r(t)\ge0\) for all \(t\in[-2\sqrt q,2\sqrt q]\), where
\[
g_r(t)=r\,\partial_r\log F_r(t)
=-\frac{2r^2}{1-r^2}+\frac{r(t-2qr)}{1-rt+qr^2}.
\]
Here \(\partial_tg_r(t)=r(1-qr^2)/(1-rt+qr^2)^2>0\), while
\[
g_r(-2\sqrt q)=-\frac{2r(\sqrt q+r)}{(1+\sqrt q\,r)(1-r^2)}<0,
\qquad
g_r(2\sqrt q)=\frac{2r(\sqrt q-r)}{(1-\sqrt q\,r)(1-r^2)}>0.
\]
Both endpoint inequalities \(1+bg_r(-2\sqrt q)\ge0\) and \(1+bg_r(2\sqrt q)\ge0\) are therefore necessary and sufficient; rearrangement gives exactly the displayed subcritical interval. The use of the entire spectral interval, rather than a finite truncation, proves necessity as well as sufficiency.

**2. A positive-matrix obstruction at and beyond critical decay.** We use the standard radial-kernel criterion on a homogeneous tree: if a radial function \(f(n)\) gives a positive semidefinite kernel, then the matrix
\[
H_{ij}=\sum_{k=0}^{\min(i,j)}q^{-k}
\bigl(f(i+j-2k)-f(i+j-2k+2)\bigr),\qquad i,j\ge0,
\]
is positive semidefinite. This is the necessary direction of Vergara's positive trace-class characterization (Theorem 1.2, cited below); only this necessary direction is used. Set
\[
\alpha=1-r^2-2br^2,\qquad\beta=b(1-r^2).
\]
Then \(f(n)-f(n+2)=r^n(\alpha+\beta n)\), and hence
\[
H_{ij}=r^{i+j}\sum_{k=0}^{\min(i,j)}(qr^2)^{-k}
\bigl(\alpha+\beta(i+j-2k)\bigr).
\]

**3. Critical decay.** At \(r=q^{-1/2}\) the preceding sum gives the exact expression
\[
H_{ij}=r^{i+j}(\min(i,j)+1)
\bigl(\alpha+\beta\max(i,j)\bigr).
\]
If \(b<0\), then \(\beta<0\) and \(H_{ii}<0\) for all sufficiently large \(i\), so positivity fails. For \(b>(q-1)/(q+1)\), one has \(\beta>0\), \(\alpha-\beta=[q-1-(q+1)b]/q<0\), and for sufficiently large \(j\),
\[
\det\begin{pmatrix}H_{00}&H_{0j}\\H_{j0}&H_{jj}\end{pmatrix}
=r^{2j}j(\alpha+\beta j)(\alpha-\beta)<0.
\]
Conversely, at \(b=0\) the matrix is \((1-1/q)r^{i+j}(\min(i,j)+1)\), a positive trace-class Gram matrix. At \(b=(q-1)/(q+1)\), one has \(\alpha=\beta=(q-1)^2/[q(q+1)]\) and \(H_{ij}=\alpha r^{i+j}(i+1)(j+1)\), again positive trace class. The function \(f(n)\) tends to zero, so the sufficient direction of the same radial-kernel criterion applies at these two endpoints. By convexity of the cone of positive semidefinite kernels, every intermediate \(b\) is admissible.

**4. Supercritical decay.** Suppose \(q^{-1/2}<r<1\), and put \(u=(qr^2)^{-1}\in(0,1)\). A geometric-sum calculation, uniform for the three index pairs \((n,n)\), \((n,n+1)\), \((n+1,n+1)\), yields
\[
r^{-(i+j)}H_{ij}=C_0+C_1(i+j)+O\bigl((i+j+1)u^{\min(i,j)+1}\bigr),
\]
where \(C_1=\beta/(1-u)\) and \(C_0=\alpha/(1-u)-2\beta u/(1-u)^2\). Consequently
\[
\lim_{n\to\infty}r^{-(4n+2)}
\det\begin{pmatrix}H_{nn}&H_{n,n+1}\\H_{n+1,n}&H_{n+1,n+1}\end{pmatrix}
=-C_1^2.
\]
If \(b\ne0\), then \(\beta\ne0\), making the determinant strictly negative for all sufficiently large \(n\). Thus \(b=0\) is necessary.

Finally, for every \(0<r<1\) the kernel \(r^{d(x,y)}\) is positive semidefinite. Indeed, sending a vertex to the indicator of edges on its path from a fixed root embeds the vertices in a Hilbert space with squared Euclidean distances equal to \(d(x,y)\); the Gaussian kernel on a Hilbert space is positive semidefinite. This proves sufficiency when \(b=0\), completing every case. \(\square\)

## Verification
The symbolic verifier `verify_tree_kernel.py` checks the resolvent spectral factor, both endpoint formulas, the critical rank-one factorization, and an exact rational supercritical minor. It is a reproducibility aid, not a substitute for the unbounded-index arguments above. The proof uses the infinite adjacency spectrum and the infinite radial positive-matrix criterion, not finite-eigenvalue extrapolation. At the critical upper boundary, the positive matrix is rank one; above critical decay, a sequence of increasingly distant principal minors supplies the obstruction.

## Relationship to prior work
Haagerup, Steenstrup and Szwarc (2009) characterize radial Schur multipliers on homogeneous trees; Schur boundedness is weaker than the positive-semidefinite classification here. Haagerup and Knudby (2013) characterize positive-definite radial functions on free groups by spherical measures. Vergara (2019), Theorem 1.2, supplies the general positive trace-class criterion used above and treats a different concrete example, not this polynomial-exponential family. The present result evaluates the exact parameter region and identifies its three-regime spectral transition; it does not claim that the underlying radial criteria or exponential positive definiteness are new.

## Limitations
This is a self-contained classification for one natural first-order exponential family on homogeneous trees, not a theorem for all graph kernels, higher polynomial multipliers, irregular trees, or \(q=1\). The result uses a published radial-kernel criterion as a standard lemma. The bounded literature search cannot exclude an equivalent classification in unindexed or differently named work. No independent audit has been performed.

## References
1. U. Haagerup, T. Steenstrup and R. Szwarc, *Schur Multipliers and Spherical Functions on Homogeneous Trees*, arXiv:0908.4424, first posted 2009-08-31; https://arxiv.org/abs/0908.4424.
2. U. Haagerup and S. Knudby, *A Lévy–Khinchin Formula for Free Groups*, arXiv:1304.5763, first posted 2013-04-21; https://arxiv.org/abs/1304.5763.
3. I. Vergara, *Positive Definite Radial Kernels on Homogeneous Trees and Products*, arXiv:1907.11476, first posted 2019-07-26, Theorem 1.2 and Sections 6–7; https://arxiv.org/abs/1907.11476.
