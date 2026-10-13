# Scientific review

**Correctness — PASS.** The statement uses distinct ordered subsequences for two deletions. Exact integral packing duals establish upper bounds at each length; an exhaustive checker re-evaluates every dual column for all binary input words and all ten explicit primal witnesses. The length-seven dual numerator is 666 at denominator 59 for list size two, strictly below twelve. The independent short-length comparisons establish first occurrence. All inequalities were verified with Python's arbitrary-precision integers. Risk: the verifier and written proof share a finite incidence definition, so a misunderstanding of the channel model would affect both; the model matches Lin's Definition 2.1.

**Originality — PASS, subject to residual literature risk.** Lin's 2026 paper gives asymptotic hypergraph bounds and Guruswami–Håstad's 2020 paper gives asymptotic code constructions, neither the exact \(11\)-word length-seven list-two capacity nor the first-length comparison. Kiah–Wei–Zeng give nonmatching general bounds. The OEIS table already has the unique-deletion value five, explicitly excluded from novelty. A previous finite table not indexed in the inspected literature remains possible.

**Value — PASS.** The inequality \(M_2(7,2)=11>10=2M_2(7,1)\) determines the smallest blocklength at which two-deletion list-two codes cannot be assembled from two optimal (or smaller) uniquely decodable codes. This is a motivated structural property of synchronization channels, not an arbitrary isolated calculation. It does not imply a separation for every length or for other deletion radii.

Self-review: passed. Independent audit: not yet performed.
