# Scientific review

## Correctness — PASS
The stated theorem has an unrestricted proof, not just numerical support. Every admissible positive summand is at least \(6\). The necessary divisor-sum inequality proves that \(945\) is the only odd Zumkeller integer at most \(971\); exact divisor witnesses establish all small numbers used. The checked primary literature supplies an even two-summand theorem for all even targets at least \(40\), with \(38\) excluded. The proof covers the k=3 upper bound and its obstruction, all even and odd four-summand targets through explicit witnesses, and a stable all-k lower obstruction: a single odd \(945\) forces a nonnegative excess of \(16\) from even increments \(0,6,14\), an impossibility. Induction by adjoining \(6\) establishes the infinite upper range.

The verifier independently constructs the defining divisor subset sums to \(4000\), tests lengths \(3\) through \(30\), and checks the key finite lemmas. These experiments are corroboration, not a proof of the unrestricted assertions.

## Originality — PASS relative to inspected sources
The nearest published mathematical premise is Somu, Kukla and Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149, Proposition 4.6(a). It classifies sums of **two** Zumkeller integers for even targets and explicitly proposes three- or four-summand exploration in Section 5. Its two-sum result implies easy upper coverage after adding small summands but does not provide the new exact thresholds or their proof of sharpness. The new result is not a claim of independence from that substantial prior work.

The primary work on individual Zumkeller numbers, the OEIS set of Zumkeller numbers, the odd-abundant list, and the OEIS two-sum exceptions do not state this all-length largest-gap formula. Numerically and semantically targeted searches found no identical theorem. The phrase *k-layered numbers* describes partitions of the divisors of one integer, not sums of k Zumkeller numbers. Residual bibliographic risk: an equivalent unindexed statement could exist; a k-layered publisher article was only accessible by abstract/excerpt.

## Value — PASS
An explicit research direction about sums of three or four Zumkeller numbers is settled by sharp thresholds and extended to all \(k\ge3\). The infinite formula shows a genuinely discontinuous base length followed by a stable affine law. Its sharpness uses a natural obstruction combining the least odd Zumkeller number with a minimal even excess rather than an arbitrary parameter slice or a recomputed membership list.

## Limits
The theorem concerns largest exceptions, not all gaps, number of representations, or lengths one and two. It invokes a cited published two-summand theorem. Unindexed equivalent work is possible; no independently conducted audit is claimed.

Self-review: passed. Independent audit: not yet performed.
