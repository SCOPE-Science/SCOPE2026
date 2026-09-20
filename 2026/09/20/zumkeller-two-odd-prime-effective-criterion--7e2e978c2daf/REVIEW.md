# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces the classical divisor-partition criterion to an exact arithmetic statement. For p>M=2^(a+1)-1, direct expansion gives

D=(sigma(2^a p q)-2·2^a p q)/2=(M(M+1)-(p-M)(q-M))/2.

If D>=0, then D<=M(M+1)/2<M^2<pq, so a distinct-divisor representation of D cannot use any divisor containing both odd primes. The remaining divisors split into three disjoint binary blocks 2^i, p2^i, q2^i. Each block realizes every coefficient from 0 to M, proving the stated x+py+qz criterion in both directions. The abundance inequality also gives a rigorous finite bound for p and q at fixed a.

The finite classifications for a<=4 were checked in two mathematically independent representations: the derived coefficient condition and exact subset-sum over the complete divisor set. The verification artifact reports zero discrepancies for every candidate in the rigorously bounded p>M abundance region. The p<=M branch follows from established Zumkeller closure results and is additionally spot-checked, but the proof does not depend on the sample.

Potential edge cases were checked: D=0 is admitted by x=y=z=0; p and q are distinct so the multiplicative closure applies in the automatic branch; and the strict inequality D<pq is valid for every a>=1 because M>=3.

## Originality

**PASS, to the best of our knowledge.** The following coverage was checked.

- Bhaskara Rao--Peng, *On Zumkeller Numbers* (arXiv:0912.0052; JNT 2013): the accessible full text was inspected for the necessary-and-sufficient excess criterion (Fact 3), multiplicative closure (Fact 6), the 2^a p sufficient condition (Fact 10), and the general np partition criterion (Proposition 15). Proposition 15 is an important adjacent general criterion, but no explicit reduction or fixed-exponent classification for 2^a p q was located.
- Mahanta--Saikia--Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers* (JNT 2020; arXiv:2008.11096): this work completely characterizes the two-distinct-prime case 2^alpha p^beta and treats bounds and k-layered questions for more prime factors. Its result for 2^alpha p q displayed in the accessible text concerns 3-layered and higher-layered numbers, not the classical two-layer Zumkeller classification obtained here.
- Somu--Kukla--Tran, *Some Results on Zumkeller Numbers* (arXiv:2310.14149, 2023): the paper's stated results concern consecutive Zumkeller runs and additive representations, not this prime-factor family.
- Current OEIS material for A083207 and recent work on unitary/generalized Zumkeller variants were checked for matching formulas or exception lists; none were found.
- Exact and synonymous searches were made for forms including “2^a p q”, “2^alpha p q”, three distinct prime factors, and explicit low-exponent slices such as 8pq and 16pq. No source located states the present criterion or the displayed complete exception lists.
- The current SCOPE archive was searched for “Zumkeller” and equivalent target terms; no prior SCOPE result covering this contribution was found.

The principal residual originality risk is that the explicit criterion may exist as an unstated or differently notated specialization of a broad divisor-partition theorem, or in literature indexed under “integer-perfect” rather than “Zumkeller”. No specifically identified inaccessible paper was found that appears uniquely likely to contain the same classification. Accordingly the originality claim is limited to “to the best of our knowledge”.

## Value

**PASS.** The result moves beyond a bounded list of examples: for every fixed binary exponent it turns an infinite prime-pair problem into a rigorously finite one, while covering an infinite automatic region at once. It also gives the first four fixed-exponent classifications in compact form and exhibits explicit abundant numbers in this natural three-prime family that nevertheless fail the Zumkeller partition condition. This directly complements the known complete classification with two distinct prime factors and the existing general partition criteria.

## Scientific limitations

The odd part is restricted to pq with exponent one on both odd primes. The criterion remains an algorithmic finite test, rather than a closed-form parametrization, for arbitrary a. No claim is made about 2^a p^b q^c with larger odd exponents or about numbers with four or more distinct prime factors. The finite verification is supporting evidence for the low-exponent corollaries; the general theorem rests on the proof above rather than on computation.
