# Exact prime-power fibers of Schemmel totients
## Finding
For a fixed positive integer \(r\), let \(S_r\) be the Schemmel totient function and define the fiber size
\[
N_r(m)=\#\{n\ge1:S_r(n)=m\}.
\]
Fix a prime \(\ell\) and an integer \(t\ge1\). Put
\[
E_{r,\ell,t}=\{j\in\{1,\ldots,t\}:r+\ell^j\text{ is prime}\}
\]
and
\[
P_{r,\ell,t}(x)=\prod_{j\in E_{r,\ell,t}}(1+x^j).
\]

If \(\ell\ne r+1\), then
\[
N_r(\ell^t)
=
\left(1+\mathbf 1_{r+1\text{ prime}}\right)[x^t]P_{r,\ell,t}(x).
\tag{1}
\]
If \(\ell=r+1\) is prime, then
\[
N_r(\ell^t)
=
[x^t]\left(2+x+x^2+\cdots\right)P_{r,\ell,t}(x).
\tag{2}
\]
Thus every prime-power fiber is given exactly by a finite subset-sum coefficient.

For prime targets \(t=1\), formulas (1)--(2) become
\[
N_r(\ell)=
\begin{cases}
1+2\mathbf 1_{2r+1\text{ prime}},&\ell=r+1\text{ prime},\\
\left(1+\mathbf 1_{r+1\text{ prime}}\right)\mathbf 1_{r+\ell\text{ prime}},&\ell\ne r+1.
\end{cases}
\tag{3}
\]
Consequently, for every fixed even \(r\), the range of \(S_r\) contains infinitely many primes if and only if there are infinitely many prime pairs with gap \(r\). For odd \(r\ge3\), the only possible prime value is \(2\), and it occurs exactly when \(r+2\) is prime.

The first specializations include
\[
\varphi^{-1}(2)=\{3,4,6\},
\qquad
\varphi^{-1}(4)=\{5,8,10,12\},
\]
and
\[
S_2^{-1}(3)=\{5,9,15\},
\qquad
S_2^{-1}(9)=\{11,27,33,45\}.
\]

## Assumptions and scope
For primes \(p\) and positive integers \(a\), the Schemmel totient is multiplicative and satisfies
\[
S_r(p^a)=
\begin{cases}
0,&p\le r,\\
p^{a-1}(p-r),&p>r.
\end{cases}
\]
The theorem concerns inverse images of prime powers \(\ell^t\). It does not classify fibers at targets containing two or more distinct prime factors.

The primary subject classification \(11A25\) is explicitly used in modern archival work on Schemmel totients.

## Proof
Suppose
\[
S_r(n)=\ell^t>0
\]
and write
\[
n=\prod_i p_i^{a_i}.
\]
Every \(p_i\) is greater than \(r\), and multiplicativity gives
\[
\ell^t=\prod_i p_i^{a_i-1}(p_i-r).
\tag{4}
\]
Each positive factor on the right of (4) must therefore be a power of \(\ell\).

Consider one prime-power block \(p^a\). If \(p\ne\ell\) and \(a\ge2\), then \(p\) divides the block value and hence divides \(\ell^t\), impossible. Thus every prime \(p\ne\ell\) occurs to the first power, and then
\[
p-r=\ell^j
\]
for some \(j\ge0\). The case \(j=0\) is the optional prime
\[
p=r+1,
\]
which contributes the unit value \(1\). For \(j\ge1\), the possible prime factor is uniquely
\[
p=r+\ell^j,
\]
and it contributes \(\ell^j\).

Now consider the block with \(p=\ell\). It can occur only when \(\ell>r\). For its Schemmel value to be a power of \(\ell\), the factor
\[
\ell-r
\]
must itself be a power of \(\ell\). Since
\[
0<\ell-r<\ell,
\]
this is possible only when
\[
\ell-r=1,
\]
that is, only in the exceptional case
\[
\ell=r+1.
\tag{5}
\]

Assume first that (5) does not hold. Then every prime divisor of \(n\) occurs once. Choosing the factors \(r+\ell^j\) with \(j\ge1\) is exactly the same as choosing a subset
\[
J\subseteq E_{r,\ell,t},
\]
and the target exponent is
\[
\sum_{j\in J}j=t.
\]
If \(r+1\) is prime, it may independently be included or omitted because its Schemmel value is \(1\). Hence every subset representation of \(t\) contributes either one or two preimages, proving (1). More explicitly, for each such \(J\), the preimages are
\[
\prod_{j\in J}(r+\ell^j)
\]
and, when \(r+1\) is prime, also
\[
(r+1)\prod_{j\in J}(r+\ell^j).
\]

