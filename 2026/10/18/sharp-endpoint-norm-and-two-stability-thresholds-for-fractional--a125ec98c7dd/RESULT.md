# Sharp endpoint norm and two stability thresholds for fractional directed-cycle differences

## Finding
Fix an integer \(n\ge2\). On the cyclic group \(\mathbb Z/n\mathbb Z\), let \((S_nf)(j)=f(j+1)\) and, for \(0<\alpha<2\), define the fractional forward-difference matrix
\[
 A_{n,\alpha}=(I-S_n)^\alpha
  =\sum_{k=0}^{\infty}(-1)^k\binom{\alpha}{k}S_n^k.
\]
The series converges absolutely in operator norm. Write \(F_n(\alpha)\) for its common induced \(\ell^1\)- and \(\ell^\infty\)-norm.

**Exact finite-size norm.** If \(0<\alpha<1\), then
\[
F_n(\alpha)=2-2\sum_{j=1}^{\infty}
 \left|\binom{\alpha}{jn}\right|
=2-\frac{2\sin(\pi\alpha)}{\pi}
 \int_0^1\frac{t^{n-\alpha-1}(1-t)^\alpha}{1-t^n}\,dt.
\]
If \(1<\alpha<2\), then
\[
F_n(\alpha)=2\alpha-2\sum_{j=1}^{\infty}
 \left|\binom{\alpha}{jn+1}\right|
=2\alpha+\frac{2\sin(\pi\alpha)}{\pi}
 \int_0^1\frac{t^{n-\alpha}(1-t)^\alpha}{1-t^n}\,dt.
\]
At \(\alpha=1\), \(F_n(1)=2\). In each of the open intervals \((0,1)\) and \((1,2)\), \(F_n(\alpha)\) increases strictly with the cycle size \(n\), with
\[
 F_2(\alpha)=2^\alpha,
 \qquad \lim_{n\to\infty}F_n(\alpha)
 =\begin{cases}2,&0<\alpha\le1,\\2\alpha,&1\le\alpha<2.\end{cases}
\]
In particular, for every noninteger \(\alpha\in(0,2)\) and \(n>2\), \(F_n(\alpha)>2^\alpha\).

**Sharp finite-size correction.** With \(\zeta\) denoting the Riemann zeta function, for each fixed \(0<\alpha<1\),
\[
\begin{aligned}
F_n(\alpha)={}&2-\frac{2\alpha\zeta(1+\alpha)}{\Gamma(1-\alpha)}n^{-1-\alpha}\\
 &-\frac{\alpha^2(\alpha+1)\zeta(2+\alpha)}{\Gamma(1-\alpha)}n^{-2-\alpha}
 +O_\alpha(n^{-3-\alpha}).
\end{aligned}
\]
For each fixed \(1<\alpha<2\),
\[
\begin{aligned}
F_n(\alpha)={}&2\alpha-\frac{2\zeta(1+\alpha)}{\Gamma(-\alpha)}n^{-1-\alpha}\\
 &+\frac{(\alpha+1)(2-\alpha)\zeta(2+\alpha)}{\Gamma(-\alpha)}n^{-2-\alpha}
 +O_\alpha(n^{-3-\alpha}).
\end{aligned}
\]
The estimates are uniform when \(\alpha\) remains in any fixed compact subinterval of \((0,1)\) or \((1,2)\).

**Positive-versus-stable semigroups.** Let \(T_{n,\alpha}(t)=e^{-tA_{n,\alpha}}\), \(t\ge0\), and let \(E_n f=n^{-1}\sum_j f(j)\) be the averaging projection. For every \(n\ge3\), \(T_{n,\alpha}\) is a positive Markov semigroup precisely when \(0<\alpha\le1\); for \(n=2\) it remains positive Markov for every \(0<\alpha<2\). For \(n\ge3\), define the spectral threshold
\[
\alpha_n^{\mathrm{stab}}=\frac{n}{n-2}.
\]
Within \(0<\alpha<2\), the convergence \(T_{n,\alpha}(t)\to E_n\) as \(t\to\infty\) holds exactly for \(\alpha<\alpha_n^{\mathrm{stab}}\). When \(\alpha=\alpha_n^{\mathrm{stab}}<2\) the semigroup is bounded but does not converge; when \(\alpha>\alpha_n^{\mathrm{stab}}\) it grows exponentially in operator norm. For \(n=2\), convergence to \(E_2\) holds throughout \(0<\alpha<2\). Thus for \(n\ge5\) there is a nonpositive but spectrally stable band \(1<\alpha<n/(n-2)\), followed by a sharply located instability threshold.

