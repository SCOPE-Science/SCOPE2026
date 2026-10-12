# Sharp composite separation for a Dirichlet-inverse prime detector

## Finding
For each integer \(k\ge2\), let \(\sigma_k(n)=\sum_{d\mid n}d^k\). Write \(\sigma_k^{(-1)}\) for the inverse under Dirichlet convolution, \(J_k(n)=n^k\prod_{p\mid n}(1-p^{-k})\) for the Jordan totient, and \(\mu\) for the Möbius function. The arithmetic function
\[ F_k(n)=\sigma_k^{(-1)}(n)+\mu(n)+J_k(n)+3 \]
is the prime-detecting function introduced in the cited 2026 work. Its **exact smallest composite residual** is
\[
\boxed{\min_{n\ge4\;\mathrm{composite}} |F_k(n)|=4^k+3, \qquad
 |F_k(n)|=4^k+3\iff n=4.}
\]
In particular, \(F_k(4)=4^k+3\). The restrictions \(n\ge4\) and composite are essential: \(F_k(1)=6\), and primes have residual zero.

## Assumptions and scope
Here \(k\) ranges over integers at least two, and \(n\) over all composite positive integers, without upper bound. The inverse is *convolution inverse*, not reciprocal. Write \(n=ab^2\) in the cube-free nonsquarefree case, with \(a,b\) squarefree, \(\gcd(a,b)=1\), and \(b>1\). All inequalities are exact. No computational primality-testing advantage is claimed; evaluating the multiplicative formulas may require factoring \(n\).

## Proof
The standard prime-power values, derived from \(\sigma_k=\mathbf1*I_k\), are
\[
\sigma_k^{(-1)}(p)=-(1+p^k),\quad
\sigma_k^{(-1)}(p^2)=p^k,\quad
\sigma_k^{(-1)}(p^e)=0\quad(e\ge3),
\]
and \(J_k(p^e)=p^{(e-1)k}(p^k-1)\). They determine \(F_k\) multiplicatively after adding \(\mu(n)+3\). We divide the composite integers into three exhaustive classes.

**A prime cube divides \(n\).** The local inverse factor vanishes and \(\mu(n)=0\), hence \(F_k(n)=J_k(n)+3\). Every prime-cube factor contributes at least \(2^{2k}(2^k-1)\) to the multiplicative \(J_k(n)\), while every other prime-power factor contributes an integer at least one. Since \(k\ge2\), we obtain \(F_k(n)\ge4^k(2^k-1)+3>4^k+3\).

**The integer \(n\) is squarefree.** Write its distinct primes as \(p_1,\ldots,p_r\) and set \(q_i=p_i^k\). A composite has \(r\ge2\). When \(r\) is even,
\[F_k(n)=\prod_i(q_i+1)+\prod_i(q_i-1)+4.\]
The two smallest possible primes are \(2,3\); each additional factor only increases both products. Therefore
\[F_k(n)\ge(2^k+1)(3^k+1)+(2^k-1)(3^k-1)+4=2\cdot6^k+6>4^k+3.\]
When \(r\) is odd, \(r\ge3\), and
\[F_k(n)=2-D_r,\qquad D_r=\prod_i(q_i+1)-\prod_i(q_i-1).\]
For three factors \(D_3=2(q_1q_2+q_1q_3+q_2q_3+1)\). If another prime with \(q=p^k\) is adjoined, then
\[D_{r+1}=qD_r+\prod_{i=1}^r(q_i+1)+\prod_{i=1}^r(q_i-1)>D_r.\]
Thus the smallest \(D_r\) for odd composite squarefree \(n\) is bounded below by the first three primes, giving
\[|F_k(n)|=D_r-2\ge2(6^k+10^k+15^k)>4^k+3.\]
This comparison covers arbitrarily many distinct primes.

**The integer \(n\) is cube-free but not squarefree.** There is a unique decomposition \(n=ab^2\) as above. Using the local values gives
\[F_k(ab^2)=b^kT+3,\qquad T=\mu(a)\sigma_k(a)+J_k(a)J_k(b).\]
If \(\mu(a)=1\), then \(T=\sigma_k(a)+J_k(a)J_k(b)\ge1+J_k(b)\). If \(b=2\), this gives \(T\ge2^k\), with equality exactly when \(a=1\): for \(a>1\), both \(\sigma_k(a)>1\) and \(J_k(a)>1\). Thus \(F_k(ab^2)\ge4^k+3\), with equality precisely at \(a=1,b=2\). If \(b>2\), then \(b\ge3\) and \(J_k(b)\ge3^k-1\): if \(b\) is an odd prime or has one, this follows from its prime factor \(p\ge3\); if \(b\) also has prime \(2\), the remaining factor only increases the product. Consequently \(F_k(ab^2)\ge b^k(1+J_k(b))+3\ge9^k+3>4^k+3\).

