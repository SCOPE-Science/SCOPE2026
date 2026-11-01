# Exact Möbius phase diagram for atomic weighted Bergman kernel zeros

## Finding

Fix \(\alpha>-1\), a point \(a\in\mathbb D\), and an atomic strength \(h>0\). Equip the holomorphic weighted Bergman space on \(\mathbb D\) with the norm
\[
\|f\|_{\alpha,h,a}^2=\frac{\alpha+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z)+h|f(a)|^2.
\]
Write \(\lambda=\alpha+2>1\), \(\mu=h(1-|a|^2)^{-\lambda}\), and \(\varphi_a(z)=(a-z)/(1-\overline a z)\). The reproducing kernel has precisely the zero fibres
\[
\varphi_a(z)\overline{\varphi_a(w)}=
1-\rho\exp(2\pi i k/\lambda),\qquad
\rho=(1+\mu^{-1})^{1/\lambda},
\]
where \(k\) ranges over the integers satisfying
\[
|k|<\lambda/6,\qquad
\mu>\mu_k(\lambda):=\Big[(2\cos(2\pi k/\lambda))^\lambda-1\Big]^{-1}.
\]
All scalar zeros are distinct and simple. Their exact number is
\[
N(\lambda,\mu)=
\begin{cases}
0,&\rho\ge2,\\
2\left\lceil\dfrac{\lambda}{2\pi}\arccos(\rho/2)\right\rceil-1,&1<\rho<2.
\end{cases}
\]
Consequently, the kernel is zero-free exactly when \(\mu\le(2^\lambda-1)^{-1}\); a nonreal conjugate scalar pair occurs for some finite mass exactly when \(\lambda>6\), equivalently \(\alpha>4\). For fixed \(\lambda\), as \(\mu\to\infty\), the number of scalar zeros saturates at \(2\lceil\lambda/6\rceil-1\). For every fixed \(a\in\mathbb D\) and \(h>0\), the number grows according to \(N(\lambda,\mu)/\lambda\to1/3\) as \(\lambda\to\infty\). The first nonreal-pair threshold has the critical divergence
\[
\mu_1(\lambda)\sim\frac{\sqrt3}{\pi(\lambda-6)}\quad(\lambda\downarrow6).
\]
For each fixed \(\lambda\) and permitted \(k\), the squared modulus of the corresponding scalar zero decreases strictly with \(\mu\), crossing the unit circle transversally at \(\mu=\mu_k\).

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(dA\) is Euclidean area, \(\alpha>-1\), \(h>0\), and \(a\in\mathbb D\). The norm is a Hilbert norm on the same set of holomorphic functions as the usual weighted Bergman space: by bounded point evaluation, \(\|f\|_\alpha^2\le\|f\|_{\alpha,h,a}^2\le(1+hK_0(a,a))\|f\|_\alpha^2\). No assertion is made about arbitrary singular measures, multiple point masses, or nonanalytic functions.

A **scalar zero** is a complex number \(u\in\mathbb D\) such that \(K_{\alpha,h,a}(z,w)=0\) for some \(z,w\in\mathbb D\) satisfying \(u=\varphi_a(z)\overline{\varphi_a(w)}\). Each scalar zero determines an infinite fibre of distinct pairs. The count \(N\) counts scalar fibres, not the infinitely many individual zero pairs, and it is not the zero count of \(z\mapsto K_{\alpha,h,a}(z,w)\) for a fixed \(w\). Every scalar root \(u\) is attainable: choose \(r\) real with \(|u|<r<1\), put \(w=\varphi_a(r)\) and \(z=\varphi_a(u/r)\).

## Proof

**1. Kernel under an atomic change of norm.** The unperturbed normalized weighted Bergman kernel is
\[
K_0(z,w)=(1-z\overline w)^{-\lambda},\qquad
K_0(a,a)=(1-|a|^2)^{-\lambda}.
\]
All powers use the analytic logarithm on the right half-plane, which contains \(1-z\overline w\). The reproducing-kernel rank-one update, verified directly in the new inner product, is
\[
K_{\alpha,h,a}(z,w)=K_0(z,w)-
\frac{hK_0(z,a)K_0(a,w)}{1+hK_0(a,a)}.\tag{1}
\]
Indeed \(K_{\alpha,h,a}(a,w)=K_0(a,w)/(1+hK_0(a,a))\), so the evaluation term in the new inner product cancels the rank-one subtraction, leaving the evaluation \(f(w)\). This proves (1) without assuming an operator-theoretic perturbation theorem.

