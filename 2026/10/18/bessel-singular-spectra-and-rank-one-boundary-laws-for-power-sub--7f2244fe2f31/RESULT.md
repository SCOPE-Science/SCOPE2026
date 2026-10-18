# Bessel singular spectra and rank-one boundary laws for power-substituted Volterra operators

## Finding

For every real \(\alpha>0\), consider the power-substituted integration operator on complex \(L^2(0,1)\),
\[
(T_\alpha f)(x)=\int_0^{x^\alpha}f(t)\,dt.
\]
Write \(j_{\mu,n}\) for the \(n\)-th strictly positive zero of the Bessel function \(J_\mu\), with \(n\geq1\). **The complete singular spectrum**, in decreasing order and with multiplicity, is
\[
\boxed{\displaystyle s_n(T_\alpha)=\frac{2\sqrt\alpha}{(1+\alpha)j_{-1/(1+\alpha),n}},\qquad n=1,2,\ldots.}
\]
All singular values are simple. Consequently,
\[
\lim_{n\to\infty}n s_n(T_\alpha)=\frac{2\sqrt\alpha}{\pi(1+\alpha)},\qquad T_\alpha\in\mathcal S_p\ \Longleftrightarrow\ p>1
\]
for each \(0<p<\infty\). Its exact second and fourth singular moments are
\[
\sum_{n\ge1}s_n(T_\alpha)^2=\frac1{1+\alpha},\qquad
\sum_{n\ge1}s_n(T_\alpha)^4=\frac1{(1+\alpha)(1+2\alpha)}.
\]

Both singular boundary regimes are explicit. As \(\alpha\downarrow0\), for each fixed integer \(k\ge1\),
\[
s_1(T_\alpha)=1-\frac34\alpha+o(\alpha),\qquad
\frac{s_{k+1}(T_\alpha)}{\sqrt\alpha}\longrightarrow\frac2{j_{1,k}},\qquad
\frac1\alpha\sum_{n\ge2}s_n(T_\alpha)^2\longrightarrow\frac12.
\]
The limiting operator is the rank-one averaging map \((Rf)(x)=\int_0^1f(t)\,dt\), with exact Hilbert--Schmidt convergence
\[
\|T_\alpha-R\|_{\mathcal S_2}^2=\frac{\alpha}{1+\alpha}.
\]
At the opposite boundary, as \(\alpha\to\infty\), for each fixed \(k\ge1\),
\[
\sqrt\alpha\,s_k(T_\alpha)\longrightarrow\frac2{j_{0,k}}.
\]
Thus a nonnormal family whose ordinary eigenvalues for \(0<\alpha<1\) decay geometrically nevertheless has harmonic singular-value decay for every fixed positive \(\alpha\), and it develops two different Bessel-zero boundary profiles.

## Assumptions and scope

The input/output Hilbert space is \(L^2((0,1),dt)\), with Lebesgue measure, and \(\alpha\) is real and strictly positive. Singular values are nonzero eigenvalues of \((T_\alpha^*T_\alpha)^{1/2}\), counted with multiplicity and listed nonincreasingly. The limiting \(\alpha=0\) operator is introduced only as a boundary limit, not as an element of the stated positive-parameter family. All limits with fixed \(k\) hold for each individual positive integer \(k\); they are not claimed uniform in a growing singular index. \(\mathcal S_p\) means the usual Schatten class of compact Hilbert-space operators.

## Proof

**1. The covariance/Gram kernel.** The integral kernel of \(T_\alpha\) is \(\mathbf1_{\{t\le x^\alpha\}}\), so \(T_\alpha\) is Hilbert--Schmidt and the kernel of \(K_\alpha=T_\alpha^*T_\alpha\) is
\[
K_\alpha(t,s)=1-\max(t,s)^\gamma,\qquad\gamma=\alpha^{-1}>0.
\]
It is positive and compact. Since \(T_\alpha f=0\) implies \(\int_0^yf=0\) for almost all \(y\in(0,1)\), it is injective. The same is true of \(K_\alpha\), so its positive eigenvalues form an infinite sequence decreasing to zero.

