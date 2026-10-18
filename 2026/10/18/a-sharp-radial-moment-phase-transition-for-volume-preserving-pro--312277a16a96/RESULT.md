# A sharp radial-moment phase transition for volume-preserving products of balls

## Finding
Let \(p,q\ge1\) be integers, \(n=p+q\), and \(B_2^d\) the closed unit Euclidean ball in \(\mathbb R^d\). Consider the determinant-one two-block deformation
\[
K_r=r^{-q/n}B_2^p\times r^{p/n}B_2^q,\qquad r>0,
\]
whose volume equals \(\kappa_p\kappa_q\) with \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\). For \(U\) uniform on \(S^{n-1}\), define its radial function \(\rho_r(U)=\max\{s\ge0:sU\in K_r\}\) and \(M_t(r)=\mathbb E\rho_r(U)^t\), for arbitrary real \(t>0\).

**Theorem.** If \(0<t<n\), there is a unique critical point of \(M_t\), and it is the unique strict global maximum. If \(t>n\), there is a unique critical point, the unique strict global minimum. The optimizer is the unique positive solution of
\[
pJ_+(r)=qJ_-(r),\qquad
J_-(r)=\int_0^1x^{q/2-1}(1+r^2x)^{-(n-t)/2}\,dx,
\quad J_+(r)=\int_1^\infty x^{(q-t)/2-1}(1+r^2x)^{-(n-t)/2}\,dx.
\]
The ratio \(J_+(r)/J_-(r)\) is strictly decreasing on \((0,\infty)\) when \(t<n\), and strictly increasing when \(t>n\). At the transition \(t=n\), \(M_n(r)=\kappa_p\kappa_q/\kappa_n\) is constant.

In particular, for equal block dimensions the optimizer is \(r=1\). For the supercritical moment \(t=n+2\), the optimizer is explicitly \(r=\sqrt{(q+2)/(p+2)}\). These conclusions concern **only the volume-preserving aspect ratio** of the displayed product bodies; no extremal claim is made among arbitrary linear images.

## Assumptions and scope
The Euclidean factors are orthogonal and have integral dimensions \(p,q\ge1\). Their radii are \(a=r^{-q/n}\) and \(b=r^{p/n}\), so \(a^pb^q=1\) and \(r=b/a\). Sphere measure is probability Haar measure. Every positive real moment \(t\), including values above ambient dimension, is well defined because each \(K_r\) contains a positive Euclidean ball. The diameter of the central line section in direction \(U\) equals \(2\rho_r(U)\), so the theorem also optimizes all positive diameter moments. The case \(t=0\), translations, higher-dimensional sections, and shear deformations are not included.

## Proof
**1. Exact radial integral.** Write \(U=(U_p,U_q)\), and set \(S=\|U_p\|^2\). Orthogonal rotational invariance gives \(S\sim\mathrm{Beta}(p/2,q/2)\). With \(Y=(1-S)/S\), the density is
\[
\frac{y^{q/2-1}}{B(p/2,q/2)(1+y)^{n/2}},\qquad y>0.
\]
The radial function becomes
\[
\rho_r(U)=a\sqrt{1+Y}\min\{1,r/\sqrt Y\}.
\]
Put \(\gamma=(n-t)/2\) and
\[
I_0(r)=\int_0^{r^2}y^{q/2-1}(1+y)^{-\gamma}\,dy,\qquad
I_1(r)=\int_{r^2}^{\infty}y^{(q-t)/2-1}(1+y)^{-\gamma}\,dy.
\]
For every finite \(r>0\), both converge, since the large-\(y\) integrand in \(I_1\) is asymptotic to \(y^{-p/2-1}\). Therefore
\[
M_t(r)=\frac{r^{-qt/n}}{B(p/2,q/2)}\bigl(I_0(r)+r^tI_1(r)\bigr).
\]

**2. The derivative and its exact sign.** Differentiating with respect to \(\log r\), the moving-boundary terms from \(I_0\) and \(r^tI_1\) cancel. Consequently,
\[
\frac{dM_t}{d\log r}=
\frac{t\,r^{-qt/n}}{nB(p/2,q/2)}
\bigl(p r^tI_1(r)-qI_0(r)\bigr).
\]
Substituting \(y=r^2x\) gives \(I_0=r^qJ_-\) and \(r^tI_1=r^qJ_+\). Thus the derivative has the sign of \(pJ_+-qJ_-\). The integrals \(J_-\) and \(J_+\) are positive and finite for every \(r>0,t>0\).

**3. Strict single crossing.** Put \(u=r^2\). Differentiation under the two integrals is justified on each compact interval of \(u>0\) by their endpoint bounds. Normalize the integrands of \(J_-\) and \(J_+\) as probability densities on \((0,1)\) and \((1,\infty)\), respectively, and denote expectations under these laws by \(\mathbb E_-\) and \(\mathbb E_+\). Then
\[
\frac{d}{du}\log\frac{J_+}{J_-}=
-\gamma\left(\mathbb E_+\frac{X}{1+uX}-\mathbb E_-\frac{X}{1+uX}\right).
\]
The function \(x/(1+ux)\) is strictly increasing for \(x>0\). Every point in the first support is smaller than every point in the second, so the difference of expectations is strictly positive. The logarithmic derivative therefore has the strict sign of \(t-n\).