**2. Möbius normalization.** The disk automorphism \(\varphi_a(z)=(a-z)/(1-\overline a z)\) satisfies
\[
1-\varphi_a(z)\overline{\varphi_a(w)}
=\frac{(1-|a|^2)(1-z\overline w)}{(1-\overline a z)(1-a\overline w)}.
\]
The analytic branches agree by continuation from \(z=w=a\) and the simply connected bidisk. Hence, with \(u=\varphi_a(z)\overline{\varphi_a(w)}\),
\[
\frac{K_0(z,w)K_0(a,a)}{K_0(z,a)K_0(a,w)}=(1-u)^{-\lambda}.
\]
Substitute into (1) to obtain the exact factorization
\[
K_{\alpha,h,a}(z,w)=\frac{K_0(z,a)K_0(a,w)}{K_0(a,a)}
\left[(1-u)^{-\lambda}-\frac\mu{1+\mu}\right].\tag{2}
\]
The prefactor never vanishes, and every \(u\in\mathbb D\) can be represented as in the assumptions. Thus the two-variable zero question is precisely the scalar equation from (2).

**3. All roots and sharp entry criteria.** Put \(\tau=\mu/(1+\mu)\in(0,1)\) and \(\rho=\tau^{-1/\lambda}>1\). Because \(\operatorname{Re}(1-u)>0\) whenever \(|u|<1\), the principal logarithm gives
\[
(1-u)^{-\lambda}=\tau
\iff -\lambda\operatorname{Log}(1-u)=\log\tau+2\pi i m
\]
for some integer \(m\). Reversing the sign of this integer yields the proposed candidates \(u_k=1-\rho e^{2\pi i k/\lambda}\). A candidate belongs to the open disk if and only if
\[
|u_k|^2=1+\rho^2-2\rho\cos(2\pi k/\lambda)<1,
\quad\text{i.e.}\quad \rho<2\cos(2\pi k/\lambda).\tag{3}
\]
For such a root the principal-argument restriction selects the unique integer representative with \(|2\pi k/\lambda|<\pi/3\), equivalently \(6|k|<\lambda\): indeed \(\rho>1\) forces \(2\cos(2\pi k/\lambda)>1\), and the actual argument of \(1-u_k\) is in \((-\pi/2,\pi/2)\). No other logarithm branch yields an interior root. On this range the right side of (3) is greater than one, and (3) is equivalent to \(\mu>\mu_k(\lambda)\). The cases of equality are boundary roots and are excluded from the count. The permitted roots cannot coincide, since two distinct such integer indices differ by less than \(\lambda/3\), while equality of their exponentials would require a nonzero integer multiple of \(\lambda\). Every root is simple because the derivative of \((1-u)^{-\lambda}-\tau\) is \(\lambda(1-u)^{-\lambda-1}\ne0\).

**4. Counting, monotonicity and phase boundaries.** For \(\rho<2\), the admissible indices are precisely the integers
\[
|k|<q:=\frac\lambda{2\pi}\arccos(\rho/2).
\]
Since \(0<q<\lambda/6\), the number is \(2\lceil q\rceil-1\), including the case that \(q\) is an integer (the endpoint indices are excluded). When \(\rho\ge2\), no indices qualify. Thus the zero-free threshold comes from \(k=0\). For each fixed \(\lambda\), the strictly increasing thresholds \(\mu_0<\mu_1<\cdots\) cause one real root followed by successively entering conjugate pairs. A nonzero index can qualify at some finite mass exactly when \(\lambda>6\).