**2. Exact boundary-value reduction.** If \(K_\alpha f=\lambda f\), let \(u=K_\alpha f\), where \(\lambda>0\). Differentiating the kernel gives
\[
u'(t)=-\gamma t^{\gamma-1}\int_0^t f(s)\,ds,
\qquad u(1)=0,
\qquad\lim_{t\downarrow0}t^{1-\gamma}u'(t)=0.
\]
Since \(f=u/\lambda\), on \((0,1)\) the differential equation is
\[
u''(t)+\frac{1-\gamma}{t}u'(t)+\frac\gamma\lambda t^{\gamma-1}u(t)=0.
\]
Set \(m=(\gamma+1)/2\), \(\nu=\gamma/(\gamma+1)\in(0,1)\), and \(z=2\sqrt{\gamma/\lambda}/(\gamma+1)\). The general solution is a linear combination of
\[
t^{\gamma/2}J_{-\nu}(zt^m)
\quad\text{and}\quad
t^{\gamma/2}J_{\nu}(zt^m).
\]
At \(t\downarrow0\), the first branch is a nonzero constant plus terms of order \(t^{\gamma+1}\), whereas the second is a nonzero constant times \(t^\gamma\) plus higher terms. The weighted derivative boundary condition eliminates the second branch. The endpoint condition \(u(1)=0\) therefore requires \(J_{-\nu}(z)=0\). Conversely the first branch at every such positive zero satisfies the differential equation and both boundary conditions; recovering \(f=u/\lambda\) yields \(K_\alpha f=\lambda f\) by integrating the differential equation twice and using the two boundary conditions. Since \(-\nu>-1\), all its positive zeros are simple. This determines **all** eigenvalues and proves the displayed singular-value formula. Right singular functions may be normalized from
\[
t^{\gamma/2}J_{-\nu}\big(j_{-\nu,n}t^{(\gamma+1)/2}\big),
\]
and the corresponding left singular functions are \(T_\alpha f_n/s_n(T_\alpha)\). Compact positivity and injectivity complete the singular system.

**3. Ideals, high ranks, and moments.** The classical fixed-order Bessel-zero asymptotic is \(j_{\mu,n}=\pi(n+\mu/2-1/4)+O(n^{-1})\), for fixed \(\mu>-1\). Substitution yields the sharp positive coefficient in the statement and the Schatten equivalence. Direct kernel integration gives
\[
\|T_\alpha\|_{\mathcal S_2}^2=\int_0^1x^\alpha\,dx=\frac1{1+\alpha}
\]
and, because \(K_\alpha\) is self-adjoint Hilbert--Schmidt,
\[
\operatorname{tr}(K_\alpha^2)=2\int_0^1t\big(1-t^\gamma\big)^2\,dt
=1-\frac4{\gamma+2}+\frac1{\gamma+1}
=\frac1{(1+\alpha)(1+2\alpha)}.
\]
These are the respective sums of the squared and fourth-powered singular values.

**4. The small-\(\alpha\) boundary.** Here \(\nu=1/(1+\alpha)\uparrow1\). The normalized Bessel series
\[
\left(\frac z2\right)^{1-\varepsilon}J_{-1+\varepsilon}(z)
=\sum_{r\ge0}\frac{(-1)^r(z/2)^{2r}}{r!\,\Gamma(r+\varepsilon)},
\qquad\varepsilon=1-\nu\downarrow0,
\]
converges locally uniformly to \(-zJ_1(z)/2\). Its constant coefficient equals \(\varepsilon+O(\varepsilon^2)\), whereas its quadratic coefficient tends \(-1/4\); hence its smallest positive zero is \(2\sqrt\varepsilon(1+o(1))\). The remaining positive zeros converge, in index order, to \(j_{1,k}\), \(k\ge1\), by simplicity, local uniform convergence, and separation of zeros. Because \(\varepsilon=\alpha/(1+\alpha)\) and the singular-value prefactor is \(2\sqrt\alpha/(1+\alpha)\), this proves \(s_1\to1\) and the fixed-rank scaled limits.

