# A unique \(3\)-adic zero in prime-power weighted Apéry sums

## Finding
For each integer \(n\ge1\), define the Apéry polynomial
\[
A_n(X)=\sum_{j=0}^n\binom nj^2\binom{n+j}j^2X^j,
\qquad S_n(X)=\sum_{k=0}^{n-1}(2k+1)A_k(X).
\]
For every odd prime \(p\) and every integer \(a\ge1\), put \(n=p^a\) and \(h=(n-1)/2\). The coefficientwise congruence
\[
S_n(X)\equiv p^aX^h\pmod{p^{a+1}}
\]
holds in \(\mathbb Z[X]\). In particular, if \(x\in\mathbb Z_p^\times\), then \(\nu_p(S_n(x))=a\).

If \(p\ge5\), every \(x\in p\mathbb Z_p\) satisfies \(\nu_p(S_n(x))=2a\). Hence \(S_n\) has no zero in \(\mathbb Z_p\).

For \(p=3\), there is instead exactly one zero \(\xi_a\in\mathbb Z_3\), with \(\xi_a\equiv6\pmod9\). Writing \(\xi_a=3u_a\), one has for every \(u\in\mathbb Z_3\)
\[
\nu_3(S_{3^a}(3u))=2a+\nu_3(u-u_a),
\]
with \(\nu_3(0)=+\infty\). Thus the numbers of roots \(x\pmod{p^k}\) of \(S_{p^a}(x)\equiv0\pmod{p^k}\), for every \(k\ge1\), are respectively
\[
N_{p,a}(k)=
\begin{cases}
p^k,&1\le k\le a,\\
p^{k-1},&a<k\le2a,\\
0,&k>2a,\ p\ge5,\\
3^{2a-1},&k>2a,\ p=3.
\end{cases}
\]
The universal fixed divisor of \(S_{p^a}\), meaning \(\gcd_{x\in\mathbb Z}S_{p^a}(x)\), is exactly \(p^a\) for odd primes \(p\). For completeness, it is exactly \(2^{2a}\) when \(p=2\).

## Assumptions and scope
The prime \(p\) is a rational prime, \(a\ge1\) is arbitrary, and \(n=p^a\). The \(p\)-adic valuation is normalized by \(\nu_p(p)=1\) and extends to zero as \(+\infty\). Congruences of polynomials are coefficientwise unless explicitly evaluated. A root modulo \(p^k\) is a residue class in \(\mathbb Z/p^k\mathbb Z\); a \(p\)-adic zero is an element of \(\mathbb Z_p\). No claim about \(2\)-adic roots is made.

## Proof
**1. Exact coefficient identity.** For \(0\le j<n\), put \(B_{n,j}=\binom{n-1}{j}\binom{n+j}{j}\). The following identity is classical (Sun, equation (1.5)):
\[
S_n(X)=n^2\sum_{j=0}^{n-1}\frac{B_{n,j}^2}{2j+1}X^j.\tag{1}
\]
For completeness it follows by telescoping. If
\(F_m=m^2\binom{m-1}{j}^2\binom{m+j}{j}^2/(2j+1)\) for \(m\ge j+1\), and \(F_j=0\), then
\[
F_m-F_{m-1}=(2m-1)\binom{m-1}{j}^2\binom{m-1+j}{j}^2.
\]
Summing \(m=j+1,\ldots,n\) yields the coefficient of \(X^j\) in \(S_n\). Every coefficient in (1) is an integer because it also equals a finite sum of binomial products.

**2. A single surviving coefficient for odd \(p\).** Take \(n=p^a\), with \(p\) odd. Since \(1\le2j+1\le2n-1\), the sole \(j\) in \([0,n-1]\) for which \(p^a\mid2j+1\) is \(h=(n-1)/2\). For all other \(j\), \(\nu_p(2j+1)\le a-1\), so (1) gives \(p^{a+1}\) dividing the coefficient. At \(j=h\), that coefficient is \(n B_{n,h}^2\). For each \(1\le i<n\), the quotient \(n/i\) belongs to \(p\mathbb Z_p\); therefore the product formulas for binomial coefficients give
\[
\binom{n-1}h\equiv(-1)^h\pmod p,
\qquad\binom{n+h}h\equiv1\pmod p.
\]
Thus \(B_{n,h}^2\equiv1\pmod p\), proving the stated polynomial congruence and the unit-input valuation.

