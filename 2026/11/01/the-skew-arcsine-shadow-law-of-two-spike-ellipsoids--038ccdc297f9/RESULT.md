# The skew-arcsine shadow law of two-spike ellipsoids

## Finding
Let \(d\ge3\), \(a>c>b>0\), and
\[
E_d=\left\{x\in\mathbb R^d:\frac{x_1^2}{a^2}+\frac{x_2^2}{c^2}+\sum_{j=3}^d\frac{x_j^2}{b^2}\le1\right\}.
\]
For a Haar-uniform hyperplane \(H=U^\perp\), let \(R_d(U)\) be **half the Euclidean diameter of the orthogonal projection** \(\Pi_H E_d\), not of the central section \(E_d\cap H\). Set
\[
A=a^2-b^2,\qquad B=c^2-b^2,\qquad \Lambda_d=R_d(U)^2-b^2,
\]
so \(0<B<A\). The support of \(\Lambda_d\) is exactly \([B,A]\). For every \(B<t<A\), put
\[
\alpha=A(t-B),\quad \beta=B(A-t),\quad \gamma=(A-t)(t-B),
\quad\vartheta_t=\arctan\sqrt{\frac{t-B}{A-t}}.
\]
Its **complete all-dimensional distribution** is
\[
\boxed{\mathbb P(\Lambda_d\le t)=\frac2\pi\int_0^{\vartheta_t}\left(1-\frac{\gamma}{\alpha\cos^2\theta-\beta\sin^2\theta}\right)^{(d-2)/2}\,d\theta.}
\]
The CDF is zero for \(t\le B\) and one for \(t\ge A\), and there are no atoms. For each fixed interior \(t\), these probabilities are **strictly decreasing** as the integer ambient dimension \(d\) increases.

In dimension \(d=4\), this integral reduces to a two-component beta mixture. Set
\[
W=\frac{\Lambda_4-B}{A-B},\qquad
k=\frac{A-B}{\sqrt{AB}}\operatorname{artanh}\sqrt{\frac BA},
\quad 0<k<1.
\]
Then
\[
\boxed{W\ \overset{\mathrm d}=\ \begin{cases}
\operatorname{Beta}(1/2,3/2),&\text{with probability }(1-k)/2,\\
\operatorname{Beta}(3/2,1/2),&\text{with probability }(1+k)/2.
\end{cases}}
\]
Equivalently its density is an affine tilt of the arcsine density,
\[
\boxed{f_W(w)=\frac{1-k+2kw}{\pi\sqrt{w(1-w)}},\qquad0<w<1.}
\]
An equivalent fully elementary CDF for \(B<t<A\) is
\[
\boxed{\mathbb P(\Lambda_4\le t)=\frac2\pi\left[\arctan\sqrt{\frac{t-B}{A-t}}-\sqrt{\frac{(A-t)(t-B)}{AB}}\operatorname{artanh}\sqrt{\frac BA}\right].}
\]
For fixed distinct semiaxis lengths, the high-dimensional endpoint fluctuation is
\[
\boxed{d\bigl(a^2-R_d(U)^2\bigr)\ \Longrightarrow\ (a^2-b^2)\,Z^2,\qquad Z\sim N(0,1).}
\]
Thus a two-spike projection has a nondegenerate all-dimensional law and a particularly simple four-dimensional skew-arcsine profile.

## Assumptions and scope
The semiaxes \(a>c>b>0\) are fixed as \(d\) varies. \(U\) is uniform on the Euclidean unit sphere; a sign change of \(U\) does not change its hyperplane. The hyperplane is through the center, and \(\Pi_H\) denotes **orthogonal** projection. There is no random translation of the ellipsoid or hyperplane. The Euclidean half-diameter equals the maximum support-function value because \(\Pi_HE_d\) is centrally symmetric. The beta variables in the mixture have standard beta densities on \((0,1)\). The asymptotic statement holds only for the fixed-gap regime \(A>B>0\), and is a distributional limit.

