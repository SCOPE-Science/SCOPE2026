# Characteristic-local adjacency among sparse-order finite-field nonsquares

## Finding

Let \(q=p^f\) be an odd prime power satisfying \(q-1=2^a\ell\), where \(\ell\) is an odd prime and \(1\leq a\leq4\). A *non-square non-primitive* (NSNP) element of \(\mathbb F_q\) is a nonzero nonsquare which does not generate \(\mathbb F_q^\times\). Let \(N(q)\) count ordered pairs \((u,u+1)\) for which both entries are NSNP. The following is a complete classification within these four multiplicative-order strata:

| Exact \(2\)-adic exponent \(a\) | \(N(q)\) |
| --- | --- |
| \(1\) | \(0\) for every permitted \(q\) |
| \(2\) | \(1\) precisely when \(q=5^f\) with odd \(f\geq3\) and prime \(\ell=(5^f-1)/4\); otherwise \(0\) |
| \(3\) | \(0\) for every permitted \(q\) |
| \(4\) | \(2\) when \(q=49\); \(4\) when \(q=17^f\) with odd \(f\geq3\) and prime \(\ell=(17^f-1)/16\); otherwise \(0\) |

The primality conditions in the table are necessary hypotheses, not assertions that infinitely many such exponents exist. In particular, \(N(125)=1\) and \(N(4913)=4\), whereas every permitted field with \(a=3\) has no such pair. At \(q=4913\) the four pairs are \((5,6),(6,7),(10,11),(11,12)\), each in the prime subfield \(\mathbb F_{17}\). The \(q=49\) count is also known from earlier work; its inclusion makes the stratified classification complete.

More generally, for *every* \(a\geq1\) and every \(q=p^f\) with \(q-1=2^a\ell\) and odd prime \(\ell\), set \(h=2^{a-1}\). Then

\[
N(q)=\deg\gcd_{\mathbb F_p[X]}\bigl(X^h+1,(X+1)^h+1\bigr).
\]

Thus, once \(a\) and the characteristic \(p\) are fixed, the pair count is independent of the odd prime \(\ell\) and the extension degree \(f\), subject to the stated order hypothesis.

## Assumptions and scope

The field has odd characteristic, the odd part of \(q-1\) is a *single prime to the first power*, and the displayed explicit classification concerns exactly \(1\le a\le4\). Consecutive means additive difference \(1\), not adjacent discrete logarithms. The count includes each possible initial element exactly once. The general gcd identity holds for any positive \(a\) under the same single-prime hypothesis; no explicit higher-\(a\) classification is asserted.

## Proof

**Reduction to cyclotomic roots.** The cyclic group \(\mathbb F_q^\times\) has order \(2^a\ell\); choose a generator \(g\). Write an element as \(g^k\). It is a nonsquare exactly when \(k\) is odd. Such an element is non-primitive exactly when \(\gcd(k,2^a\ell)>1\); because \(k\) is odd and \(\ell\) is prime, this means \(\ell\mid k\). Consequently the NSNP elements are precisely the primitive \(2^a\)-th roots of unity. For \(a\ge1\), these are exactly the roots of \(F_a(X)=X^{2^{a-1}}+1\). Every root is in \(\mathbb F_q\) because \(2^a\mid q-1\). Since \(p\ne2\), the derivative \(2^{a-1}X^{2^{a-1}-1}\) shows that \(F_a\) is squarefree. Therefore the number of \(u\) with \(F_a(u)=F_a(u+1)=0\) equals the degree of the *monic* gcd of these two polynomials over \(\mathbb F_p\). This proves the general identity and its characteristic-locality conclusion.

**Finite arithmetic at the first four levels.** Put \(h=2^{a-1}\) and let \(R_a\) be the integral resultant \(\operatorname{Res}_{X}(X^h+1,(X+1)^h+1)\). The exact values, evaluated as determinants of integral Sylvester matrices, are

\[
R_1=1,\quad R_2=5,\quad R_3=3^2\cdot17,\quad
R_4=7^2\cdot17^4\cdot257.
\]

An integral resultant not divisible by \(p\) precludes a common root in characteristic \(p\). For its possible prime divisors, the monic gcds over \(\mathbb F_p\), with their degrees, are as follows:

| \(a\) | \(p\) | \(\gcd(F_a(X),F_a(X+1))\) over \(\mathbb F_p\) | Degree |
| --- | --- | --- | --- |
| \(2\) | \(5\) | \(X-2\) | \(1\) |
| \(3\) | \(3\) | \(X^2+X-1\) | \(2\) |
| \(3\) | \(17\) | \(X-8\) | \(1\) |
| \(4\) | \(7\) | \(X^2+X-1\) | \(2\) |
| \(4\) | \(17\) | \(X^4+2X^3-3X^2-4X+2\) | \(4\) |
| \(4\) | \(257\) | \(X-128\) | \(1\) |

