# Uniform volume has strictly larger affine projection amplification than cone-boundary sampling

## Finding

Let \(d\ge 1\), and let \(K\subset\mathbb R^d\) be a compact convex body with nonempty interior and centroid at the origin. Write \(\mu\) for normalized \(d\)-dimensional volume on \(K\). Define its **radial cone-boundary probability** \(\nu\) as the law of
\[
Z=Y/\|Y\|_K,\qquad Y\sim\mu,
\]
where \(\|\cdot\|_K\) is the Minkowski gauge of \(K\). Thus \(Z\in\partial K\), and \(\nu\) is not ordinary surface-area probability in general. For each \(\rho\in\{\mu,\nu\}\), let \(P_\rho\) be the \(L^2(\rho)\)-orthogonal projector onto restrictions of all real affine functions, viewed as affine outputs on \(K\). Set
\[
\Lambda_\rho(x)=\int|\mathcal K_\rho(x,y)|\,d\rho(y),\qquad x\in K,
\]
where \(\mathcal K_\rho\) is the affine reproducing kernel. Its \(L^\infty(\rho)\)-operator norm is \(\max_{x\in K}\Lambda_\rho(x)\).

**Universal pointwise ordering.** For every centered convex body and every \(x\in K\),
\[
\boxed{\Lambda_\mu(x)\ge\Lambda_\nu(x).}
\]
An explicit formula for the nonnegative difference and its exact equality criterion are given below. **Strict norm separation.** If \(K=-K\), then the inequality is strict for **every** \(x\in\partial K\), and consequently
\[
\boxed{\|P_\mu\|_{L^\infty\to L^\infty}>\|P_\nu\|_{L^\infty\to L^\infty}\qquad(d\ge1).}
\]
The same strict comparison holds for the largest negative values that the two projectors can produce from inputs between zero and one, since those sharp positivity-loss defects equal \((\|P_\rho\|_{\infty\to\infty}-1)/2\).

For a concrete sharp benchmark, on the Euclidean unit disk \(B^2\), \(\nu\) is uniform angular measure on the circle and
\[
\boxed{\|P_\mu\|_{\infty\to\infty}=\frac{11\sqrt{15}}{8\pi}+\frac2\pi\arcsin\!\left(\frac14\right),\qquad
\|P_\nu\|_{\infty\to\infty}=\frac13+\frac{2\sqrt3}{\pi}.}
\]
These are approximately \(1.8559734677\) and \(1.4359911242\), respectively. On an interval, the corresponding values are exactly \(5/3\) and \(1\).

## Assumptions and scope

Only first-degree (affine) least-squares projectors are compared. A common convex body serves as the output domain, but the two input measures and their \(L^2\) inner products differ. The boundary law is the radial pushforward of interior volume, often called the boundary version of cone-volume measure; on a polytope it is uniform within each facet, with facet masses proportional to their cone volumes. The pointwise inequality needs merely that \(K\) be centered; central symmetry is used to prove strict separation at every boundary point. All statements include dimension one.

The scalar kernel is the real reproducing kernel. The same operator norms apply to complex-valued input functions, because the pointwise integral-operator norm is the integral of the absolute kernel. No claim is made for higher polynomial degrees, ordinary surface-area sampling on a nonspherical body, or nonlinear projections.

## Proof

**1. Radial disintegration.** Let \(R=\|Y\|_K\) and \(Z=Y/R\), ignoring the zero event. Since \(\mu(rK)=r^d\) for \(0\le r\le1\), homogeneity shows that \(R\) and \(Z\) are independent and
\[
\mathbb P(R\le r)=r^d,\qquad d\mathbb P_R(r)=d r^{d-1}\,dr.
\]
In particular, \(\mathbb ER=d/(d+1)\), \(\mathbb ER^2=d/(d+2)\), and \(\mathbb EZ=0\) because \(\mathbb EY=0\). Put
\[
\Sigma=\mathbb E(ZZ^{\mathsf T}).
\]
Full dimensionality makes \(\Sigma\) positive definite; the covariance of \(Y\) is \(d\Sigma/(d+2)\).

**2. Kernels.** The constant and coordinate functions are mutually orthogonal under each centered probability, except for the coordinate covariance matrix. Thus, for \(u_x(z)=x^{\mathsf T}\Sigma^{-1}z\),
\[
\mathcal K_\nu(x,z)=1+u_x(z),\qquad
\mathcal K_\mu(x,rz)=1+\frac{d+2}{d}\,r u_x(z).
\]
Both kernels have integral one. The two corresponding Lebesgue functions are continuous and convex in \(x\).

**3. An exact one-dimensional positive-part comparison.** Define \(s_x(z)=(-u_x(z))_+\) and, for \(s\ge0\),
\[
G_d(s)=\mathbb E_R\left[\left(\frac{d+2}{d}sR-1\right)_+\right].
\]
Elementary integration at the single sign-changing radius gives
\[
G_d(s)=
\begin{cases}
0,&0\le s\le d/(d+2),\\[2mm]
\displaystyle\frac{d+2}{d+1}s-1+\frac1{d+1}
\left(\frac{d}{(d+2)s}\right)^d,&s>d/(d+2).
\end{cases}
\]
Because \(\mathbb E_Zu_x(Z)=0\), the identity \(|v|=v+2(-v)_+\) yields
\[
\Lambda_\mu(x)=1+2\mathbb E_Z G_d(s_x(Z)),
\qquad
\Lambda_\nu(x)=1+2\mathbb E_Z(s_x(Z)-1)_+.
\]
Consequently, the **exact defect formula** is
\[
\boxed{\Lambda_\mu(x)-\Lambda_\nu(x)=2\mathbb E_Z\left[G_d(s_x(Z))-(s_x(Z)-1)_+\right].}
\]
For \(s\le d/(d+2)\), both terms vanish. For \(d/(d+2)<s\le1\), \(G_d(s)>0\) and the other term is zero. For \(s>1\),
\[
G_d(s)\ge\mathbb E_R\left[\frac{d+2}{d}sR-1\right]
=\frac{d+2}{d+1}s-1>s-1.
\]
Thus the integrand is nonnegative everywhere, and is positive precisely when \(s>d/(d+2)\). This proves the pointwise ordering, with exact equality criterion
\[
\boxed{\Lambda_\mu(x)=\Lambda_\nu(x)
\iff \nu\{z:u_x(z)<-d/(d+2)\}=0.}
\]

