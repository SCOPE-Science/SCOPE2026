# Totient-scale primorial barriers for primitive Frobenius representations

## Finding

For coprime positive integers \(a,b\), let \(G(a,b)\) be the largest nonnegative integer not expressible as \(ax+by\) with nonnegative integers \(x,y\) satisfying \(\gcd(x,y)=1\). Finiteness of \(G\) is known [1]. **Theorem.** For every fixed integer \(a\ge3\),

\[
\limsup_{\substack{b\longrightarrow\infty\\\gcd(a,b)=1}}
\frac{G(a,b)}{b\log b}\ \ge\ \varphi(a).
\]

More precisely, the explicit sieve-product construction below produces infinitely many eligible \(b=b_T\), together with integers \(Q_T\le G(a,b_T)\), such that \(Q_T/(b_T\log b_T)\longrightarrow\varphi(a)\). The prime-divisor sieve used in the construction is asymptotically optimal among all integer products which share a prime factor with every integer in the forced residue class.

## Assumptions and scope

Fix \(a\ge3\), let \(T\) run through sufficiently large positive integers, and denote Euler's totient by \(\varphi\). Let

\[
Q_T=\prod_{\substack{p\le\sqrt T\\p\nmid a}}p\ \cdot\!
\prod_{\substack{\sqrt T<p\le T\\p\equiv-1\pmod a}}p,
\]

where every product is over distinct prime numbers. Let \(b_T\) be the **smallest positive integer** satisfying

\[
b_T\ge Q_T/T,\qquad b_T\equiv-Q_T\pmod a.
\]

For large \(T\), we have \(\gcd(a,Q_T)=\gcd(a,b_T)=1\) and \(b_T>a\). No upper estimate for \(G(a,b)\) or claim of global asymptotic sharpness is required.

## Proof

**1. Arithmetic obstruction.** Every prime factor of \(Q_T\) is coprime to \(a\), so both \(Q_T\) and \(b_T\) are coprime to \(a\). Assume that

\[
Q_T=ax+b_Ty,\qquad x,y\in\mathbb Z_{\ge0}.
\]

Reducing modulo \(a\) and using \(b_T\equiv-Q_T\pmod a\) gives \(y\equiv-1\pmod a\). Since \(a\ge3\), necessarily \(y\ge2\), and \(\gcd(y,a)=1\). Furthermore \(y\le Q_T/b_T\le T\). If \(y\) is composite, its least prime divisor \(p\le\sqrt y\le\sqrt T\) is coprime to \(a\) and hence divides \(Q_T\). If \(y\) is prime, then \(y=p\le T\) and \(p\equiv-1\pmod a\), so again \(p\mid Q_T\). In both cases \(p\mid y\), \(p\mid Q_T\) and \(p\nmid a\). The displayed equation forces \(p\mid x\). Consequently \(\gcd(x,y)\ge p>1\). There is no primitive representation, and \(G(a,b_T)\ge Q_T\).

**2. Size of the obstruction.** The prime number theorem in fixed reduced arithmetic progressions says

\[
\sum_{\substack{p\le T\\p\equiv-1\pmod a}}\log p
=\frac{T}{\varphi(a)}+o(T).
\]

The difference between this sum and \(\log Q_T\) involves only primes at most \(\sqrt T\), of total logarithmic weight \(O(\sqrt T\log T)=o(T)\). Thus

\[
\log Q_T=\frac{T}{\varphi(a)}+o(T).
\]

By minimality in the fixed residue class, \(Q_T/T\le b_T<Q_T/T+a\), so \(b_T\sim Q_T/T\), \(\log b_T\sim T/\varphi(a)\), and

\[
\frac{Q_T}{b_T\log b_T}\longrightarrow\varphi(a).
\]

In particular \(b_T\to\infty\). Combining with the first part proves the asserted \(\limsup\) bound.

**3. Optimal exponential weight of the sieve cover.** Let \(\mathcal C_{a,T}\) be the positive integers \(M\), coprime to \(a\), such that

\[
\gcd(M,y)>1\quad\text{for every }2\le y\le T\text{ with }y\equiv-1\pmod a.
\]

The first part shows \(Q_T\in\mathcal C_{a,T}\). Conversely, taking \(y=p\) for each prime \(p\le T\) with \(p\equiv-1\pmod a\) shows every \(M\in\mathcal C_{a,T}\) must be divisible by the product of all such primes. Therefore

\[
\inf_{M\in\mathcal C_{a,T}}\log M
=\frac{T}{\varphi(a)}+o(T).
\]

The lower bound uses only obligatory prime divisors; the upper bound is supplied by \(Q_T\). This establishes optimality **within this prime-divisor-cover model**, not a sharp value of the unrestricted primitive Frobenius limsup.

## Verification

The standalone standard-library program `verify.py` constructs \(Q_T,b_T\) for \(3\le a\le14\) and \(\max(a,8)\le T\le60\), and tests every nonnegative solution of \(ax+b_Ty=Q_T\). It checks 615 parameter pairs and confirms that no primitive solutions exist. For \(a=3,T=20\) it obtains \(Q_T=1870\), \(b_T=95\) and six nonprimitive solutions. These finite checks do not establish the universal or asymptotic assertions; the proof above does.

## Relationship to prior work

Ding, Wang and Zhang [1, Theorem 1.7] proved that for each fixed \(a>2\), the corresponding limsup normalized by \(b\log b\) exceeds an unspecified positive constant depending on \(a\). Their Section 4 proof uses CRT choices tailored to finitely many solution parameters, with a bound using all primes up to a multiple of the parameter. The present construction uses an explicit residue-class sieve and gives the specific coefficient \(\varphi(a)\), plus an asymptotically optimal sieve-cover statement. Neither the numerical coefficient nor this product obstruction appears as a conclusion of [1].

The known logarithmic lower-growth order for fixed \(a\) is not claimed as new. Earlier uniform estimates requiring both coefficients to increase do not imply the fixed-coefficient result.

## Limitations

The coefficient \(\varphi(a)\) is a proved lower bound for the limsup, not a proved exact maximal-order constant. The optimality conclusion is explicitly restricted to the divisor-cover model. The proof uses the established prime number theorem in arithmetic progressions with modulus \(a\) fixed, and does not assert uniformity for growing \(a\). Exhaustive literature search is impossible, and an equivalent earlier explicit construction is a residual originality risk. Independent assessment has not been performed.

## References

1. Y. Ding, W. Wang and H. Zhang, *The Diophantine Frobenius Problem revisited*, arXiv:2509.08599v1 (first posted 10 September 2025), in particular Theorem 1.7 and its proof in Section 4. https://arxiv.org/html/2509.08599v1
2. Prime number theorem for primes in a fixed reduced arithmetic progression (standard theorem).
