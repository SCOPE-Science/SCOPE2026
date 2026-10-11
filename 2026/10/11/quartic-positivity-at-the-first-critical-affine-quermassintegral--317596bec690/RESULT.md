# Quartic positivity at the first critical affine-quermassintegral threshold

## Finding

Let \(n=10\), fix a unit vector \(e\in\mathbb R^{10}\), and define the degree-four zonal spherical harmonic
\[
Y_e(u)=(u\cdot e)^4-\frac37(u\cdot e)^2+\frac1{56},\qquad u\in S^9.
\]
For every real \(t\) with \(|t|<56/143\), the function \(h_t=1+tY_e\) is the support function of an origin-symmetric, smooth, strictly convex body \(K_t\). Using the normalized negative-ten affine quermassintegrals defined below, the **critical comparison deficit** obeys
\[
\boxed{\log\frac{I_{1,-10}(K_t)}{I_{2,-10}(K_t)^{1/2}}=\frac{139863}{3147038720}\,t^4+O(t^5)\quad(t\to0).}
\]
In particular, the quadratic and cubic coefficients vanish, the first nonzero coefficient is strictly positive, and \(I_{1,-10}(K_t)>I_{2,-10}(K_t)^{1/2}\) for every sufficiently small nonzero real \(t\), of either sign. This is a local statement along this one-parameter family, not a general inequality for all ten-dimensional convex bodies.

## Assumptions and scope

The Haar probability measure on \(G(10,j)\) is denoted \(dF\), \(P_F\) is orthogonal projection, and \(\kappa_j\) is the volume of the unit Euclidean ball in dimension \(j\). Let \(B_K\) be the centered Euclidean ball of the same ten-volume as \(K\). For \(j=1,2\), define
\[
I_{j,-10}(K)=\left(\frac{\int_{G(10,j)}\operatorname{vol}_j(P_FK)^{-10}\,dF}{\int_{G(10,j)}\operatorname{vol}_j(P_FB_K)^{-10}\,dF}\right)^{-1/10}.
\]
All asymptotic statements refer to \(t\to0\) with dimension and \(e\) fixed. The positive smallness threshold in the strict inequality is not specified explicitly; an explicit convexity range is proved, but the sign of the comparison over that entire range is not asserted.

## Proof

**1. Convexity of the perturbation.** Write \(s=u\cdot e\) and \(v=s^2\in[0,1]\). A direct spherical-Hessian calculation shows that the eigenvalues of the curvature-radius perturbation \(\nabla^2_{S^9}Y_e+Y_e g\) are the tangential and meridional polynomials
\[
\tau(v)=-3v^2+\frac37v+\frac1{56},\qquad
\mu(v)=-15v^2+\frac{93}7v-\frac{47}{56}.
\]
The extrema on \([0,1]\) give \(\tau(1)=\mu(1)=-143/56\), \(\tau(1/14)=13/392\), and \(\mu(31/70)=4121/1960\). Therefore \(\|\nabla^2Y_e+Y_e g\|_{\mathrm{op}}\le143/56\). Also \(\|Y_e\|_\infty=33/56\). For \(|t|<56/143\), \(h_t>0\) and \(g+t(\nabla^2Y_e+Y_e g)\) is positive definite, ensuring the asserted convex support function. Evenness gives origin symmetry.

**2. Eliminate the equal-volume-ball normalization.** Put
\[
v_j(F,t)=\operatorname{vol}_j(P_FK_t)/\kappa_j,
\qquad M_j(t)=\int_{G(10,j)}v_j(F,t)^{-10}\,dF.
\]
Writing \(r_t^{10}=\operatorname{vol}_{10}(K_t)/\kappa_{10}\), the defining normalization yields \(I_{j,-10}(K_t)=r_t^jM_j(t)^{-1/10}\). Hence the global volume factor cancels *exactly*:
\[
\Delta(t):=\log\frac{I_{1,-10}(K_t)}{I_{2,-10}(K_t)^{1/2}}=\frac1{10}\left(\frac12\log M_2(t)-\log M_1(t)\right).
\]

**3. Exact projected areas.** For a line, a unit direction \(u\) satisfies \(v_1(u,t)=1+tY_e(u)\). For a plane \(F\), set \(z=\|P_Fe\|^2\). On its unit circle, with the angular variable chosen so that \(u\cdot e=\sqrt z\cos\theta\), the restricted support function has the Fourier form
\[
Y_e|_F=a(z)+b(z)\cos(2\theta)+c(z)\cos(4\theta),
\]
where
\[
a(z)=\frac38z^2-\frac3{14}z+\frac1{56},\quad
b(z)=\frac12z^2-\frac3{14}z,\quad c(z)=\frac18z^2.
\]
For a planar support function \(h\), its enclosed area is \(\frac12\int_0^{2\pi}h(h+h'')\,d\theta\). By orthogonality of the circle Fourier modes, this gives the **exact quadratic identity**
\[
v_2(F,t)=1+2t\,a(z)+t^2d(z),\qquad
d(z)=a(z)^2-\frac32b(z)^2-\frac{15}{2}c(z)^2.
\]
Here \(z\) has Beta\((1,4)\) law, while \(s=u\cdot e\) for a uniform sphere direction has \(s^2\) distributed Beta\((1/2,9/2)\). Thus for every nonnegative integer \(r\),
\[
\mathbb E[z^r]=\frac{(1)_r}{(5)_r},\qquad \mathbb E[s^{2r}]=\frac{(1/2)_r}{(5)_r},
\]
where \((q)_r=q(q+1)\cdots(q+r-1)\) and \((q)_0=1\). These rules determine every moment required below by exact rational arithmetic.

