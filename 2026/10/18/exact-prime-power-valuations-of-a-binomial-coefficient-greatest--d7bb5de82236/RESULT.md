# Exact prime-power valuations of a binomial-coefficient greatest common divisor

## Finding

For each integer \(n\ge3\), write
\[
D(n-1)=\gcd_{2\le q\le n}\binom{q(n-1)}{n-1}.
\]
For every prime \(p\) with \(p^a\parallel n\), put \(m=n/p^a\) and let \(b\) be the unique nonnegative integer satisfying \(p^b\le m<p^{b+1}\). Then the **exact** gcd, including every prime-power multiplicity, is
\[
\boxed{D(n-1)=\prod_{p^a\parallel n}p^{\max\{0,a-b\}}.}
\]
When \(b<a\), the \(p\)-adic minimum is achieved by an explicit index in the original gcd interval:
\[
q_p=\begin{cases}2,&m=1,\\1+p^a(m-p^b),&m>1.\end{cases}
\]
Consequently \(D(n-1)=n\) if and only if \(n\) is a prime power. Illustrative exact values include \(D(8)=9\), \(D(17)=9\), and \(D(47)=8\).

## Assumptions and scope

All numbers are ordinary positive integers. The notation \(p^a\parallel n\) means \(a\ge1\), \(p^a\mid n\) and \(p^{a+1}\nmid n\). Here \(\nu_p(t)\) is the \(p\)-adic valuation of a positive integer and \(\lfloor\log_p m\rfloor\) is the unique \(b\) with \(p^b\le m<p^{b+1}\). Only \(q\in\{2,\ldots,n\}\) participates in the gcd. The proof uses Kummer's elementary carry-counting theorem, and uses the published \(p\)-divisibility criterion of Guo et al. solely for the already-known zero-valuation branch \(m>p^a\).

## Proof

**Prime support.** Put \(k=n-1\) and \(F(x)=\binom{kx}{k}\), an integer-valued polynomial of degree \(k\). For a positive integer \(d\) dividing all \(F(2),\ldots,F(k+1)\), its forward differences at \(1\) satisfy \(\Delta^r F(1)\equiv(-1)^r\pmod d\) for \(0\le r\le k\), because \(F(1)=1\). Newton interpolation gives
\[
0=F(0)=\sum_{r=0}^k\binom{-1}{r}\Delta^rF(1)\equiv k+1=n\pmod d.
\]
Thus \(D(k)\mid n\). In particular, no prime outside the support of \(n\) occurs.

Fix \(p^a\parallel n\), write \(n=p^a m\), \(p\nmid m\), and choose \(b\) so that \(p^b\le m<p^{b+1}\).

**Zero branch \(b\ge a\).** Since \(p\nmid m\) and \(a\ge1\), \(b\ge a\) implies \(m>p^a\). Lemma 9 of Guo–Qiu–Cao–Feng–Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, proves that \(p\nmid D(n-1)\) exactly when \(m>p^a\). Therefore \(\nu_p(D(n-1))=0\), matching the formula.

**Lower bound for \(b<a\).** Fix any integer \(2\le q\le n\), and put \(k=n-1\), \(X=qk\), \(t=\nu_p(q-1)\). Kummer's theorem identifies \(\nu_p\binom{X}{k}\) with the number of positive integers \(j\) for which the least residues satisfy
\[
[X]_{p^j}<[k]_{p^j}.
\]
For \(1\le j\le a\), \([k]_{p^j}=p^j-1\) and \([X]_{p^j}=[-q]_{p^j}\). Hence these \(a\) positions contribute exactly \(a-\min(a,t)\) carries, because a carry fails exactly when \(q\equiv1\pmod{p^j}\).

For every integer \(h\) with \(b<h\le t\), note that \(p^{a+h}>n\) (since \(p^h>m\)) and \(p^{a+h}\mid n(q-1)\). Since
\[
X=q(n-1)=n(q-1)+(n-q),\qquad 0\le n-q<n-1<p^{a+h},
\]
we have \([X]_{p^{a+h}}=n-q<[k]_{p^{a+h}}=n-1\). These are another \(\max(0,t-b)\) distinct carries, disjoint from the first \(a\) positions. Consequently
\[
\nu_p\binom{q(n-1)}{n-1}\ge a-\min(a,t)+\max(0,t-b)\ge a-b,
\]
where the last inequality holds for all \(t\ge0\) when \(b<a\). It follows that \(\nu_p(D(n-1))\ge a-b\).

