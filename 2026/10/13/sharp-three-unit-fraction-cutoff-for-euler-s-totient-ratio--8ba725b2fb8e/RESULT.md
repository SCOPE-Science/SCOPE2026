# Sharp three-unit-fraction cutoff for Euler's totient ratio

## Finding
Let \(\varphi\) be Euler's totient function. For integers \(n\ge2\), suppose that positive integers \(x,y,z\) satisfy
\[
\frac{\varphi(n)}n=\frac1x+\frac1y+\frac1z.
\]
Then \(\varphi(n)/n\le6/7\). Equality occurs **if and only if** \(n=7^k\) for an integer \(k\ge1\); each such equality case is represented by
\[
\frac67=\frac12+\frac13+\frac1{42}.
\]
The denominators \(x,y,z\) are positive and need not be distinct. Hence, if
\[
\mathcal C=\left\{c\in(0,1]:\ \forall n\ge2,\quad
\frac{\varphi(n)}n\ge c\ \Longrightarrow\
\frac{\varphi(n)}n\ne\frac1x+\frac1y+\frac1z
\text{ for every }x,y,z\in\mathbb Z_{>0}\right\},
\]
then \(\mathcal C=(6/7,1]\) and \(\inf\mathcal C=6/7\). The infimum is not attained.

## Assumptions and scope
All rational numbers are considered in lowest terms when their *reduced denominator* is discussed. No distinctness assumption on unit-fraction denominators is used. The restriction \(n\ge2\) is essential: \(\varphi(1)/1=1=1/2+1/3+1/6\). The result gives a sharp upper endpoint, not a decision algorithm or classification for smaller totient ratios.

## Proof
**Denominator gap lemma.** If a rational \(q\) satisfies \(6/7<q<1\) and \(q=1/x+1/y+1/z\) with \(x,y,z\in\mathbb Z_{>0}\), its reduced denominator is divisible by \(2\) or \(3\).

Arrange \(x\le y\le z\). Since \(q<1\), \(x\ge2\), whereas \(q\le3/x\) and \(q>6/7\) imply \(x\le3\). If \(x=2\), \(y=2\) gives \(q>1\), and \(y\ge6\) gives \(q\le1/2+2/6=5/6<6/7\). Therefore \(y\in\{3,4,5\}\). If \(x=3\), \(y\ge4\) gives \(q\le1/3+2/4=5/6\), so \(y=3\).

There are consequently four possibilities.

* \((x,y)=(2,3)\): Here \(q=5/6+1/z\). The strict interval implies \(7\le z\le41\). If the reduced denominator of \(q\) is coprime to \(6\), comparison of the \(2\)- and \(3\)-adic valuations of \(5/6\) and \(1/z\) forces \(v_2(z)=v_3(z)=1\). Indeed, when either valuation differs from \(1\), the valuation of the sum equals the smaller negative valuation. Thus \(z=6k\), where \(\gcd(k,6)=1\), and \(q=(5k+1)/(6k)\). To cancel the factor \(6\) requires \(6\mid5k+1\), equivalently \(k\equiv1\pmod6\). But \(7\le6k\le41\) requires \(2\le k\le6\), a contradiction.
* \((x,y)=(2,4)\): Here \(q=3/4+1/z\), so \(5\le z\le9\). For the reduced denominator to be odd, the unequal-valuation argument forces \(v_2(z)=2\). None of the integers \(5,6,7,8,9\) has \(2\)-adic valuation \(2\). Thus its reduced denominator is even.
* \((x,y)=(2,5)\): Here the inequalities give \(z\in\{5,6\}\), hence \(q\in\{9/10,13/15\}\), whose reduced denominators are divisible by \(2\) or \(3\).
* \((x,y)=(3,3)\): Here \(z\in\{4,5\}\), hence \(q\in\{11/12,13/15\}\), again with reduced denominator divisible by \(2\) or \(3\).

This proves the gap lemma; the infinite range of denominators is fully exhausted by the interval inequalities, not by numerical testing.

Now let \(n\ge2\) and assume \(\varphi(n)/n>6/7\). Euler's product is
\[
\frac{\varphi(n)}n=\prod_{p\mid n}\left(1-\frac1p\right).
\]
Every prime \(p\mid n\) must satisfy \((p-1)/p>6/7\), hence \(p\ge11\). The reduced denominator of the product divides \(\prod_{p\mid n}p\), which is coprime to \(6\). Since the ratio lies strictly between \(6/7\) and \(1\), the denominator gap lemma prohibits a three-unit-fraction representation.

For the equality \(\varphi(n)/n=6/7\), its reduced denominator \(7\) divides \(\prod_{p\mid n}p\), so \(7\mid n\). In the Euler product, the factor for \(p=7\) is already \(6/7\), and every further distinct prime contributes a factor strictly below \(1\). Hence \(n=7^k\) with \(k\ge1\). Conversely all these powers have totient ratio \(6/7\) and the displayed representation. Finally, the universal nonrepresentation statement with the weak hypothesis \(\varphi(n)/n\ge c\) holds exactly when \(c>6/7\); it fails at every \(c\le6/7\) by taking \(n=7\). This completes the proof.

## Verification
The included standalone program `verify_threshold.py` uses Python's exact `fractions.Fraction` arithmetic. It enumerates all unit-fraction triples inside the rigorously bounded search region, verifies that each reduced denominator meets the divisibility obstruction, checks the equality witness, and independently sieves totients through \(300000\). The captured output is in `VERIFIER_OUTPUT.txt`. The code does not certify the infinite statement; the preceding denominator-gap argument is its proof.

## Relationship to prior work
Sagar Mandal, *On an Erdős–Straus type problem* (2026), asks in its Future Research section for the infimum of thresholds above which the totient ratio is not a sum of three unit fractions. Its Theorem 1 establishes the prime-power case for primes at least \(11\) and exhibits \(6/7=1/2+1/3+1/42\). The present result settles the sharp threshold uniformly over **all** integers \(n\ge2\) and characterizes its complete equality class. The paper also contains a broad \(4/5\) nonrepresentation assertion in that section, but it is inconsistent with the paper's explicit \(n=7\) example and therefore does not supply a valid stronger bound. The proof here is independent of that assertion. Earlier literature on unrestricted Egyptian-fraction representations concerns a different quantifier and does not imply this totient-specific maximality claim.

## Limitations
This result does not characterize representability for ratios below \(6/7\); no claim of mathematical novelty follows from absence of a search match. The primary preprint listing contains a month-level date in 2025, while an explicit dated author full-text upload is documented on 2026-04-11; the latter is the earliest **day-specific public-access date verified** for source eligibility, not an assertion that no earlier exposure occurred. Independent external validation has not been performed.

## References
1. S. Mandal, *On an Erdős–Straus type problem*, Annales Universitatis Paedagogicae Cracoviensis Studia Mathematica 26 (2026), 5–17, journal site https://studmath.uken.krakow.pl/article/view/12935 ; DOI: 10.2478/aupcsm-2026-0001. Publication date 2026-07-09.
2. S. Mandal, *On an Erdős–Straus type problem*, public preprint text https://www.researchgate.net/publication/397442304_On_an_Erdos-Straus_type_problem ; DOI: 10.13140/RG.2.2.19272.99845/1. Author-upload date 2026-04-11.