Suppose \(\mu(a)=-1\). Then \(a>1\). The exact Euler product bound
\[
\frac{\sigma_k(a)}{J_k(a)}=
\prod_{p\mid a}\frac{1+p^{-k}}{1-p^{-k}}
<\prod_p\frac{1+p^{-k}}{1-p^{-k}}
=\frac{\zeta(k)^2}{\zeta(2k)}
\le\frac{\zeta(2)^2}{\zeta(4)}=\frac52
\]
holds for every \(k\ge2\). Therefore
\[T>J_k(a)\bigl(J_k(b)-\tfrac52\bigr).\]
If \(b=2\), then \(a\) is odd with at least one prime factor, and \(J_k(a)\ge3^k-1\). It follows that
\[T>(3^k-1)(2^k-\tfrac72)>2^k.\]
The last inequality is immediate at \(k=2\), where the left-hand product equals \(4\), and for \(k\ge3\) because \(2^k-7/2>2^{k-1}\) and \(3^k-1>2\). If \(b>2\), then \(J_k(b)\ge3^k-1\) and \(J_k(a)\ge2^k-1\); hence
\[T>(2^k-1)(3^k-\tfrac72)>2^k\quad(k\ge2).\]
Thus whenever \(\mu(a)=-1\), \(F_k(ab^2)=b^kT+3>4^k+3\), because \(b\ge2\) and \(T>2^k\).

The cases exhaust all composite integers. Directly, at \(n=4\) the local values give \(F_k(4)=2^k+2^k(2^k-1)+3=4^k+3\), completing both the sharp bound and the equality characterization.

## Verification
The supplied standalone \(\texttt{verify.py}\) checks the exact convolution-inverse recurrence independently of the prime-power formulas, independently recomputes Jordan totients by divisor sums, and checks the claimed least composite residual for all \(2\le k\le7\) and \(1\le n\le4000\). Its saved output records 24,000 tested values. These are finite corroborations only; the infinite proof is the case analysis and Euler-product inequality above. Execute \(\texttt{python3 verify.py}\) with standard Python 3.

## Relationship to prior work
Zhichen Liu's September 2026 primary paper introduces \(F_k\), proves its zeros are exactly the primes for \(k\ge2\), and supplies the local product formulas used here. The present claim is stronger in a different quantitative direction: it determines the optimal nonzero composite magnitude and its unique extremizer, neither of which is asserted in that source. The published note *Sharp parameter stability for mixed Dirichlet-inverse prime criteria* treats the related continuous family \(P_{k,t}(n)=\sigma_k^{(-1)}(n)+J_k(n)+2+t(\mu(n)+1)\) and establishes zero-set stability for \(t>-2\). Its exact theorem and proof imply sign information but not the optimal composite absolute-residual bound \(4^k+3\). The equality case requires a separate extremal comparison across all prime-exponent patterns.

## Limitations
The result does not cover \(k=1\); the primary paper exhibits a composite zero there. The distinguished input \(n=1\) has value \(6\), so it is excluded from the composite minimum. The bound applies to exact arithmetic-function values, not to computational complexity or probabilistic primality testing. An equivalent exact-minimum statement in unindexed literature remains a residual originality risk. No independent audit is asserted.

## References
1. Z. Liu, *Prime-Detecting Identities from Dirichlet Inversion and Jordan Totients*, arXiv:2609.33278v2 (first publicly posted 2026-09-27), https://arxiv.org/html/2609.33278v2.
2. *Sharp parameter stability for mixed Dirichlet-inverse prime criteria*, published 2026 note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-parameter-stability-for-mixed-dirichlet-inverse-prime-crit--09c92f70d81c.
3. Euler products for \(\zeta(2)\) and \(\zeta(4)\), including \(\zeta(2)^2/\zeta(4)=5/2\), standard classical identities.