## Proof
**Step 1: compress a rank-two quadratic form.** Write \(Q=\operatorname{diag}(a^2,c^2,b^2,\ldots,b^2)=b^2I+A e_1e_1^{\mathsf T}+B e_2e_2^{\mathsf T}\). The support function of \(E_d\) is \(h_{E_d}(v)=\sqrt{v^{\mathsf T}Qv}\). Hence
\[
R_d^2=\max_{\substack{v\perp U\\ \|v\|=1}}v^{\mathsf T}Qv.
\]
Set \(x=U_1^2\), \(y=U_2^2\). Apart from \(b^2I\), the nonzero eigenvalues of this compression are the eigenvalues of the real symmetric matrix
\[
T=\begin{pmatrix}A(1-x)&-\sqrt{AB}\,U_1U_2\\-\sqrt{AB}\,U_1U_2&B(1-y)\end{pmatrix}.
\]
Thus \(\Lambda_d\) is its largest eigenvalue. The largest eigenvalue belongs to \([B,A]\): the upper bound is immediate, while \(U^\perp\) meets the two-dimensional span of the first two axes nontrivially, so its maximum Rayleigh quotient is at least \(B\). Both endpoints occur at coordinate-normal directions and are in the closure of values realized on open sets, proving exact support. A direct calculation gives
\[
\det(tI-T)=-(A-t)(t-B)+A(t-B)x-B(A-t)y.
\]
The smaller eigenvalue of \(T\) is at most \(B\). Therefore for \(B<t<A\), \(\Lambda_d\le t\) **if and only if**
\[
A(t-B)U_1^2-B(A-t)U_2^2\ge(A-t)(t-B).
\]
This implication does not use a numerical eigenvalue approximation.

**Step 2: exact spherical integration.** Write
\(U_1=\sqrt S\cos\Theta\) and \(U_2=\sqrt S\sin\Theta\). The angle is uniform modulo a full rotation, independent of \(S\), and
\[
S\sim\operatorname{Beta}\left(1,\frac{d-2}{2}\right).
\]
The inequality in Step 1 becomes
\[
S(\alpha\cos^2\Theta-\beta\sin^2\Theta)\ge\gamma.
\]
The right side is positive. The angular threshold permitting any solution is determined by \(\alpha\cos^2\Theta-\beta\sin^2\Theta=\gamma\), or equivalently
\[
\tan^2\Theta=\frac{\alpha-\gamma}{\beta+\gamma}=\frac{t-B}{A-t}.
\]
The allowed angular set consists of four symmetric intervals with total angular fraction \(2\vartheta_t/\pi\). For \(0\le\Theta<\vartheta_t\), the beta survival function is
\[
\mathbb P(S\ge s)=(1-s)^{(d-2)/2}.
\]
Conditioning on \(\Theta\) proves the CDF integral. Its integrand is strictly between zero and one for an interval of positive angular length, so increasing \(d\) strictly decreases every interior CDF value. The endpoint values follow by continuity and the eigenvalue support.

**Step 3: the four-dimensional cancellation.** When \(d=4\), the exponent is one. Substitute \(z=\tan\theta\) into the rational term:
\[
\int_0^{\vartheta_t}\frac{d\theta}{\alpha\cos^2\theta-\beta\sin^2\theta}
=\int_0^{\sqrt{(t-B)/(A-t)}}\frac{dz}{\alpha-\beta z^2}
=\frac{\operatorname{artanh}\sqrt{B/A}}{\sqrt{\alpha\beta}}.
\]
Since \(\gamma/\sqrt{\alpha\beta}=\sqrt{(A-t)(t-B)/(AB)}\), the claimed elementary CDF follows. Differentiate with respect to \(t\):
\[
\frac{d}{dt}\mathbb P(\Lambda_4\le t)
=\frac{1-\frac{\operatorname{artanh}\sqrt{B/A}}{\sqrt{AB}}(A+B-2t)}{\pi\sqrt{(t-B)(A-t)}}.
\]
Applying \(w=(t-B)/(A-B)\) gives \(f_W(w)\). Indeed the standard beta densities with shapes \((1/2,3/2)\) and \((3/2,1/2)\) are respectively \(2(1-w)/(\pi\sqrt{w(1-w)})\) and \(2w/(\pi\sqrt{w(1-w)})\); the proposed mixture yields the displayed affine tilt exactly.

