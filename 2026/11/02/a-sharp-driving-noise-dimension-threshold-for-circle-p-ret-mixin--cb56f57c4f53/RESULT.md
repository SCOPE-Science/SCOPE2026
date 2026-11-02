# A sharp driving-noise dimension threshold for circle p-Ret mixing and discrete Poisson solvability

## Finding

A parameter-coordinate retraction (p-Ret) heat walk on the circle has a sharp and rather surprising threshold at the number of **driving-noise coordinates**. Different factorizations of the **same** scalar diffusion tensor give the same continuous heat equation and the same small-step generator, yet have fundamentally different fixed-step long-time behavior.

For every integer \(r\ge1\) and \(h>0\), let \(P_{r,h}\) be the one-step operator defined below, and let \(\Pi\) denote projection onto constants in Haar-normalized \(L^2(\mathbb T)\).

* At \(r=1\), \(\|P_{1,h}^n-\Pi\|_{2\to2}=1\) for **every** \(n\ge1\); the discrete mean-zero Poisson inverse is not bounded. The walk is nonergodic if \(\sqrt h/\pi\) is rational; otherwise it converges strongly to Haar on \(L^2\), without an operator-norm rate. For every finite \(n\), the law started at a point is atomic and has total-variation distance one from Haar.
* For **every** \(r\ge2\), the exact sharp number
  \[
  q_r(h)=\sup_{k\ge1}|\rho_{r,k}(h)|<1
  \]
  gives \(\|P_{r,h}^n-\Pi\|_{2\to2}=q_r(h)^n\). Transition laws from points converge to Haar exponentially in total variation, and the mean-zero discrete Poisson operator has a bounded inverse on \(L^2\).

The multiplier for nonzero integer frequencies is
\[
\rho_{r,k}(h)=\Gamma(r/2)\left(\frac{2}{|k|\sqrt{rh}}\right)^{r/2-1}
J_{r/2-1}(|k|\sqrt{rh}),
\]
where \(J_\nu\) is the Bessel function of the first kind; in particular
\[
\rho_{1,k}=\cos(k\sqrt h),\qquad
\rho_{2,k}=J_0(k\sqrt{2h}),\qquad
\rho_{3,k}=\frac{\sin(k\sqrt{3h})}{k\sqrt{3h}}.
\]

## Assumptions and scope

Take the unit circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), globally parametrized modulo period by \(\Phi(\theta)=(\cos\theta,\sin\theta)\). Its induced metric is one and its Christoffel symbol in the coordinate \(\theta\) is zero. The intended generator is \(\mathcal L=\tfrac12\partial_\theta^2\). For each positive integer \(r\), choose \(r\) identical smooth noise fields
\[
\sigma_j=r^{-1/2}\partial_\theta,\qquad j=1,\ldots,r.
\]
Their total tensor is \(\sum_j\sigma_j\otimes\sigma_j=\partial_\theta\otimes\partial_\theta\), independent of \(r\). Set drift to zero and fix \(h>0\). The precise p-Ret transition in the referenced numerical scheme is formed from a uniform random vector \(Z\) on \(\mathbb S^{r-1}\), with increment \(\sqrt{rh}\,\Sigma Z\). Since \(\Sigma=(r^{-1/2},\ldots,r^{-1/2})\), rotational invariance gives
\[
\theta_{n+1}=\theta_n+\sqrt{rh}\,U_n\pmod{2\pi},
\quad U_n\stackrel{d}=Z_{n,1},
\]
with independent steps. At \(r=1\), this mathematical transition requires an independent fair sign; the paper's dimension-\(r-1\) continuous-uniform sampler is not asserted to implement that zero-dimensional edge case.

Here \(L^2\) is with respect to normalized Haar measure. A zero-mean discrete Poisson solution means a function \(u\in L^2\) with \(\Pi u=0\) and \((I-P_{r,h})u=f\), for prescribed \(f\in L^2\) with \(\Pi f=0\). Total variation is \(\sup_B|\mu(B)-\nu(B)|\), between zero and one.

## Proof

**1. Exact multipliers.** The spherical coordinate \(U\) is symmetric. For \(r\ge2\) it has probability density
\[
p_r(u)=\frac{\Gamma(r/2)}{\sqrt\pi\,\Gamma((r-1)/2)}(1-u^2)^{(r-3)/2}\mathbf 1_{(-1,1)}(u).
\]
For \(r=1\), \(U\) is equally likely to be \(+1\) or \(-1\). On the Fourier characters \(e_k(\theta)=e^{ik\theta}\), convolution diagonalization gives \(P_{r,h}e_k=\rho_{r,k}e_k\), with \(\rho_{r,k}=\mathbb E\cos(k\sqrt{rh}U)\). Integrating the beta density using the standard Bessel integral establishes the displayed formula, with \(\rho_{r,0}=1\). Moreover, \(\mathbb EU=0\) and \(\mathbb EU^2=1/r\), so for every fixed mode the multiplier is \(1-k^2h/2+O(h^2)\); the local heat generator is the same for all \(r\).

**2. The sharp spectral threshold.** If \(r\ge2\), the step has a nondegenerate absolutely continuous law on an interval. Consequently \(|\mathbb E e^{itU}|<1\) for every nonzero real \(t\): equality in the triangle inequality would force \(e^{itU}\) constant almost surely, impossible on an interval. The Riemann–Lebesgue lemma implies \(\rho_{r,k}\to0\) as \(|k|\to\infty\). Therefore the supremum of \(|\rho_{r,k}|\) over \(k\ne0\) is attained and strictly less than one. Fourier diagonalization now proves, for every positive integer \(n\), the exact identity \(\|P_{r,h}^n-\Pi\|_{2\to2}=q_r(h)^n\).

