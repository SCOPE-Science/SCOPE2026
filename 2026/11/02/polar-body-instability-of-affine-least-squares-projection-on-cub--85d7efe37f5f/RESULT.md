# Polar-body instability of affine least-squares projection on cubes and cross-polytopes

## Finding
For each integer \(d\ge1\), let \(D_d=\{x\in\mathbb R^d:\sum_{j=1}^d|x_j|\le1\}\) be the solid cross-polytope and \(Q_d=[-1,1]^d\) its polar cube. Equip each with normalized volume measure, and let \(P_D,P_Q\) be the \(L^2\)-orthogonal projectors onto all real affine functions. Their exactly attained \(L^\infty\)-operator norms are
\[
\boxed{\|P_D\|_{\infty\to\infty}=1+\frac{d+2}{2}\left(1-\frac{2}{(d+1)(d+2)}\right)^{d+1}.}\tag{1}
\]
Writing \(b_d=(3d-1)/6\), the cube norm is the finite rational sum
\[
\boxed{\|P_Q\|_{\infty\to\infty}=1+\frac{12}{(d+1)!}\sum_{k=0}^{\lfloor b_d\rfloor}(-1)^k\binom dk(b_d-k)^{d+1}.}\tag{2}
\]
Both kernels attain their maximum absolute row integral **only at vertices** of their respective domains. The sign of the kernel row at any vertex is a norm-attaining input. For \(0\le f\le1\), the sharp negative excursion of the projected function is \((\|P\|_{\infty\to\infty}-1)/2\). The two polar families display different dimensional scales:
\[
\lim_{d\to\infty}\frac{\|P_D\|_{\infty\to\infty}}d=\frac12,\qquad
\lim_{d\to\infty}\frac{\|P_Q\|_{\infty\to\infty}}{\sqrt d}=\sqrt{\frac6\pi},\qquad
\lim_{d\to\infty}\frac{\|P_D\|_{\infty\to\infty}}{\sqrt d\,\|P_Q\|_{\infty\to\infty}}=\sqrt{\frac\pi{24}}.\tag{3}
\]
In particular, the polar pair has a diverging sharp ratio despite each projection having the same affine target dimension \(d+1\).

## Assumptions and scope
Every function and vector is real. Uniform measure means volume normalized to total mass one on the solid, not the boundary measure, and \(d\) is any integer at least one. Each affine projector is defined first on \(L^2\) and extends by the same explicit bounded kernel to \(L^\infty\). The \(L^\infty\)-output norm is the essential supremum with respect to volume; for its continuous affine output this equals the maximum on the closed solid. The norm is a property of this specified projector, not the minimum norm over all projections onto the same affine subspace.

For any centered volume-uniform convex body \(K\) with invertible covariance \(\Sigma_K\), the affine reproducing kernel is
\[
K_K(x,y)=1+x^{\mathsf T}\Sigma_K^{-1}y.\tag{4}
\]
In the present cases \(\Sigma_D=2I_d/((d+1)(d+2))\) and \(\Sigma_Q=I_d/3\), so
\[
K_D(x,y)=1+\frac{(d+1)(d+2)}2\,x\cdot y,\qquad K_Q(x,y)=1+3x\cdot y.\tag{5}
\]
The cross-polytope and cube are related by polarity in their stated coordinate normalization, not by an affine equivalence when \(d\ge3\).

## Proof
**Kernel normalization and vertex maximization.** By origin symmetry, the constant function is orthogonal to the coordinate functions and the coordinate Gram matrix is the covariance. This proves (4) from orthogonal expansion. Since \(\int K_K(x,y)\,d\mu_K(y)=1\), the absolute row integral \(R_K(x)=\int|K_K(x,y)|\,d\mu_K(y)\) equals \(1+2\int(-K_K(x,y))_+\,d\mu_K(y)\). The operator norm is \(\max_xR_K(x)\). For each \(y\), \(x\mapsto|K_K(x,y)|\) is convex. Hence \(R_K\) is convex and its maximum on either polytope occurs at some vertex. Symmetry makes the row integral the same at every vertex.

**Strictness away from vertices.** The maximum is attained *only* at vertices. For any two distinct vertices \(v,w\) of \(D_d\), choose an interior \(y\) close enough to \(-v\) that \(K_D(v,y)<0<K_D(w,y)\): this works because the coefficient in (5) exceeds one, and \(v\cdot w\in\{0,-1\}\). For any distinct cube corners \(v,w\), select a coordinate where their signs differ and choose an interior \(y\) concentrated on that coordinate, opposite to its sign in \(v\) and of magnitude greater than \(1/3\). Then \(K_Q(v,y)<0<K_Q(w,y)\). The strict sign inequalities persist on a positive-volume neighborhood. Thus \(R_K\) is strictly Jensen-convex along a chord joining any distinct vertices. Every nonvertex is a nontrivial convex combination of at least two vertices; isolating two positive-weight terms in that combination yields \(R_K(x)<\max_v R_K(v)\). This proves the claimed vertex rigidity.

**Cross-polytope evaluation.** For \(Y\) uniform on \(D_d\), the first coordinate has density \(\tfrac d2(1-|t|)^{d-1}\), \(-1\le t\le1\), and variance \(2/((d+1)(d+2))\). Put \(\alpha=(d+1)(d+2)/2\) and \(a=\alpha^{-1}\). At \(x=e_1\), symmetry, reproducing constants and integration of the negative kernel give
\[
R_D(e_1)=1+d\int_a^1(\alpha t-1)(1-t)^{d-1}\,dt
=1+\frac{d+2}{2}(1-a)^{d+1},\tag{6}
\]
which is (1).