The mixture weights are strictly positive: for \(r=\sqrt{B/A}\in(0,1)\),
\[
k=\frac{1-r^2}{r}\operatorname{artanh}r,
\]
and \(0<\operatorname{artanh}r<r/(1-r^2)\), with the latter inequality obtained by integrating the increasing function \(1/(1-s^2)\) from zero to \(r\). This proves \(0<k<1\), including absence of hidden sign or normalization problems.

**Step 4: endpoint fluctuations in growing dimension.** For fixed \(A>B>0\), the top eigenvalue of \(T\) is a smooth function near \(U_1=U_2=0\), and its first-order expansion in \(x=U_1^2\), \(y=U_2^2\) is \(\Lambda_d=A-Ax+O(xy+x^2+y^2)\). The error is uniform in a fixed neighborhood of zero because the spectral gap is \(A-B>0\). Represent \(U=G/\|G\|\) for standard Gaussian \(G\in\mathbb R^d\). Then \(dU_1^2\Rightarrow Z^2\), while \(d(xy+x^2+y^2)\to0\) in probability. Since \(a^2-R_d^2=A-\Lambda_d\), the claimed chi-square limit follows by Slutsky's theorem.

## Verification
Run the standalone `verify_projection.py` with Python 3, NumPy and SciPy. It checks 1,960 exact rational characteristic-polynomial identities, 76 independent comparisons of the beta-mixture elementary formula against the angular quadrature, 700 random full-matrix shadow-radius eigenvalue comparisons, 24 Monte Carlo CDF comparisons, and strict stochastic ordering at six thresholds. The verifier passed on the packaged source code. Exact rational identities and numerical experiments corroborate, but **do not replace**, Steps 1–4, which establish the infinite-dimensional-family statements.

## Relationship to prior work
Guedon, Litvak, Tatarko, and Vritsiou (2026) study the random **central-section** radius and its high-probability bounds for general convex bodies and \(p\)-ellipsoids. Hinrichs, Krieg, Novak, Prochno, and Ullrich (2019/2021) analyze related random kernel sections of ellipsoids. Both are the motivation for seeking distributional information for natural Gaussian/Haar Grassmannian models. Here the statistic is instead the **largest radius of an orthogonal projection** and the principal axes have **two distinct exceptional values**; a section radius uses a different compressed inverse quadratic form and cannot be interchanged with the projection radius.

A published exact one-spike random-*section* calculation gives a beta transform for rank-one perturbations, not this rank-two random-projection law. The general spectral fact that the nonzero eigenvalues of a product of rectangular matrices agree in reverse order, and the spherical beta law, are standard inputs; the combined skew-arcsine mixture and dimension-ordering result are the new statements claimed here. Searches under two-spike, double-spike, random ellipsoid shadow, affine arcsine, random eigenvalue compression, and triaxial projected-diameter terminology did not identify an exact equivalent.

## Limitations
The exact two-beta-mixture simplification is proved specifically for an **ambient four-dimensional** ellipsoid with one larger and one intermediate semiaxis and all remaining semiaxes equal. The integral formula and stochastic dimension ordering hold for all \(d\ge3\), but we do not claim an elementary beta mixture for arbitrary \(d\), arbitrary semiaxis lists, or random higher-codimensional shadows. The theorem concerns orthogonal shadows, **not** central sections or surface-area sampling. The high-dimensional limit assumes fixed positive spectral gaps. A potentially equivalent formula may exist in older multivariate-spectral statistics or random projection tomography under different terminology; definitive historical priority and independent mathematical review remain outstanding.

## References
1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1, first publicly posted 21 September 2026, https://arxiv.org/abs/2609.24131.
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639v2, https://arxiv.org/html/1901.06639v2; Trans. Amer. Math. Soc. 374 (2021), 8691–8713.
3. D. Rockenfeller, *Modeling Height Distributions in Tilted Ellipsoids With Applications to Pennate Muscle Geometry*, Journal of Applied Mathematics (2026), https://doi.org/10.1155/jama/3099113. This concerns fixed-axis tilted projections and height distributions, not the Haar random maximal radius studied here.