**Matching upper bound and an explicit minimizing index.** If \(m=1\), select \(q=2\). In the binomial coefficient \(\binom{2(p^a-1)}{p^a-1}\), there is a carry at each digit boundary \(1\le j\le a\), and none above them, since \(2(p^a-1)<p^{a+1}\). Thus its valuation is precisely \(a\), as desired for \(b=0\).

Suppose \(m>1\) and \(b<a\). As \(p\nmid m\), the integer \(m-p^b\) is positive and coprime to \(p\) (when \(b=0\), use \(1<m<p\)). Define
\[
q=1+p^a(m-p^b),\qquad u=m(m-p^b).
\]
Then \(2\le q\le n\), \(p\nmid u\), and direct multiplication gives
\[
q(n-1)=p^{2a}u+p^{a+b}-1.
\]
Because \(p^b<m<p^{b+1}\) and \(b<a\),
\[
p^{a+b}\le k=n-1<p^{a+b+1}\le p^{2a}.
\]
For \(1\le j\le a+b\), the upper argument is congruent to \(-1\pmod{p^j}\), so its residue is \(p^j-1\); no carry is possible. For \(a+b<j\le2a\), its residue is \(p^{a+b}-1<k=[k]_{p^j}\), so **every** such boundary gives a carry. For \(j>2a\), the residue is
\[
p^{2a}[u]_{p^{j-2a}}+p^{a+b}-1\ge p^{2a}>k,
\]
since \(p\nmid u\); therefore there are no further carries. Precisely \(a-b\) carries occur. Thus \(\nu_p(D(n-1))=a-b\).

Combining every prime completes the stated product identity.

**Extremal corollary.** If \(n=p^a\), then \(m=1\) and the product gives \(D(n-1)=n\). If \(n\) has at least two distinct prime factors, take its smallest prime factor \(p\). Then \(m=n/p^a\) contains a prime greater than \(p\), so \(m>p\) and \(b\ge1\), forcing \(\nu_p(D(n-1))<a\); since \(D(n-1)\mid n\), equality with \(n\) is impossible.

## Verification

A standalone, standard-library-only program `verify.py` independently computes prime valuations via Legendre's factorial formula; it exhaustively checks the minimum over the full gcd range on a bounded collection of integers, and checks the explicit minimizing index on a wider interval. It separately checks the finite-difference divisibility and the displayed special examples. Run `python3 verify.py`. These checks supplement, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

Guo, Qiu, Cao, Feng and Gao (arXiv:2606.22997v1, June 22, 2026), Theorem 1 and Lemma 9, settle OEIS A080170 by determining exactly **when** this gcd equals one and, locally, exactly **which primes** divide it. Their displayed results do not give the powers of those primes. The present theorem determines the complete gcd and provides a minimizing multiplier for every nonzero prime-power exponent; the newly proved valuation bound and witness carry analysis distinguish it from the published zero/nonzero test. The authors' local zero criterion is explicitly used, not claimed anew.

The OEIS A080170 entry lists indices at which the gcd equals one, not a complete formula for its values. Chai Wah Wu's arXiv:2606.20940 concerns the distinct family \(\gcd_{1\le j<n}\binom{mn}{mj}\), with both binomial entries varying. Standard Kummer and Legendre formulas are foundational tools, not claims of novelty.

## Limitations

This is a complete result for the **particular finite window** \(2\le q\le n\); no claim is made for altered windows or more general binomial gcd families. The calculation depends on the previously proved p-primary zero criterion when \(m>p^a\). Novelty comparisons cannot rule out unindexed earlier deductions of the exact power formula; no independent mathematical audit has been performed.

## References

1. D. Guo, R. Qiu, Y. Cao, R. Feng and X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (first posted 2026-06-22), https://arxiv.org/html/2606.22997v1.
2. OEIS Foundation, *A080170: indices where a selected binomial gcd equals one*, https://oeis.org/A080170 (accessed 2026-10-16).
3. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940 (2026-06-18), https://arxiv.org/abs/2606.20940.
4. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik 44 (1852), 93–146 (classical carry theorem).