**3. Inputs divisible by \(p\).** Substituting \(X=pu\) into (1) gives
\[
\frac{S_n(pu)}{p^{2a}}
=\sum_{j=0}^{n-1}\frac{p^jB_{n,j}^2}{2j+1}u^j
=:F_{p,a}(u)\in\mathbb Z_p[u].\tag{2}
\]
Indeed \(\nu_p(2j+1)\le j\) for each \(j\ge1\). If \(p\ge5\), the stronger strict inequality holds, because \(p^j>2j+1\) for all \(j\ge1\). Thus \(F_{p,a}(u)\equiv1\pmod p\) for all \(u\), giving exact valuation \(2a\) and no integral \(p\)-adic root.

For \(p=3\), \(3^j>2j+1\) for every \(j\ge2\), but the \(j=1\) term survives. As \(B_{n,1}=n^2-1\), equation (2) yields
\[
F_{3,a}(u)\equiv1+(n^2-1)^2u\equiv1+u\pmod3.
\]
There is exactly one simple root modulo \(3\), at \(u\equiv-1\pmod3\). Hensel's lemma gives a unique lift \(u_a\in\mathbb Z_3\). Moreover for any \(u\in\mathbb Z_3\), the quotient \((F_{3,a}(u)-F_{3,a}(u_a))/(u-u_a)\) (with its polynomial interpretation when equal) is congruent to \(1\pmod3\), hence is a unit. This proves the exact valuation formula and uniqueness of \(\xi_a=3u_a\). Nonmultiples of three cannot be roots by step 2.

**4. Root counts.** If \(k\le a\), the congruence in step 2 makes every residue a root. If \(a<k\le2a\), precisely the multiples of \(p\) are roots, giving \(p^{k-1}\) classes. For \(k>2a\), step 3 gives no roots when \(p\ge5\). When \(p=3\), write \(x=3u\) with \(u\) defined modulo \(3^{k-1}\); the valuation condition is \(u\equiv u_a\pmod{3^{k-2a}}\), leaving exactly \(3^{2a-1}\) classes.

**5. Fixed divisors.** For odd \(p\), all values are divisible by \(p^a\), while \(\nu_p(S_n(1))=a\) and \(S_n(0)=n^2=p^{2a}\); thus the gcd over all integer inputs is exactly \(p^a\). For \(p=2\), equation (1) has odd denominators, so every coefficient of \(S_{2^a}\) is divisible by \(2^{2a}\). Its constant coefficient equals \(2^{2a}\), giving equality for the fixed divisor.

## Verification
The standalone file `verify.py` independently forms the coefficients from both the defining sum and (1), checks the odd-prime coefficientwise congruence for eight prime-power cases, checks numerical valuations, and counts roots modulo small prime powers against the piecewise formula. It also tests dyadic coefficient divisibility in six cases. Run `python3 verify.py`. These finite checks corroborate but do not establish the general theorem.

## Relationship to prior work
Sun's 2011 Apéry-polynomial paper (Theorem 1.1(ii), equation (1.5)) supplies the exact all-index coefficient formula used as input and some prime-index numerical congruences. Guo and Zeng and Pan establish related divisibility properties. Those ingredients are not claimed to be new. The point added here is the complete integral local zero-locus and valuation/root-count dichotomy at every odd prime-power index, especially the unique \(3\)-adic zero versus absence of integral roots at every prime \(p\ge5\), together with sharp universal fixed divisors. The local conclusion requires the analysis of all \(p\)-adic inputs, not just the published divisibility of sums by their length.

## Limitations
The classification is restricted to prime-power indices and to odd-prime root loci. There is no classification of the \(2\)-adic roots, of roots in nonintegral \(p\)-adic extensions, or of arbitrary composite index. It relies on Sun's published coefficient identity; a logically equivalent derivation in unlocated literature remains a genuine originality risk. It has not received independent mathematical validation.

## References
- Zhi-Wei Sun, *On sums of Apéry polynomials and related congruences*, arXiv:1101.1946 (first posted 2011-01-10), Theorem 1.1(ii), especially equation (1.5), and the numerical congruences in equations (1.6)–(1.7). https://arxiv.org/abs/1101.1946
- Victor J. W. Guo and Jiang Zeng, *New congruences for sums involving Apéry numbers or central Delannoy numbers*, arXiv:1008.2894 (first posted 2010-08-17). https://arxiv.org/abs/1008.2894
- Hao Pan, *On divisibility of sums of Apéry polynomials*, arXiv:1108.1546 (first posted 2011-08-07), Introduction and Theorem 1.1. https://arxiv.org/abs/1108.1546