## Assumptions and scope
All matrices act on real or complex \(\mathbb C^n\), with cyclic indices and counting-measure sequence norms. In the spectral discussion, \((1-z)^\alpha\) is the branch continuous from \(|z|<1\), with value zero at \(z=1\); it agrees with the absolutely convergent binomial series for positive \(\alpha\). Claims cover integer \(n\ge2\), real \(0<\alpha<2\), and the specified parameter boundaries. No assertion concerns fractional powers of symmetric Laplacians or arbitrary directed graphs.

## Proof
Put \(w_k=(-1)^k\binom{\alpha}{k}\). For \(\alpha>0\), the identity
\[
 w_k=\frac{\Gamma(k-\alpha)}{\Gamma(-\alpha)\Gamma(k+1)}\quad(k>\alpha)
\]
shows \(w_k=O_\alpha(k^{-1-\alpha})\). Hence the series converges absolutely. Since \(\sum_{k\ge0}w_k=(1-1)^\alpha=0\), its cyclic convolution coefficients
\[
 c_r=\sum_{j\ge0}w_{jn+r},\qquad 0\le r<n,
\]
sum to zero. Translation invariance implies \(\|A_{n,\alpha}\|_{\ell^1\to\ell^1}=\|A_{n,\alpha}\|_{\ell^\infty\to\ell^\infty}=\sum_r|c_r|\), and this norm is attained by a sign input (in \(\ell^\infty\)) or a point mass (in \(\ell^1\)).

For \(0<\alpha<1\), \(w_0=1\) and every \(w_k\) for \(k\ge1\) is negative. Thus \(c_0>0\) and all \(c_r<0\) for \(r\ge1\). The zero-sum property yields \(F_n=2c_0\), which gives the first series. For \(1<\alpha<2\), \(w_0=1\), \(w_1=-\alpha\), and all \(w_k>0\) for \(k\ge2\). Since their positive tail sums to \(\alpha-1<\alpha\), exactly \(c_1\) is negative, so \(F_n=-2c_1\), giving the second series. At \(\alpha=1\), only \(w_0=1,w_1=-1\) survive.

For \(k>\alpha\), Euler's beta integral and the reflection identity give
\[
 |w_k|=\frac{|\sin(\pi\alpha)|}{\pi}
 \int_0^1t^{k-\alpha-1}(1-t)^\alpha\,dt.
\]
Summing the geometric series under the positive integral proves both exact integral formulas. For every fixed \(\alpha\) in either open interval, \(|w_k|\) is strictly decreasing once \(k>\alpha\), since \(|w_{k+1}|/|w_k|=(k-\alpha)/(k+1)<1\). This proves strict growth in \(n\). At \(n=2\), \(S_2\) has eigenvalues \(1,-1\), so \(A_{2,\alpha}=2^{\alpha-1}(I-S_2)\), proving \(F_2=2^\alpha\). The limits follow by decay of the displayed coefficient tails.

For fixed noninteger \(\alpha\in(0,2)\), the gamma-ratio expansion
\[
\frac{\Gamma(k-\alpha)}{\Gamma(k+1)}
=k^{-\alpha-1}\left(1+\frac{\alpha(\alpha+1)}{2k}+O_\alpha(k^{-2})\right)
\]
is uniform for large integer \(k\). Substitute \(k=jn\) in the lower-order strip and \(k=jn+1\) in the upper strip; the latter changes the coefficient of \(k^{-\alpha-2}\) to \((\alpha+1)(\alpha-2)/2\). Summing over \(j\ge1\) proves the two zeta expansions, with an absolutely summable remainder uniformly on compact order ranges.

