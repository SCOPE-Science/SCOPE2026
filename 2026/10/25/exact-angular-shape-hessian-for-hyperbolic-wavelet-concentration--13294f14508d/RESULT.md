# Exact angular shape Hessian for hyperbolic wavelet concentration

## Finding
For fixed \(a>0\) and hyperbolic-area parameter \(H>0\), the largest localization eigenvalue in the normalized weighted Bergman space has a completely explicit second-order angular-Fourier shape Hessian. Unlike a bound for a fixed test function, the result **optimizes over every unit analytic function** after the observation domain is perturbed. Define
\[
 u=\frac{H}{1+H},\quad b_m=\frac{(a)_m}{m!}u^m,\quad B_m=\sum_{j=1}^{m}b_j,\quad
 q_m=1-\frac{(a+m)b_m}{(a+1)B_m}\quad(m\ge1).
\]
For any real, mean-zero \(h\in C^2(\mathbb T)\) and \(\widehat h_m=(2\pi)^{-1}\int_0^{2\pi}h(\theta)e^{-im\theta}d\theta\), one has
\[
 \Lambda(\Omega_\varepsilon)=1-(1+H)^{-a}
 -\varepsilon^2\frac{a(a+1)}{(1+H)^{a+2}}
 \sum_{m\ge2}q_m|\widehat h_m|^2+o(\varepsilon^2).
\]
The shape multipliers obey \(q_1=0\) and \(0<q_2<q_3<\cdots<1\), with \(q_m\to1\). The exact **sharp transverse curvature** is
\[
 C_{a,H}=\frac{a(a+1)}{(1+H)^{a+2}}\frac{2-u}{2+(a+1)u}.
\]
In particular, the quadratic deficit is at least \(C_{a,H}\sum_{m\ge2}|\widehat h_m|^2\), with equality precisely when \(\widehat h_m=0\) for all \(m\ge3\). A pure second angular harmonic attains the sharp nonzero coefficient; first harmonics have zero curvature because they are tangent to hyperbolic disk motions.

## Assumptions and scope
Let \(A^2_{a-1}(\mathbb D)\), for \(a>0\), be the Hilbert space of analytic functions in the unit disk with probability-normalized measure
\[
 d\rho_a(z)=\frac{a}{\pi}(1-|z|^2)^{a-1}\,dA(z).
\]
For measurable \(\Omega\subset\mathbb D\), define \(T_\Omega\) by \(\langle T_\Omega f,g\rangle=\int_\Omega f\overline g\,d\rho_a\), and let \(\Lambda(\Omega)=\|T_\Omega\|\). This is the optimized analytic-wavelet concentration after the standard upper-half-plane-to-disk Bergman correspondence; the wavelet parameter is \(a/2>0\).

Given \(H>0\) and real \(h\in C^2(\mathbb T)\) with \(\widehat h_0=0\), take sufficiently small real \(\varepsilon\) such that \(H+\varepsilon h(\theta)>0\) and define
\[
 \Omega_\varepsilon=\left\{re^{i\theta}:0\le r^2<\frac{H+\varepsilon h(\theta)}{1+H+\varepsilon h(\theta)}\right\}.
\]
Exactly (not merely asymptotically), \(\int_{\Omega_\varepsilon}(1-|z|^2)^{-2}\,dA(z)=\pi H\) for every such \(\varepsilon\). All limits hold with \(a,H,h\) fixed as \(\varepsilon\to0\). There is no assertion of uniformity over families with growing Fourier frequencies.

## Proof
**1. Radial spectrum and gap.** Let \(c_n=(a+1)_n/n!\) and \(e_n(z)=\sqrt{c_n}\,z^n\), an orthonormal basis. For the disk \(\Omega_0=\{|z|^2<u\}\), the localization operator is diagonal with
\[
 \lambda_n=a c_n\int_0^u s^n(1-s)^{a-1}\,ds=I_u(n+1,a),\qquad \lambda_0=1-(1-u)^a.
\]
Here \(I_u\) denotes the regularized incomplete beta integral. Its standard recurrence gives
\[
 \lambda_{n-1}-\lambda_n=\frac{(a)_n}{n!}u^n(1-u)^a=b_n(1-u)^a\quad(n\ge1).
\]
Hence \(\lambda_0-\lambda_n=(1-u)^a B_n>0\): \(\lambda_0\) is a simple isolated largest eigenvalue.

**2. Differentiable operator family.** Write \(v_\varepsilon(\theta)=H+\varepsilon h(\theta)\) and \(u_\varepsilon=v_\varepsilon/(1+v_\varepsilon)\). In the monomial basis the matrix entries are
\[
 (T_\varepsilon)_{mn}=a\sqrt{c_m c_n}\left\langle e^{i(n-m)\theta}
 \int_0^{u_\varepsilon(\theta)}s^{(m+n)/2}(1-s)^{a-1}\,ds\right\rangle_\theta,
\]
where \(\langle\cdot\rangle_\theta\) is normalized angular averaging. Since all perturbed domains stay in a compact subdisk, these integrals and their first two derivatives converge in trace norm: use \(\sum_n|e_n(z)|^2=(1-|z|^2)^{-a-1}\) and its differentiated geometric-power series on the compact subdisk. Thus isolated-simple-eigenvalue perturbation applies without a finite-rank assumption. Direct differentiation yields
\[
 \frac12\langle e_0,T''_0 e_0\rangle
 =-\frac{a(a+1)}{2(1+H)^{a+2}}\langle h^2\rangle_\theta
 =-\frac{a(a+1)}{(1+H)^{a+2}}\sum_{m\ge1}|\widehat h_m|^2
\]
and, for \(m\ge1\),
\[
 |\langle e_m,T'_0 e_0\rangle|^2
 =\frac{a^2c_m u^m}{(1+H)^{2a+2}}|\widehat h_m|^2.
\]
The first eigenvalue derivative vanishes because \(\widehat h_0=0\).

