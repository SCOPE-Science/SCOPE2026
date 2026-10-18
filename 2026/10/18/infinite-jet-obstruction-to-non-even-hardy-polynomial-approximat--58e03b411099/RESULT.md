# Infinite-jet obstruction to non-even Hardy polynomial approximation

## Finding
For a nonlinear Hardy exponent \(p>0\) that is **not** a positive even integer, no finite Taylor jet of an inner function determines its complete polynomial-approximation objective for any polynomial degree bound \(d\ge1\). The obstruction is witnessed by two explicit finite Blaschke products with arbitrarily long identical initial jets. More sharply, the very first distinction in a real one-parameter polynomial probe is exactly calculable and occurs at order \(2M+1\) of the probe parameter, although the inner functions differ already at coefficient \(M\).

For real \(0<a<1\), integer \(M\ge1\), and \(\alpha=p/2\), define
\[
 F_M(z)=\frac{a-z^M}{1-a z^M},\qquad
 G_M(z)=\frac{a-z^{M+1}}{1-a z^{M+1}},\qquad
 q_\lambda(z)=\lambda(1+z).
\]
Let \(I_H(\lambda)=\|1-q_\lambda H\|_{H^p}^{p}\), for real \(|\lambda|<1/2\). Write \(\beta_j=(-1)^j\binom{\alpha}{j}\). Then
\[
 [\lambda^r]I_{F_M}=[\lambda^r]I_{G_M}\quad(0\le r\le2M),
\qquad
 [\lambda^{2M+1}](I_{F_M}-I_{G_M})
 =-2(1-a^2)\beta_M\beta_{M+1}\ne0.
\]

## Assumptions and scope
The disk is \(\mathbb D\), the circle integral uses probability-normalized Lebesgue measure, and \(\|h\|_{H^p}^{p}=\int_{\partial\mathbb D}|h|^p\,dm\) for bounded analytic \(h\). The assertion is about equality of the **entire objective function** on the polynomials of degree at most \(d\), not about equality of minimizing polynomials, minimizing errors, or any recovery algorithm. The probe is degree one, so it belongs to every polynomial class with bound \(d\ge1\). Every asserted equality of coefficients in \(\lambda\) concerns an ordinary convergent real Taylor series at zero. For \(0<p\le1\), the Hardy expression is a quasi-norm power and no uniqueness of an optimizer is asserted.

## Proof
**1. Two inner functions with a long common jet.** For \(0<a<1\), \(b_a(w)=(a-w)/(1-aw)\) is a one-zero Blaschke factor. Its compositions with \(z^M\) and \(z^{M+1}\) are finite Blaschke products. Expanding the geometric denominator gives
\[
 F_M(z)=a-(1-a^2)z^M+O(z^{2M}),\qquad
 G_M(z)=a-(1-a^2)z^{M+1}+O(z^{2M+2}).
\]
Therefore their Taylor coefficients through degree \(M-1\) agree and their degree-\(M\) coefficients differ by \(-(1-a^2)\).

**2. Absolutely convergent moment expansion.** Set \(\alpha=p/2\) and \(\beta_j=(-1)^j\binom{\alpha}{j}\). For real \(|\lambda|<1/2\), the boundary inequality \(|\lambda(1+z)H(z)|<1\) holds almost everywhere for any inner \(H\). Hence two generalized-binomial series may be multiplied and integrated termwise, uniformly on every smaller compact interval:
\[
 I_H(\lambda)=\sum_{j,k\ge0}\beta_j\beta_k\lambda^{j+k}
 \int_{\partial\mathbb D}(1+z)^j(1+\bar z)^k
 H(z)^j\overline{H(z)}^{\,k}\,dm(z).
\]
Because \(|H|=1\) almost everywhere, if \(j>k\) the inner factor simplifies to \(H^{j-k}\); if \(j=k\) it simplifies to \(1\). For \(j>k\), by expanding \((1+\bar z)^k\) the integral is determined only by the first \(k+1\) Taylor coefficients (degrees \(0\) through \(k\)) of \(H\), since it equals a finite combination of the coefficients through degree \(k\) of the analytic function \((1+z)^jH^{j-k}\). For \(k>j\) it is the conjugate of the swapped case. Therefore, all moment coefficients with total order \(j+k\le2M\) depend on the inner input through degrees strictly below \(M\): in an unequal pair \(\min(j,k)\le M-1\). These coefficients agree for \(F_M,G_M\).

