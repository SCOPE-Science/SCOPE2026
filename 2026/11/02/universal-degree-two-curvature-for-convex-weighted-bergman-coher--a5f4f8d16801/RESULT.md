# Universal degree-two curvature for convex weighted Bergman coherent-state functionals

## Finding

Fix \(\beta>1\). Every non-affine \(C^2\) convex observable \(G:[0,1]\to\mathbb R\) with \(G(0)=0\) has an exactly diagonal, strictly ordered infinitesimal deficit spectrum at every normalized coherent state of the weighted analytic Bergman disk. The sole non-phase flat direction is infinitesimal disk translation (holomorphic degree one), and the **unique least-stable transverse degree is two**, independently of the choice of \(G\).

More precisely, write \(e_n(z)=\sqrt{(\beta)_n/n!}\,z^n\), where \((\beta)_n=\Gamma(\beta+n)/\Gamma(\beta)\). For \(g=\sum_{n\ge1}a_ne_n\) and real \(\varepsilon\), normalize
\[
 f_{\varepsilon,g}=\frac{1+\varepsilon g}{\sqrt{1+\varepsilon^2\|g\|_\beta^2}}.
\]
Then the convex-functional deficit satisfies
\[
 \mathcal F_G(1)-\mathcal F_G(f_{\varepsilon,g})
 =\varepsilon^2\sum_{n\ge2}\lambda_n|a_n|^2+o_g(\varepsilon^2),
\]
where \(\lambda_1=0<\lambda_2<\lambda_3<\cdots<\lambda_\infty<\infty\). Put \(C_n=(\beta)_n/n!\), and for \(s\in(0,1)\) set \(a=s^{1/\beta}\). The complete, exact curvature spectrum is determined by
\[
\boxed{\lambda_{n+1}-\lambda_n=
 \frac{C_n}{\beta(n+1)}\int_0^1
 a^{\beta-1}(1-a)^n(1+na)G''(s)\,ds,\qquad n\ge1.}
\]
In particular, the sharp transverse curvature is
\[
\boxed{\lambda_2=\frac12\int_0^1
 s^{1-1/\beta}(1-s^{2/\beta})G''(s)\,ds>0,}
\]
and the accumulation point is
\[
\boxed{\lambda_\infty=\int_0^1 t^{\beta-2}
 \bigl(G'(t^\beta)-G'(0)\bigr)\,dt.}
\]
The quadratic inequality \(\sum_{n\ge2}\lambda_n|a_n|^2\ge\lambda_2\sum_{n\ge2}|a_n|^2\) is sharp, with equality precisely for pure degree-two perturbations. These statements concern the second variation, not a claimed globally optimal stability constant.

For the power observable \(G(s)=s^p\) with integer \(p\ge2\), the entire spectrum additionally simplifies to
\[
 \lambda_n=\frac{p}{\beta p-1}
 \left(1-\frac{p(\beta)_n}{(\beta p)_n}\right),\qquad
 \lambda_2=\frac{p\beta(p-1)}{\beta^2p^2-1}.
\]

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), with normalized area \(dA/\pi\) and hyperbolic area \(d\mu(z)=dA(z)/(\pi(1-|z|^2)^2)\). Let \(A^2_\beta\) be the analytic Hilbert space
\[
 \|f\|_\beta^2=(\beta-1)\int_{\mathbb D}
 |f(z)|^2(1-|z|^2)^\beta\,d\mu(z).
\]
Thus \(\|1\|_\beta=1\) and \((e_n)_{n\ge0}\) is an orthonormal basis. For unit-norm \(f\), its coherent-state density is \(u_f(z)=|f(z)|^2(1-|z|^2)^\beta\), taking values in \([0,1]\) by the reproducing-kernel pointwise bound. Define
\[
 \mathcal F_G(f)=\int_{\mathbb D}G(u_f(z))\,d\mu(z),
 \qquad G\in C^2([0,1]),\quad G(0)=0,\quad G''\ge0,
\]
with \(G''\) not identically zero. The integral converges since \(|G(u)|\le C u\) and \(\int u_f\,d\mu=1/(\beta-1)\). The parameter \(\beta\), rather than the usual Bergman weight \(\alpha\), equals \(\alpha+2\). All modes and normalizations are specified above.

