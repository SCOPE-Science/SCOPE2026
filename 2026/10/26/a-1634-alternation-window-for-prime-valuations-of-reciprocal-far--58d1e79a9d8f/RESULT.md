# A 1634-alternation window for prime valuations of reciprocal Farey products

## Finding

Let \(\overline F_N=\prod_{1\le a\le d\le N,\ \gcd(a,d)=1}\frac da\) be the reciprocal product of all nonzero reduced Farey fractions of order \(N\). For a prime \(p\), set \(f_p(N)=\nu_p(\overline F_N)\), an integer which may be negative.

**Theorem.** For every prime \(p>1{,}344{,}800\) and every integer \(m\) with \(3\le m\le819\),
\[
f_p(mp-1)<0<f_p(mp).
\]
At the very next multiple, \(f_p(820p)<0\). Therefore the values of \(f_p(N)\), read at the increasing sequence
\[
3p-1,\ 3p,\ 4p-1,\ 4p,\ldots,\ 819p-1,\ 819p,\ 820p,
\]
have alternating strict signs. In particular the sequence \(f_p(N)\) has at least **1634** strict sign changes between the first and last sampled indices (with any intermediate zero entries discarded).

There is also a precise limiting coefficient. Define
\[
A_m=\sum_{j=1}^{m}\varphi(j),\qquad S_m=\sum_{j=1}^{m}\frac{\varphi(j)}j,\qquad C_m=2A_m-mS_m.
\]
For every fixed positive integer \(m\), \(f_p(mp)/p\to C_m\) as primes \(p\to\infty\). Exact rational certification establishes
\[
\frac65\le C_m\le\varphi(m)-\frac12\quad(3\le m\le819),\qquad -9<C_{820}<-8.
\]
Consequently \(820\) is the first \(m\ge3\) for which the prime-scale coefficient fails to lie strictly between \(0\) and \(\varphi(m)\).

## Assumptions and scope

The prime \(p\) is arbitrary above the stated explicit threshold, and \(N\) is an integer. The elementary scaling lemma below assumes \(m<p\); the theorem's bound guarantees this for all indices needed. The arithmetic function \(\varphi\) is Euler's totient, and \(\tau(k)\) is the number of positive divisors of \(k\). An expression such as \(\nu_p\) denotes the usual integer-valued exponent of a prime in a positive rational number.

## Proof

**Prime-scale counting lemma.** For integers \(1\le m<p\),
\[
f_p(mp)=pC_m+E_m(p),\qquad |E_m(p)|\le m^2,
\]
and
\[
f_p(mp-1)=p(C_m-\varphi(m))+E_m(p)+\varphi(m).
\]
To prove the first identity, collect contributions from all denominators \(d\le mp\) divisible by \(p\). Since \(m<p\), these denominators are exactly \(jp\) with \(1\le j\le m\), all of valuation one. Their total contribution is
\[
(p-1)\sum_{j=1}^m\varphi(j)=(p-1)A_m.
\]
The numerators divisible by \(p\) are \(kp\), where \(1\le k<m\). A numerator \(kp\) occurs once for each denominator \(d\) satisfying \(kp<d\le mp\) and \(\gcd(d,kp)=1\). Let \(T_k\) count integers \(d\) in this interval with \(\gcd(d,k)=1\), and \(L_k\) count integers \(j\) with \(k<j\le m\) and \(\gcd(j,k)=1\). Because \(p>m\), precisely the \(L_k\) denominators of the form \(jp\) must be removed, so the numerator contribution is \(T_k-L_k\).

Möbius inversion gives the **exact** formula
\[
T_k=\sum_{q\mid k}\mu(q)\left(\left\lfloor\frac{mp}{q}\right\rfloor-\left\lfloor\frac{kp}{q}\right\rfloor\right)
=p(m-k)\frac{\varphi(k)}k+\eta_k,
\]
where \(|\eta_k|\le\tau(k)\): each divisor's difference of floors differs from the corresponding real difference by less than one. Therefore
\[
\begin{aligned}
f_p(mp)&=(p-1)A_m-\sum_{k=1}^{m-1}(T_k-L_k)\\
&=p\left(A_m-\sum_{k=1}^{m-1}(m-k)\frac{\varphi(k)}k\right)-A_m-\sum_{k=1}^{m-1}\eta_k+\sum_{k=1}^{m-1}L_k.
\end{aligned}
\]
The parenthesis equals \(2A_m-mS_m=C_m\), because \(\sum_{k<m}(m-k)\varphi(k)/k=mS_m-A_m\). Put \(E_m(p)=-A_m-\sum_{k<m}\eta_k+\sum_{k<m}L_k\). Since \(A_m\le m(m+1)/2\), \(\sum_{k<m}\tau(k)\le m(m-1)/2\), and \(\sum_{k<m}L_k\le m(m-1)/2\), we have \(-m^2\le E_m(p)<m^2\). This proves the bound without any asymptotic assumption.