**3. Exactly one new coefficient at the first possible order.** For total order \(2M+1\), the only pairs whose smaller index reaches \(M\) are \((j,k)=(M+1,M)\) and its reversal. In the first pair, the coefficient of degree \(M\) in \((1+z)^{M+1}H(z)\) contains the coefficient of degree \(M\) of \(H\) exactly once, with factor one. Indeed the highest negative Fourier monomial in \((1+\bar z)^M\) is \(\bar z^M\) with coefficient one, while lower negative degrees see only lower Taylor coefficients. The reversal supplies its conjugate. Since the two Blaschke products have real coefficients,
\[
 [\lambda^{2M+1}](I_{F_M}-I_{G_M})
 =2\beta_{M+1}\beta_M\bigl([z^M]F_M-[z^M]G_M\bigr)
 =-2(1-a^2)\beta_M\beta_{M+1}.
\]
When \(p/2\) is not a nonnegative integer, the generalized binomial coefficients \(\binom{p/2}{j}\) are nonzero for every integer \(j\ge0\). The displayed coefficient is therefore nonzero, and the analytic functions of \(\lambda\) differ on every neighborhood of zero. Choosing \(M>K\) contradicts determination of the full objective by any fixed jet through degree \(K\). This proves the result for each \(d\ge1\).

## Verification
The accompanying standard-library Python verifier computes all real-parameter Taylor coefficients using exact rational arithmetic. For \(p/2\in\{1/2,3/2,5/2,7/4\}\), \(a\in\{1/2,1/3\}\), and \(1\le M\le9\), it checks all orders through \(2M+1\): the first \(2M+1\) coefficients agree and the next matches the closed formula, in 72 independent parameter triples. For example \(p=3\), \(a=1/2\), \(M=3\) gives difference coefficient \(-9/4096\) at order seven. The infinite statement follows from the algebraic proof above, not from these finite tests.

## Relationship to prior work
Centner, Cheng, and Felder introduced the nonlinear \(H^p\) optimal-polynomial-approximant framework and examined the inner-function case. Cheng and Felder subsequently studied structural and error properties of these approximants. The earlier even-exponent finite-jet observation relies on the termination of the binomial series at an integral exponent. The present result shows a precise contrasting obstruction at every non-even exponent and quantifies its earliest appearance in a polynomial probe. It does **not** claim that existing approximation minima or optimizer theorems fail, and does not imply that matching jets produce distinct minimizers.

## Limitations
The nonzero sensitivity is proved for the full objective at one prescribed nonoptimal polynomial probe; the minimum error and the optimal approximating polynomial are not classified. The indicator \(M\) controls the first power of the probe parameter at which the two objectives split, not an estimated numerical size of the discrepancy at a fixed nonzero probe. No claim is made about finite interpolation from non-Taylor measurements. Earlier equivalent statements under binomial-moment or Toeplitz language are possible; bibliographic completeness is not asserted.

## References
1. R. Centner, R. Cheng, and C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, first arXiv version 2023-05-25, arXiv:2305.16068. https://arxiv.org/abs/2305.16068
2. R. Cheng and C. Felder, *More properties of optimal polynomial approximants in Hardy spaces*, first arXiv version 2023-10-24, arXiv:2310.16010. https://arxiv.org/abs/2310.16010
3. R. Centner, *Optimal Polynomial Approximants in \(L^p\)*, first arXiv version 2021-12-28, arXiv:2112.14002. https://arxiv.org/abs/2112.14002
4. C. Bénéteau and R. Centner, *A survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, first arXiv version 2021-02-02, arXiv:2102.01725. https://arxiv.org/abs/2102.01725