For \(\theta_k=2\pi k/\lambda\), differentiation of \(\rho=(1+\mu^{-1})^{1/\lambda}\) gives
\[
\frac{d\rho}{d\mu}=-\frac{\rho}{\lambda\mu(1+\mu)},\qquad
\frac{d|u_k|^2}{d\mu}=-\frac{2\rho(\rho-\cos\theta_k)}{\lambda\mu(1+\mu)}<0.\tag{4}
\]
The inequality uses \(\rho>1\ge\cos\theta_k\). At the threshold \(\rho=2\cos\theta_k\) the derivative is \(-4\cos^2\theta_k/[\lambda\mu_k(1+\mu_k)]<0\), proving transverse entry. As \(\mu\to\infty\), \(q\uparrow\lambda/6\) and the exact saturation count follows. For fixed \(a,h\), \(\mu=h(1-|a|^2)^{-\lambda}\ge h\), hence \(\rho\to1\) as \(\lambda\to\infty\); then \(q/\lambda\to1/6\) and \(N/\lambda\to1/3\). Finally, Taylor expansion at \(\lambda=6+\varepsilon\) gives
\[
(2\cos(2\pi/\lambda))^\lambda-1
=\frac\pi{\sqrt3}\varepsilon+O(\varepsilon^2),
\]
so inversion proves the displayed divergence of the first nonreal threshold. All claimed boundaries follow.

## Verification

The standalone `check.py` uses only the Python standard library. It checks the rank-one kernel against the monomial series, the fractional-power Möbius identity for deterministic test points, the complete integer count versus direct root filtering, selected argument-principle winding numbers, threshold crossings and derivative finite differences, and realization of scalar zeros by disk pairs. Execute `python check.py`. In the recorded execution **2,491 deterministic assertions passed**. The contour sampler is finite and never replaces the branch and modulus arguments in the proof. The global uniqueness, counts, and asymptotics follow analytically from Steps 1–4, not from numerical sampling.

## Relationship to prior work

Perälä (arXiv:1703.05976v1, Section 3 and Remark 3.2) proves that suitably chosen radial absolutely continuous weights can produce arbitrarily many Bergman kernel zeros, and discusses the effect of equivalent Hilbert norms. That supplies the motivation but not an atomic mass threshold or the Möbius-invariant complete zero diagram. Boudreaux (arXiv:1802.01099v1, Theorem 2) proves the stronger **qualitative** general existence of an equivalent weight with kernel zeros and therefore already covers mere existence; the contribution here is the exact classification for a prescribed, single-atom measure family, the sharp first nonreal bifurcation, and the count asymptotic. Han–Qiu–Wang (arXiv:2111.07575v1, Theorem 1.1) establish a general completeness/point-evaluation principle for positive Radon measures, not this zero classification. Miña-Díaz (arXiv:2212.08118v1, Theorem 1.1) develops explicit representations for absolutely continuous weights from products of Blaschke-factor powers, without the displayed atomic rank-one zero diagram.

A separate radial-weight result using \(1-q|z|^{2\gamma}\) proves zero-freeness for all its allowed continuous density parameters; its norm and kernel family differ from the present positive Dirac perturbation. Studies of Bergman jet Gram kernels concern derivative evaluations as feature functionals rather than adding a point mass to the norm. Neither class subsumes the asserted singular-measure phase boundaries. The rank-one identity (1) and the disk automorphism are classical tools; novelty is **not** claimed for those tools alone. Priority risk remains from unindexed atomic-measure or rank-one kernel literature.

## Limitations

Only one positive atom, the standard power-weighted analytic disk space, and finite positive atomic strength are treated. For a fixed \(w\), its actual number of zeros in \(z\) depends additionally on \(|\varphi_a(w)|\); the theorem counts intrinsic scalar zero fibres instead. Zero multiplicities are scalar multiplicities, not a finite count of pairs in the bidisk. The numerical checks are finite and cannot certify global statements. The originality comparison is not an exhaustive historical proof, and no independent mathematical validation has been performed.

## References

- A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1 (March 17, 2017), https://arxiv.org/abs/1703.05976.
- B. J. Boudreaux, *Equivalent Bergman Spaces With Inequivalent Weights*, arXiv:1802.01099v1 (February 4, 2018), https://arxiv.org/html/1802.01099v1.
- Y. Han, Y. Qiu, Z. Wang, *Complete weighted Bergman spaces have bounded point evaluations*, arXiv:2111.07575v1 (November 15, 2021), https://arxiv.org/abs/2111.07575.
- E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118v1 (December 15, 2022), https://arxiv.org/abs/2212.08118.
- *Zero-free power-deficit radial Bergman kernels* (2026), publicly available mathematical result on continuous radial-density perturbations; different from the present atomic measure.
