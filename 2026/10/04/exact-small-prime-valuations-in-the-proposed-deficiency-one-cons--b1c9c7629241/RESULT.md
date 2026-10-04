# Exact small-prime valuations in the proposed deficiency-one construction

## Finding
For every integer \(k\ge2\), and every prime \(p\le k\), define
\[
r_p=\lfloor\log_p k\rfloor+1,
\qquad
M=\prod_{q\le k\atop q\ \mathrm{prime}} q^{r_q},
\qquad
n=M+k-1.
\]
Then the interval \((n-k,n]=(M-1,M+k-1]\) contains exactly one \(k\)-smooth integer, namely \(M\), so its deficiency is one. However,
\[
\nu_p\!\binom{n}{k}=r_p-\nu_p(k)\ge1
\]
for every prime \(p\le k\). Hence every prime at most \(k\) divides \(\binom{n}{k}\), and this binomial coefficient is never good.

Consequently, the construction proposed in arXiv:2609.25042v1 does produce deficiency one, but it does not produce a good binomial coefficient. The paper's claimed infinitude of good deficiency-one binomial coefficients therefore does not follow from that construction. This result does not settle whether infinitely many good deficiency-one binomial coefficients exist.

## Assumptions and scope
A positive integer is \(k\)-smooth if all of its prime factors are at most \(k\). A binomial coefficient \(\binom{N}{k}\) is good if every prime divisor of \(\binom{N}{k}\) is greater than \(k\), equivalently if \(\gcd(\binom{N}{k},k!)=1\).

For a prime \(p\), \(\nu_p(a)\) denotes the exponent of \(p\) in the positive integer \(a\). The theorem concerns exactly the value of \(M\) and the coefficient \(\binom{M+k-1}{k}\) appearing in arXiv:2609.25042v1. No claim is made about other possible constructions.

## Proof
Fix \(k\ge2\).

First prove the deficiency statement. The integer \(M\) is \(k\)-smooth. Suppose that \(M+i\) is also \(k\)-smooth for some \(1\le i\le k-1\). Write
\[
M+i=\prod_{p\le k}p^{e_p}.
\]
Since \(M+i>M\), there is at least one prime \(q\le k\) with \(e_q>r_q\). Define
\[
M'=\prod_{p\le k}p^{\min(e_p,r_p)}.
\]
Then \(M'\mid M\) and \(M'\mid M+i\), so \(M'\mid i\). But the chosen prime \(q\) satisfies \(q^{r_q}\mid M'\), while the definition of \(r_q\) gives \(q^{r_q}>k\). Hence \(M'>k>i\), a contradiction. Thus none of \(M+1,\ldots,M+k-1\) is \(k\)-smooth, and the deficiency is exactly one.

Now fix a prime \(p\le k\), put \(r=r_p\), and write
\[
M=p^rQ,
\qquad p\nmid Q.
\]
Because \(k<p^r\), all base-\(p\) digits of \(k\) lie in positions \(0,\ldots,r-1\). Let \(t=\nu_p(k)\). Then the first nonzero base-\(p\) digit of \(k\) occurs in position \(t\).

The number \(M-1\) has base-\(p\) digits \(p-1\) in positions \(0,\ldots,r-1\), because
\[
M-1=(Q-1)p^r+(p^r-1).
\]
When adding \(k\) to \(M-1\), there is no carry below position \(t\). At position \(t\), the digit \(p-1\) plus the first nonzero digit of \(k\) creates a carry. That carry then propagates through every position \(t+1,\ldots,r-1\), since each corresponding digit of \(M-1\) is \(p-1\). At position \(r\), the digit of \(M-1\) is the least base-\(p\) digit of \(Q-1\), which is at most \(p-2\) because \(p\nmid Q\); adding the incoming carry therefore creates no further carry.

Thus the addition of \(k\) and \(M-1=n-k\) in base \(p\) has exactly
\[
r-t=r_p-\nu_p(k)
\]
carries. Kummer's theorem gives
\[
\nu_p\!\binom{M+k-1}{k}=r_p-\nu_p(k).
\]
Since \(\nu_p(k)\le\lfloor\log_p k\rfloor=r_p-1\), this valuation is positive for every prime \(p\le k\). Therefore \(\binom{M+k-1}{k}\) is not good. \(\square\)

## Verification
The standalone program `verify.py` reconstructs \(M\), computes \(\binom{M+k-1}{k}\) exactly for \(2\le k\le120\), checks every stated \(p\)-adic valuation directly, and independently verifies that among \(M,M+1,\ldots,M+k-1\) only \(M\) is \(k\)-smooth.

Running

`python3 verify.py`

produces exactly

`VERIFY_OK k_cases=119 valuation_pairs=2037 deficiency_cases=119`

The finite computation is corroborative only; the all-\(k\) statement is proved above.

## Relationship to prior work
Xu Zhang's arXiv:2609.25042v1 proposes the same \(M\) and \(n=M+k-1\), proving that \(M\) is the unique \(k\)-smooth integer in the relevant interval and claiming that \(\binom{M+k-1}{k}\) is good. The discrepancy is in the carry criterion: Kummer's theorem counts carries in the base-\(p\) addition of \(k\) and \(n-k\). Digits equal to \(p-1\) in \(n-k=M-1\) force carries once a nonzero digit of \(k\) is encountered; they do not prevent carries. The exact carry count above quantifies the failure.

The classical definition of a good binomial coefficient requires \(\gcd(\binom{N}{k},k!)=1\). The valuation formula here gives the opposite extreme for the proposed construction: every prime \(p\le k\) divides the coefficient.

Targeted searches for the source title together with Kummer carries, exact valuations, correction, and the formula \(r_p-\nu_p(k)\) found no prior published correction or equivalent theorem. The current arXiv record inspected for the source remained version 1.

## Limitations
This correction concerns the explicit construction \(n=M+k-1\). It does not disprove the existence of infinitely many good binomial coefficients of deficiency one, nor does it classify such coefficients. The 1993 primary article defining the deficiency problem was available through metadata and secondary summaries but was not materially inspected in full text; that limitation does not affect the self-contained valuation proof but leaves a small bibliographic risk of an older equivalent observation.

## References
1. Xu Zhang, *Infinitely Many Binomial Coefficients of Deficiency One*, arXiv:2609.25042v1, first public 2026-08-28.
2. P. Erdős, C. B. Lacampagne, and J. L. Selfridge, *Estimates of the Least Prime Factor of a Binomial Coefficient*, Mathematics of Computation 61 (1993), 215--224, DOI: 10.1090/S0025-5718-1993-1199990-6.
3. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik 44 (1852), 93--146.
