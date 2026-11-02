# Fredholm beta curves and exact real crossings for generalized Hilbert operators

## Finding

For every real \(b>0\), consider the generalized Hilbert operator on the complex Hardy space \(H^2(\mathbb D)\):
\[
(\mathcal H_b f)(z)=\int_0^1 \frac{f(t)(1-t)^b}{(1-tz)^{b+1}}\,dt.
\]
Define its **Fredholm essential spectrum** to be the set of complex \(\lambda\) for which \(\mathcal H_b-\lambda I\) is not Fredholm. The exact answer is
\[
\boxed{\sigma_{\mathrm{ess}}^{F}(\mathcal H_b)=
\{0\}\cup\left\{\mathrm B\!\left(b+\tfrac12-i\xi,\tfrac12+i\xi\right):\xi\in\mathbb R\right\}.}
\]
Here \(\mathrm B(u,v)=\Gamma(u)\Gamma(v)/\Gamma(u+v)\). The curve is compact because its two ends converge to zero. Moreover, at every \(\lambda\) outside this curve,
\[
\boxed{\operatorname{ind}(\mathcal H_b-\lambda I)
=\operatorname{wind}_{\xi:-\infty\to+\infty}
\left(\mathrm B\!\left(b+\tfrac12-i\xi,\tfrac12+i\xi\right)-\lambda\right).}
\]
The winding number is taken in the indicated increasing-\(\xi\) orientation, with the ends of the curve joined at the common value \(-\lambda\).

For an **integer** parameter \(b=m\ge1\), the beta curve has exactly
\[
\boxed{\left\lfloor\frac{m-1}{2}\right\rfloor}
\]
distinct **nonzero transverse double points** and no other nonzero self-intersections. Their locations are real and alternate in sign. More explicitly, for each integer \(j\ge1\) with \(2j<m\), there is a unique \(\xi_{m,j}>0\) satisfying
\[
\sum_{r=0}^{m-1}\arctan\left(\frac{\xi_{m,j}}{r+1/2}\right)=j\pi,
\]
and the double point is
\[
\lambda_{m,j}=\frac{\pi}{m!\cosh(\pi\xi_{m,j})}
\prod_{r=0}^{m-1}\left(r+\tfrac12-i\xi_{m,j}\right)
\in(-1)^j(0,\infty).
\]
In particular, nonzero self-crossings first occur at \(m=3\), and a further crossing appears at every subsequent odd positive integer \(m\ge5\).

## Assumptions and scope

All operators and Hilbert spaces are complex. \(b\) is a fixed strictly positive real number; only the double-point classification additionally requires \(b\) to be a positive integer. The symbol \(\mathrm B\) is the Euler beta function with arguments having strictly positive real parts, so there is no issue of poles. The Fredholm essential spectrum, not the full spectrum or approximate-point spectrum, is determined. Our convention is \(\widehat{k}(\xi)=\int_{\mathbb R}k(u)e^{-i\xi u}\,du\), and the operator index is dimension of kernel minus dimension of cokernel.

By Li--Pan--Zhou's norm theorem, the operator is bounded on \(H^2\). Alternatively, boundedness follows from the compact-model argument below and the boundedness of the Wiener--Hopf convolution operator.

## Proof

**1. The exact coefficient matrix.** In the orthonormal monomial basis \((z^j)_{j\ge0}\), the matrix \(A_b\) of \(\mathcal H_b\) has entries
\[
 a_{jk}=\frac{\Gamma(j+b+1)\Gamma(j+k+1)}
 {\Gamma(j+1)\Gamma(j+k+b+2)}\qquad(j,k\ge0).
\]
Indeed, the coefficient of \(z^j\) in \((1-tz)^{-b-1}\) is \(\Gamma(j+b+1)t^j/[\Gamma(b+1)\Gamma(j+1)]\), and integration against \(t^k(1-t)^b\) yields the beta integral. In particular, \(A_b\) is genuinely nonsymmetric for \(b>0\).