For \(r=1\), \(\rho_{1,k}=\cos(k\sqrt h)\). When \(\sqrt h/\pi\) is rational, one of the nonzero harmonics has multiplier of modulus one. When it is irrational, density of its integer multiples modulo \(\pi\) yields multipliers with modulus arbitrarily close to one. Hence in either case the same operator norm is exactly one at every finite \(n\). For irrational ratio every individual nonzero Fourier multiplier has modulus strictly below one; dominated convergence of Fourier squares proves strong \(L^2\) convergence to constants. For rational ratio a nonzero harmonic has multiplier one, giving nonuniqueness of invariant measures and failure of strong convergence.

**3. Total-variation dichotomy.** For \(r=1\), an \(n\)-step point-started law has at most \(n+1\) atoms, and is singular to Haar, hence at total-variation distance one. For \(r\ge2\), standard stationary phase or the Bessel asymptotic gives \(\rho_{r,k}=O(|k|^{-(r-1)/2})\). Thus the two-step convolution law has a square-integrable Haar density, since \(\sum_k|\rho_{r,k}|^4<\infty\). For later steps, Fourier contraction gives
\[
\|\mathcal L(\theta_n\mid\theta_0=x)-\mathrm{Haar}\|_{\mathrm{TV}}
\le \tfrac12 q_r(h)^{n-2}\|g_{r,h,2}-1\|_{L^2},\qquad n\ge2,
\]
where \(g_{r,h,2}\) is the two-step Haar density for a point start (translated without changing its norm). This proves geometric total-variation mixing, uniformly over initial points.

**4. Exact discrete Poisson solvability.** For \(r\ge2\), on the zero-mean subspace \(I-P_{r,h}\) has the Fourier inverse \(\widehat u(k)=\widehat f(k)/(1-\rho_{r,k})\); the denominator is at least \(1-q_r(h)>0\) in modulus. Existence and uniqueness of an \(L^2\) solution, with \(\|u\|_2\le(1-q_r(h))^{-1}\|f\|_2\), follow immediately.

For \(r=1\) and rational \(\sqrt h/\pi\), there is a nonconstant harmonic with multiplier one, so the discrete Poisson operator has a kernel. For irrational ratio, infinitely many distinct integers \(k_j\) satisfy \(0<1-\cos(k_j\sqrt h)<2^{-j}\). The real uniformly convergent series
\[
f(\theta)=\sum_{j\ge1}\big(1-\cos(k_j\sqrt h)\big)\cos(k_j\theta)
\]
is continuous and mean zero. A Poisson solution would have cosine-Fourier coefficients equal to one on every \(k_j\), contradicting square summability. Thus not every continuous forcing has an \(L^2\) solution. Together these cases prove the sharp threshold at \(r=2\).

## Verification

Run `python3 check.py` with standard-library Python 3. The package includes an executable supplementary check of sphere moments, the characteristic-function series, its cosine/Bessel/sinc specializations, representative spectral inequalities and exact angular resonances. It passed **377** checks. The infinite-frequency and all-step claims are established by the proof above, not by finite tests. In particular, Bessel decay, rational-versus-irrational density, and the explicit small-divisor construction are essential analytic steps.

## Relationship to prior work

He, Hui, Sheng, Su and Zhou (2026) define the p-Ret transition, permit the driving-noise dimension to differ from manifold dimension, and prove local weak accuracy and finite-horizon error properties. The present result specializes that exact transition to the circle and asks a different, long-time question: invariance under noise-factorization choice. The paper's Sections 2 and 3 do not supply the rank-threshold mixing and discrete Poisson classification.

For \(r=1\), the two-point random walk is classical. Su (1998) and Berkes–Borda (2023) study its irrational-rotation and arithmetic mixing behavior in depth; no originality is claimed for this established random-walk theory in isolation. The new object of comparison is the family of p-Ret discretizations with **identical diffusion generator but varying redundant spherical driving dimension**, combining exact spectral and resolvent consequences. The standard compact-group Fourier theory supplies tools and potential antecedents for pieces of the proof; complete priority beyond inspected sources is not certified.

## Limitations

This result concerns the circle's homogeneous Laplace–Beltrami heat generator and the exact mathematical p-Ret transition for identical noise fields. It is not a general theorem for arbitrary curved manifolds, drift, changing steps, or all possible noise factorizations. The \(r=1\) transition uses a fair sign and does not claim a zero-dimensional continuous-uniform RQMC implementation. The \(r\ge2\) geometric constants depend on fixed \(h\) and \(r\), and are not uniform as \(h\downarrow0\). Finite-time weak accuracy does not imply the long-time conclusions. Independent mathematical review has not been performed.

## References

1. Z. He, Z. Hui, C. Sheng, B. Su and T. Zhou, *Quasi-Monte Carlo based meshfree methods for parabolic equations on parameterized Riemannian manifolds*, arXiv:2610.23341v1 (first publicly submitted 2026-10-16), Sections 2.1–3. https://arxiv.org/html/2610.23341v1
2. F. E. Su, *Convergence of random walks on the circle generated by an irrational rotation*, Transactions of the American Mathematical Society 350 (1998), 3717–3741. https://doi.org/10.1090/S0002-9947-98-02152-7
3. I. Berkes and B. Borda, *Random walks on the circle and Diophantine approximation*, Journal of the London Mathematical Society 108 (2023), 409–440. https://doi.org/10.1112/jlms.12749
