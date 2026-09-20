# Review: multiplier-four iterated unitary divisor sums on two-prime powers

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof of the prime-rigidity theorem was rederived from the prime-power product formula
\[
\sigma^*(n)=\prod_{p^\alpha\parallel n}(p^\alpha+1).
\]
For \(N=2^a p^b\), the exact \(2\)-power in \(\sigma^*(N)\) is \(2^s\) with
\[
s=v_2(p^b+1).
\]
Because \(2^s+1\) is then a unitary-sigma factor of \(\sigma^*(N)\), the equation
\[
\sigma^*(\sigma^*(N))=2^{a+2}p^b
\]
forces
\[
2^s+1=p^c
\]
for some \(1\le c\le b\). If \(b\) is even, \(s=1\) and therefore \(p=3\). If \(b\) is odd, \(s=v_2(p+1)\); the cases \(c=1\) and \(c\ge2\) were checked separately. In the latter, congruence modulo \(2^s\) forces \(c\) even, and factoring
\[
p^c-1=(p^{c/2}-1)(p^{c/2}+1)=2^s
\]
forces \(p=3,c=2,s=3\), contradicting \(v_2(3+1)=2\). No appeal to unproved prime-distribution assumptions is used.

For the \(b=2\) classification, prime rigidity first reduces to \(p=3\). When \(5\nmid2^a+1\), multiplicativity reduces the equation to
\[
\sigma^*(2^a+1)=2^{a+1}.
\]
The proof that this forces \(a=1\) was checked at each step: every prime-power component of \(2^a+1\) must occur to exponent one and be a Mersenne prime \(2^{d_i}-1\); the exponent sum is \(a+1\); modulo \(2^d\) and \(2^{d+1}\), where \(d=\min d_i\), excludes two or more components. When \(5\mid2^a+1\), writing \(2^a+1=5^c h\) forces \(5^{c+1}+1\) to be \(2\)-\(3\)-smooth. Even \(c+1\) is excluded modulo \(8\) and \(3\); odd \(c+1\ge3\) is excluded by the exact \(2\)- and \(3\)-adic valuations and the inequality \(5^m+1>6m\).

The converse endpoint was checked directly:
\[
\sigma^*(18)=30,\qquad \sigma^*(30)=72=4\cdot18.
\]
A separate exact-integer program checked 10,528 triples with \(1\le a\le16\), odd prime \(p<500\), and \(1\le b\le7\), finding only \((1,3,2)\). This computation supports but is not needed for the proof.

## Originality

The originality claim is **to the best of our knowledge**.

The following evidence was checked:

- The full Sitaramaiah--Subbarao (1998) paper was inspected at its main two-prime theorem for the multiplier-\(2\) equation and at its appendix. The appendix reports bounded solutions of \(\sigma^*(\sigma^*(n))=kn\); for \(k=4\) it lists only \(18\) below \(10^8\), but does not state the present infinite-range rigidity or square-exponent theorem.
- Guy's 2004 *Unsolved Problems in Number Theory* repeats the six listed \(k=3\) examples and \(n=18\) for \(k=4\), without a classification theorem for the present forms.
- Current OEIS A038843 was checked; it concerns the multiplier-\(2\) unitary-superperfect sequence, not the multiplier-\(4\) classification.
- Chehade--Miari--Alkhezi (2023) was checked as recent literature using “unitary superperfect” terminology. Its integer discussion cites the 1998 multiplier-\(2\) work; its own results concern bi-unitary superperfect polynomials over \(\mathbb F_2\), not the integer multiplier-\(4\) equation here.
- Searches covered exact notation and textual variants of \(\sigma^*(\sigma^*(n))=4n\), “iterated unitary divisor sum”, “unitary superperfect” plus multiplier \(4\), “(2,4)-unitary perfect”, “two prime factors”, \(2^a p^b\), and \(2^a p^2\).
- The current SCOPE archive was searched for “unitary superperfect”, “sigma* sigma* 3n”, and broader “unitary” overlap; no matching accepted record was located.

No located source states the prime-rigidity theorem, the exact \(2^a p^2\) classification, or a stronger theorem implying either one.

### Residual originality risk

Terminology for iterated divisor-sum equations is inconsistent, and multiplier-\(4\) results could appear under generalized \((m,k)\)-perfect terminology without “unitary superperfect” in the title or abstract. The 1998 paper and Guy's book are strong evidence that \(18\) was known computationally, so novelty is claimed only for the proved infinite-range statements, not for discovering the integer \(18\).

## Value

The result upgrades a bounded \(k=4\) datum from the classical literature into a structural theorem over an infinite two-prime-power family. The \(2\)-adic argument proves that any two-prime-support candidate must lie in the much thinner family \(2^a3^{2m}\), and the first nontrivial exponent slice is then closed completely. This is a reusable reduction for any attempt at a full two-prime-support classification.

## Limitations

The remaining family \(2^a3^{2m}\) with \(m\ge2\) is not classified. The result makes no statement about integers with at least three distinct prime factors. The finite computation is not formal verification, and no independent audit is asserted.
