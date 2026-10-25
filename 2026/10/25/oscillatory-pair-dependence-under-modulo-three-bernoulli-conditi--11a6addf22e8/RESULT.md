# Oscillatory pair dependence under modulo-three Bernoulli conditioning

## Finding
For every integer \(n\ge3\), bias \(0<p<1\), and residue \(r\in\{0,1,2\}\), let \(X_1,\ldots,X_n\) be independent Bernoulli\((p)\) variables, and condition their joint law on \(E_{n,r}=\{\sum_{j=1}^{n}X_j\equiv r\pmod3\}\). Let \(C_{n,r}(p)=\operatorname{Cov}(X_1,X_2\mid E_{n,r})\), \(q=1-p\), \(\omega=e^{2\pi i/3}\), and \(z=q+p\omega=\rho e^{i\theta}\), where \(\rho=\sqrt{1-3pq}\) and \(0<\theta<2\pi/3\). Define
\[
\phi_{n,r}=(n-2)\theta-\frac\pi3-\frac{2\pi r}{3}.
\]
Then the **exact finite-sample pair covariance** is
\[
C_{n,r}(p)=
\frac{3p^2q^2\rho^{n-2}\bigl(2\cos\phi_{n,r}-\rho^{n-2}\bigr)}
{\bigl[1+2\rho^n\cos(n\theta-2\pi r/3)\bigr]^2}.
\tag{1}
\]
For each fixed \(p\in(0,1)\) and each residue \(r\), the sequence \(C_{n,r}(p)\) is strictly positive for infinitely many integers \(n\) and strictly negative for infinitely many others. Moreover,
\[
\frac{C_{n,r}(p)}{6p^2q^2\rho^{n-2}}=
\cos\phi_{n,r}+O_p(\rho^{n-2}).\tag{2}
\]
Whenever \(\theta/(2\pi)\) is irrational (which holds for every \(p\) outside a countable set), the empirical distribution of the normalized covariances in (2) converges to the arcsine law with density \(1/(\pi\sqrt{1-u^2})\) on \((-1,1)\); the positive and negative signs each have limiting natural density \(1/2\). In particular, the normalized sequence has limsup \(1\) and liminf \(-1\).

For fair bits \(p=1/2\), the sign is **exactly six-periodic from \(n=3\) onward**:
\[
\operatorname{sgn} C_{n,r}(1/2)=
\begin{cases}
+1,&n-3-2r\pmod6\in\{0,1,5\},\\
-1,&n-3-2r\pmod6\in\{2,3,4\}.
\end{cases}\tag{3}
\]
All covariance signs in (3) are strict.

## Assumptions and scope
Only independent, identically distributed Bernoulli trials with a common fixed \(p\in(0,1)\) are considered before conditioning. Conditioning is on a *congruence class of the total*, not on a fixed total. The event \(E_{n,r}\) has positive probability for every \(n\ge3\) and every \(r\in\{0,1,2\}\). The subscripts on \(C_{n,r}(p)\) specify the number of coordinates and the residue; by exchangeability, any two distinct coordinates have the same conditional covariance. All asymptotic statements hold as integer \(n\to\infty\) with \(p,r\) fixed. The \(O_p\)-constant may depend on \(p\) but can be selected uniformly across the three residues.

## Proof
**1. Residue probabilities.** Put \(A_j(m)=\Pr\{\sum_{k=1}^{m}X_k\equiv j\pmod3\}\) for any integer \(m\ge0\) and index \(j\) interpreted modulo three. The finite root-of-unity filter yields
\[
A_j(m)=\frac{1+2\operatorname{Re}(\omega^{-j}z^m)}3.\tag{4}
\]
Each \(A_r(n)>0\) in the stated range, since at least one feasible sum among \(0,1,2,3\) represents each residue and every Bernoulli word has positive probability. Independence before conditioning gives
\[
\Pr(X_1=1\mid E_{n,r})=\frac{pA_{r-1}(n-1)}{A_r(n)},\qquad
\Pr(X_1=X_2=1\mid E_{n,r})=\frac{p^2A_{r-2}(n-2)}{A_r(n)}.
\]
Consequently,
\[
C_{n,r}(p)=p^2\frac{A_{r-2}(n-2)A_r(n)-A_{r-1}(n-1)^2}{A_r(n)^2}.\tag{5}
\]

**2. Exact cancellation of the Fourier square.** Substitute (4) into the numerator of (5). In its terms linear in a nontrivial Fourier mode, the factor is
\[
\omega^{-r}z^{n-2}(z^2-2\omega z+\omega^2)
=q^2\omega^{-r}z^{n-2}(1-\omega)^2.
\]
In its quadratic terms, the nonconjugate mode products cancel. The remaining cross terms combine as
\[
2|z|^{2n-4}\bigl(\operatorname{Re}(\omega z^2)-|z|^2\bigr)
=-3q^2|z|^{2n-4},
\]
where the last identity follows by direct expansion of \(z=q+p\omega\), using \(\omega^2+\omega+1=0\). Thus the numerator of (5) equals
\[
\frac{q^2}{9}\left[2\operatorname{Re}\bigl((1-\omega)^2\omega^{-r}z^{n-2}\bigr)-3|z|^{2n-4}\right].\tag{6}
\]
Now \((1-\omega)^2=3e^{-i\pi/3}\), \(|z|^2=1-3pq\), and \(9A_r(n)^2=[1+2\operatorname{Re}(\omega^{-r}z^n)]^2\). Inserting (6) into (5) proves (1), including its normalization and the quadratic correction.