The generator \(-A_{n,\alpha}\) produces a positive semigroup exactly when every off-diagonal matrix entry of \(-A_{n,\alpha}\) is nonnegative; its row sums are always zero. The signs above make all off-diagonal entries nonnegative for \(0<\alpha\le1\). For \(n\ge3\), \(1<\alpha<2\) gives \(c_2>0\), and the \((0,2)\) entry of \(T_{n,\alpha}(t)\) equals \(-t c_2+O(t^2)<0\) for small positive \(t\). The two-state exception follows from the explicit matrix formula.

The Fourier eigenvalues are \(\lambda_k=(1-e^{2\pi i k/n})^\alpha\) for \(k=0,\ldots,n-1\), with \(\lambda_0=0\). For \(1\le k<n\),
\[
 1-e^{2\pi i k/n}
 =2\sin(\pi k/n)
  e^{i(\pi k/n-\pi/2)}.
\]
Thus the largest absolute phase among nonzero eigenvalues is \(\alpha(\pi/2-\pi/n)\). Since \(\alpha<2\), all nonconstant eigenvalues have positive real part exactly when \(\alpha<n/(n-2)\). At equality, a conjugate Fourier pair has purely imaginary eigenvalues; beyond it a pair has negative real part. Normal Fourier diagonalization proves all convergence, boundedness and exponential-growth statements. For \(n=2\), the only nonzero eigenvalue is the positive number \(2^\alpha\).

## Verification
The accompanying `checker.py` independently reconstructs all cyclic matrices from their Fourier eigenvalues, compares the row-norm formula against beta-integral quadrature, checks the signs and strict dimension growth for representative values, checks the zeta expansions at increasing sizes, and checks the spectral sign threshold. Numerical tests support and do not replace the analytic proof. Formulae for \(\alpha\) close to 0, 1 or 2 require careful numerical conditioning; the proof treats the integer boundary separately.

## Relationship to prior work
Abdeljawad and collaborators (2013) develop binomial-coefficient definitions of discrete Grünwald–Letnikov differences and their equivalence with discrete Riemann–Liouville differences. Stanisławski (2012) studies filters approximating these differences. Neither inspected article treats sharp cyclic endpoint norms, monotonicity in cycle size, or the sign-versus-spectral stability thresholds. Michelitsch, Collet, Nowakowski and Nicolleau (2014, arXiv:1412.5904) analyze *symmetric* periodic fractional Laplacian matrices, generated by the centered difference \(2I-S_n-S_n^*\); their kernels are reflection symmetric. The present generator instead uses the one-sided \(I-S_n\), which is nonselfadjoint and has different phases, positivity and stability. General subordination theory implies Markov preservation for fractional orders below one, but not the exact endpoint norm, size correction, or higher-order spectral threshold.

## Limitations
The novel subject is the **combined exact sharp stability profile** for the directed cyclic fractional difference: the norm series and its asymptotics together with the positivity/convergence phase diagram. The Fourier eigenvalue formula, generalized binomial identity, beta integral and positive-semigroup generator criterion are classical ingredients, not asserted as independent discoveries. No universal statement about nonsymmetric graphs, arbitrary fractional orders \(\alpha\ge2\), or the intermediate \(\ell^p\) operator norms is proved. The literature search is not a proof of historical priority; equivalent treatments under fractional Markov generators, circulant matrices or numerical stability terminology remain possible. A relevant 2026 overview could only be examined in search-result excerpts due to access limitations.

## References
- T. Abdeljawad, F. Jarad and D. Baleanu, *Fractional Sums and Differences with Binomial Coefficients*, Discrete Dynamics in Nature and Society (2013), DOI: 10.1155/2013/104173; first published 2013-05-20.
- R. Stanisławski, *New Laguerre Filter Approximators to the Grünwald–Letnikov Fractional Difference*, Mathematical Problems in Engineering (2012), DOI: 10.1155/2012/732917; first published 2012-12-30.
- T. Michelitsch, B. Collet, A. Nowakowski and F. Nicolleau, *Fractional Laplacian matrix on the finite periodic linear chain and its periodic Riesz fractional derivative continuum limit*, arXiv:1412.5904, first public version 2014-12-18.