**4. Strictness on centrally symmetric bodies.** Fix \(x\in\partial K\). Choose a supporting linear functional \(\ell\) normalized so that \(\ell(x)=1\) and \(|\ell(z)|\le1\) throughout \(K\); symmetry ensures the latter. Then \(\ell^{\mathsf T}\Sigma\ell=\mathbb E\ell(Z)^2\le1\). Cauchy--Schwarz for the positive definite matrix \(\Sigma\) gives
\[
1=(\ell^{\mathsf T}x)^2\le (\ell^{\mathsf T}\Sigma\ell)(x^{\mathsf T}\Sigma^{-1}x)
\le x^{\mathsf T}\Sigma^{-1}x.
\]
The antipode \(-x\) lies in \(\partial K\), and therefore \(u_x(-x)\le-1<-d/(d+2)\). The cone-boundary law has full support on \(\partial K\), so a relative neighborhood of \(-x\) has positive \(\nu\)-measure and still satisfies the strict threshold. The equality criterion proves \(\Lambda_\mu(x)>\Lambda_\nu(x)\) for every boundary \(x\). Convexity and continuity ensure that \(\Lambda_\nu\) attains its maximum at a boundary point; strict separation at this point proves the asserted operator-norm inequality.

**5. Explicit benchmarks.** On \([-1,1]\), the cone law is uniform on the two endpoints; its affine projection is identity and has norm one. Uniform interior measure has kernel \(1+3xy\) and norm \(\frac12\int_{-1}^1|1+3y|dy=5/3\). On the unit disk, rotational symmetry reduces maxima to the circle. The circular boundary has kernel \(1+2\cos\theta\) at a unit boundary point, giving
\[
\frac1{2\pi}\int_0^{2\pi}|1+2\cos\theta|d\theta
=\frac13+\frac{2\sqrt3}{\pi}.
\]
The disk-volume kernel at the same point is \(1+4y_1\), and the first-coordinate density is \(\frac2\pi\sqrt{1-y_1^2}\) on \([-1,1]\). Integrating across the sign change at \(-1/4\) yields
\[
\frac2\pi\int_{-1}^1|1+4t|\sqrt{1-t^2}\,dt
=\frac{11\sqrt{15}}{8\pi}+\frac2\pi\arcsin(1/4).
\]
Finally, for a nonnegative input bounded by one, the negative kernel mass at \(x\) is \((\Lambda_\rho(x)-1)/2\); taking the supremum proves the positivity-loss interpretation.

## Verification

The self-contained companion `check.py` verifies the closed formula for \(G_d\) against independent numerical radial quadrature for dimensions \(1,2,3,5,11\) and several thresholds, and checks the exact one-dimensional and disk constants using distinct integral representations. It additionally tests the pointwise defect identity on triangles and regular polygons through independent perimeter quadrature. Its recorded result is `PASS: 91 analytical-formula consistency assertions`. The infinite-dimensional and all-body conclusions above are proved analytically, not inferred from these finite consistency tests.

## Relationship to prior work

Böröczky and Henk (arXiv:1407.7272) define cone-volume measure and develop subspace concentration and stability inequalities; their theorems concern convex-geometric measures, not affine least-squares projector norms. Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424) study boundedness of \(L^2\) least-squares projectors in kernel approximation on manifolds, with a local stable basis; their statements do not compare interior-volume and cone-boundary affine projectors. A published exact affine projector calculation on a simplex addresses uniform volume alone and supplies no cross-measure ordering. These papers motivate the combined geometric/approximation question, while the comparison here depends on the exact radial law and a new positive-part inequality.

The radial disintegration itself, covariance scaling, affine reproducing kernels, and cone-volume measure are standard ingredients. The claimed contribution is their complete combination into a **pointwise universal Lebesgue-function comparison with an exact equality criterion**, and the strict norm ordering for every centrally symmetric convex body. In particular, the simplex norm formula under interior volume does not imply a comparison with its distinct boundary-cone projector. Public literature searches and the examined primary results did not identify an equivalent theorem; this is not a proof of priority.

## Limitations

The ordering may fail for unrelated pairs of sampling measures and is not asserted beyond the radial cone-boundary law. Without central symmetry the pointwise nonstrict inequality still holds, but no blanket strictness is asserted. The result determines a comparison, not separate exact projector norms for arbitrary bodies. It does not address higher-degree polynomial spaces. A differently named historical formulation involving radial mixtures of reproducing kernels is a residual bibliographic risk. Mathematical and bibliographic validation by an independent party has not been performed.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424, first posted 2010-05-13, especially introduction and Section 5.
2. K. J. Böröczky and M. Henk, *Cone-Volume Measure and Stability*, arXiv:1407.7272, first posted 2014-07-27, especially definition (1.1), the introductory theorems, and cone-volume facets formula (1.2).
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, publicly accessible result, 2026-10-04, `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34`.