Now assume \(\ell=r+1\) is prime. Besides the squarefree factors indexed by \(E_{r,\ell,t}\), the prime \(\ell\) itself may be absent or may occur with any positive exponent \(a\). If it is absent, its exponent contribution is \(0\); if \(a=1\), its contribution is again \(0\); and if \(a\ge2\), its contribution is \(a-1\). Its generating factor is therefore
\[
2+x+x^2+\cdots.
\]
Multiplying by the independent factors \(1+x^j\) proves (2).

Taking \(t=1\) gives (3). If \(r\) is even, every sufficiently general prime target \(\ell\) occurs exactly when \(\ell\) and \(\ell+r\) are both prime; the single possible extra target is \(\ell=r+1\). Hence infinitude of prime targets is equivalent to infinitude of prime pairs at gap \(r\). If \(r\ge3\) is odd, an odd prime \(\ell\) makes \(r+\ell\) an even integer greater than \(2\), while \(r+1\) is an even composite integer. Thus only \(\ell=2\) can occur, and formula (3) reduces to the primality of \(r+2\).

## Verification
The attached `verify.py` implements the Schemmel prime-power formula directly and compares it with an independent factorization-based evaluation of \(S_r(n)\) in a finite stress-test window.

For
\[
1\le r\le8,
\]
for all primes
\[
\ell\le19,
\]
and for
\[
1\le t\le3,
\]
it scans every
\[
1\le n\le50000
\]
and verifies that the observed preimages of \(\ell^t\) are exactly the predicted preimages lying in that window. It also checks the four displayed specializations.

The finite replay is corroborative only. The unrestricted theorem is proved by the prime-block factorization above.

## Relationship to prior work
Subbarao and Yip introduced the inverse-fiber notation \(N_r(m)\) into the Schemmel-totient analogue of Carmichael's and Sierpiński's problems. Their 1989 paper studies the multiplicities of fibers in detail. In the order-\(2\) section it explicitly observes that, for an odd prime \(p\), the equation
\[
S_2(x)=p
\]
has no solution when \(p+2\) is composite. This is exactly the zero side of the \(r=2\), \(t=1\) specialization of (3). The paper does not state the complementary exact multiplicities, the all-order prime-target formula, or the prime-power coefficient formula (1)--(2).

Their 1991 paper again defines \(N_r(m)\), formulates a general multiplicity conjecture, and proves conditional results for certain orders. It does not specialize the inverse problem to a complete prime-power fiber formula.

For \(r=1\), formula (2) recovers the classical structure behind the solutions of
\[
\varphi(n)=2^t:
\]
the odd prime factors are precisely primes of the form \(1+2^j\), hence Fermat primes when prime, while the power of \(2\) supplies the geometric-series factor. This classical Euler-totient specialization is not claimed as new.

Defant's later work on Schemmel nontotients uses the same normalization and records primary MSC \(11A25\). Its focus is absence from the range rather than exact inverse multiplicities at prime powers.

## Limitations
The theorem is confined to prime-power target values. Composite targets with several prime divisors permit interactions among several block values and are not covered by the subset-sum formula.

The equivalence with the fixed-gap prime-pair problem is an equivalence of infinitude statements; it does not resolve any case of Polignac's conjecture.

A 1989 doctoral thesis by L. W. Yip has the same broad Schemmel inverse-value theme and is cited by the inspected primary papers. A complete thesis text was not available through the inspected public routes, so an equivalent observation there remains the principal residual originality risk.

## References
1. M. V. Subbarao and L. W. Yip, “Carmichael's conjecture and some analogues,” in *Théorie des nombres / Number Theory*, De Gruyter, 1989, pp. 928–941, doi:10.1515/9783110852790.928.
2. M. V. Subbarao and L. W. Yip, “On Sierpinski's Conjecture Concerning the Euler Totient,” *Canadian Mathematical Bulletin* 34(3) (1991), 401–404, doi:10.4153/CMB-1991-064-3.
3. C. Defant, “On Schemmel Nontotient Numbers,” arXiv:1412.3089, 2014.
