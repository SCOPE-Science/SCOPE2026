# Nearest-neighbor asymptotics of sharp supercritical lattice Sobolev constants

## Finding

For every integer \(d\ge3\), let \(C_{d,q}\) be the sharp homogeneous discrete Sobolev embedding norm from the standard nearest-neighbor Dirichlet space on \(\mathbb Z^d\) into \(\ell^q(\mathbb Z^d)\), for real \(q>2d/(d-2)\). Define
\[
K_d=\frac1{(2\pi)^d}\int_{[-\pi,\pi]^d}\frac{dt}{2d-2\sum_{j=1}^d\cos t_j},\qquad
\rho_d=1-\frac1{2dK_d}.
\]
Then \(0<\rho_d<1\), and
\[
\boxed{\ C_{d,q}=\sqrt{K_d}\left(1+\frac{2d}{q}\rho_d^q+o\left(\frac{\rho_d^q}{q}\right)\right),\quad q\longrightarrow\infty.\ }
\]
Equivalently, \(\lim_{q\to\infty}q\rho_d^{-q}(C_{d,q}/\sqrt{K_d}-1)=2d\). The precise base \(\rho_d\) and prefactor \(2d\) encode the first lattice shell around the Green-function peak.

## Assumptions and scope

Let \(\mathcal D^{1,2}(\mathbb Z^d)\) denote the completion of finitely supported real or complex sequences in the Hilbert norm
\[
\|u\|_{\mathcal D}^2=\sum_{n\in\mathbb Z^d}\sum_{j=1}^d|u(n+e_j)-u(n)|^2.
\]
The discrete Sobolev inequality \(\|u\|_{\ell^{p_*}}\le B_d\|u\|_{\mathcal D}\), with \(p_*=2d/(d-2)\), supplies continuous embeddings and a pointwise representative vanishing at infinity. For each real \(q>p_*\), define
\[
C_{d,q}=\sup_{\|u\|_{\mathcal D}=1}\|u\|_{\ell^q}.
\]
No attainment of the supremum is assumed. The assertion concerns the infinite homogeneous lattice, not finite graphs, not the critical exponent itself, and not nonlinear or fractional gradient energies.

## Proof

**1. Green kernel and shell isolation.** Write \(Lu(n)=\sum_{j=1}^d(2u(n)-u(n+e_j)-u(n-e_j))\). For \(d\ge3\), the Fourier multiplier of \(L\) is \(\lambda(t)=2d-2\sum_j\cos t_j\), whose reciprocal is integrable. Its positive Green kernel
\[
G(n)=\frac1{(2\pi)^d}\int_{[-\pi,\pi]^d}\frac{e^{-in\cdot t}}{\lambda(t)}\,dt
\]
satisfies \(LG=\delta_0\), \(G(0)=K_d\), \(\|G\|_{\mathcal D}^2=K_d\), and \(G(n)\to0\) as \(|n|\to\infty\). Positivity follows, for example, from the integral of the positive lattice heat kernel. The normalized Green function \(h=G/K_d\) has \(h(0)=1\). By the reproducing identity \(\langle u,h\rangle_{\mathcal D}=u(0)/K_d\), the optimal point-evaluation constant is \(\sqrt{K_d}\).

Since \(LG(0)=1\) and every neighbor of zero has the same Green value,
\[
h(\pm e_j)=1-\frac1{2dK_d}=\rho_d\quad (j=1,\ldots,d).
\]
The maximum principle applied to the positive harmonic function \(h\) off the origin, together with its decay at infinity, proves \(0<h(n)<\rho_d\) whenever \(|n|_1\ge2\). In fact, there exists \(\theta_d<\rho_d\) with \(h(n)\le\theta_d\) on that set. The discrete Sobolev embedding also gives \(h\in\ell^{p_*}\). Consequently, if
\[
A_q=\sum_{n\ne0}h(n)^q,
\]
then the two-sided first shell contributes precisely \(2d\rho_d^q\), while the remaining sites contribute at most \(\theta_d^{q-p_*}\sum_n h(n)^{p_*}=o(\rho_d^q)\). Thus
\[
A_q=2d\rho_d^q+o(\rho_d^q).
\]

**2. Near-optimal vectors concentrate at the Green peak.** Fix \(q>p_*+1\) and choose \(u\) with \(\|u\|_{\mathcal D}=1\) and
\[
\|u\|_q^q/K_d^{q/2}\ge (C_{d,q}/\sqrt{K_d})^q-\eta_q\ge1+A_q-\eta_q,
\qquad \eta_q=\rho_d^{3q}.
\]
Such a vector exists by the definition of supremum; the second inequality uses the normalized Green-kernel test vector \(\sqrt{K_d}h\). Translation and multiplication by a unimodular scalar arrange \(u(0)=\|u\|_\infty=a>0\). The point-evaluation inequality ensures \(a\le\sqrt{K_d}\). Decompose orthogonally
\[
u=a h+v,\quad v(0)=0,\quad 1=a^2/K_d+\|v\|_{\mathcal D}^2.
\]
Write \(b=a/\sqrt{K_d}\), \(t=\|v\|_{\mathcal D}\), and \(w=v/\sqrt{K_d}\). Then \(b^2+t^2=1\), \(u/\sqrt{K_d}=bh+w\), \(w(0)=0\), and
\[
\|w\|_\infty\le t,\qquad \|w\|_{p_*}\le (B_d/\sqrt{K_d})t.
\]
The interpolation estimate \(\|u\|_q^q\le\|u\|_\infty^{q-p_*}\|u\|_{p_*}^{p_*}\le a^{q-p_*}B_d^{p_*}\), together with \(\|u\|_q\ge\sqrt{K_d}(1-o(1))\), implies \(b\ge\exp(-O_d(1/q))\), hence initially \(t=O_d(q^{-1/2})\).