**2. A Hilbert--Schmidt continuous model.** On \(L^2([1,\infty),dx)\), define
\[
 (K_bf)(x)=\int_1^\infty \kappa_b(x,y)f(y)\,dy,
 \qquad \kappa_b(x,y)=\frac{x^b}{(x+y)^{b+1}}.
\]
Let \(J:\ell^2(\mathbb N_0)\to L^2([1,\infty))\) be the isometry sending the \(j\)-th basis vector to the indicator of the unit interval \([j+1,j+2)\). We claim
\[
 \boxed{JA_bJ^*-K_b\in\mathcal S_2.}
\]
The standard uniform gamma-ratio estimates, with \(N\ge1\), are
\[
 \frac{\Gamma(N+b)}{\Gamma(N)}=N^b(1+O_b(N^{-1})),\qquad
 \frac{\Gamma(N)}{\Gamma(N+b+1)}=N^{-b-1}(1+O_b(N^{-1})).
\]
They imply, writing \(x_j=j+1\) and \(y_k=k+1\),
\[
 |a_{jk}-\kappa_b(x_j,y_k)|\le
 C_b\left[\frac{x_j^{b-1}}{(x_j+y_k)^{b+1}}+
 \frac{x_j^b}{(x_j+y_k)^{b+2}}\right].
\]
The squares of both terms are summable over \(j,k\ge0\). For example, summing or integrating first in the \(y\)-variable bounds the sum of the first square by a constant times \(\int_1^\infty x^{2b-2}(x+1)^{-2b-1}\,dx<\infty\); the second is similar. Thus the stepwise kernel with cell values \(a_{jk}\) differs in \(L^2([1,\infty)^2)\) from the stepwise kernel with cell values \(\kappa_b(x_j,y_k)\).

Also, direct differentiation gives
\[
 |\partial_x\kappa_b|\le C_b\left[\frac{x^{b-1}}{(x+y)^{b+1}}+
 \frac{x^b}{(x+y)^{b+2}}\right],\qquad
 |\partial_y\kappa_b|\le C_b\frac{x^b}{(x+y)^{b+2}}.
\]
Both derivatives lie in \(L^2([1,\infty)^2)\): after integration in \(y\), their squared bounds decay as \(O_b(x^{-3})\). A unit-cell fundamental-theorem-of-calculus estimate then proves that replacing \(\kappa_b(x,y)\) by its lower-left unit-cell value changes the kernel by an \(L^2\) function. This establishes the claimed Hilbert--Schmidt difference, not merely a pointwise asymptotic.

**3. Logarithmic Wiener--Hopf conjugacy.** The map \((Uf)(s)=e^{s/2}f(e^s)\) is unitary from \(L^2([1,\infty),dx)\) to \(L^2([0,\infty),ds)\). A direct substitution shows
\[
 (UK_bU^{-1}g)(s)=\int_0^\infty k_b(s-t)g(t)\,dt,
 \qquad k_b(u)=\frac{e^{(b+1/2)u}}{(1+e^u)^{b+1}}.
\]
This kernel is positive and in \(L^1(\mathbb R)\): as \(u\to-\infty\) it decays like \(e^{(b+1/2)u}\), while as \(u\to+\infty\) it decays like \(e^{-u/2}\). Substitution \(v=e^u\) gives its Fourier symbol
\[
 m_b(\xi)=\int_{\mathbb R}k_b(u)e^{-i\xi u}\,du
 =\int_0^\infty\frac{v^{b-1/2-i\xi}}{(1+v)^{b+1}}\,dv
 =\mathrm B\!\left(b+\tfrac12-i\xi,\tfrac12+i\xi\right).
\]
By the Riemann--Lebesgue lemma, \(m_b\in C_0(\mathbb R)\).

