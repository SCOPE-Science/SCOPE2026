# No square of a semiprime is superharmonic

## Finding

For any two **distinct primes** \(p<q\), put \(n=(pq)^2\). With \(\sigma(n)\) the sum of positive divisors, \(\tau(n)\) their number, and \(\operatorname{rad}(m)\) the product of the distinct prime divisors of \(m\), one has

\[
\operatorname{rad}(\sigma((pq)^2))\nmid3pq.
\]

Consequently no square of a semiprime is **superharmonic**: for every integer \(k\ge1\),

\[
\sigma((pq)^2)\nmid(pq)^{2k}\tau((pq)^2).
\]

The proof identifies all candidate pairs satisfying the necessary local restrictions on the first cyclotomic factor and the permitted prime support of the second factor. They are precisely \((2,7)\), \((3,13)\), and \((13,61)\); each fails by an explicit extra prime factor.

## Assumptions and scope

All primes are positive rational primes. No congruence condition on \(p\) or \(q\) is assumed. The exponent pattern is exactly \((2,2)\), and the primes must be distinct. This theorem does **not** classify all superharmonic numbers with two prime divisors or all odd superharmonic numbers. The first verified source date for the superharmonic definition used here is September 5, 2008 (electronic publication stated in the source itself).

## Proof

Set \(\Phi_3(t)=t^2+t+1\). Multiplicativity of the divisor sum and the divisor count gives

\[
\sigma(p^2q^2)=\Phi_3(p)\Phi_3(q),\qquad \tau(p^2q^2)=9.
\]

If the necessary prime-support condition \(\operatorname{rad}(\sigma(p^2q^2))\mid3pq\) holds, then every prime factor of \(\Phi_3(p)\) lies in \(\{3,q\}\), and every prime factor of \(\Phi_3(q)\) lies in \(\{3,p\}\), because \(\Phi_3(r)\equiv1\pmod r\).

We use two elementary facts. First, for any prime \(r\ne3\),

\[
\nu_3(\Phi_3(r))=
\begin{cases}1,&r\equiv1\pmod3,\\0,&r\equiv2\pmod3.\end{cases}
\]

Indeed, when \(r=1+3t\), \(\Phi_3(r)=3(1+3t+3t^2)\); in the other residue class the polynomial is \(1\) modulo \(3\). Second, if \(\ell\ne3\) is prime and \(\ell\mid\Phi_3(r)\) for a prime \(r\), then \(r^3\equiv1\pmod\ell\) but \(r\not\equiv1\pmod\ell\): the identity \(\gcd(r-1,\Phi_3(r))\mid3\) excludes that possibility. Thus \(r\) has multiplicative order \(3\) modulo \(\ell\), and \(\ell\equiv1\pmod3\).

**Case \(p=2\).** The factor \(\Phi_3(2)=7\) forces \(q=7\). Yet \(\Phi_3(7)=57=3\cdot19\), where \(19\notin\{2,3,7\}\), contradicting the support condition.

**Case \(p=3\).** The factor \(\Phi_3(3)=13\) forces \(q=13\). Yet \(\Phi_3(13)=183=3\cdot61\), where \(61\notin\{3,13\}\), again contradicting support.

**Case \(p\ge5\).** Here \(q>p\ge5\). Since \(\Phi_3(q)>3\), and \(\nu_3(\Phi_3(q))\le1\), its factorization using only \(\{3,p\}\) forces \(p\mid\Phi_3(q)\). The order-three fact then gives \(p\equiv1\pmod3\), in particular \(p\ge7\). The exact three-adic valuation gives

\[
\Phi_3(p)=3q^a\quad\text{for some integer }a\ge1.
\]

But \(\Phi_3(p)/3=(p^2+p+1)/3<p^2<q^2\), so \(a=1\) and

\[
3q=p^2+p+1,\quad\text{hence }3q\equiv1\pmod p.
\]

Since \(p\mid\Phi_3(q)\), multiplying by nine yields

\[
0\equiv9(q^2+q+1)=(3q)^2+3(3q)+9\equiv1+3+9=13\pmod p.
\]

Therefore \(p=13\) and \(q=(13^2+13+1)/3=61\). Yet

\[
\Phi_3(61)=3783=3\cdot13\cdot97,
\]

and \(97\notin\{3,13,61\}\), again impossible. Every ordered prime pair belongs to one of these cases, proving \(\operatorname{rad}(\sigma(p^2q^2))\nmid3pq\). If \(\sigma(p^2q^2)\mid(pq)^{2k}\tau(p^2q^2)\), then necessarily its prime support would divide \(3pq\), a contradiction. \(\square\)

## Verification

The included `verify.py` independently sieves the primes at most \(2000\), checks the necessary prime-support condition on every distinct prime pair from this list, and verifies the three forced candidate pairs and their explicit obstructions. The expected output is `VERIFY_OK`, with \(45{,}753\) tested pairs. The exact proof above, rather than this finite computation, supplies the universal quantifier.

## Relationship to prior work

Cohen's introduction of superharmonic numbers derives the prime-support criterion and proves that odd squarefree numbers are not superharmonic; it explicitly notes difficulty with the broader two-prime-factor question. Those results do not exclude the non-squarefree family \((pq)^2\). Pollack and Pomerance prove asymptotic estimates for the much larger superharmonic set, not this exact exponent-profile obstruction. Luca's work on numbers for which the prime divisors of \(\sigma(n)\) are among those of \(n\) concerns the stricter condition excluding the extra permitted factor \(3\); the available bibliographic evidence does not establish coverage of the present claim.

## Limitations

The theorem addresses precisely two distinct primes with exponent two each. It neither excludes other two-prime exponent vectors nor settles the existence of odd superharmonic integers. The reported novelty is limited to accessible published material and mathematical-record comparisons; an uninspected broader valuation or cyclotomic-support theorem might imply the result. No independent audit has been performed.

## References

1. G. L. Cohen, *Superharmonic numbers*, Mathematics of Computation 78 (2009), 421–429; electronic publication September 5, 2008, DOI 10.1090/S0025-5718-08-02147-9. Full text: https://opus.lib.uts.edu.au/bitstream/10453/8271/1/2008007907OK.pdf.
2. P. Pollack and C. Pomerance, *Prime-perfect numbers*, Integers 12 (2012). Full text: https://www.pollack-math.net/pperfs16.pdf, especially Section 5.2.
3. F. Luca, *On numbers n for which the prime factors of sigma(n) are among the prime factors of n*, Results in Mathematics 45 (2004), 79–87, DOI 10.1007/BF03322999. Full text not inspected.
