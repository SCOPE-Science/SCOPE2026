# Exact logarithmic-observable covariance and finite-sample variance for the doubling map

## Finding

Let \(T:[0,1)\to[0,1)\) be \(T(x)=2x\pmod 1\), preserve Lebesgue probability measure \(m\), and let \(g(x)=-\log x\) for \(0<x<1\) (its value at the null point \(0\) is immaterial). Define the centered Birkhoff sum
\[
S_N(x)=\sum_{j=0}^{N-1}(g(T^jx)-1),\qquad N\ge1,
\]
and its time-lag covariance \(C_k=\int_0^1(g(x)-1)(g(T^kx)-1)\,dx\) for \(k\ge1\).

Put
\[
c=-\frac12\log(2\pi)-\int_0^1\log\Gamma(t)\,\log t\,dt
=1.0102793965954957479\ldots.
\]
The integral converges absolutely. The following statements hold for every integer \(k\ge1\):
\[
\begin{split}
 C_k&=\frac1{2^k}\int_0^1\log t\left[\log\Gamma(2^k+t)-\log\Gamma(t)-2^k\log(2^k)\right]dt-1,\\
 C_1&=1-\frac{\pi^2}{24},\\
 C_k&>0,\\
 \left|C_k-2^{-k}\left(\frac{k\log2}{4}+c\right)\right|&\le4^{-k}.
\end{split}
\]
In particular \(C_k\sim(k\log2)/(4\cdot2^k)\), displaying a sharp logarithmic enhancement over plain exponential decay in the lag.

Define the convergent constants
\[
 \sigma^2=1+2\sum_{k\ge1}C_k=3.705485920780\ldots,
 \qquad B=2\sum_{k\ge1}kC_k=6.109398659356\ldots.
\]
Then **every** \(N\ge1\) obeys the exact quantitative expansion
\[
\boxed{\left|\operatorname{Var}_m(S_N)-\left[N\sigma^2-B+2^{-N}\bigl(N\log2+3\log2+4c\bigr)\right]\right|\le\frac89\,4^{-N}.}
\]
Consequently the finite-size intercept is genuinely nonzero and the remaining approach to it has a specified, positive-order \(N2^{-N}\) leading term. No central limit theorem, large-deviation principle, or closed elementary form of \(\sigma^2\) is claimed.

For finite computation, put \(Q_K=1+2\sum_{k=1}^K C_k+2^{-K}[(K+2)\log2/2+2c]\). Then
\[
 |\sigma^2-Q_K|\le\frac{2}{3\,4^K},\qquad K\ge1.
\]
This is an explicit analytical truncation bound; numerical quadrature errors in evaluating the finite integrals must additionally be controlled if certified decimal digits are required.

## Assumptions and scope

The only probability distribution is Lebesgue measure on \([0,1)\). Time is the discrete iterate index; logarithms are natural. The observable has an integrable logarithmic singularity and belongs to \(L^2(m)\); trajectories passing through \(0\) form a null set and do not affect the integrals. The gamma function is the usual Euler gamma function. The result applies to the specified doubling map and logarithmic observable, not an arbitrary expanding map or a general observable.

## Proof

**1. Covariance and exact gamma integral.** Lebesgue measure is invariant under \(T\), and \(\int_0^1-\log x\,dx=1\), \(\int_0^1(-\log x)^2dx=2\). Hence \(\operatorname{Var}(g)=1\). For every integer \(q\ge2\), partition \([0,1)\) into the \(q\) intervals of equal length and write \(x=(j+t)/q\), \(0\le j<q\), \(0<t<1\). With \(D_q=\int(g(x)-1)(g(\{qx\})-1)dx\), this gives
\[
 D_q=\frac1q\int_0^1\log t\sum_{j=0}^{q-1}\log(j+t)\,dt+\log q-1.
\]
The gamma identity \(\prod_{j=0}^{q-1}(j+t)=\Gamma(q+t)/\Gamma(t)\) proves the displayed exact integral for \(D_q\). Taking \(q=2^k\) yields \(C_k=D_{2^k}\). At \(q=2\), elementary integration using
\[
\int_0^1\log(1+t)\log t\,dt=2-2\log2-\frac{\pi^2}{12}
\]
yields \(C_1=1-\pi^2/24\).

**2. Strict positivity.** Let \(H_q(t)=q^{-1}\sum_{j=0}^{q-1}[-\log((j+t)/q)]\). Both \(H_q\) and \(-\log t\) are strictly decreasing on \((0,1)\), and each has integral \(1\). The identity
\[
2D_q=\int_0^1\!\int_0^1\bigl[H_q(s)-H_q(t)\bigr]\bigl[(-\log s)-(-\log t)\bigr]ds\,dt
\]
shows \(D_q>0\).