**4. Fredholm criterion and orientation.** The scalar Wiener--Hopf Fredholm theorem for the kernel \(k_b\in L^1(\mathbb R)\) says that its half-line convolution minus \(\lambda I\), for \(\lambda\ne0\), is Fredholm precisely when the continuous compactified symbol \(m_b(\xi)-\lambda\) is nowhere zero. With the negative Fourier exponent chosen above, its index is the winding number as \(\xi\) increases from \(-\infty\) to \(+\infty\) (equivalently the negative winding in the positive-exponential convention). Because the model discrepancy in Step 2 is Hilbert--Schmidt, the two operators have equal Fredholm properties and indices away from zero: \(JA_bJ^*\) acts as \(A_b\) on \(\operatorname{ran}J\) and as zero on its orthogonal complement; subtracting any \(\lambda\ne0\) gives an invertible scalar operator on that complement. This proves the claimed spectrum and index for nonzero \(\lambda\).

To include \(\lambda=0\) rigorously, note that
\[
 \|A_be_k\|_2^2\le C_b\sum_{j=0}^\infty
 \frac{(j+1)^{2b}}{(j+k+2)^{2b+2}}
 \le \frac{C'_b}{k+1}\longrightarrow0.
\]
The unit vectors \(e_k\) are weakly null. A Fredholm operator cannot send a weakly null normalized sequence to a strongly null sequence (project away its finite-dimensional kernel and use bounded-below behavior on its orthogonal complement). Hence \(A_b\), and therefore \(\mathcal H_b\), is not Fredholm at zero.

**5. Exact double-point classification at positive integers.** When \(b=m\in\mathbb N\), the gamma recurrence and reflection formula give
\[
 m_m(\xi)=\frac{\pi}{m!\cosh(\pi\xi)}
 \prod_{r=0}^{m-1}\left(r+\tfrac12-i\xi\right).
\]
For \(\xi>0\), its continuous argument beginning at zero is
\[
 \theta_m(\xi)=-\sum_{r=0}^{m-1}\arctan\!\frac{\xi}{r+1/2}.
\]
It is strictly decreasing from zero to \(-m\pi/2\). Its modulus \(R_m(\xi)\) is also strictly decreasing on \((0,\infty)\). To see this *without assuming any graphical evidence*, use the classical Euler product
\[
 \cosh(\pi\xi)=\prod_{r=0}^\infty
 \left(1+\frac{\xi^2}{(r+1/2)^2}\right).
\]
With \(a_r=r+1/2\), the quotient \(R_m(\xi)/R_m(0)\) becomes
\[
 \prod_{r=0}^{m-1}\left(1+\frac{\xi^2}{a_r^2}\right)^{-1/2}
 \prod_{r=m}^\infty\left(1+\frac{\xi^2}{a_r^2}\right)^{-1},
\]
which strictly decreases for \(\xi>0\). Consequently, equal nonzero curve values at distinct real parameters require parameters \(+\xi\) and \(-\xi\). Because \(m_m(-\xi)=\overline{m_m(\xi)}\), equality is equivalent to \(\sin\theta_m(\xi)=0\). Strict phase monotonicity yields exactly one solution of \(\theta_m(\xi)=-j\pi\) for each integer \(j\ge1\) with \(2j<m\), and none otherwise. The corresponding values are real with sign \((-1)^j\), and their strictly decreasing radii make them distinct. Finally, \(R'_m(\xi)<0\) and \(\theta'_m(\xi)<0\) at these parameters, so the tangents at \(+\xi\) and \(-\xi\) are not parallel: every double point is transverse. This exhausts all nonzero intersections.

## Verification

The proof gives an operator-theoretic equivalence **modulo Hilbert--Schmidt operators**, not just convergence of individual matrix entries. It checks both exceptional boundaries: \(b>0\) and \(\lambda=0\). It also distinguishes the Fredholm essential spectrum from the full spectrum, whose possible isolated eigenvalues are not classified.

A standard-library Python script, `CHECK.py`, provides independent finite arithmetic checks of the exact coefficient formula, gamma/beta normalization at zero, reflection symmetry, integer-phase monotonicity, the predicted double-point counts and locations, model approximations, and weakly null finite columns. It passed **6,909 deterministic assertions** when run on the packaged source. These tests do not prove a Fredholm theorem or an infinite-series identity; Steps 1--5 above do.

As a consistency check, \(m_b(0)=\mathrm B(b+\tfrac12,\tfrac12)\) is the \(H^2\) norm computed by Li--Pan--Zhou. The equality of norms follows from positivity of the Wiener--Hopf kernel and the compact model, but the known norm is **not** claimed as new.

## Relationship to prior work

Li--Pan--Zhou (arXiv:2608.19660, first public August 20, 2026) determine Hardy-space norms of precisely \(\mathcal H_b\); their stated results do not determine Fredholm essential spectra or index curves. Bhuyan--Naik (2025) study the identical coefficient matrix on analytic function spaces, emphasizing boundedness and mapping criteria rather than spectral topology. Silbermann (2021) describes the spectra of **shifted classical Hankel Hilbert matrices** with entries \(1/(j+k+\lambda)\). These are not the nonsymmetric, row-weighted matrices above. Pushnitski (arXiv:2103.12642, 2021) develops a continuous-model method for **Hermitian** homogeneous Hardy kernels and self-adjoint spectral density; the kernel \(x^b/(x+y)^{b+1}\) is non-Hermitian when \(b>0\). Bellavita--Chalmoukis--Daskalogiannis--Stylogiannis (arXiv:2307.15334) analyze the related but different Hausdorff-matrix construction, with boundedness, norms and compactness as their main results.

The discrete-to-Wiener--Hopf comparison mechanism is classical. The contribution claimed here is its explicit implementation for this **specific nonsymmetric Hardy-space operator**, the beta-function Fredholm boundary and index formula for all positive \(b\), and the complete transverse self-crossing classification at every positive integer parameter. An earlier equivalent spectral computation under another operator normalization remains possible and should be checked before asserting publication priority.

## Limitations

The theorem does **not** identify the full spectrum, point spectrum, isolated eigenvalues, or kernel/cokernel dimensions outside the Fredholm-index information. It concerns only \(H^2\), not the Banach spaces \(H^p\) for \(p\ne2\). For noninteger positive \(b\), it establishes the exact beta curve but does not classify all of its double points. The result uses the standard scalar Wiener--Hopf Fredholm theorem and the classical Euler product for \(\cosh\); these are cited inputs, not newly proved general results. Independent mathematical review and publication-priority certification remain to be done.

## References

1. S. Li, W. Pan, M. Zhou, *Norm of the generalized Hilbert operator on Hardy spaces*, arXiv:2608.19660 (first posted August 20, 2026). https://arxiv.org/abs/2608.19660
2. S. Bhuyan, S. Naik, *Generalized Hilbert operator on analytic function spaces*, Arab Journal of Mathematical Sciences (online September 24, 2025), DOI:10.1108/AJMS-07-2024-0111. https://doi.org/10.1108/AJMS-07-2024-0111
3. B. Silbermann, *On the Spectrum of Hilbert Matrix Operator*, Integral Equations and Operator Theory 93 (2021), article 21, DOI:10.1007/s00020-021-02637-5. https://link.springer.com/article/10.1007/s00020-021-02637-5
4. A. Pushnitski, *The spectral density of Hardy kernel matrices*, arXiv:2103.12642 (2021), Journal of Operator Theory 89 (2023), 3--21. https://arxiv.org/abs/2103.12642
5. C. Bellavita, N. Chalmoukis, V. Daskalogiannis, G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, arXiv:2307.15334 (2023), Proceedings of the American Mathematical Society 152 (2024), 4759--4773. https://arxiv.org/abs/2307.15334
6. *Wiener--Hopf operator*, Encyclopedia of Mathematics, Fredholm-symbol and winding-number criteria. https://encyclopediaofmath.org/wiki/Wiener-Hopf_operator
7. Euler's infinite product for \(\cosh\), derivable from the Weierstrass products for the gamma function and the gamma reflection identity (classical).
