# Carathéodory control of positive-power radial Bergman kernels

## Finding
For every real \(\gamma>0\) and \(q\ge0\), let \(K_{q,\gamma}(z,w)=\mathcal K_{q,\gamma}(z\overline w)\) be the weighted Bergman reproducing kernel defined below. For all \(|t|<1\),
\[
\operatorname{Re}\big[(1-t)\mathcal K_{q,\gamma}(t)\big]>0,
\]
and more precisely
\[
\operatorname{Re}\big[(1-t)\mathcal K_{q,\gamma}(t)\big]
\ge \frac{1+\gamma}{1+\gamma+q}\frac{1-|t|}{1+|t|}.
\]
The kernel is therefore zero-free on \(\mathbb D\times\mathbb D\). The principal assertion is the half-plane inclusion, which is stronger than zero-freeness.

## Assumptions and scope
Fix arbitrary real \(q\ge0\) and \(\gamma>0\). The Hilbert norm is
\[
\|f\|_{q,\gamma}^2=\int_{\mathbb D}|f(z)|^2(1+q|z|^{2\gamma})\,\frac{dA(z)}{\pi}.
\]
The planar area is normalized so that \(\int_{\mathbb D}dA/\pi=1\). The scalar kernel variable is \(t=z\overline w\), with \(z,w\in\mathbb D\). Put \(c=\gamma/(1+q)>0\), \(d=\gamma q/(1+q)\ge0\).

## Proof
The monomials are orthogonal and their squared norms equal
\[
m_n=\frac1{n+1}+\frac{q}{n+\gamma+1},\qquad n\ge0.
\]
Therefore the kernel Taylor coefficients are
\[
\frac1{m_n}=\frac{n+1}{1+q}\left(1+\frac{d}{n+1+c}\right).
\]
The geometric-series derivative identity and the moment formula \(\int_0^1x^{n+c}dx=(n+c+1)^{-1}\) give the absolutely and locally uniformly convergent integral representation
\[
\mathcal K_{q,\gamma}(t)=\frac1{1+q}\left[\frac1{(1-t)^2}+d\int_0^1\frac{x^c}{(1-xt)^2}\,dx\right],\quad |t|<1.
\]
We establish an elementary positivity lemma. For every \(x\in[0,1]\), the analytic function \(h_x(t)=(1-t)/(1-xt)^2\) has strictly positive real part throughout the open unit disk. At \(x=1\), \(h_1(t)=1/(1-t)\) has positive real part directly. For \(0\le x<1\), the boundary values are continuous and, for \(t=e^{i\theta}\),
\[
\operatorname{Re}h_x(e^{i\theta})
=\frac{(1-\cos\theta)[1+2x-x^2(1+2\cos\theta)]}{(1-2x\cos\theta+x^2)^2}\ge0.
\]
Indeed, the square bracket is bounded below by \((1-x)(1+3x)\ge0\). Harmonicity and the minimum principle imply nonnegative real part in the disk; it is strictly positive because \(h_x(0)=1\) and a nonnegative harmonic function with an interior zero must vanish identically. Multiplying the integral formula by \(1-t\), then integrating positive-real quantities against the positive measure \(d x^c dx\), proves the strict half-plane assertion even when \(d=0\).

Finally \(H(t)=(1-t)\mathcal K_{q,\gamma}(t)\) has positive real part and \(H(0)=\mathcal K_{q,\gamma}(0)=(1+\gamma)/(1+\gamma+q)>0\). The classical Carathéodory estimate for \(H(t)/H(0)\) yields the displayed quantitative bound. Since \(1-t\ne0\) on \(\mathbb D\), the kernel never vanishes.

## Verification
The standalone script `verify.py` checks the monomial-moment and integral-coefficient identities with exact rational arithmetic for several parameter values and tests the boundary positivity formula and quantitative real-part lower bound numerically. It reports 24,416 finite assertions passed when executed with Python's standard library. These finite tests are diagnostic; the infinite-parameter theorem follows from the analytic proof above.

## Relationship to prior work
Known general results on radial log-subharmonic weighted Bergman kernels yield Bergman-type representations and canonical divisor properties; they do not give the explicit Carathéodory inclusion for the particular normalizing factor \(1-t\) here. Zeytuncu's examples show why radial comparability alone is insufficient for zero-free kernels. Miña-Díaz provides an explicit representation for a different family of weights built from Blaschke factors. The present positive-power perturbation produces a positive mixture of elementary Carathéodory functions and thus quantitative off-diagonal half-plane control.

## Limitations
The result is restricted to the unit disk and the two-parameter positive radial perturbation \(1+q|z|^{2\gamma}\). It does not assert that arbitrary increasing, log-subharmonic, or comparable radial weights have this half-plane property. The lower bound is a universal Carathéodory consequence, not claimed optimal for each fixed \(q,\gamma\). Historical priority for the precise half-plane normalization has not been independently certified.

## References
- E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118 (first public 2022-12-15).
- Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: \(L^p\) Regularity and Zeros*, arXiv:1009.2806 (2010).
- S. Shimorin, *An Integral Formula for Weighted Bergman Reproducing Kernels*, Complex Variables 47 (2002), 1015–1028; DOI: 10.1080/02781070290034566.
- A. Aleman, H. Hedenmalm, S. Richter, *Recent progress and open problems in the Bergman space*, survey, Section 12.
- B. J. Boudreaux, *Equivalent Bergman Spaces with Inequivalent Weights*, arXiv:1802.01099 (2018).