**3. Asymptotic cosine.** For fixed \(0<p<1\), \(1/2\le\rho<1\). Divide (1) by \(6p^2q^2\rho^{n-2}\) to get
\[
Y_{n,r}=\frac{\cos\phi_{n,r}-\rho^{n-2}/2}
{[1+2\rho^n\cos(n\theta-2\pi r/3)]^2}.\tag{7}
\]
The denominator tends to one. More explicitly, whenever \(2\rho^n\le1/2\), the elementary bound on \((1+u)^{-2}\) for \(|u|\le1/2\) gives \(|Y_{n,r}-\cos\phi_{n,r}|\le22\rho^{n-2}\), uniformly over \(r\). This proves (2).

**4. Infinitely many opposite signs for every bias.** The argument \(\theta(p)\) lies strictly between \(0\) and \(2\pi/3\). If \(\theta/(2\pi)\) is irrational, the phases \(\phi_{n,r}\) are dense modulo \(2\pi\), so there are infinitely many values of \(n\) in each of the open sets where the cosine exceeds \(1/2\) or is below \(-1/2\). If \(\theta/(2\pi)=a/m\) in lowest terms, then \(0<a/m<1/3\) forces \(m\ge4\). Each period of phases has \(m\) equally spaced points; its cosine values sum to zero and cannot all vanish. Hence the period contains a strictly positive and a strictly negative cosine. Repetition along each corresponding residue class of integers \(n\), together with (2), gives eventually strict positive and negative covariances. Thus either case gives infinitely many sign changes.

**5. Arcsine empirical limit and exceptional biases.** When \(\theta/(2\pi)\) is irrational, rotation by \(\theta\) is equidistributed on the circle. The continuous image under cosine is the arcsine measure; the error in (2) vanishes, so the normalized covariance has the same empirical limiting law. The boundary of the positive half-circle has zero angular measure, giving asymptotic positive/negative frequencies \(1/2\) each; density also gives limsup and liminf. Differentiating \(\arg(q+p\omega)\) gives
\[
\frac{d\theta}{dp}=\frac{\sqrt3}{2(1-3p(1-p))}>0.
\]
Consequently \(p\mapsto\theta/(2\pi)\) is strictly increasing; its preimage of the rationals is countable, proving the stated almost-everywhere assertion.

**6. Exact six-cycle at fair bias.** If \(p=1/2\), then \(z=\tfrac12e^{i\pi/3}\), and \(\phi_{n,r}=\pi(n-3-2r)/3\). For every integer argument, this cosine belongs to \(\{1,1/2,-1/2,-1\}\). For \(n\ge3\), the negative correction in the numerator of (1) is \(2^{-(n-2)}\le1/2\), strictly smaller than \(2|\cos\phi_{n,r}|\). The denominator is positive. Therefore the sign is exactly that of the cosine, yielding (3).

## Verification
The standalone file `check_mod3.py` implements the residue probabilities by exact rational binomial sums and, independently, the spectral formula in the quadratic number field \(\mathbb Q(\omega)\) using pairs of rationals with \(\omega^2+\omega+1=0\). The two forms agree **exactly**, not numerically, in 588 triples: seven rational biases \(p\in\{1/10,1/5,1/3,1/2,2/3,4/5,9/10\}\), every \(3\le n\le30\), and all three residues. The same script verifies the six-class sign rule at fair bias across the tested range. The exact algebra in the proof, not these finite checks, establishes the infinite results.

## Relationship to prior work
Heng, Jacob, and Ju (2020) analyze independent Bernoulli variables conditioned on a *fixed* sum and give a sampling-chain convergence theorem; their fixed-level conditioning is different from the union of sum levels modulo three used here. Fontana and Semeraro (2022) develop convex-geometric bounds for Bernoulli dependence at fixed marginals; such general bounds do not determine the signs of this explicit dimension-dependent conditional family. Mutti and Semeraro (2023) characterize extremal negative dependence and certain correlation summaries for symmetric Bernoulli vectors; their convex-order and copula results do not assert the oscillatory modulus-three covariance identity, the six-class sign law, or the arcsine empirical limit. A published modular-freedom theorem for pairwise-independent fair bits instead asks which *residue distributions* can be attained when pair independence is retained, not what correlation is *created* by conditioning independent coordinates on one residue. The algebraic root-of-unity filter and Weyl equidistribution are classical tools and are not claimed as original. The contribution assessed here is their exact combined consequence for this concrete conditioned family. A priority search did not identify a covering statement; it is not a proof of historical uniqueness.

## Limitations
This is a self-reviewed mathematical argument, not an independently audited result. The exact covariance formula concerns pairwise dependence only, not negative association or full multivariate stochastic ordering. Biases with rational angular frequency may have different empirical normalized distributions; an arcsine limit is claimed only for irrational frequencies. For fixed \(p\), the raw covariance decays exponentially even though its sign reverses indefinitely. Wider historical priority, especially work on congruence-restricted binary words under different terminology, remains a residual risk.

## References
1. J. Heng, P. E. Jacob, and N. Ju, *A simple Markov chain for independent Bernoulli variables conditioned on their sum*, arXiv:2012.03103, first posted 2020-12-05. https://arxiv.org/abs/2012.03103
2. R. Fontana and P. Semeraro, *Computational and Analytical Bounds for Multivariate Bernoulli Distributions*, Journal of Statistical Theory and Practice 16 (2022), article 6, https://doi.org/10.1007/s42519-021-00231-x
3. A. Mutti and P. Semeraro, *Symmetric Bernoulli distributions and minimal dependence copulas*, arXiv:2309.17346, first posted 2023-09-29. https://arxiv.org/abs/2309.17346
