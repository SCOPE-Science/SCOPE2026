# Review

## Correctness
**PASS.** For five equal queries \(q\), every minimal recovery set of size at most two is either a singleton of type \(q\) or one of the three complementary pairs summing to \(q\). This gives the exact repeated-query capacity \(A_q\). Summing the seven capacities counts every unordered pair of distinct nonzero column types exactly once. At total length \(10\), balancing gives the sharp bound \(\sum_{u<v}\min(c_u,c_v)\le24\), hence \(\sum_q A_q\le34<35\). The length-eleven witness is then checked exhaustively against all \(462\) five-query multisets. Risks are confined to implementation error in the finite checker; the independent analytic lower-bound derivation and explicit recovery-option reconstruction reduce that risk.

## Originality
**PASS.** The closest unrestricted literature gives minimum length \(10\) for dimension \(3\), five functional-batch requests, but permits arbitrary recovery-set sizes. The closest bounded-recovery paper defines the locality-two problem and proves general bounds, but the inspected full text does not state the exact \([n,3,5,2]\) minimum. Focused searches for the exact parameter, equivalent “locality two” language, and an explicit \([11,3,5,2]\) statement located no source covering the claim. Residual risk remains that an unindexed source contains the same exact finite value.

## Value
**PASS.** This is a natural first intermediate point after the dimension-three simplex code serves four requests at locality two and before the doubled-simplex construction serves eight. The result quantifies the locality restriction sharply: the unrestricted five-request problem has exact length \(10\), whereas locality two requires and attains \(11\). It also supplies a reusable repeated-query capacity inequality that is substantially stronger here than the general labeling count.

## Closest literature and limitations
The closest sources are arXiv:2508.02586 for unrestricted functional-batch length, the 2025 Tartu thesis for the exact unrestricted \(k=3,t=5\) value, and arXiv:2601.12302 for the locality-bounded model. The theorem does not address nonlinear encoders, other dimensions, other request counts, larger recovery sets, or a full isomorphism classification of optimal codes.

Same-model review: passed. Independent audit: not yet performed.
