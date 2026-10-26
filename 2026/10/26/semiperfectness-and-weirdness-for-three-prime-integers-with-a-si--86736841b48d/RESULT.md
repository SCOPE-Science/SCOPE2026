# Semiperfectness and weirdness for three-prime integers with a single factor of two

## Finding
An integer is **semiperfect** (also called pseudoperfect) when it is the sum of distinct positive proper divisors. A **weird** number is abundant but not semiperfect, where abundance means \(\sigma(n)>2n\), and \(\sigma\) is the sum of all positive divisors. A semiperfect integer is **primitive semiperfect** if none of its proper divisors is semiperfect.

**Theorem.** For all distinct odd primes \(3\le p<q\) and all integers \(a,b\ge1\), let \(n=2p^aq^b\). Then \(n\) is semiperfect **if and only if** at least one of the following holds:

\[
\begin{aligned}
&p=3;\\
&(p,q)=(5,7)\text{ and }(a\ge2\text{ or }b\ge2);\\
&(p,q)\in\{(5,11),(5,13)\}\text{ and }a\ge2.
\end{aligned}
\]

Equivalently, the semiperfect members of this family are precisely the multiples of at least one of \(6,350,490,550,650\). The **only weird member** of this family is \(70\). The **primitive semiperfect members** are exactly \(350,490,550,650\) (the primitive semiperfectness condition is taken among all positive divisors, not just members of the family).

## Assumptions and scope
The quantifiers cover arbitrarily large exponents \(a,b\), but precisely three distinct prime factors, with the prime \(2\) occurring exactly once. The classification does not assert anything for integers with additional prime factors or a higher power of \(2\). The special case \(p=3\) is retained, although its smallest semiperfect divisor \(6\) has only two prime factors. We use standard multiplicativity of the divisor-sum function for coprime arguments.

## Proof
**1. Multiplicative closure.** If \(m\) is semiperfect and \(m=\sum_{d\in S}d\) is a sum of distinct positive proper divisors, then every positive multiple \(tm\) is semiperfect: \(tm=\sum_{d\in S}td\), where the summands are distinct and divide \(tm\) properly. In particular, \(6=1+2+3\) implies every integer in the theorem with \(p=3\) is semiperfect.

**2. Exclusion by deficiency.** If \(n=2p^aq^b\), then

\[
\frac{\sigma(n)}n
=\frac32\left(\sum_{i=0}^a p^{-i}\right)
                 \left(\sum_{j=0}^b q^{-j}\right)
<\frac32\frac p{p-1}\frac q{q-1}.
\]

If \(p\ge7\), then \(q\ge11\), so the upper bound is at most \(77/40<2\). Thus these integers are deficient and not semiperfect. If \(p=5\) but \(q\ge17\), the upper bound is at most \(255/128<2\), with the same conclusion. Only \((p,q)=(5,7),(5,11),(5,13)\) remain.

When \(p=5\), \(a=1\) and \(q=11\) or \(13\), the more precise bound

\[
\frac{\sigma(n)}n
<\frac32\left(1+\frac15\right)\frac q{q-1}
\le\frac{99}{50}<2
\]

excludes all \(b\ge1\). The remaining squarefree odd-part case \(n=2\cdot5\cdot7=70\) has \(\sigma(70)=144>140\), so is abundant, but it is not semiperfect: to represent \(70\) using its distinct proper divisors, one would have to exclude divisors summing to \(\sigma(70)-140=4\); the only proper divisors below or equal to \(4\) are \(1\) and \(2\), totaling \(3\).

**3. Exact existence certificates.** For each of the four seed integers \(s\), the following displayed sets \(E_s\) consist of distinct positive proper divisors of \(s\) and satisfy \(\sum_{d\in E_s}d=\sigma(s)-2s\):

\[
\begin{array}{c|c|c}
s&E_s&\sigma(s)-2s\\\hline
350&\{2,7,10,25\}&44\\
490&\{1,10,35\}&46\\
550&\{1,5,10\}&16\\
650&\{2\}&2
\end{array}
\]