**3. Eliminate deformation at exponential order.** For \(n\ne0\), put \(z(n)=b h(n)+|w(n)|\). Then \(\|z\|_{p_*}=O_d(1)\) and \(\|z\|_\infty\le\rho_d+t\). The complex modulus mean-value inequality and Hölder's inequality give
\[
\left|\sum_{n\ne0}\big(|bh(n)+w(n)|^q-b^qh(n)^q\big)\right|
\le q\sum_{n\ne0}|w(n)|z(n)^{q-1}
\le C_d q t(\rho_d+t)^{q-p_*}.
\]
Here the last step uses \(\sum z^{(q-1)p_*'}\le\|z\|_\infty^{(q-1)p_*'-p_*}\sum z^{p_*}\), valid for \(q>p_*\). Denote this remainder by \(R_q\). The initial bound on \(t\) gives
\[
|R_q|\le C_d q t\rho_d^q\exp(C_d\sqrt q).
\]
Since \(\|u/\sqrt{K_d}\|_q^q=b^q(1+A_q)+R_q\), near-optimality yields
\[
(1+A_q)(1-b^q)\le C_d qt\rho_d^q e^{C_d\sqrt q}+\eta_q.
\]
The right side tends to zero using \(t=O_d(q^{-1/2})\); therefore \(qt^2\to0\). For sufficiently large \(q\), \(1-b^q=1-(1-t^2)^{q/2}\ge qt^2/4\). Solving the resulting quadratic bound gives
\[
t=O_d\big(\rho_d^qe^{C_d\sqrt q}\big).
\]
Substitution into the mean-value bound shows \(R_q=O_d(q\rho_d^{2q}e^{C'_d\sqrt q})=o(\rho_d^q)\). Likewise \(1-b^q=O_d(qt^2)=o(\rho_d^q)\). It follows, for the chosen near-optimal vectors, that
\[
(C_{d,q}/\sqrt{K_d})^q=1+A_q+o(\rho_d^q)
=1+2d\rho_d^q+o(\rho_d^q).
\]
Taking positive \(q\)-th roots proves the claimed sharp asymptotic. The argument applies to both real and complex scalar sequences.

## Verification

The analytic proof uses no extrapolation from finite experiments. An accompanying independent finite-box calculation constructs a Dirichlet Green kernel for a cubic box of side length \(11\), checks its inverse-Laplacian residual and nearest-neighbor identity, and displays the first-shell ratio for five finite exponents. Its finite-volume data are corroborative only and do not certify an infinite-volume limit. Run `python check_lattice_green.py` with NumPy and SciPy. The proof above is self-contained given the standard discrete Sobolev embedding and elementary Green-kernel properties.

## Relationship to prior work

Ilyin, Laptev and Zelik (arXiv:1407.0675v1, 2014; published 2015), Theorem 4.1 and Remark 4.1, obtain the sharp endpoint point-evaluation constant and the Green-function extremizer; Theorem 6.2 and Remark 6.4 discuss the supercritical \(\ell^q\) inequality without claiming sharp finite-exponent constants. The present statement does not assert an exact formula for those constants. It determines their sharp first exponentially small correction as \(q\to\infty\), showing that the coefficient is the number of nearest neighbors and the base is their normalized Green value. Complete statement/implication comparisons and literature-access limits are recorded separately in the accompanying review.

## Limitations

The result is asymptotic, with no explicit uniform threshold or explicit numerical remainder coefficient for fixed \(q\). It concerns only the standard homogeneous nearest-neighbor energy and integer dimensions \(d\ge3\). It neither determines all finite-\(q\) extremizers nor gives the critical Sobolev constant. A generic abstract perturbation formulation could cover this consequence without the same terminology; its absence cannot be established by search alone. No independent audit or external certification has been performed.

## References

- A. Ilyin, A. Laptev and S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1 (public 2 July 2014); *Bulletin of Mathematical Sciences* **5** (2015), 19–57, doi:10.1007/s13373-014-0060-8. Specific comparisons: Theorem 4.1, Remark 4.1, Theorem 6.2, Remark 6.4.
- K. Takemura, Y. Kametaka and A. Nagai, *A hierarchical structure for the sharp constants of discrete Sobolev inequalities on a weighted complete graph*, *Symmetry* **10** (2018), article 1, doi:10.3390/sym10010001 (finite-graph comparison; abstract and available introductory text only).
