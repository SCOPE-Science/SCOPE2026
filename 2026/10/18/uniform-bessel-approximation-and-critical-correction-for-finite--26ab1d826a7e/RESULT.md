# Uniform Bessel approximation and critical correction for finite Euler summability matrices

## Finding

For integers \(N\ge 1\) and parameters \(0\le r\le1\), define the real finite Euler summability matrix \(E_N(r)\) on \(\ell_2^N\) by
\[
(E_N(r))_{jk}=\begin{cases}\binom jk r^k(1-r)^{j-k},&0\le k\le j<N,\\0,&k>j.\end{cases}
\]
Use the continuous binomial convention at \(r=0,1\). Set \(\beta=r(1-r)\) and denote by \(S_N(r)=\|E_N(r)\|_{S_2}^2=\operatorname{tr}(E_N(r)^*E_N(r))\) its total squared singular-value mass. Let \(I_0,I_1\) be the standard modified Bessel functions of the first kind, equivalently
\[
I_m(z)=\frac1{2\pi}\int_0^{2\pi}e^{z\cos\theta}\cos(m\theta)\,d\theta\qquad(m=0,1).
\]
Then the **finite-dimensional, all-parameter error bound** is
\[
\boxed{0\le S_N(r)-H_N(\beta)<\tfrac12,\qquad H_N(\beta)=N e^{-2N\beta}[I_0(2N\beta)+I_1(2N\beta)].}
\]
In particular, \(S_N(r)=S_N(1-r)\), despite the distinct triangular operators. Furthermore, in the critical parameter window \(\beta=\lambda/N\), define
\[
K(\lambda)=\lambda e^{-2\lambda}[I_0(2\lambda)-I_1(2\lambda)].
\]
For each \(L\ge0\), uniformly over \(0\le\lambda\le L\), \(N\ge\max\{1,8L\}\), and both choices of \(r\in[0,1]\) satisfying \(r(1-r)=\lambda/N\),
\[
\boxed{\left|S_N(r)-H_N(\lambda/N)-K(\lambda)\right|\le\frac{32L^2/3+200L^3/9}{N}.}
\]
The universal error bound consequently yields the full crossover \(S_N(r_N)/N\to e^{-2\lambda}[I_0(2\lambda)+I_1(2\lambda)]\) whenever \(N r_N(1-r_N)\to\lambda<\infty\), and \(S_N(r_N)\sim\sqrt{N/(\pi r_N(1-r_N))}\) whenever \(N r_N(1-r_N)\to\infty\).

## Assumptions and scope

All vector spaces and matrix entries are real. The Schatten-\(2\) norm is the Hilbert–Schmidt/Frobenius norm: its square is the sum of squares of every matrix entry and, equivalently, the sum of squared singular values. The result applies to every finite \(N\), including \(N=1\), and both degenerate Euler parameters \(r=0,1\); in these endpoint cases \(S_N=H_N=N\). The asymptotic statements concern arbitrary sequences \(r_N\in[0,1]\), with \(\beta_N=r_N(1-r_N)\), and have no unstated rate assumptions. No assertion is made about individual singular values or an operator-norm limit.

## Proof

**1. Exact row identity and generating function.** For row \(j\), Parseval's identity applied to \(((1-r)+r e^{i\theta})^j\) gives
\[
\sum_{k=0}^j\binom jk^2 r^{2k}(1-r)^{2(j-k)}
=\frac1{2\pi}\int_0^{2\pi}(1-a(\theta))^j\,d\theta,
\quad a(\theta)=4\beta\sin^2(\theta/2)\in[0,1].
\]
Summing rows gives the exact finite integral
\[
S_N(r)=\frac1{2\pi}\int_0^{2\pi}\frac{1-(1-a(\theta))^N}{a(\theta)}\,d\theta,
\]
with integrand \(N\) at \(a=0\). This proves parameter-reflection symmetry. The row generating function also has the exact algebraic form
\[
\sum_{j=0}^\infty z^j\sum_{k=0}^j(E_N(r))_{jk}^2
=\frac{1}{\sqrt{(1-z)(1-(1-4\beta)z)}}\qquad(|z|<1),
\]
where the row expression is interpreted for the infinite Euler matrix and hence is independent of the truncation \(N\). Indeed one integrates \((1-z(1-a))^{-1}\) using the elementary cosine integral. The generating function is a supporting classical binomial identity, not a separate novelty claim.

**2. Continuous-time proxy.** Replace the discrete geometric sum by its exponential integral:
\[
H_N(\beta)=\frac1{2\pi}\int_0^{2\pi}\frac{1-e^{-N a(\theta)}}{a(\theta)}\,d\theta
=\int_0^N e^{-2\beta t}I_0(2\beta t)\,dt.
\]
The Bessel derivative identities \(I_0'=I_1\) and \(I_1'=I_0-I_1/z\) imply, by differentiating in \(t\),
\[
\int_0^N e^{-2\beta t}I_0(2\beta t)\,dt
=N e^{-2N\beta}[I_0(2N\beta)+I_1(2N\beta)].
\]
Continuity covers \(\beta=0\).

**3. Uniform error.** For any \(0\le a\le1\), \(0\le1-a\le e^{-a}\) and \(0\le e^{-a}-(1-a)\le a^2/2\). Factoring the difference of \(N\)-th powers gives
\[
0\le\frac{e^{-Na}-(1-a)^N}{a}
\le\frac{Na}{2}e^{-(N-1)a}.
\]
For \(N=1\), the right side is at most \(1/2\). For \(N\ge2\), maximization in \(a\ge0\) yields \(Na e^{-(N-1)a}\le N/[e(N-1)]\le2/e<1\). Hence the integrand difference is at most \(1/2\), and is strictly smaller on a set of positive measure for every parameter. Angular averaging proves the claimed bound.