**3. Uniform gamma remainder and sharp lag law.** For \(q\ge2\), \(0\le t\le1\), set
\[
R_q(t)=\log\Gamma(q+t)-(q+t-1/2)\log q+q-\frac12\log(2\pi).
\]
The standard positive Stirling remainder \(0<r(y)<1/(12y)\) for \(y=q+t\) gives
\[
R_q(t)=(q+t-1/2)\log(1+t/q)-t+r(q+t).
\]
Using \(u-u^2/2\le\log(1+u)\le u\) for \(u=t/q\in[0,1/2]\), the bounds \(t(t-1/2)\ge-1/16\) and \(t(t-1/2)\le1/2\) imply
\[
-\frac{11}{16q}\le R_q(t)\le\frac7{12q},\qquad\text{hence } |R_q(t)|\le1/q.
\]
(The lower estimate follows from \((q+t-1/2)t^2/(2q^2)\le(q+1/2)/(2q^2)\le5/(8q)\).) Substitution into the gamma-integral expression, together with \(\int_0^1\log t\,dt=-1\) and \(\int_0^1t\log t\,dt=-1/4\), gives
\[
D_q=\frac{\log q/4+c}{q}+\frac1q\int_0^1\log t\,R_q(t)\,dt.
\]
Because \(\int_0^1|\log t|dt=1\), the final term has absolute value at most \(q^{-2}\). Replacing \(q\) by \(2^k\) completes the covariance estimates and proves convergence of \(\sigma^2\) and \(B\).

**4. Exact variance identity and all-time finite-size remainder.** Stationarity gives, for every \(N\ge1\),
\[
\operatorname{Var}(S_N)=N+2\sum_{k=1}^{N-1}(N-k)C_k.
\]
Adding and subtracting the two absolutely convergent infinite sums yields the exact identity
\[
\operatorname{Var}(S_N)=N\sigma^2-B+2\sum_{k=N}^{\infty}(k-N)C_k.
\]
Write \(C_k=2^{-k}(k\log2/4+c)+E_k\) with \(|E_k|\le4^{-k}\). The geometric identities \(\sum_{j\ge1}j2^{-j}=2\) and \(\sum_{j\ge1}j^22^{-j}=6\) evaluate the leading tail exactly as \(2^{-N}(N\log2+3\log2+4c)\). The remaining tail is bounded by
\[
2\sum_{j\ge1}j4^{-(N+j)}=\frac89\,4^{-N}.
\]
The finite computation error for \(Q_K\) follows analogously from \(2\sum_{k>K}4^{-k}=2/(3\cdot4^K)\). This closes the proof for all \(N\) and \(k\).

## Verification

The standalone `VERIFY.py` uses independent subinterval quadrature and the gamma-product representation to compare covariances for \(q=2,4,8,16\), checks the elementary first-lag identity, verifies the asymptotic inequality at eight lags, and directly integrates finite Birkhoff-sum squares for \(N=1,\ldots,7\). It also compares the exact gamma-series truncation intervals with the stated approximate variance. Run `python VERIFY.py` with `mpmath` installed. The finite computations test implementation and algebra; the unbounded-time statements rely on the proof above.

## Relationship to prior work

Defaveri and Smith, *Dynamical phase transition for a logarithm observable in chaotic systems*, arXiv:2610.21288v1 (first public 2026-10-15), study this exact doubling map and observable. In Section II.1, their asymptotic variance is reported numerically as approximately \(3.71N\), while their closed-form Green–Kubo computation in Appendix A.3 is for the **logistic** map. The present result gives a sharp positive covariance at every doubling-map lag, the explicit log-enhanced lag coefficient, an exact rapidly computable variance constant, and the quantitative finite-size offset and remainder. These statements are not consequences of the paper's numerical approximation.

Schindler, *Trimmed sums for observables on the doubling map*, arXiv:1810.03223 (2018), concerns a **nonintegrable** observable and trimmed-sum laws, not the square-integrable \(-\log x\) Green–Kubo computation here. The general Green–Kubo identity is a known tool; neither that identity alone nor the standard exponential-mixing bounds imply the present sharp coefficient or finite-size expansion. Equivalent historical formulas under special-function or ergodic-sum terminology have not been excluded exhaustively.

## Limitations

The proof neither establishes independence of the observations nor analyzes the non-Gaussian large-deviation tail. The decimal constants are approximate numerical evaluations of exact integral-series definitions, and their floating-point error is not certified solely by the analytical series tail bounds. The exact gamma representation does not assert that \(\sigma^2\) has a finite elementary closed form. Searches and text comparisons support originality under available evidence, but do not certify historical priority. No independent audit has been carried out.

## References

1. L. Defaveri and N. R. Smith, *Dynamical phase transition for a logarithm observable in chaotic systems*, arXiv:2610.21288v1 (2026-10-15), https://arxiv.org/html/2610.21288v1 . Especially Section II.1 and Appendix A.
2. T. Schindler, *Trimmed sums for observables on the doubling map*, arXiv:1810.03223v1 (2018-10-07), https://arxiv.org/abs/1810.03223 .
3. Classical Euler gamma multiplication/product identities and Stirling's formula with its positive remainder, as used explicitly in the proof.