To exchange the remaining squared-singular-value sum and the limit, use the standard Bessel zero bound \(j_{-\nu,k+1}\ge c k\) for \(\nu\in[1/2,1)\), \(k\ge1\), with an absolute \(c>0\) (also following from the uniform large-zero asymptotic for orders in \([-1,-1/2]\)). Dominated convergence gives
\[
\lim_{\alpha\downarrow0}\frac1\alpha\sum_{k\ge1}s_{k+1}(T_\alpha)^2
=4\sum_{k\ge1}j_{1,k}^{-2}=\frac12.
\]
The last equality is the classical Rayleigh sum \(\sum_{k\ge1}j_{\mu,k}^{-2}=1/(4(\mu+1))\) at \(\mu=1\), which also follows by comparing the quadratic coefficient in the canonical product for \(J_\mu\). Subtract this tail from the exact squared Hilbert--Schmidt norm \((1+\alpha)^{-1}=1-\alpha+o(\alpha)\); thus \(s_1^2=1-3\alpha/2+o(\alpha)\), and taking square roots proves \(s_1=1-3\alpha/4+o(\alpha)\). Finally the difference \(T_\alpha-R\) has kernel \(-\mathbf1_{\{t>x^\alpha\}}\), so its squared Hilbert--Schmidt norm is the area \(\int_0^1(1-x^\alpha)dx=\alpha/(1+\alpha)\).

**5. The large-\(\alpha\) boundary.** The order \(-1/(1+\alpha)\) tends to zero, each positive zero converges to the corresponding positive zero of \(J_0\), and \(2\alpha/(1+\alpha)\to2\). Multiplication of the exact singular-value formula by \(\sqrt\alpha\) gives the claimed \(2/j_{0,k}\) limit.

## Verification

A standalone checker reproduces the Bessel-zero spectrum using root brackets for orders in \((-1,0)\), compares its first five singular values against independently discretized Gram kernels on seven parameter values, and checks the two boundary profiles and exact moment identities. It is included as `check_spectrum.py` and requires Python, NumPy and SciPy. Run `python check_spectrum.py` in the extracted directory. Discretized finite matrices are used only as consistency checks; every general identity and limiting statement above is proved analytically.

## Relationship to prior work

Domanov's 2007 study `doi:10.4064/bc75-0-8` determines the **ordinary eigenvalues and eigenfunctions** of the same nonnormal operator for \(0<\alpha<1\): its ordinary eigenvalues are \((1-\alpha)\alpha^{n-1}\). The complete six-page primary text was inspected, including the proposition, remarks and references: it does not provide the **singular** spectrum or the two singular boundary profiles. The difference matters: geometrically decaying nonzero eigenvalues coexist with singular values comparable to \(\(1/n\)\), so ordinary eigenvalues do not determine low-rank approximation error. Domanov's 2008 extension `doi:10.4064/sm185-1-3` concerns ordinary spectral properties of general substitution maps; only its accessible bibliographic description and abstract were available during comparison.

General Volterra singular-value asymptotic theory, for example Tuan and Gorenflo (1996), provides related first-order decay for weighted integral operators; the present finding does **not** claim the generic \(\(1/n\)\) law as new. The specific whole-sequence Bessel-zero identification, explicit rank-one boundary layer (including its coefficient and escaping residual spectrum), and opposite Bessel boundary profile are the object-specific conclusions assessed here. The Bessel identities used in the proof are classical (NIST DLMF, Section 10.21). Neither an absence of search results nor this comparison proves absolute publication priority.

## Limitations

The operator parameter is a positive **real** power, with ordinary unweighted \(L^2(0,1)\); no extension to complex powers, arbitrary substitution maps or other \(L^p\) spaces is asserted. The fixed-rank extreme-parameter limits do not claim uniformity over a growing singular index. The asymptotic formula for ordinary eigenvalues is credited to prior literature, not presented as a new claim. Accessible abstracts cannot exclude unindexed or inaccessible work containing equivalent full singular-spectrum formulas. Independent mathematical and bibliographic validation has not been performed.

## References

1. I. Yu. Domanov, *On the spectrum and eigenfunctions of the operator \((Vf)(x)=\int_0^{x^\alpha}f(t)\,dt\)*, Banach Center Publications 75 (2007), 137–142. DOI: `10.4064/bc75-0-8`. Public full text: `https://impan.pl/shop/en/publication/transaction/download/product/85864`. Dated arXiv deposit `1301.4886v1`, 2013-01-21.
2. I. Domanov, *On the spectrum of the operator which is a composition of integration and substitution*, Studia Mathematica 185 (2008), 49–65. DOI: `10.4064/sm185-1-3`.
3. Vu Kim Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461. DOI: `10.1080/01630569608816704`.
4. NIST Digital Library of Mathematical Functions, §10.21, *Zeros of Bessel and Hankel Functions*, `https://dlmf.nist.gov/10.21`.