At the denominator \(d=mp\), all its reduced numerators are prime to \(p\); the jump is precisely \(\varphi(mp)=(p-1)\varphi(m)\). Thus \(f_p(mp)-f_p(mp-1)=(p-1)\varphi(m)\), proving the second identity.

**Exact finite totient certificate.** Use the sieve recursion \(\varphi(j)=j\prod_{q\mid j,\ q\text{ prime}}(1-1/q)\), with the products evaluated in integer arithmetic. Set \(A_0=S_0=0\) and update \(A_m=A_{m-1}+\varphi(m)\), \(S_m=S_{m-1}+\varphi(m)/m\). The accompanying self-contained `verify.py` compares rational numbers exactly for every \(3\le m\le819\), obtaining
\[
\min_{3\le m\le819}C_m=\frac65\quad(m=6),\qquad
\min_{3\le m\le819}(\varphi(m)-C_m)=\frac12\quad(m=3),
\]
and also \(-9<C_{820}<-8\). No unenumerated \(m\) in the claimed finite range is inferred from sampling. The code includes independent direct Farey-pair computations at small primes to test the counting lemma separately.

For the theorem, use \(p>1{,}344{,}800=2\cdot820^2\). For \(3\le m\le819\), the lemma and certificate give
\[
f_p(mp)\ge\frac65p-m^2>0,
\]
and
\[
f_p(mp-1)\le-\frac p2+m^2+\varphi(m)
\le-\frac p2+819^2+819<0.
\]
At \(m=820\), the lemma gives \(f_p(820p)<-8p+820^2<0\). There are \(817\) pairs \((mp-1,mp)\) for \(3\le m\le819\), followed by one final sample at \(820p\). These \(1635\) nonzero samples alternate signs, hence force at least \(1634\) distinct sign transitions in the full sequence. The finite certificate also shows the claimed first departure of \(C_m\) from the open interval for \(m\ge3\). This completes the proof.

## Verification

Run `python3 verify.py` in the directory containing this document. The script uses only Python's standard library; it sieves \(\varphi\) to \(820\), carries every \(C_m\) as an exact `Fraction`, checks all \(817\) strict-window cases and both extreme values, certifies the first failure at \(820\), and independently checks the counting lemma with direct coprime-pair enumeration for small primes. Expected terminal text begins `CERTIFICATE_OK`. The original theorem for all sufficiently large primes is a deduction of the counting lemma and the complete finite certificate, not an extrapolation from the small-prime tests.

## Relationship to prior work

Lagarias and Mehta, *Products of Farey Fractions* (arXiv:1503.00199, posted 2015-03-01), study exactly the same reduced reciprocal Farey product and its prime valuations. Their Theorem 4.10 proves a positive value at \(p\) and negative values up to \(3p-1\), supplying at least one sign change for every prime, while Property (P3) asks for a much stronger eventual proportion of positive and negative valuations for each fixed prime. The present theorem gives \(1634\) guaranteed alternations over a specified **linear prime-scale window** for every sufficiently large prime, plus an exact first cutoff in its scaling coefficient; neither assertion is established by Theorem 4.10. Their arithmetic methods and general valuation formula are relevant context, but the implication from them to the new certified sign window is not stated there. Their earlier arXiv:1409.4145 studies **unreduced** products and supplies no matching reduced-product sign classification.

## Limitations

The result is uniform over varying sufficiently large primes on a fixed linear window; it does **not** show infinitely many changes for any fixed prime and does not establish Property (P3), the prime-square sign conjecture, or a global density statement. The threshold \(1{,}344{,}800\) is sufficient, not optimal, and \(820\) is a first failure only for the indicated *scaled coefficient* starting at \(m=3\), not the last or first actual sign reversal for every finite prime. A literature or database search cannot guarantee publication priority against unindexed equivalent statements; no independent audit has been performed.

## References

1. J. C. Lagarias and H. Mehta, *Products of Farey Fractions*, arXiv:1503.00199 (first posted 2015-03-01), especially §4, Theorem 4.10 and Properties (P1)–(P4).
2. J. C. Lagarias and H. Mehta, *Products of binomial coefficients and unreduced Farey fractions*, arXiv:1409.4145 (first posted 2014-09-15), particularly the distinction between reduced and unreduced products.