**4. Coefficients and cancellation.** Expand \((1+x)^{-10}\) to order four, then integrate with the preceding Beta moments. The resulting identities are
\[
\begin{aligned}
M_1(t)&=1+\frac{363}{12544}t^2-\frac{1573}{153664}t^3+\frac{4492917}{550731776}t^4+O(t^5),\\
M_2(t)&=1+\frac{363}{6272}t^2-\frac{1573}{76832}t^3+\frac{4968273}{275365888}t^4+O(t^5).
\end{aligned}
\]
For reproducibility, the raw moments are
\[
\begin{gathered}
\mathbb E[Y_e^2]=\frac{33}{62720},\quad \mathbb E[Y_e^3]=\frac{143}{3073280},\quad \mathbb E[Y_e^4]=\frac{31419}{2753658880},\\
\mathbb E[a^2]=\frac1{6272},\quad \mathbb E[a^3]=\frac{29}{6146560},\quad \mathbb E[a^4]=\frac{291}{757256192},\\
\mathbb E[d]=-\frac{143}{62720},\quad \mathbb E[ad]=-\frac{17}{307328},\\
\mathbb E[a^2d]=-\frac{61473}{15145123840},\quad\mathbb E[d^2]=\frac{115287}{2163589120}.
\end{gathered}
\]
All first-order terms vanish. If \(A_2,A_3,A_4\) denote the displayed coefficients of \(M_1\), and \(B_2,B_3,B_4\) those of \(M_2\), then \(B_2=2A_2\) and \(B_3=2A_3\). Consequently the degree-two and degree-three terms of \(\Delta\) cancel exactly. Since \(\log(1+u)=u-u^2/2+O(u^3)\), the degree-four coefficient of \(\Delta\) equals
\[
\frac{B_4-2A_4-A_2^2}{20}=\boxed{\frac{139863}{3147038720}}>0.
\]
For small \(|t|\), all projected volumes are uniformly positive over their compact Grassmannians, so their negative powers and integrated logarithms are analytic near zero. Their Taylor expansions therefore have genuine uniform \(O(t^5)\) remainders, proving the two-sided strict sign for sufficiently small nonzero \(t\).

## Verification

The included `verify.py` uses only Python standard-library exact fractions, binomial coefficients, and beta-moment polynomials to reconstruct every rational coefficient, its cancellations, the positive quartic coefficient, and the stated curvature bound. It prints `VERIFY_OK` when all assertions pass. Independent high-precision quadrature also evaluated \(\Delta(t)\) at \(t=\pm0.1,\pm0.05,\pm0.02\); the resulting ratios \(\Delta(t)/t^4\) approached the displayed rational constant from both sides. Numerical checks are corroborative only; the proof of the local inequality is the exact moment computation plus analyticity.

## Relationship to prior work

Chen, Li and Wang's 2026 monotonicity paper supplies the canonical zonal quartic perturbation and proves a negative second-order comparison coefficient under the strict condition \(n>(m+2)(k+2)-2\). It provides only a second-order expansion with an \(O(t^3)\) remainder at the critical equality \(n=(m+2)(k+2)-2\). The present result addresses its first pair \((m,k)=(1,2)\) at equality \(n=10\), identifying cancellation of the next term and the sign of the first surviving term. Milman and Yehudayoff's sharp affine isoperimetric inequalities bound each normalized affine quermassintegral against the terminal quantity and establish certain cross-dimensional comparisons, but their relevant comparison theorem assumes the higher projection dimension is at least the absolute moment exponent; \(2<10\) here. Neither inspected statement yields this critical local quartic coefficient.

## Limitations

The inequality is proved only along the explicitly specified zonal-harmonic support deformation in dimension ten and only for sufficiently small nonzero parameters. It does not prove the full affine-quermassintegral monotonicity conjecture at this dimension, does not classify other perturbations or optimize a fourth-order stability constant, and gives no explicit threshold for strict positivity throughout the entire convexity range. A mathematically equivalent prior calculation outside the inspected literature cannot be categorically excluded. The verification script checks exact algebra but is not an independent scientific audit.

## References

1. S. Chen, Y. Li, X. Wang, *On the monotonicity of affine quermassintegrals*, arXiv:2604.26828v1, first posted 2026-04-29; inspected open-access text: https://arxiv.org/html/2604.26828v3 .
2. E. Milman, A. Yehudayoff, *Sharp Isoperimetric Inequalities for Affine Quermassintegrals*, arXiv:2005.04769; inspected open-access text: https://arxiv.org/html/2005.04769v4 .