**3. Optimize over the analytic function.** The Rayleigh–Schrödinger formula for the simple top eigenvalue gives
\[
 \frac12\Lambda''(0)=\frac12\langle e_0,T''_0e_0\rangle
 +\sum_{m\ge1}\frac{|\langle e_m,T'_0e_0\rangle|^2}{\lambda_0-\lambda_m}.
\]
Use \((1-u)^a=(1+H)^{-a}\) and \((a+m)b_m=a c_mu^m\). The coefficient of \(|\widehat h_m|^2\) in the *negative* of this formula is exactly
\[
 \frac{a(a+1)}{(1+H)^{a+2}}
 \left(1-\frac{(a+m)b_m}{(a+1)B_m}\right).
\]
This proves the complete Hessian formula. The spectral-gap denominator \(B_m\) is essential: omitting the eigenfunction response would give a different, fixed-test-function coefficient.

**4. Strict multiplier ordering and sharpness.** Set \(r_m=1-q_m=(a+m)b_m/((a+1)B_m)\). As \(b_{m+1}=u(a+m)b_m/(m+1)\), the strict inequality \(r_{m+1}<r_m\) is equivalent to
\[
 P_m(u):=(m+1-(a+m+1)u)B_m+u(a+m)b_m>0.
\]
The finite binomial sum satisfies \((1-u)B'_m(u)=a+aB_m(u)-(a+m)b_m(u)\). Therefore
\[
 P_m(u)=a u+(1-u)\sum_{j=1}^{m}(m+1-j)b_j>0
\]
for \(a>0\), \(0<u<1\). Also \(r_1=1\), and \(b_m\to0\) exponentially fast while \(B_m\ge b_1>0\), so \(r_m\to0\). Finally, \(q_2=(2-u)/(2+(a+1)u)\) by two-term substitution. Thus the first nontranslation angular frequency, \(m=2\), uniquely minimizes the positive multipliers, giving the claimed sharp transverse coefficient and equality cases.

## Verification
A self-contained finite-section numerical script, `wavelet_hessian_check.py`, computes the weighted Bergman Toeplitz matrix from regularized incomplete beta integrals on angular grids, rechecks the explicit monotone multiplier formula, and compares the predicted second-order deficit to actual largest eigenvalues. For \(a=1.7\), \(H=0.9\), and \(h(\theta)=\cos(2\theta)+\tfrac12\cos(3\theta)\), the predicted coefficient is approximately \(0.0677565765851\); the finite-section ratios converge toward this value as \(\varepsilon\downarrow0\). These finite computations corroborate normalization; the proof above supplies the infinite-dimensional justification.

## Relationship to prior work
Ramos–Tilli (first public preprint 2022) prove the global hyperbolic-area Faber–Krahn inequality: pseudohyperbolic disks maximize continuous Cauchy-wavelet concentration. Their theorem does not provide a shape derivative of the **fully optimized** principal eigenvalue. Gómez–Kalaj–Melentijević–Ramos (first public 2024-11-24) prove global wavelet stability and, in Section 4.1, compute exact second variations \(W_k\) for a **different optimization order**: vary the analytic function and choose a maximizing superlevel domain along with it. Their displayed \(W_k\) are not the present fixed-mask, optimized-function coefficients \(q_k\); in particular, the latter contain the radial localization eigenvalue gap in the denominator. The 2024 results establish global quantitative control but do not state the full present domain-shape spectrum or the exact sharp fixed-area transverse curvature. The Gaussian/Fock analogue also concerns a distinct geometry and weight; it neither entails the all-real-\(a\) hyperbolic formula nor fixes the different curvature profile here.

## Limitations
The theorem concerns one complex dimension, smooth star-shaped radial perturbations of a centered pseudohyperbolic disk, and fixed positive \(a,H\). It does not prove a global sharp deficit, optimal constants in a nonlocal asymmetry metric, a shape Hessian for rough domains, or higher-eigenvalue behavior. The indexed and primary-source comparisons do not exclude every obscure or unindexed historical proof. No independent audit or independent validation has been performed.

## References
1. J. P. G. Ramos and P. Tilli, *A Faber–Krahn inequality for Wavelet transforms*, arXiv:2205.07998v1 (first public 2022-05-16); *Bulletin of the London Mathematical Society* **55** (2023), 2018–2034, doi:10.1112/blms.12833. https://arxiv.org/abs/2205.07998 ; https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12833
2. J. Gómez, D. Kalaj, P. Melentijević and J. P. G. Ramos, *Uniform stability of concentration inequalities and applications*, arXiv:2411.16010v1 (2024-11-24), Section 4.1, particularly Lemma 4.7 and Proposition 4.4. https://arxiv.org/html/2411.16010v1
3. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423v1 (2021), *Inventiones mathematicae* **230** (2022), 1–30. https://arxiv.org/abs/2106.03423