The endpoint ratios, with zero interpreted as a limit and with logarithmic divergence at boundary indices, are
\[
\lim_{r\downarrow0}\frac{J_+}{J_-}=
\begin{cases}+\infty,&t\le q,\\q/(t-q),&t>q,\end{cases}
\qquad
\lim_{r\to\infty}\frac{J_+}{J_-}=
\begin{cases}0,&t\le p,\\ (t-p)/p,&t>p.\end{cases}
\]
For instance, the finite left endpoint follows by setting \(r=0\) in the integrable \(t>q\) expressions; the finite right endpoint follows after factoring \((r^2)^{-\gamma}\) and applying dominated convergence when \(t>p\). For \(t\le q\) at the left and \(t\le p\) at the right, the appropriate divergent or logarithmic asymptotics give the stated infinite or zero limits. These limits are valid whether \(\gamma\) is positive or negative.

If \(0<t<n=p+q\), the left ratio is strictly larger than \(q/p\), and the right ratio is strictly smaller. If \(t>n\), the inequalities reverse. Therefore \(J_+/J_-\) crosses \(q/p\) exactly once, and its strict monotonicity gives exactly one critical point. The derivative is first positive then negative in the subcritical range, and first negative then positive in the supercritical range. This proves the unique strict global maximum or minimum, with no assumption about an unverified existence theorem.

**4. Critical and explicit special cases.** Polar integration gives
\[
M_n(r)=\frac{\operatorname{Vol}_n(K_r)}{\kappa_n}=\frac{\kappa_p\kappa_q}{\kappa_n},
\]
independent of \(r\). If \(p=q\), swapping the factors maps \(r\) to \(1/r\), so uniqueness forces \(r_*=1\) for every \(t\ne n\). Finally, polar integration at \(t=n+2\) relates \(M_t\) to \(\int_{K_r}\|x\|^2\,dx\), whose variable part is proportional to
\[
\frac{p}{p+2}r^{-2q/n}+\frac{q}{q+2}r^{2p/n}.
\]
Differentiation gives the unique minimizer \(r_*^2=(q+2)/(p+2)\). This last identity is consistent with the established isotropic-position extremal principle; it is not claimed as a newly discovered general principle.

## Verification
A standalone Python 3 file `CHECK.py` numerically evaluates the two exact angular integrals using composite Simpson quadrature. The checker tests five optimizer values, signs of local optimality, twenty instances of critical-moment volume invariance, three supercritical isotropic benchmarks, and the exact \(p=q=2,t=1\) moment \(4-2\sqrt2\). The observed output is `VERIFY_OK roots=5 critical_moments=20 isotropic_checks=3 closed_example=1`. The checker is supplemental; the single-crossing proof above treats every permitted parameter, not just sampled values. One representative nontrivial optimizer is \(r_*\approx1.0934711358927625\) for \(p=2,q=3,t=1\).

## Relationship to prior work
Guédon, Litvak, Tatarko, and Vritsiou (2026) study random diameters of general convex-body sections and \(\ell_p\)-ellipsoids, motivating a precise one-dimensional distributional optimization. Bastero and Romance (2003) formulate dual-quermassintegral extremal positions and obtain general necessary isotropy conditions; their discussion notes the lack of a general sufficient criterion in the subcritical interval. Bastero, Bernués, and Romance (2006) give general sufficient criteria and uniqueness in a supercritical index range, so the existence/uniqueness phenomenon above for \(t>n\) must not be attributed as wholly new. The content established here is the explicit, uniform two-block spherical-beta integral formula and strict optimizer classification, particularly subcritical sufficiency along all volume-preserving aspect ratios. No claim of global novelty or unrestricted affine optimality is made.

## Limitations
The comparison class consists solely of centered, orthogonal two-factor Euclidean-ball products under determinant-one rescaling of the two blocks. It does not prove the optimizer is extremal among all determinant-one linear images, nor does it address higher-dimensional sections or translations. The optimizer generally has an implicit integral characterization, not an elementary closed form. Older or unindexed stereological or dual-quermassintegral literature could contain an equivalent explicit product-ball calculation; scientific priority is not independently certified.

## References
1. O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On random diameters of convex bodies* (first public version September 21, 2026), https://arxiv.org/abs/2609.24131.
2. J. Bastero and M. Romance, *Positions of convex bodies associated to extremal problems and isotropic measures*, *Advances in Mathematics*, DOI 10.1016/S0001-8708(03)00095-1, https://anamat.unizar.es/bastero/archivos/Positionsof.pdf.
3. J. Bastero, J. Bernués, and M. Romance, *Dual quermassintegrals, extremal positions and isotropic measures* (2006), https://anamat.unizar.es/bastero/archivos/Dual_quermass.pdf.
