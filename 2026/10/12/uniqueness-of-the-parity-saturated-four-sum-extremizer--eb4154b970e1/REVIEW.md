# Review

## Correctness
PASS. For every even \(a\) in the entire middle range \(6\le a\le2n-4\), the proof gives an explicit four-tuple whose pairwise sums lie in \(A_E\). Hence a witness-free three-even set can use only \(2,4,2n-2,2n\). Two explicit four-tuples eliminate three of the four boundary triples. For the remaining triple \(\{2,2n-2,2n\}\), the parity argument is exhaustive: three same-parity summands would require three distinct even sums among only two usable even values, while a two-two parity split forces a cross-sum above \(2n\). The finite verifier independently confirms small cases but is not used to prove the infinite statement.

## Originality
PASS with residual historical-search risk. The 2026 van Doorn--Erlbacher paper proves the sharp value \(h_4(n)=4\), gives the surviving lower-bound set, and supplies a middle-even witness mechanism, but does not state a uniqueness theorem for the three-even parity-saturated equality class. Its 2026 predecessor contains an analogous all-odd narrow-sense theorem only for five integers. Targeted searches for the exact \(h_4\), all-odd, three-even, boundary-triple, parity-saturated, extremal, and uniqueness formulations found no equivalent or stronger statement. The remaining risk is an unindexed equality-case observation in older literature.

## Value
PASS. The theorem classifies the equality case in the canonical parity-saturated class at the exact sharp lower-bound cardinality \(n+3\). This is the natural class singled out by the published extremal construction, and the predecessor itself treats comparable all-odd narrow-sense extremality as a meaningful structural question. Exact uniqueness explains which three even positions can coexist with all odds without creating the six pairwise sums, rather than merely giving another witness-free example.

## Closest literature and limitations
The closest source is arXiv:2609.39314v1: Lemma 4.1 proves that the claimed surviving set is witness-free, and Section 5.1 eliminates every configuration containing a middle even by a construction that specializes to this setting. What remains after that published mechanism is a four-element boundary choice, and the present proof supplies the uniform endpoint classification. arXiv:2605.00040v1 gives the closest analogous narrow-sense statement, but for five integers. The result here does not classify arbitrary witness-free sets of size \(n+3\) that omit some odds.

Self-review: passed. Independent audit: not yet performed.
