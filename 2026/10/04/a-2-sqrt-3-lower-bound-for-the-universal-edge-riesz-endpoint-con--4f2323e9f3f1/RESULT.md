# A \(2/\sqrt{3}\) lower bound for the universal edge-Riesz endpoint constant
## Finding
Let \(C_\mathrm{edge}\) denote the least constant with the following property: for every infinite connected locally finite undirected graph with positive symmetric edge weights, normalized Laplacian \(\Delta\), edge differential \(D_E\), and edge Riesz transform \(R_E=D_E\Delta^{-1/2}\) in the polar-extension sense, every real \(f\in \ell^1(V,m)\cap\ell^2(V,m)\) satisfies
\[
\sup_{\lambda>0}\lambda\,\mu_E\{e:|R_Ef(e)|>\lambda}\le C_\mathrm{edge}\|f\|_{1,m}.
\]
Then
\[
\frac{2}{\sqrt{3}}\le C_\mathrm{edge}\le 2.
\]
The upper bound is Theorem 2.1 of Wang. The new content is the lower bound, realized asymptotically by an explicit family of infinite weighted graphs and real inputs.

## Assumptions and scope
For \(\varepsilon>0\), first consider the weighted complete graph on vertices \(\{0,1,2,3\}\) with edge weights
\[
w_{01}=\varepsilon,\quad w_{02}=\varepsilon^{-1},\quad w_{03}=\frac13,\quad
w_{12}=\varepsilon,\quad w_{13}=1,\quad w_{23}=\varepsilon^2.
\]
Its vertex masses are the weighted degrees
\[
d_0=\varepsilon+\varepsilon^{-1}+\frac13,\quad d_1=1+2\varepsilon,\quad
d_2=\varepsilon^{-1}+\varepsilon+\varepsilon^2,\quad d_3=\frac43+\varepsilon^2.
\]
This finite graph is only a core. It is lifted below to an infinite graph satisfying the hypotheses of the source theorem. The test input on the core is \(f=\mathbf 1_{\{1\}}\).

## Proof
Let \(M_\varepsilon=\operatorname{diag}(d_0,d_1,d_2,d_3)\), let \(W_\varepsilon=(w_{ij})\), and put
\[
S_\varepsilon=I-M_\varepsilon^{-1/2}W_\varepsilon M_\varepsilon^{-1/2}.
\]
This is the symmetric representative of the normalized Laplacian. As \(\varepsilon\downarrow0\),
\[
S_\varepsilon\longrightarrow S_0=
\begin{pmatrix}
1&0&-1&0\\
0&1&0&-\sqrt3/2\\
-1&0&1&0\\
0&-\sqrt3/2&0&1
\end{pmatrix}.
\]
The eigenvalues of \(S_0\) are \(0,2,1-\sqrt3/2,1+\sqrt3/2\). Hence its nonzero spectrum is separated from zero. Since each core graph is connected, \(S_\varepsilon\) has a one-dimensional kernel, and continuity of eigenvalues implies that its other three eigenvalues remain uniformly separated from zero for small \(\varepsilon\). Therefore the generalized inverse square roots converge:
\[
S_\varepsilon^{\dagger,-1/2}\to S_0^{\dagger,-1/2}.
\]
For \(x_\varepsilon=M_\varepsilon^{1/2}f=\sqrt{d_1}e_1\), one has \(x_\varepsilon\to e_1\). On the \(\{1,3\}\)-block,
\[
A=\begin{pmatrix}1&-r\\-r&1\end{pmatrix},\qquad r=\frac{\sqrt3}2,
\]
and
\[
A^{-1/2}e_1
=\frac12\left((1-r)^{-1/2}\binom11+(1+r)^{-1/2}\binom1{-1}\right)
=\binom{\sqrt3}1,
\]
because \((1-r)^{-1/2}=\sqrt3+1\) and \((1+r)^{-1/2}=\sqrt3-1\). Transforming back by \(M_\varepsilon^{-1/2}\) gives, for \(u_\varepsilon=\Delta_\varepsilon^{-1/2}f\),
\[
(u_\varepsilon(0),u_\varepsilon(1),u_\varepsilon(2),u_\varepsilon(3))
\longrightarrow (0,\sqrt3,0,\sqrt3/2).
\]
Thus, with edge orientations \((01),(02),(03),(12),(13),(23)\),
\[
R_Ef\longrightarrow(-\sqrt3,0,-\sqrt3/2,\sqrt3,\sqrt3/2,-\sqrt3/2).
\]
Fix \(0<\lambda<\sqrt3/2\). For all sufficiently small \(\varepsilon\), the five edge types other than \((02)\) satisfy \(|R_Ef|>\lambda\). Their total core edge measure is
\[
\frac43+2\varepsilon+\varepsilon^2,
\]
while \(\|f\|_{1,m}=d_1=1+2\varepsilon\). Hence the core weak ratio has lower limit at least \(4\lambda/3\), and then \(\lambda\uparrow\sqrt3/2\) gives \(2/\sqrt3\).

