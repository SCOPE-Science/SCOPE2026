# Complete collision-profile positivity for overlapping Bernoulli sums

## Finding

Let \(m\geq1\) and let \(w_1,\ldots,w_m\) be arbitrary positive integers. With independent \(B_i\sim\operatorname{Bernoulli}(p)\), \(0\leq p\leq1\), put \(S_p=\sum_{i=1}^{m}w_iB_i\) and let
\[
C_w(p)=\sum_{s\in\mathbb Z}\mathbb P(S_p=s)^2.
\]
This is the exact collision probability of two independent copies of \(S_p\), and \(-\log C_w(p)\) is its order-two Rényi entropy. Write \(u=(1-2p)^2\). There are explicitly defined coefficients \(\gamma_0,\ldots,\gamma_m\), **all strictly positive**, such that
\[
C_w(p)=\sum_{j=0}^{m}\gamma_j u^j,
\qquad \sum_{j=0}^{m}\gamma_j=1,
\qquad \gamma_0=C_w(1/2).
\]
Consequently, the order-two Rényi entropy is strictly increasing on \([0,1/2]\), strictly decreasing on \([1/2,1]\), and has a unique maximum at \(p=1/2\), irrespective of subset-sum collisions. With \(v=p(1-p)\), the collision profile \(F_w(v)=C_w(p)\) satisfies, for every integer \(1\leq k\leq m\),
\[
(-1)^k\frac{d^k}{dv^k}F_w(v)>0,
\qquad 0\leq v\leq1/4.
\]
It also obeys the global, sharp-across-all-lengths bounds
\[
\gamma_0+\gamma_1u\ \leq\ C_w(p)\ \leq\ \gamma_0+(1-\gamma_0)u.
\]
For \(m\geq2\), both inequalities are strict whenever \(0<u<1\). The upper bound is an equality for every \(p\) if \(m=1\), demonstrating that its universal coefficient cannot be reduced. In particular, the exact central loss of Rényi entropy is
\[
[-\log C_w(1/2)]-[-\log C_w(p)]
=\frac{\gamma_1}{\gamma_0}(1-2p)^2+O_w((1-2p)^4)
\]
as \(p\to1/2\), with strictly positive leading coefficient.

## Assumptions and scope

The integer \(m\) is finite but unrestricted, all weights are positive integers (repetitions and arbitrary additive relations are allowed), and all Bernoulli variables have the same parameter \(p\). The weights may depend on \(m\); no limiting regime is assumed. In the recursive overlap distribution of Neunhäuserer, take \(m=n\) and \(w_1=1\), \(w_j=a_j-a_{j-1}\) for \(2\leq j\leq n\); its state value is \(1+S_p\) or its reflection, so its collision probability and Rényi entropy equal those here. The result concerns order-two Rényi entropy, **not** the conjectured Shannon entropy concavity.

## Proof

Let \(\mu_p\) be the probability mass function of \(S_p\). Its characteristic function on the circle is
\[
\widehat\mu_p(\theta)=\prod_{i=1}^{m}(1-p+pe^{\mathrm i w_i\theta}).
\]
Plancherel for a finitely supported sequence gives
\[
C_w(p)=\frac1{2\pi}\int_0^{2\pi}|\widehat\mu_p(\theta)|^2\,d\theta.
\]
The factor identity
\[
|1-p+pe^{\mathrm i w\theta}|^2
=\cos^2(w\theta/2)+(1-2p)^2\sin^2(w\theta/2)
\]
is exact at both endpoints as well. Define \(c_i(\theta)=\cos^2(w_i\theta/2)\) and \(s_i(\theta)=\sin^2(w_i\theta/2)\). Expansion of the finite product gives the explicit coefficients
\[
\gamma_j=\frac1{2\pi}\sum_{\substack{J\subseteq\{1,\ldots,m\}\\|J|=j}}
\int_0^{2\pi}\prod_{i\in J}s_i(\theta)\prod_{i\notin J}c_i(\theta)\,d\theta.
\]
Every integrand is nonnegative. For each nonzero integer weight, its sine-square and cosine-square factors vanish at only finitely many points in \([0,2\pi]\). Thus every displayed product is strictly positive almost everywhere, and every \(\gamma_j>0\). Summing the coefficients uses \(s_i+c_i=1\), giving \(\sum_j\gamma_j=1\). At \(p=1/2\), \(u=0\), yielding \(C_w(1/2)=\gamma_0\).

