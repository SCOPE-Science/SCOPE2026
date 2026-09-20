# Review: exact two-prime-support criterion for \(\lambda^\star\)-practical numbers

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the subset-sum problem to the complete-sequence criterion for the divisor weights \(\lambda(d)\).

For \(n=2^ap^b\), the divisors split naturally into the base block \(2^i\) and the blocks \(2^ip^j\) for fixed \(j\ge1\). The base weights
\[
1,1,2,2,4,\ldots,2^{a-2}
\]
are complete and sum to \(S_0=2^{a-1}+2\).

For an odd prime \(p\), with \(q=p-1\),
\[
\lambda(2^ip^j)
=p^{j-1}\operatorname{lcm}(\lambda(2^i),q).
\]
The normalized weights in a fixed positive-\(p\) block are initial \(1\)'s followed by powers of \(2\), so after the smallest weight of that block fits after the preceding complete interval, every remaining weight in the block fits as well. The sum of one normalized block is the stated value \(C(a,p)\).

The total preceding weight before block \(j\) is
\[
S_0+C(p^{j-1}-1),
\]
using \(p-1=q\). Therefore the smallest new weight \(p^{j-1}q\) fits exactly under inequality (1). If the inequality fails, the immediately next integer after the preceding total cannot be formed by any current or later divisor weight, establishing necessity as well as sufficiency.

The algebra reducing the family of inequalities to the two cases \(C\ge q\) and \(C<q\) is valid. For \(b=1\), the condition becomes \(p-1\le2^{a-1}+3\), equivalently \(p\le2^{a-1}+3\) because \(p\) is odd.

The counting corollary chooses a power of two \(z\) with \(\sqrt X\le z<2\sqrt X\) and counts primes up to
\[
Y=\min(z/2,X/z)\ge\sqrt X/2.
\]
Each corresponding \(zp\) lies below \(X\) and satisfies the \(b=1\) criterion. The prime number theorem therefore gives the claimed
\[
F_{\lambda^\star}(X)\ge(1-o(1))\sqrt X/\log X.
\]

The standalone exact verifier independently constructs every divisor weight and applies the complete-sequence test. On \(3\le a\le12\), odd primes \(p<300\), and \(1\le b\le5\), it checks 3050 triples with zero mismatches. The \(b=1\) threshold is separately checked on 610 pairs with zero mismatches.

## Originality

**PASS, to the best of our knowledge.**

The closest primary source is Schwab--Thompson, *A generalization of the practical numbers* (arXiv:1701.08504; IJNT 2018). The relevant portions were inspected directly. The paper:

- gives the complete-sequence criterion used here;
- treats the Carmichael function separately because it is not multiplicative;
- defines the \(\lambda^\star\)-practical subset-sum notion;
- proves \(F_{\lambda^\star}(X)\ll X/\log X\);
- explicitly states that a reasonable lower bound was not obtained and that the \(X/\log X\) order was unclear from their computations.

The paper's general prime-power adjunction theorem is stated for multiplicative functions and therefore does not directly provide the present Carmichael classification.

OEIS A336508 was also inspected. It records the \(\lambda^\star\)-practical sequence, computational counts, and the Schwab--Thompson reference, but does not state the \(2^ap^b\) criterion or a lower bound of the form proved here.

Current literature searches used the exact terms “lambda*-practical” and “lambda-star practical,” the OEIS identifier A336508, the family \(2^ap\) and \(2^ap^b\), equivalent “Carmichael subset sum” terminology, the explicit prime threshold, and lower-bound phrases involving \(\sqrt X/\log X\). No prior statement matching the classification or counting consequence was located. The current SCOPE archive was also checked under the same objects and synonymous terminology and no overlapping record was found.

No inaccessible paper was identified as a specific close match likely to overturn originality. Residual risk remains because this is a sparsely used terminology and a result could be embedded in literature under a different practical-number formulation.

## Value

**PASS.**

The result completely classifies a natural infinite two-prime-support family for a nonmultiplicative arithmetic function where the standard multiplicative construction theorem does not apply directly. The \(b=1\) specialization is particularly simple and immediately produces a family of cardinality \(\asymp\sqrt X/\log X\) below \(X\).

This gives a polynomial lower bound in the precise counting problem for which the foundational paper reported no reasonable lower bound. It does not reach the empirically suggested \(X/\log X\) order, but it materially narrows the gap between the previously explicit upper bound and elementary sparse families such as powers of two.

## Limitations

- The exact classification is only for \(2^ap^b\) with \(a\ge3\) and \(p\) odd prime.
- The lower bound is of square-root order and does not determine the true order of \(F_{\lambda^\star}(X)\).
- Originality is to the best of our knowledge rather than an exhaustive guarantee.
- The computational verification is finite and supports, but is not needed for, the general proof.
- No formal proof-assistant verification or independent audit has been performed.

## Sources checked

- Nicholas Schwab and Lola Thompson, *A generalization of the practical numbers*, arXiv:1701.08504 / International Journal of Number Theory 14 (2018), 1487--1503.
- OEIS A336508.
- Current SCOPE2026 records under exact and synonymous terminology.