It remains to place the example in the infinite-graph class. Put \(e_k=2^{-|k|}\) for \(k\in\mathbb Z\), \(a_k=e_{k-1}+e_k\), so \(\sum_k a_k=6\). On vertices \((i,k)\in\{0,1,2,3\}\times\mathbb Z\), give horizontal edges \((i,k)\sim(j,k)\) weight \(a_k w_{ij}\), and vertical edges \((i,k)\sim(i,k+1)\) weight \(\tau d_i e_k\), where \(\tau>0\). The resulting graph is infinite, connected, locally finite, and has positive symmetric weights. Its vertex mass is
\[
m(i,k)=(1+\tau)a_kd_i.
\]
For a level-constant function \(Jf(i,k)=f_i\), the Markov operator satisfies
\[
P_GJf=\frac{\tau}{1+\tau}Jf+\frac1{1+\tau}JP_\varepsilon f,
\]
so
\[
\Delta_GJ=\frac1{1+\tau}J\Delta_\varepsilon.
\]
The level-constant subspace reduces the self-adjoint Laplacian; functional calculus therefore gives
\[
\Delta_G^{-1/2}J=\sqrt{1+\tau}\,J\Delta_\varepsilon^{-1/2}
\]
with both sides zero on constants. Consequently the vertical edge transform vanishes and every horizontal edge value is \(\sqrt{1+\tau}\) times its core value. For any core threshold \(\lambda\),
\[
\frac{\sqrt{1+\tau}\lambda\,\mu_G\{|R_EJf|>\sqrt{1+\tau}\lambda\}}{\|Jf\|_{1,m_G}}
=\frac1{\sqrt{1+\tau}}\,
\frac{\lambda\,\mu_\varepsilon\{|R_Ef|>\lambda\}}{\|f\|_{1,m_\varepsilon}}.
\]
Letting first \(\varepsilon\downarrow0\), then \(\lambda\uparrow\sqrt3/2\), and finally \(\tau\downarrow0\) proves \(C_\mathrm{edge}\ge2/\sqrt3\).

## Verification
The accompanying `verify_graph_riesz_lower_bound.py` rebuilds the four-vertex symmetric normalized Laplacian, computes its generalized inverse square root by a standard-library Jacobi eigensolver, and checks convergence of all six edge values and the weak ratio. At \(\varepsilon=10^{-5}\) it obtains weak ratio \(1.154645887493503\), within \(5.5\times10^{-5}\) of \(2/\sqrt3\), and maximum edge-value error \(5.1\times10^{-5}\). It also checks \(\sum_k a_k=6\) and the exact lift penalty \((1+\tau)^{-1/2}\). These computations are sanity checks only; the proof above is the infinite argument.

## Relationship to prior work
Wang proves the universal upper estimate \(C_\mathrm{edge}\le2\) for the same edge-space transform on every infinite connected locally finite normalized weighted graph, and explicitly permits finite total vertex mass. The paper does not state sharpness or optimality, and full-text searches for those terms returned no occurrence. Its proof obtains the factor \(2\) by adding a support estimate and an \(\ell^2\) estimate.

Russ proved weak type \((1,1)\) under doubling and heat-kernel assumptions for an earlier graph Riesz transform, with a geometry-dependent constant rather than a universal best-constant calculation. Chen--Coulhon--Hua studied \(\ell^p\) boundedness for bounded graph Laplacians and distinguished edge and vertex gradient notions, but their main results concern \(1<p<\infty\), not a universal endpoint best constant. No checked source gives the explicit lower bound \(2/\sqrt3\) or the level-lift construction above.

## Limitations
The result does not determine the optimal universal constant: the interval \([2/\sqrt3,2]\) remains. The core family is highly inhomogeneous and uses edge weights with ratios diverging as \(\varepsilon\downarrow0\); no corresponding lower bound is claimed for unweighted, bounded-degree-with-uniform-weights, doubling, or fixed-geometry subclasses. The numerical verifier does not certify the limiting argument; it only checks representative finite parameters and the exact algebraic identities used in the proof.

## References
1. Zihao Wang, *Endpoint Riesz transforms on normalized graphs*, arXiv:2609.28531v1, submitted 22 September 2026. Primary MSC 42B20.
2. Emmanuel Russ, *Riesz transforms on graphs for \(1\le p\le2\)*, Mathematica Scandinavica 87 (2000), 133--160, DOI 10.7146/math.scand.a-14303.
3. Li Chen, Thierry Coulhon, and Bobo Hua, *Riesz transforms for bounded Laplacians on graphs*, arXiv:1708.05476v1; Math. Z. 294 (2020), 397--417.