The exact statement is for normalized paths transverse to the constant coefficient. Complex coefficients in \(g\) are allowed. In the full unit sphere, constant-phase variation is another zero mode. Disk automorphisms transport the same curvature spectrum to every coherent-state center. No claim of a globally uniform nonlinear remainder or global optimal stability coefficient is made.

## Proof

**1. Second variation.** For a fixed \(g\perp 1\), let \(S=\|g\|_\beta^2\), \(t=1-|z|^2\) and \(u_0=t^\beta\). The normalized coherent density expands pointwise as
\[
 u_{f_{\varepsilon,g}}=u_0\bigl[1+2\varepsilon\operatorname{Re}g+
 \varepsilon^2(|g|^2-S)\bigr]+o(\varepsilon^2).
\]
Rotational symmetry and analyticity give \(\int g\,w=\int g^2\,w=0\) for every integrable radial weight \(w\) for which these expressions are defined. Consequently, angular integration converts \(2(\operatorname{Re}g)^2\) into \(|g|^2\), and the quadratic coefficient of \(\mathcal F_G(f_{\varepsilon,g})-\mathcal F_G(1)\) becomes
\[
 Q_G(g)=\int_{\mathbb D}\left[u_0G'(u_0)+u_0^2G''(u_0)\right]|g|^2d\mu
 -S\int_{\mathbb D}u_0G'(u_0)d\mu.
\]
The kernel pointwise estimate \(u_g(z)\le S\) makes these expansions dominated in hyperbolic measure: \(t^\beta|g|^2\) is integrable, \(t^{2\beta}|g|^4\le S t^\beta|g|^2\), and \(G',G''\) are bounded and uniformly continuous on \([0,1]\). Thus the remainder is indeed \(o_g(\varepsilon^2)\), not merely a formal expansion. Angular orthogonality diagonalizes \(Q_G\) in the basis \(e_n\).

**2. Convex decomposition and hinge-mode coefficient.** For \(0\le u\le1\),
\[
 G(u)=G'(0)u+\int_0^1(u-s)_+G''(s)ds.
\]
The affine term gives a constant functional on the unit sphere. Hence the Hessian is the \(G''\)-weighted integral of the individual hinge-mode Hessians. Fix \(s\in(0,1)\), set \(a=s^{1/\beta}\), and define
\[
 H_n(a)=C_n\left[\int_a^1t^{\beta-2}(1-t)^n\,dt
 +\frac{a^{\beta-1}(1-a)^n}{\beta}\right].
\]
This follows by substituting \(G_s'(u)=\mathbf1_{u>s}\) and the distributional second derivative \(G_s''=\delta_s\) into the exact quadratic form, or equivalently by applying Fubini to the \(C^2\) representation. The common normalization term is \(J(a)=(1-a^{\beta-1})/(\beta-1)\). In fact, \(H_1(a)=J(a)\): directly integrate the \(n=1\) expression by parts. Thus
\[
 \lambda_n=\int_0^1\bigl[H_1(s^{1/\beta})-H_n(s^{1/\beta})\bigr]G''(s)ds.
\]

**3. Strict universal ordering.** The identity \(C_{n+1}=C_n(\beta+n)/(n+1)\) and elementary differentiation give
\[
 C_{n+1}(1-t)^{n+1}-C_n(1-t)^n
 =\frac{C_n}{n+1}(1-t)^n\bigl[(\beta-1)-(\beta+n)t\bigr]
\]
and
\[
 \frac{d}{dt}\left[t^{\beta-1}(1-t)^{n+1}\right]
 =t^{\beta-2}(1-t)^n\bigl[(\beta-1)-(\beta+n)t\bigr].
\]
Integrating over \([a,1]\) and combining the explicit endpoint terms yields the exact identity
\[
 H_{n+1}(a)-H_n(a)=-\frac{C_n}{\beta(n+1)}
 a^{\beta-1}(1-a)^n(1+na).
\]
It is strictly negative for all \(0<a<1\) and all integers \(n\ge0\). Since a non-affine convex \(C^2\) observable has \(G''>0\) on some interior interval, integration proves \(0=\lambda_1<\lambda_2<\cdots\). The formula for \(\lambda_2\) follows from \(C_1=\beta\) and \(\lambda_1=0\). No unsupported claim about the sign of a general high-degree Taylor coefficient is needed.

**4. Endpoint, sharpness and symmetry.** For each fixed \(a\in(0,1)\), \(H_n(a)\to0\) because \(C_n\) grows polynomially and \((1-a)^n\) decays exponentially. Moreover \(0\le H_n(a)\le H_1(a)\), so dominated convergence yields \(\lambda_\infty=\int J(s^{1/\beta})G''(s)ds\); Fubini gives the displayed expression using \(G'(t^\beta)-G'(0)=\int_0^{t^\beta}G''(s)ds\). Positivity and strict ordering imply the sharp quadratic gap, attained only in the \(e_2\) direction. Since the weighted Bergman automorphism representation preserves the coherent density distribution, it conjugates the Hessians at different coherent-state centers and preserves their spectra. For \(G(u)=u^p\), direct beta integration gives the explicit closed form in the Finding section.

## Verification

Run the standalone checker `verify_modes.py` with Python 3.9 or newer. It performs exact rational comparisons of the mode-gap identity and closed-form power spectra at \(\beta=2,3,5,9\), \(p=2,3,4,6\), modes up to \(17\), together with finite-perturbation Taylor tests. Its observed output in this package was `PASS 704 rational identities and Taylor checks`. These finite checks verify arithmetic and normalization; they do not establish the universal \(\beta\), \(G\), or infinite-mode assertions, which are proved above.

## Relationship to prior work

Kulikov's 2022 theorem proves that coherent states maximize all convex weighted Bergman functionals of this type; the global inequality and Möbius invariance are previously established. Frank, Nicola and Tilli's 2023 generalized Wehrl quantitative theorem concerns Gaussian Fock coherent states and quantitative distance to them. Melentijević's 2025 weighted Bergman stability theorem gives nonlinear stability estimates for convex functionals. None of these inspected statements identifies the entire weighted Bergman Hessian spectrum for every non-affine \(C^2\) convex observable, the strict ordering of all holomorphic degrees, or the explicit degree-two curvature integral. This is a statement-level comparison, not a guarantee that all historic literature has been exhausted.

## Limitations

The results are infinitesimal and concern analytic Hilbert disk spaces with \(\beta>1\), normalized pure states, and \(C^2\) convex \(G\). The proof does not give a globally sharp stability coefficient, mixed-state Hessian, arbitrary Banach Bergman exponent, or higher-dimensional ball formula. Novelty remains subject to independent historical-priority checking; independent mathematical validation has not been performed.

## References

1. A. Kulikov, *Functionals with extrema at reproducing kernels*, arXiv:2203.12349, first posted 2022-03-23, https://arxiv.org/html/2203.12349v1 .
2. R. L. Frank, F. Nicola and P. Tilli, *The generalized Wehrl entropy bound in quantitative form*, arXiv:2307.14089, first posted 2023-07-26, https://arxiv.org/abs/2307.14089 .
3. P. Melentijević, *Stability of convex functionals on weighted Bergman spaces with applications*, arXiv:2508.01939, first posted 2025-08-03, https://arxiv.org/abs/2508.01939 .
4. J. Gómez, D. Kalaj, P. Melentijević and J. P. G. Ramos, *Uniform stability of concentration inequalities and applications*, arXiv:2411.16010, first posted 2024-11-24, https://arxiv.org/abs/2411.16010 .