**Cube evaluation.** For \(Y\) uniform on \(Q_d\), the coordinates \(U_1,\ldots,U_d\) are independent \(\mathrm{Unif}[-1,1]\), and at \(x=(1,\ldots,1)\)
\[
R_Q(x)=\mathbb E\left|1+3\sum_{i=1}^dU_i\right|.\tag{7}
\]
Let \(T=\tfrac12\sum_{i=1}^d(U_i+1)\), a sum of \(d\) independent \(\mathrm{Unif}[0,1]\) variables. Since \(\mathbb E[1+6T-3d]=1\),
\[
R_Q(x)=1+12\,\mathbb E\left[(b_d-T)_+\right],\quad b_d=\frac{3d-1}{6}.\tag{8}
\]
The Irwin–Hall distribution has cumulative distribution function
\[
\Pr(T\le t)=\frac1{d!}\sum_{k=0}^d(-1)^k\binom dk(t-k)_+^d.\tag{9}
\]
Integrating this expression over \(0\le t\le b_d\) gives \(\mathbb E(b_d-T)_+=\frac1{(d+1)!}\sum_{k=0}^{\lfloor b_d\rfloor}(-1)^k\binom dk(b_d-k)^{d+1}\), proving (2).

**Extremizers and negative excursion.** Given a maximizing spatial vertex \(v\), the input \(f(y)=\operatorname{sgn}K_K(v,y)\) has \(\|f\|_\infty=1\) and \((P_Kf)(v)=\int|K_K(v,y)|\,d\mu_K(y)\). For \(0\le f\le1\), the most negative possible output at \(v\) is attained by the indicator of the negative set of the row kernel and equals \(-\int(-K_K(v,y))_+\,d\mu_K(y)=-(R_K(v)-1)/2\). Convexity supplies the universal bound at all spatial points. Thus the stated negativity constant follows.

**Asymptotics.** In (1), \((1-2/((d+1)(d+2)))^{d+1}\to1\); the leading term is \(d/2\). In (7), \((3\sum_iU_i)/\sqrt d\) converges in distribution to \(N(0,3)\) by the central limit theorem. Its second moment equals three for every \(d\), providing uniform integrability of its absolute value (the added term \(1/\sqrt d\) is negligible). Consequently \(R_Q/\sqrt d\to\mathbb E|N(0,3)|=\sqrt{6/\pi}\). Dividing the two limits gives (3).

## Verification
The standalone `verification/check.py` reproduces the cross-polytope beta integral by exact polynomial expansion in forty dimensions, checks its coordinate variance by exact factorial integration, and compares the cube sum with an independently integrated piecewise Irwin–Hall density through dimension eighteen. These account for 102 exact rational checks. Twelve additional Monte Carlo regressions on the two distinct solid bodies are noncertifying sanity checks. The program passed all 114 checks from the packaged Python source. Finite checks corroborate (1)–(2); the proof above establishes the statements for every integer dimension and the limiting behavior.

The exact first examples are \(\|P_D\|=\|P_Q\|=5/3\) for \(d=1\), and \(233/108\) for \(d=2\); in dimension three they differ: \(\|P_D\|=10561/4000\) versus \(\|P_Q\|=415/162\).

## Relationship to prior work
The issue is the \(L^\infty\) stability of \(L^2\)-orthogonal projections, a classical question in approximation theory. Oswald (2006) establishes an instability of global continuous piecewise-linear spline projection on certain triangulations; this does not imply an exact constant for a single solid cube or cross-polytope. Hangelbroek–Narcowich–Sun–Ward (2010) prove \(L^\infty\)-stability bounds for kernel approximation spaces on manifolds, under different hypotheses, rather than (1)–(3). Migliorati–Nobile (2015) study *discrete* least-squares polynomial approximations over multivariate domains, with a distinct sampling operator.

Closely related published exact computations cover affine projection on a single simplex, on a solid Euclidean bipyramid, and on products of simplices. Their formulas are not (2), and their different volume distributions do not cover the polar-pair comparison (3). Calculations of the cross-polytope covariance or its isotropic constant determine only the kernel (5), not its absolute integral. Nonlinear nearest-point projection onto a cross-polytope is likewise a different operator from this linear \(L^2\) projection. The contribution claimed here is the coupled exact endpoint formulas, spatial extremizer rigidity, and contrasting sharp dimension growth on the *dual* solid bodies, not the covariance identities, the Irwin–Hall distribution, the central limit theorem, or prior results for other domains.

## Limitations
The result is limited to uniform **volume** distributions on the solid real coordinate cube and its polar cross-polytope, and projection onto affine functions only. It does not treat surface measure, arbitrary unconditional convex bodies, higher polynomial degree, or discontinuous finite-element meshes. Exact projector norms on cubes and convex polytopes may have been calculated historically using a different terminology; searches and full-text comparisons reduce but do not eliminate that priority risk. No assertion of global optimality among *all* projections or independent scientific certification is made.

## References
1. P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces* (2006), arXiv:math/0611573, https://arxiv.org/abs/math/0611573.
2. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector* (2010), arXiv:1005.2424, https://arxiv.org/abs/1005.2424.
3. G. Migliorati and F. Nobile, *Analysis of discrete least squares on multivariate polynomial spaces with evaluations at low-discrepancy point sets*, Journal of Complexity **31** (2015), 517–542.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026), published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34.
5. *Sharp isotropic-constant range of all Hanner polytopes* (2026), published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2.
