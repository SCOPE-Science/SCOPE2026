# Primitive prime divisors yield infinitely many two-prime semi-Carmichael integers

## Finding

Let \(\mathcal S\) be the set of composite positive integers \(n\) satisfying
\[
 d^n\equiv d\pmod n\qquad\text{for every positive divisor }d\mid n.
\]
For every prime \(p\ge 5\) there exists a prime \(q>p\) with
\[
 \operatorname{ord}_q(p)=p-1,\qquad q\equiv1\pmod{p-1},\qquad pq\in\mathcal S.
\]
Here \(\operatorname{ord}_q(p)\) means the least positive \(h\) such that \(p^h\equiv1\pmod q\). Consequently, \(\mathcal S\) contains infinitely many squarefree integers with exactly two prime factors, and the smaller prime factor can be any prime at least \(5\).

More quantitatively, put
\[
 S_2(X)=\#\{n\le X:n\in\mathcal S,\ n=pq\text{ with primes }p<q\}.
\]
Then
\[
 \liminf_{X\to\infty}\frac{S_2(X)(\log\log X)^2}{\log X}\ge1.
\]
Every constructed example is **not** a Carmichael number. The result gives an affirmative solution to the infinitude question recorded for the equivalent semiprime sequence OEIS A294169 (in the publicly available record inspected), although that question was already formulated well before the terminology used here.

## Assumptions and scope

All primes are positive rational primes. A *semi-Carmichael integer* is a composite integer satisfying the displayed divisor-base congruences; the definition is the one used by López (2026, Definition 5.8). The theorem concerns squarefree semiprimes; it makes no claim about semiprimes with repeated prime factors, the density of \(\mathcal S\) among all integers, or a complete characterization of \(\mathcal S\).

The only substantial external theorem needed for existence is the classical Bang–Zsigmondy primitive-prime-divisor theorem: for coprime integers \(a>b\ge1\), \(a^h-b^h\) has a prime factor dividing no \(a^j-b^j\) with \(1\le j<h\), provided \(h>1\), except when \(h=2\) and \(a+b\) is a power of two, or \((a,b,h)=(2,1,6)\). The proof of this classical result can be found in the reference listed below. The prime number theorem is used only for the quantitative lower bound, not for infinitude.

## Proof

**Step 1: the exact semiprime test.** If \(p<q\) are distinct primes and \(n=pq\), its positive divisors are precisely \(1,p,q,pq\). The divisor condition therefore holds if and only if
\[
 p^{pq}\equiv p\pmod{pq},\qquad q^{pq}\equiv q\pmod{pq}.
\]
For the first congruence the reduction modulo \(p\) is automatic; modulo \(q\) we can cancel the invertible \(p\), obtaining \(p^{pq-1}\equiv1\pmod q\). Since
\[
 pq-1=p(q-1)+(p-1),
\]
Fermat's little theorem reduces this to \(p^{p-1}\equiv1\pmod q\). Interchanging \(p\) and \(q\) similarly gives \(q^{q-1}\equiv1\pmod p\). Thus the *necessary and sufficient* criterion is
\[
 \boxed{\ q\mid p^{p-1}-1\quad\text{and}\quad p\mid q^{q-1}-1.\ }
\]
This exact equivalence is also recorded in OEIS A294169; it is not asserted as a new observation.

**Step 2: a prime with full prescribed order.** Fix any prime \(p\ge5\), and apply the Bang–Zsigmondy theorem with \(a=p\), \(b=1\) and \(h=p-1\). The exponent is at least \(4\), so the exponent-two exception is irrelevant. The exceptional triple with \(a=2\) is also irrelevant. We obtain a prime \(q\) dividing \(p^{p-1}-1\) but dividing no \(p^j-1\) with \(1\le j<p-1\). Because \(p^{p-1}\equiv1\pmod q\), the multiplicative order of \(p\) modulo \(q\) exists and divides \(p-1\); primitivity forces that order to be exactly \(p-1\).

By Lagrange's theorem in the multiplicative group of the prime field \(\mathbb F_q\), this order divides \(q-1\), whence
\[
 p-1\mid q-1.
\]
Clearly \(q\ne p\), since \(p\) does not divide \(p^{p-1}-1\). Moreover \(q\equiv1\pmod{p-1}\) and \(q\) is a prime different from \(p\), so \(q\ge2p-1>p\). By construction \(q\mid p^{p-1}-1\). By Fermat's theorem modulo \(p\), together with \(p-1\mid q-1\), we also have \(p\mid q^{q-1}-1\). Step 1 therefore shows that \(pq\in\mathcal S\).