All other characteristics have gcd degree zero. These finite identities are determined by the ordinary Euclidean polynomial algorithm and an exact-integer Sylvester determinant computation; the standalone script `check.py` constructs both objects rather than relying on a table or a floating-point approximation. A second symbolic-algebra calculation of all determinants and gcds agrees. The numerical resultants themselves have appeared previously in the general shifted-resultant table OEIS A255831 and are not claimed as new.

**Imposing prime-power field orders.** At \(a=1\), \(R_1=1\), so the count vanishes. At \(a=2\), only \(p=5\) can contribute. The condition \(v_2(5^f-1)=2\) forces \(f\) odd; \(f=1\) has \(\ell=1\) and is excluded. All remaining admissible \(f\) are exactly those in the theorem, with gcd degree one.

At \(a=3\), the possible characteristics from \(R_3\) are \(3\) and \(17\). The latter has \(16\mid17^f-1\), contradicting \(v_2(q-1)=3\). For \(p=3\), the valuation condition forces \(f=2m\) with \(m\) odd. If \(m=1\), then \((q-1)/8=1\); if \(m\ge3\), the identity

\[
\frac{3^{2m}-1}{8}=\frac{3^m-1}{2}\cdot\frac{3^m+1}{4}
\]

writes the odd factor as a product of two integers greater than one, contrary to primality. Thus the \(a=3\) stratum has no pairs.

At \(a=4\), the resultant leaves \(p=7,17,257\). Characteristic \(257\) is impossible because \(2^8\mid257^f-1\). For \(p=7\), the requirement \(v_2(7^f-1)=4\) forces \(f=2m\) with \(m\) odd, and

\[
\frac{7^{2m}-1}{16}=3\sum_{j=0}^{m-1}49^j.
\]

This odd factor is prime only at \(m=1\), yielding \(q=49\), \(\ell=3\), and exactly two roots. For \(p=17\), the valuation \(v_2(17^f-1)=4\) holds exactly when \(f\) is odd, and admissibility excludes \(f=1\). Every remaining admissible field has gcd degree four. No other characteristic yields a pair. This proves all cases.

## Verification

Run `python3 check.py` with Python 3 and its standard library. The script constructs the Sylvester matrices in exact integers, evaluates them by fraction-free elimination, factors the resulting small integers by trial division, and performs Euclidean gcd computations modulo every resultant prime. It independently enumerates NSNP elements and consecutive pairs in the finite fields of orders \(49\), \(125\), \(4913\), \(41\), \(89\), and \(113\). The reproducible output is included in `certificate.txt`. A separate symbolic-algebra reconstruction of all four integer resultants and modular gcds agreed. These small-field enumerations are checks only; the proof for all admissible prime powers is the group-theoretic and valuation argument above.

## Relationship to prior work

Cohen's 2026 paper studies consecutive NSNP pairs and proves existence under \(\varphi(q-1)/(q-1)\le1/3\) apart from specified exceptions. Its Table 3 already records two such pairs at \(q=49\). For the present single-odd-prime order condition, the ratio equals \((\ell-1)/(2\ell)\), which exceeds \(1/3\) whenever \(\ell\ge5\); neither Cohen's threshold nor his table determines the sparse high-ratio families \(q=125\) and \(q=4913\), or the all-field stratified classification. Earlier Jarso–Trudgian work treats smaller primitive-density regimes, largely in prime fields. Zhou–Wu's July 2026 work concerns existence of *three* consecutive NSNP elements at a still smaller density threshold and gives a separate bound for longer tuples; its abstract does not imply the exact counts here, but the full text was not accessible for inspection. OEIS A255831 already tabulates the needed integral shifted resultants: the contribution here is not their recomputation but the modular gcd ranks, the prime-power order sieve, and the complete NSNP-pair consequences. A derivation elsewhere from these ingredients remains an originality risk.

## Limitations

There is no claim of an infinite number of primes \(\ell=(5^f-1)/4\) or \((17^f-1)/16\), of classifications for \(a\ge5\), or of analogous formulas when the odd part of \(q-1\) is composite or a higher prime power. Only pair counts, not full triple or higher-tuple counts, are determined. The finite displayed cutoff is the first four \(2\)-adic strata; general higher strata may require larger resultants and different local patterns. Published resultant tabulations and inaccessible potentially related full texts limit any assertion of global novelty.

## References

1. S. D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429v1 (first public 23 April 2026), https://arxiv.org/html/2604.21429v1.
2. T. Jarso and T. Trudgian, *Quadratic residues that are not primitive roots*, arXiv:1710.04320, https://arxiv.org/abs/1710.04320.
3. J. Zhou and H. Wu, *Consecutive non-square non-primitive tuples in finite fields*, arXiv:2607.17267 (19 July 2026), https://arxiv.org/abs/2607.17267.
4. OEIS A255831, *Square array of resultants of shifted binomial polynomials*, https://oeis.org/A255831 (2015).
