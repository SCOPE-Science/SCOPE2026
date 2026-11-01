# A Gaussian interface-merger law for projective Fock concentration bands

## Finding

The spectral defect of a circular band in projective Gaussian Fock quantization exhibits a **sharp two-interface merger crossover**. Let \(m=n+1\) and \(0\le a<b\le1\). Define \(V_n(a,b)=\operatorname{tr}(T_{n;a,b}(I-T_{n;a,b}))\). For independent copies of the monotone binomial interval defined below, there is the finite-dimensional exact identity
\[
V_n(a,b)=\tfrac12\mathbb E|I_1\triangle I_2|.
\]
For any sequences \(a_n\to t\in(0,1)\), \(b_n-a_n\to0\), and \(\sqrt{n+1}(b_n-a_n)\to c\in[0,\infty]\),
\[
\lim_{n\to\infty}\frac{V_n(a_n,b_n)}{\sqrt{n+1}}=H_t(c),\quad
H_t(c)=c\operatorname{erfc}\!\left(\frac{c}{2\sigma}\right)+\frac{2\sigma}{\sqrt\pi}\left(1-e^{-c^2/(4\sigma^2)}\right),\quad\sigma=\sqrt{t(1-t)}.
\]
The value at \(c=\infty\) is \(2\sigma/\sqrt\pi\). At finite \(c\ge0\), \(H_t'(c)=\operatorname{erfc}(c/(2\sigma))\), and at finite \(c>0\), \(H_t''(c)=-e^{-c^2/(4\sigma^2)}/(\sigma\sqrt\pi)<0\). Thus two close projective interfaces do not contribute independent boundary defects at the critical separation \(b-a\asymp n^{-1/2}\). The formula interpolates sharply between vanished width and the sum of two separated interface contributions.

## Assumptions and scope

Use the analytic Gaussian Fock Hilbert space
\[
\mathcal F^2(\mathbb C^2)=\left\{f\text{ entire}:\ \pi^{-2}\int_{\mathbb C^2}|f(z)|^2e^{-|z|^2}\,dA(z_1)dA(z_2)<\infty\right\}.
\]
For integer \(n\ge0\), let \(\mathcal H_n\) be its homogeneous polynomials of total degree \(n\), with orthonormal basis \(e_{n,k}(z)=z_1^kz_2^{n-k}/\sqrt{k!(n-k)!}\), \(0\le k\le n\). Let \(q(z)=|z_1|^2/(|z_1|^2+|z_2|^2)\) outside the Gaussian-null origin. For \(0\le a<b\le1\), the self-adjoint compression \(T_{n;a,b}:\mathcal H_n\to\mathcal H_n\) is defined by
\[
\langle T_{n;a,b}f,g\rangle=\pi^{-2}\int_{\mathbb C^2}\mathbf1_{\{a<q(z)<b\}}f(z)\overline{g(z)}e^{-|z|^2}\,dA(z_1)dA(z_2).
\]
The theorem is **degreewise**, not a trace-class assertion on the full infinite direct sum. All expectations below are taken over newly specified auxiliary uniform variables, not over a claimed physical random-point process.

## Proof

**1. Exact eigenvalues and normalization.** Angular integration makes \(T_{n;a,b}\) diagonal in \(e_{n,k}\). Under the probability density \(|e_{n,k}|^2\pi^{-2}e^{-|z|^2}\), the independent squared moduli \(|z_1|^2\), \(|z_2|^2\) are gamma with respective integer shapes \(k+1\) and \(n-k+1\). Hence \(q\sim\mathrm{Beta}(k+1,n-k+1)\), and
\[
\lambda_{n,k}(a,b)=\frac{m!}{k!(n-k)!}\int_a^b x^k(1-x)^{n-k}\,dx,
\qquad m=n+1.
\]
The beta–binomial tail identity gives, for a binomial variable \(B_x\sim\mathrm{Bin}(m,x)\),
\[
\lambda_{n,k}=\mathbb P(B_a\le k)-\mathbb P(B_b\le k).
\]
In particular \(0\le\lambda_{n,k}\le1\). Summing beta densities over \(k=0,\ldots,n\) yields \(\sum_k\frac{m!}{k!(n-k)!}x^k(1-x)^{n-k}=m\); therefore
\[
\operatorname{tr}T_{n;a,b}=m(b-a).
\]

**2. A monotone coupling and the exact defect.** Take \(m\) independent uniform random variables \(U_1,\ldots,U_m\) on \([0,1]\). For each \(x\in[0,1]\), put \(X_x=\sum_{j=1}^m\mathbf1_{\{U_j<x\}}\). The coupled counts obey \(X_a\le X_b\) almost surely. Define the random set of integers \(I=\{X_a,X_a+1,\ldots,X_b-1\}\subseteq\{0,\ldots,n\}\), interpreted as empty if endpoints coincide. Then
\[
\mathbb P(k\in I)=\mathbb P(X_a\le k)-\mathbb P(X_b\le k)=\lambda_{n,k}.
\]
Let \(I_1,I_2\) be independent copies. For every integer \(k\), independence implies
\[
\mathbb P(k\in I_1\triangle I_2)=2\lambda_{n,k}(1-\lambda_{n,k}).
\]
Sum over the finite range \(0\le k\le n\) to obtain the exact identity claimed, without an asymptotic approximation.

**3. Finite critical-width limit.** Assume \(a_n\to t\in(0,1)\), \(b_n-a_n\to0\), and \(\sqrt m(b_n-a_n)\to c<\infty\). For either independent interval index \(i=1,2\), the binomial central limit theorem gives
\[
\frac{X_{a_n}^{(i)}-ma_n}{\sqrt m}\ \Longrightarrow\ \sigma Z_i,\qquad \sigma^2=t(1-t),
\]
with independent standard normal \(Z_1,Z_2\). Furthermore, each increment \(X_{b_n}^{(i)}-X_{a_n}^{(i)}\) is binomial with parameters \(m,b_n-a_n\); its scaled expectation tends to \(c\), while its scaled variance is at most \(b_n-a_n\to0\). By joint convergence, the two rescaled random intervals converge to \([\sigma Z_1,\sigma Z_1+c]\) and \([\sigma Z_2,\sigma Z_2+c]\). Symmetric-difference length of two bounded intervals is continuous in their endpoints, and discrete cardinality divided by \(\sqrt m\) converges to the continuous length under this endpoint convergence.

For any two intervals with endpoints \((A_i,B_i)\), one has \(|I_1\triangle I_2|\le|A_1-A_2|+|B_1-B_2|\). Each endpoint difference here has second moment bounded by \(m/2\) (two independent binomials with variance at most \(m/4\)), so the squared normalized cardinalities are uniformly bounded in expectation. Uniform integrability permits passage to expected values. The symmetric difference of two length-\(c\) real intervals separated by distance \(d\) has length \(2\min(c,d)\). Thus
\[
\lim_{n\to\infty}\frac{V_n(a_n,b_n)}{\sqrt m}=\mathbb E\min\!\left(c,\sigma|Z_1-Z_2|\right).
\]
Since \(Z_1-Z_2\sim N(0,2)\), its scaled absolute value has survival function \(\operatorname{erfc}(u/(2\sigma))\) for \(u\ge0\). The layer-cake identity gives
\[
\mathbb E\min(c,\sigma|Z_1-Z_2|)=\int_0^c\operatorname{erfc}\!\left(\frac{u}{2\sigma}\right)du
=c\operatorname{erfc}\!\left(\frac{c}{2\sigma}\right)+\frac{2\sigma}{\sqrt\pi}\left(1-e^{-c^2/(4\sigma^2)}\right).
\]
This covers \(c=0\) without requiring \(b_n-a_n\) to be exactly zero.

**4. Diverging critical width.** Suppose instead \(\sqrt m(b_n-a_n)\to\infty\), while \(a_n,b_n\to t\in(0,1)\). Each interval length is \(m(b_n-a_n)+O_{\mathbb P}(\sqrt{m(b_n-a_n)})\), much larger than its endpoint fluctuation \(O_{\mathbb P}(\sqrt m)\). Hence the two coupled random integer intervals intersect with probability tending to one. On their intersection event,
\[
|I_1\triangle I_2|=|X_a^{(1)}-X_a^{(2)}|+|X_b^{(1)}-X_b^{(2)}|.
\]
The previously used endpoint-difference upper bound and uniform \(L^2\) bounds show that discarding the complement changes the normalized expected value by \(o(1)\). The binomial difference CLT, with uniform integrability, gives independently for \(x=a_n\) or \(x=b_n\) that
\[
\frac{\mathbb E|X_x^{(1)}-X_x^{(2)}|}{\sqrt m}\longrightarrow \mathbb E|N(0,2\sigma^2)|=\frac{2\sigma}{\sqrt\pi}.
\]
Half the sum yields \(H_t(\infty)=2\sigma/\sqrt\pi\). This proves all stated regimes and also the derivative assertions by differentiating the explicit integral.

## Verification

The independent finite-dimensional formulas permit both exact rational and numerical checks. Run the included standard-library-only script `checks.py` with Python 3.10 or newer. It computes beta–binomial spectra by two routes; checks the exact trace and the random-interval coupling by complete finite multinomial enumeration at small dimensions; and compares the normal crossover with direct spectral-defect sums at growing degrees. These finite checks corroborate the constants and normalizations but **do not constitute a proof of the infinite limits**; the proof above uses the binomial central limit theorem, interval geometry, and a uniform-integrability estimate.

## Relationship to prior work

González-Flores, Dupont-García, López-Martínez and Hérnandez-Zamora (2023), Theorem 2 and Section 6, decompose circle-invariant Gaussian Fock Toeplitz operators into projective Bergman components, providing the natural degreewise setting. That result does not itself state the finite symmetric-difference identity or the critical two-interface crossover. The projective determinantal ensemble of Beltrán and Etayo (2017) provides a parallel interpretation of the finite-rank projective kernel, not an asymptotic statement about this collapsing band. Charlier (2021, Corollary 1.6) establishes higher-order counting cumulants for **fixed separated** radial jumps and their asymptotic independence; his assumption of fixed distinct radii does not imply the \(m^{-1/2}\) merging regime. Akemann, Byun and Ebke (2022) establish radial **single-disk** bulk and edge number-variance laws, not the covariance needed for shrinking annular differences. The new claim is explicitly a merging-band refinement rather than another proof of a separated-boundary constant.

## Limitations

The asymptotic profile is proved for interior projective latitudes \(0<t<1\), two radial boundaries merging to that same latitude, and the indicated critical or larger separation scales. It does not treat bands approaching projective poles, non-rotational sets, higher complex dimensions, or all higher cumulants. The identification with a determinantal process is not needed for the proof. Historical priority remains subject to possible equivalent formulations in broader random-normal-matrix and Toeplitz concentration literature. No independent mathematical audit has been performed.

## References

1. C. González-Flores, L. A. Dupont-García, R. R. López-Martínez and F. G. Hérnandez-Zamora, *Toeplitz Operators on Fock Space over Cn with Invariant Symbols under the Action of the Unit Circle*, Axioms 12 (2023), 1080, published 25 November 2023, https://doi.org/10.3390/axioms12121080. MSC2020 primary 30H20.
2. C. Charlier, *Asymptotics of determinants with a rotation-invariant weight and discontinuities along circles*, arXiv:2109.03660 (first posted 8 September 2021), https://arxiv.org/abs/2109.03660.
3. G. Akemann, S.-S. Byun and M. Ebke, *Universality of the number variance in rotational invariant two-dimensional Coulomb gases*, arXiv:2206.08815 (first posted 17 June 2022), https://arxiv.org/abs/2206.08815.
4. C. Beltrán and U. Etayo, *The projective ensemble and distribution of points in odd-dimensional spheres*, arXiv:1703.00416 (first posted 1 March 2017), https://arxiv.org/abs/1703.00416.