**Step 3: distinctness and the explicit counting lower bound.** The map sending \(p\) to one such product \(pq\) is injective: the smaller prime factor of the product is exactly \(p\). Every chosen \(q\) divides \(p^{p-1}-1\), hence
\[
 pq\le p\bigl(p^{p-1}-1\bigr)<p^p.
\]
Consequently, whenever \(p^p\le X\), its product is counted by \(S_2(X)\). For sufficiently large \(X\), define \(Y=\lfloor\log X/\log\log X\rfloor\). The elementary bounds \(Y<\log X\) and \(\log Y<\log\log X\) imply \(Y\log Y<\log X\), hence \(p^p\le X\) for every prime \(p\le Y\). Excluding only \(2\) and \(3\),
\[
 S_2(X)\ge\pi(Y)-2.
\]
As \(X\to\infty\), the prime number theorem gives
\[
 \pi(Y)\sim\frac{Y}{\log Y}\sim\frac{\log X}{(\log\log X)^2},
\]
proving the stated liminf. In particular the construction gives infinitely many distinct members of \(\mathcal S\) with exactly two prime factors.

**Step 4: distinction from ordinary Carmichael numbers.** Were a product \(pq\), with \(p<q\), a Carmichael number, Korselt's criterion would give both \(p-1\mid pq-1\) and \(q-1\mid pq-1\). Reducing the two divisibilities shows \(p-1\mid q-1\) and \(q-1\mid p-1\). They force \(p=q\), a contradiction. Thus no constructed product is Carmichael. This is a standard exclusion, not an additional novel assertion.

## Verification

The entire argument is symbolic, conditional only on well-established theorems cited above. An independent finite check is supplied in `check.py` (Python 3, standard library only) with reference output in `certificate_stdout.txt`. It checks seven selected constructed pairs by deterministic primality testing, modular order, both exact semiprime conditions and the original congruences. Separately, it enumerates every distinct-prime semiprime at most \(100000\), compares the original condition with the reduced condition for all \(23313\) candidates, and checks that the first sixteen selected integers agree with OEIS A294169. It reports \(52\) qualifying semiprimes in that range. The finite certificate neither proves Zsigmondy's theorem nor replaces the proof for arbitrary \(p\).

The supplied sample pairs \((p,q)\) are
\[
 (5,13),\ (7,43),\ (11,13421),\ (13,28393),\ (17,18913),\ (19,199),\ (29,427822081).
\]
All primality and congruence checks for these examples are reproduced by the attached program. Prime factorization of the full values \(p^{p-1}-1\) is not needed: verifying a selected \(q\) is prime and has exact order \(p-1\) suffices for the example.

## Relationship to prior work

López (2026) defines semi-Carmichael integers using the divisor-base condition and exhibits a list of initial values, including two-prime members. Its relevant Section 5 does not give a general infinitude construction via primitive prime divisors. OEIS A294169, present since 2018, studies precisely the equivalent two-prime condition and explicitly asks whether infinitely many such integers exist. The semiprime equivalence in Step 1 and the initial values were therefore already known. The new contribution here is the unconditional prime-by-prime existence theorem using Zsigmondy's theorem and its accompanying quantitative lower bound.

The classical primitive-divisor theorem by itself does not mention semi-Carmichael numbers. The implication requiring both prime-factor congruences, and the injection through the smaller prime factor, supply the bridge. The nearby literature on Carmichael and weak Carmichael numbers concerns different universal or averaged base-congruence conditions and does not, without an additional implication, establish the theorem above.

## Limitations

The construction selects one permissible prime \(q\) for each \(p\ge5\) but does not give a practical polynomial-time procedure to find it. The quantitative count is a lower bound only. It need not reflect the correct order of growth of all semi-Carmichael semiprimes. Earlier work not located in the comparisons may have already made this observation; the public OEIS question should not be taken as proof of absolute novelty. The infinite result is a written mathematical argument, not independently reviewed or formally certified.

## References

1. Miguel Ángel López, *Idempotence in Carmichael and Giuga numbers and its application to the Agoh–Giuga conjecture*, arXiv:2610.09129v1, public 2026-10-06, especially Definition 5.8 and Proposition 5.9; https://arxiv.org/html/2610.09129.
2. OEIS A294169, *Semiprimes \(k=pq\) with \(p^k\equiv p\pmod k\) and \(q^k\equiv q\pmod k\)*, entries and infinitude question; https://oeis.org/A294169 (initial public entry 2018).
3. Karl Zsigmondy, *Zur Theorie der Potenzreste*, Monatshefte für Mathematik und Physik **3** (1892), 265–284, classical primitive-prime-divisor theorem.
4. *Zsigmondy's Theorem*, ProofWiki, theorem and detailed proof with exceptions; https://proofwiki.org/wiki/Zsigmondy%27s_Theorem.
5. AMS MSC2020, class 11A51, *Factorization; primality*; https://mathscinet.ams.org/msc/msc2020.html?t=11A15.