**4. Critical second-order correction with an explicit remainder.** Let \(0\le\lambda\le L\), \(N\ge\max\{1,8L\}\), set \(u=2-2\cos\theta\in[0,4]\) and \(x=\lambda u\le4L\), so \(a=x/N\le1/2\). Write
\[
N\log(1-x/N)=-x-\frac{x^2}{2N}-\delta,
\qquad0\le\delta\le\frac{2x^3}{3N^2}.
\]
Put \(t=x^2/(2N)+\delta\). The inequality \(|1-e^{-t}-t|\le t^2/2\), together with \(\delta\le2x^3/(3N^2)\) and \(t\le5x^2/(6N)\), gives for \(x>0\)
\[
\left|\frac{e^{-x}-(1-x/N)^N}{x/N}-\frac{x e^{-x}}2\right|
\le\frac1N\left(\frac{2x^2}{3}+\frac{25x^3}{72}\right).
\]
Both sides extend continuously to \(x=0\). Averaging over \(\theta\) bounds the remainder by \((32L^2/3+200L^3/9)/N\). Finally,
\[
\frac{1}{2\pi}\int_0^{2\pi}\frac{\lambda u}{2}e^{-\lambda u}\,d\theta
=\lambda e^{-2\lambda}[I_0(2\lambda)-I_1(2\lambda)]=K(\lambda),
\]
completing the uniform critical expansion.

**5. Regimes.** For finite limiting \(\lambda\), divide the all-parameter error bound by \(N\) and use continuity of the Bessel functions. If \(N\beta_N\to\infty\), the classical fixed-order asymptotic \(e^{-z}I_m(z)\sim(2\pi z)^{-1/2}\) for \(z\to\infty\) implies \(H_N(\beta_N)\sim\sqrt{N/(\pi\beta_N)}\), diverging to infinity because \(\beta_N\le1/4\). The error below \(1/2\) is therefore relatively negligible.

## Verification

The accompanying standard-library file `check_euler.py` recomputes \(S_N(r)\) by direct row coefficients, computes \(I_0,I_1\) by their convergent power series, tests positivity and the uniform bound at 72 parameter/dimension pairs, verifies 8 exact rational center-parameter identities, and checks 18 critical-window remainder instances. Its actual run returned `CHECK_OK 98 finite tests; no claim of exhaustive proof`. These computations corroborate rather than prove the universal bounds; the preceding pointwise inequalities provide the proof. At \(r=1/2\), the exact closed form
\[
S_N(1/2)=\sum_{j=0}^{N-1}\frac{\binom{2j}{j}}{4^j}
=(2N-1)\frac{\binom{2N-2}{N-1}}{4^{N-1}}
\]
follows from the central binomial identity and telescoping, giving independent rational regression cases.

## Relationship to prior work

The Euler/Hausdorff binomial summability matrix is classical. Başarır, Kara, and Konca (2014) explicitly define the Euler matrix and study weighted sequence spaces, duality, and compact operator classes. Yavuz (arXiv:1610.01411, first version 2016) uses binomial Euler means for Tauberian convergence. Meng and Song (2017) study binomial difference sequence spaces. Roopaei (2020) proves the binomial–Euler operator equivalence and computes the infinite-dimensional \(\ell_p\) operator norm. The last result does **not** imply the finite-dimensional Hilbert–Schmidt energy: singular-value sum versus supremum norm are different invariants, and the new \(r\leftrightarrow1-r\) symmetry is absent from the \(\ell_2\) operator-norm formula. Neither the inspected sections nor the statements of those works supply the uniform Bessel error estimate and critical order-one correction here. Classical Parseval, binomial generating functions, and modified Bessel identities are used as known tools, not claimed as new. No uniqueness of this result in the entirety of historical literature is asserted.

## Limitations

The estimate \(1/2\) is explicit and dimension independent but **not claimed optimal**. The critical remainder constant is conservative; its claimed scope is only \(N\ge8L\) and \(\lambda\le L\). The result is for Hilbert–Schmidt energy, not for the largest singular value, the full singular-value distribution, or all Schatten exponents. Older source material may contain equivalent binomial collision formulas under other terminology; the full historical record cannot be exhaustively certified by the searches described here. The first-public-date metadata follows a dated public manuscript-upload record and is not claimed to date the Euler method's invention.

## References

1. M. Başarır, E. E. Kara, Ş. Konca, *On some new weighted Euler sequence spaces and compact operators*, Mathematical Inequalities & Applications 17 (2014), 649–664. DOI: 10.7153/mia-17-48. Public author-upload dated 2014-03-31.
2. E. Yavuz, *Euler summability method of sequences of fuzzy numbers and a Tauberian theorem*, arXiv:1610.01411v1 (2016-10-05), later journal version. Accessible preprint: https://arxiv.org/abs/1610.01411.
3. J. Meng, M. Song, *On some binomial \(B^{(m)}\)-difference sequence spaces*, Journal of Inequalities and Applications (2017), article 241. DOI: 10.1186/s13660-017-1470-4.
4. H. Roopaei, *Binomial Operator as a Hausdorff Operator of the Euler Type*, Constructive Mathematical Analysis 3 (2020), 165–177. DOI: 10.33205/cma.783993. Full text: https://dergipark.org.tr/en/download/article-file/1252223.