Consequently, the proper divisors outside \(E_s\) sum exactly to \(s\), proving that all four seeds are semiperfect. Multiplicative closure proves that every allowed remaining integer is semiperfect: for \((5,7)\) with \(a\ge2\) it is divisible by \(350\); with \(b\ge2\), by \(490\); for \(q=11\) or \(13\) with \(a\ge2\), by \(550\) or \(650\), respectively. This proves the full if-and-only-if assertion. All excluded integers except \(70\) were shown deficient, so \(70\) is the only weird member.

**4. Primitivity.** The four seeds have exact prime factorizations \(350=2\cdot5^2\cdot7\), \(490=2\cdot5\cdot7^2\), \(550=2\cdot5^2\cdot11\), and \(650=2\cdot5^2\cdot13\). A proper divisor retaining all three prime supports and one factor \(2\) can only be \(70\), \(110\), or \(130\), respectively; the first is non-semiperfect and the latter two are deficient because \(\sigma(110)=216<220\) and \(\sigma(130)=252<260\). A proper divisor with fewer prime supports is also deficient: for distinct odd primes \(r\ge5<s\), its divisor-sum quotient is bounded above by \(r/(r-1)\cdot s/(s-1)\le35/24<2\); for support \(\{2,r\}\) with \(r\ge5\) and a single factor \(2\), it is bounded above by \(3r/(2(r-1))\le15/8<2\). The one-prime cases are deficient as well. Therefore all four seeds are primitive semiperfect. Every other semiperfect member has a proper semiperfect divisor \(6\) or one of the four seeds, completing the proof.

## Verification
The companion `verify.py` verifies the four exact divisor-complement identities and checks primitivity of each seed by exhaustive proper-divisor subset-sum search. It also independently checks the classification on \(550\) parameter combinations with \(n\le20000\) and verifies that \(70\) is the only weird instance within that finite test. Its successful output is documented in `VERIFICATION.md`. These finite computations corroborate, but do not establish, the unrestricted theorem; the inequalities, factor divisibilities, and constructions above provide the infinite proof.

## Relationship to prior work
Benkoski and Erdős (1974) introduced and investigated weird and pseudoperfect numbers, including a finite table of weird numbers and the seed \(70\), but the inspected article does not state the above all-exponent semiperfect classification. OEIS A109761 and A109762, introduced on August 12 and 13, 2005 respectively, tabulate rare semiperfect and rare primitive semiperfect numbers and include the four seeds; those finite sequence entries do not logically establish the absence of other members of the full unbounded prime-power family. Amato, Hasler, Melfi and Parton (2018), in the inspected full paper, study primitive abundant and weird numbers and give restrictions involving a bounded number of prime factors **counted with multiplicity**; those restrictions are not the present unrestricted-exponent semiperfectness characterization. Nearby work on strongly pseudoperfect, prime-power pseudoperfect and unitary Zumkeller numbers treats different representations or arithmetic conditions. The presented result is the closed all-exponent classification and unique weird exception, not discovery of the known seeds.

## Limitations
This is an elementary classification restricted to \(v_2(n)=1\) and exactly two distinct odd prime divisors. No classification with higher \(2\)-adic exponent, extra odd supports, or arbitrary weird integers follows. The four seed values and the number \(70\) are classical or tabulated; the novelty assessment concerns the universal combination and exclusions. Priority could be affected by unindexed historical statements or stronger results in older primitive-abundant-number literature. The exact day of publication of the 1974 article is not asserted; the chosen precisely dated archival anchor is the 2005 OEIS entry. No independent mathematical audit or priority certification is claimed.

## References
1. S. J. Benkoski and P. Erdős, “On Weird and Pseudoperfect Numbers,” *Mathematics of Computation* **28** (1974), 617–623. Full text: https://www.renyi.hu/~p_erdos/1974-24.pdf .
2. OEIS A109761, “Rare pseudoperfect (or semiperfect) numbers,” introduced by Walter Kehowski, August 12, 2005. https://oeis.org/A109761 .
3. OEIS A109762, “Rare primitive pseudoperfect numbers,” introduced by Walter Kehowski, August 13, 2005. https://oeis.org/A109762 .
4. G. Amato, M. F. Hasler, G. Melfi and M. Parton, “Primitive abundant and weird numbers with many prime factors,” arXiv:1802.07178 (2018). https://arxiv.org/pdf/1802.07178 .