Since \(u\) decreases strictly as \(p\) increases from zero to one-half, the polynomial with positive coefficients is strictly decreasing in that direction (and symmetric about one-half). Taking its negative logarithm reverses the sign and proves the Rényi statement. Moreover \(u=1-4v\) and direct differentiation gives
\[
(-1)^kF_w^{(k)}(v)
=4^k\sum_{j=k}^m\frac{j!}{(j-k)!}\gamma_j(1-4v)^{j-k}>0.
\]
At \(v=1/4\), the term \(j=k\) remains strictly positive, so the endpoint is included.

For \(0\leq u\leq1\), use \(0\leq u^j\leq u\) for every \(j\geq1\), and \(u^j\geq0\) for every \(j\geq2\), to obtain both bounds. When \(m\geq2\) and \(0<u<1\), the positive coefficient \(\gamma_2\) makes both strict. When \(m=1\), only the constant and linear terms exist and equality holds throughout. The central expansion follows from the exact polynomial and \(-\log(\gamma_0+\gamma_1u+O(u^2))=-\log\gamma_0-(\gamma_1/\gamma_0)u+O(u^2)\).

## Verification

The standalone `check_collision.py` independently constructs the coefficient polynomial via Laurent-polynomial constant terms and the collision probability via exact convolution of rational masses. Running `python3 check_collision.py` passed **9,681 exact assertions** for all positive-integer weight multisets of length one through six with entries at most five, at six rational bias parameters per multiset. The checker verifies coefficient positivity, normalization, both envelope inequalities and exact equality of the two independently computed polynomials. These finite checks support but do not replace the preceding proof, which covers every finite weight vector.

For a genuinely overlapping instance, \(w=(1,2,3)\) yields
\[
C_w(p)=\frac{5+9u+15u^2+3u^3}{32},\quad u=(1-2p)^2.
\]
The repeated subset sum at total three is included automatically; the coefficient positivity remains strict.

## Relationship to prior work

Neunhäuserer introduced the recursive overlap Bernoulli family, proved a Shannon-entropy concavity statement in its nonoverlap and binomial cases, and proposed concavity in all overlap configurations. The present result instead treats collision probability and order-two Rényi entropy for **every** integer-weight family, supplying a positive-coefficient representation, derivative hierarchy and a global bias envelope; it does not infer the Shannon conjecture. Li studies multiplicative comparisons **between Rényi orders** for fair weighted Bernoulli sums and explicitly discusses the obstacle of biased variables; those comparisons do not yield the bias-profile coefficients or the stated strict bounds. Rasa's binomial index-of-coincidence log-convexity concerns equal weights and a different curvature inequality. The broader Fourier method is standard; novelty is claimed only for the stated joint structural conclusions in the arbitrary-overlap, common-bias setting, subject to the literature limitations below.

## Limitations

No claim is made that Shannon entropy is concave, that order-two Rényi entropy is concave in \(p\), or that arbitrary distributions of differing Bernoulli biases satisfy the same coefficient positivity. The chord inequality is sharp in the class allowing one effective weight, but not an optimal bound specialized to every fixed length \(m\geq2\). A general older Fourier/spectral theorem could subsume the coefficient representation; independent priority and mathematical review have not been performed.

## References

1. J. Neunhäuserer, *Recursive overlap Bernoulli distributions and an entropy concavity conjecture*, arXiv:2609.05546v1 (first public 2026-09-02), https://arxiv.org/abs/2609.05546.
2. J. Li, *Multiplicative comparisons of Rényi entropies for weighted Bernoulli sums*, arXiv:2609.01529 (first public 2026-09-01), https://arxiv.org/abs/2609.01529.
3. I. Raşa, *The index of coincidence for the binomial distribution is log-convex*, arXiv:1706.05178 (2017), https://arxiv.org/abs/1706.05178.
4. E. Hillion and O. Johnson, *A proof of the Shepp–Olkin entropy concavity conjecture*, Bernoulli 23 (2017), 3638–3649.
5. M. Madiman, J. Melbourne and C. Roberto, *Bernoulli sums and Rényi entropy inequalities*, Bernoulli 29 (2023), 1578–1599, arXiv:2103.00896.
