# Sharp local valuation law for Guo’s quartic Delannoy congruence defect

## Finding

For every odd prime \(p\), define \(D_k(x)=\sum_{j=0}^k\binom{k}{j}\binom{k+j}{j}x^j\) and the integer polynomial
\[H_p(x)=\sum_{k=0}^{p-1}(-1)^k(2k+1)D_k(x)^4-p\sum_{j=0}^{(p-1)/2}(-1)^j\binom{2j}{j}^2[x(x+1)]^j(2x+1)^{2j}.\]
For every integer \(x\ne0,-1\) with \(p\mid x(x+1)\), one has the exact valuation
\[\nu_p(H_p(x))=3+\nu_p(x(x+1)).\]
More precisely, if \(h=\nu_p(x)\ge1\), then \(H_p(x)\equiv4p^3x\pmod{p^{h+4}\); if \(h=\nu_p(x+1)\ge1\), then \(H_p(x)\equiv-4p^3(x+1)\pmod{p^{h+4}\). At \(x=0,-1\), the defect is zero. The result applies to every odd prime, every positive depth \(h\), and every integer in the two stated residue neighborhoods; it does not establish the conjectured cubic congruence at other residue classes.

Thus Guo's proposed \(p^3\)-congruence admits a **sharp, strictly stronger local refinement** on the two naturally distinguished residue classes \(x\equiv0,-1\pmod p\). For instance, when \(\nu_p(x(x+1))=1\), its defect has valuation exactly four, so the congruence is true modulo \(p^4\) and cannot be strengthened uniformly to modulo \(p^5\).

## Assumptions and scope

Here \(p\) is any odd prime, \(x\) any integer, and \(\nu_p\) is the ordinary prime-adic valuation of nonzero integers. The two conditions \(p\mid x\) and \(p\mid x+1\) are disjoint. The notation \(H_p\) refers only to the displayed difference, not either summand separately. For \(x=0,-1\), \(H_p(x)=0\), so a finite valuation is not asserted. No statement is made for other residue classes.

## Proof

**1. Coefficientwise divisibility.** For \(0\le k<p\) one has the polynomial congruence \(D_{p-1-k}(x)\equiv D_k(x)\pmod p\). Indeed, the coefficient of \(x^j\), for \(0\le j<p\), is
\[\frac{\prod_{r=0}^{j-1}(k-r)(k+r+1)}{(j!)^2}.\]
The denominator is a unit modulo \(p\), the numerator is invariant under \(k\mapsto-k-1\), and for \(j>k\) this product is zero; hence it represents both entire polynomials through degree \(p-1\). Pairing \(k\) with \(p-1-k\) reverses \(2k+1\) modulo \(p\) without changing \((-1)^k\). The central index, when present, has \(p\mid2k+1\). Therefore the entire first sum defining \(H_p(x)\) belongs to \(p\mathbb Z[x]\), coefficient by coefficient. The second sum visibly does as well. Writing \(H_p(x)=\sum_{m\ge0}h_mx^m\), we have
\[p\mid h_m\qquad\text{for all }m\ge0.\]

**2. Exact low-degree coefficients.** Put
\[a=k(k+1),\quad b=\frac{(k-1)k(k+1)(k+2)}4,\quad c=\frac{(k-2)(k-1)k(k+1)(k+2)(k+3)}{36}.\]
Then \(D_k(x)=1+ax+bx^2+cx^3+O(x^4)\), so the coefficients of \(x,x^2,x^3\) in \(D_k(x)^4\) are \(4a\), \(6a^2+4b\), and \(4a^3+12ab+4c\), respectively. Their weighted alternating sums, for each odd positive integer \(p\), are exactly
\[S_1=4p(p^2-1),\]
\[S_2=p(p^2-1)(7p^2-16),\]
\[S_3=\frac{2p(p^2-1)(32p^4-191p^2+324)}9.\]
These identities are ordinary rational-polynomial identities (their evaluations are integers). Each follows by induction in steps of two: if \(f_m(k)=(2k+1)[x^m]D_k(x)^4\), then \(S_m(p+2)-S_m(p)=-f_m(p)+f_m(p+1)\), and \(S_m(1)=0\). Substitution of the three displayed polynomials and the explicit \(a,b,c\) makes both sides identical; `verification.py` checks these polynomial identities exactly via degree bounds.

Let \(Q_p(x)\) denote the sum after \(p\) in the definition of \(H_p\). Its coefficients are \([x^0]Q_p=1\), \([x^1]Q_p=-4\); for \(p\ge5\), \([x^2]Q_p=16\), and for \(p=3\), this coefficient is \(-20\). For \(p\ge7\), \([x^3]Q_p=-72\); it equals \(328\) for \(p=5\) and \(-32\) for \(p=3\) because the higher-index terms are truncated. Consequently,
\[h_0=0,\qquad h_1=4p^3,\]
and, for \(p\ge5\),
\[h_2=p^3(7p^2-23),\]
while \(h_2=1188=44\cdot3^3\) for \(p=3\). For \(p\ge7\),
\[h_3=\frac{2p^3(32p^4-223p^2+515)}9,\]
which is divisible by \(p^3\). The exceptional values are \(h_3=6480\) for \(p=3\) and, for \(p=5\), the same rational expression minus \(400p\), still divisible by \(p^3\). Thus universally
\[p^3\mid h_2,\quad p^3\mid h_3,\quad p\mid h_m\ (m\ge4).\]

**3. Exact valuations near zero.** Let \(x\ne0\) and \(h=\nu_p(x)\ge1\). From Step 2 and the coefficientwise divisibility in Step 1,
\[H_p(x)=4p^3x+\sum_{m\ge2}h_mx^m\equiv4p^3x\pmod{p^{h+4}}.\]
Indeed, the terms of degrees two and three have valuations at least \(3+2h\) and \(3+3h\), and every term of degree \(m\ge4\) has valuation at least \(1+mh\); each is at least \(h+4\). Since \(p\) is odd, \(4p^3x\) has valuation exactly \(h+3\), proving the first branch.

**4. Reflection near minus one.** The Legendre-polynomial identity \(D_k(-1-x)=(-1)^kD_k(x)\) follows from \(D_k(x)=P_k(2x+1)\) and parity of \(P_k\). Thus the fourth power is invariant. Moreover, \(x(x+1)\) and \((2x+1)^2\) are invariant under \(x\mapsto-1-x\). Hence \(H_p(-1-x)=H_p(x)\). Applying Step 3 to \(y=-1-x\) proves the second branch. Finally \(H_p(0)=0\), and symmetry gives \(H_p(-1)=0\). \(\square\)

## Verification

Run `python3 verification.py` with a standard Python 3 interpreter. It verifies the exact finite-difference polynomial certificates for all three alternating sums, including their degree bounds; the exceptional low-degree coefficients at \(p=3,5\); and independent exact modular evaluations over multiple primes, valuations and unit multipliers. These checks supplement the preceding infinite argument; numerical sampling alone would not prove the theorem.

## Relationship to prior work

Guo's Theorem 1.4, equation (1.7), proves \(H_p(x)\equiv0\pmod{p^2}\) for every integer \(x\) and odd prime \(p\). His Conjecture 5.2 proposes the stronger but not established universal congruence modulo \(p^3\). This result does **not** resolve the universal conjecture; it exactly determines the defect on the two residue neighborhoods where \(p\mid x(x+1)\), including all possible positive depths. Its first nonzero digit proves sharpness at each depth. The coefficientwise \(p\)-divisibility component is compatible with broader Schmidt-polynomial divisibility results, but those do not provide the cubic coefficient or the exact valuation. Other literature concerning linear Delannoy sums or differently weighted generalized Delannoy sums does not imply the quartic alternating defect valuation.

## Limitations

There is no assertion for \(x\not\equiv0,-1\pmod p\), no proof of Guo's conjecture for those classes, and no claim about other power exponents. The result has been reviewed within the same mathematical analysis; independent mathematical audit and publication-priority verification have not been performed. Some later related papers were examined at abstract level only, and unindexed prior coverage remains possible.

## References

1. Victor J. W. Guo, *Some congruences involving powers of Delannoy polynomials*, arXiv:1412.7724v1 (public 2014-12-10). Theorem 1.4, equation (1.7), and Conjecture 5.2. Relevant sections of the original 10-page preprint inspected in full-text rendering at https://www.researchgate.net/publication/269997599_Some_congruences_involving_powers_of_Delannoy_polynomials ; original arXiv abstract https://arxiv.org/abs/1412.7724.
2. Qi-Fei Chen and Victor J. W. Guo, *On the divisibility of sums involving powers of multi-variable Schmidt polynomials*, International Journal of Number Theory (2017). Abstract/summary available via the citations of Guo's article; coefficient divisibility is different from the sharp valuation here.
3. Lin-Yue Li and Rong-Hua Wang, *Arithmetic properties of generalized Delannoy polynomials and Schröder polynomials*, arXiv:2503.12748 (2025). The stated weighted integrality family differs from the defect polynomial studied here.
4. Rong-Hua Wang and Michael X. X. Zhong, *Congruences for sums of Delannoy numbers and polynomials*, arXiv:2505.05728 (2025). Published abstract concerns weighted linear sums, not quartic alternating differences.
