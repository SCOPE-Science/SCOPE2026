# All prime factors at least seven in fourth-power Fibonacci window gcds

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\) for \(n\ge0\). For an integer \(k\ge1\), define
\[
C_4(k)=\gcd_{n\ge0}\left(\sum_{i=0}^{k-1}F_{n+i}^{4}\right).
\]
For every prime \(p\ge7\), put \(R_p=\mathbb F_p[t]/(t^2+3t+1)\), and let \(h_p\) be the multiplicative order of the class \(\bar t\) in \(R_p^\times\). This order exists because \(\bar t(\bar t+3)=-1\). Then **for every** \(k\ge1\) and **every** prime \(p\ge7\),
\[
\boxed{\nu_p(C_4(k))=\begin{cases}\nu_p(k),&h_p\mid k,\\0,&h_p\nmid k.\end{cases}}
\]
The result determines the complete part of \(C_4(k)\) supported on primes at least seven; it does not claim values for the prime factors \(2,3,5\). The order always divides \(p-(5/p)\), where \((5/p)\) is the Legendre symbol.

## Assumptions and scope
All Fibonacci numbers and window sums are integers, and \(\nu_p(N)\) is the exponent of a prime \(p\) in a positive integer \(N\). The gcd is the positive gcd of the infinite family; this is well-defined as the gcd of finite initial subfamilies, and the proof shows that its first five members already suffice. The finite algebra \(R_p\) is either a quadratic field or a product of two finite fields; in both cases its displayed element is invertible. The theorem applies to every positive window length, with no parity restriction.

## Proof
**1. Five independent modes.** Let \(\alpha=(1+\sqrt5)/2\), and set \(\mu=-\alpha^2\). The Binet formula and the Lucas identities give, for all \(n\ge0\),
\[
25F_n^4=6-4(\mu^n+\mu^{-n})+\mu^{2n}+\mu^{-2n}.
\]
Here \(\mu\) is an algebraic unit satisfying \(\mu^2+3\mu+1=0\). For \(s_k(z)=1+z+\cdots+z^{k-1}\), this yields
\[
25\sum_{i=0}^{k-1}F_{n+i}^4
=6k-4\mu^n s_k(\mu)-4\mu^{-n}s_k(\mu^{-1})
 +\mu^{2n}s_k(\mu^2)+\mu^{-2n}s_k(\mu^{-2}).
\]
The five roots \(1,\mu,\mu^{-1},\mu^2,\mu^{-2}\) are roots of
\[
Q(x)=(x-1)(x^2+3x+1)(x^2-7x+1)
=x^5-5x^4-15x^3+15x^2+5x-1.
\]
Thus the window-sum sequence in \(n\) satisfies the monic, integral, order-five recurrence with characteristic polynomial \(Q\). Consequently every term is an integer linear combination of the initial five. In particular, \(\nu_p(C_4(k))\) can be determined from those five windows.

**2. Local diagonalization away from \(2,3,5\).** Fix \(p\ge7\) and \(e\ge1\). Work in \(A= (\mathbb Z/p^e\mathbb Z)[t]/(t^2+3t+1)\). The discriminant of \(Q\) is \(2^4 3^2 5^{10}\). Thus all five roots in the preceding formula are pairwise distinct modulo \(p\), and every root difference is a unit of \(A\). The five-by-five Vandermonde matrix in these roots is consequently invertible over \(A\). Since \(25,6,4\) are also units, the first five window sums vanish modulo \(p^e\) if and only if both
\[
p^e\mid k\qquad\text{and}\qquad s_k(t)=0\quad\text{in }A.
\]
The coefficients of \(s_k(t^{-1})\) and of the two squared modes then automatically vanish if \(s_k(t)=0\), because inversion is the ring involution, and \(t^2-1\) is also a unit (its norm is \(-5\)), so \(t^{2k}=1\) implies \(s_k(t^2)=0\).

The element \(t-1\) has norm \(5\), which is invertible modulo \(p\). Therefore \(s_k(t)=0\) is equivalent to \(t^k=1\) in \(A\). We conclude that
\[
 p^e\mid C_4(k)\quad\Longleftrightarrow\quad p^e\mid k\ \text{and}\ t^k=1\pmod{p^eA}.
\]
(The last notation means equality in the residue algebra \(A\).)

**3. Prime-power lifting.** Reduction of \(t\) modulo \(p\) has order \(h_p\), and this order is prime to \(p\): if \(5\) is a square modulo \(p\), the roots are reciprocal nonzero elements of \(\mathbb F_p\), so \(h_p\mid p-1\); otherwise their Frobenius conjugation is inversion, so \(h_p\mid p+1\). If \(h_p\nmid k\), already \(t^k\ne1\) modulo \(p\), proving \(\nu_p(C_4(k))=0\). If \(h_p\mid k\) and \(v=\nu_p(k)\), write \(k=h_pm\), so \(\nu_p(m)=v\). Since \(t^{h_p}=1+p a\) in the unramified \(p\)-adic quadratic algebra, the binomial theorem, valid also in its split case, gives \((t^{h_p})^m\equiv1\pmod{p^{v+1}}\). In particular \(t^k=1\pmod{p^v}\) whenever \(v\ge1\). By step 2, \(p^v\mid C_4(k)\), whereas \(p^{v+1}\nmid C_4(k)\) because \(p^{v+1}\nmid k\). If \(v=0\), the constant-mode condition also gives valuation zero. This completes the proof.

## Verification
The standalone standard-library script `artifacts/verify.py` independently calculates the gcd of five integer window sums, determines \(h_p\) by arithmetic in the finite quadratic algebra, and compares the formula for all \(1\le k\le400\) and all relevant prime divisors. It additionally checks that no unexpected prime at least seven divides the observed gcds. Explicit witnesses include \(C_4(56)=21\), \(C_4(91)=13\), \(C_4(110)=11\), and \(C_4(153)=34\). Computation is corroborative; the proof above establishes all quantifiers.

## Relationship to prior work
Mbirika and Spilker (arXiv:2204.12626, initially public 2022-04-26) compute the gcd of sums of consecutive **squares** of generalized Fibonacci numbers and ask about higher powers in Section 6, Question 6.1. Adegoke (arXiv:1706.00407, initially public 2017-05-28) derives formulas for sums of fourth powers (including the Binet/Lucas decomposition), but not the gcd of all translated windows or the exact prime-by-prime classification proved here. Earlier cubic-power gcd work concerns a different power and does not imply the local fourth-power spectrum without new analysis. The conclusion applies to every window length and every \(p\ge7\), rather than a finite collection of examples.

## Limitations
The theorem gives no values of \(\nu_2(C_4(k))\), \(\nu_3(C_4(k))\), or \(\nu_5(C_4(k))\). Consequently no full closed form for \(C_4(k)\) is claimed. The approach relies on invertibility of the Vandermonde discriminant, which fails at exactly the excluded small primes. An independent mathematical audit has not been performed; possible unpublished or unindexed coincident results remain a literature risk.

## References
Adegoke, K., *Sums of fourth powers of Fibonacci and Lucas numbers*, arXiv:1706.00407 (2017), https://arxiv.org/pdf/1706.00407.

Mbirika, aBa, and Spilker, J., *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (2022), https://arxiv.org/pdf/2204.12626; especially Section 6, Question 6.1.
