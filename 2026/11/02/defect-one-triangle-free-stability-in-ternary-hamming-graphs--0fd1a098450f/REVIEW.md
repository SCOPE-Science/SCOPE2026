# Scientific review: defect-one triangle-free stability in ternary Hamming graphs

## Correctness — PASS

A triangle in the unit-distance ternary Hamming graph is precisely a complete coordinate line. Complementing converts the claim to hitting all three-point lines with one more point than the minimum. Counting line intersections in every direction leaves one doubled line. Counting their two-coordinate planes forces all doubled lines to share one anchor. Deleting the anchor, if present, gives the unique maximum completion. If absent, all weight-one neighbors are included, weight-two points excluded, and every weight-three section must select a sign-parity class. In a four-coordinate face the required four weight-four points cannot exist because all four parity conditions admit at most one sign vector. Small-dimensional hole patterns are exhaustive; maximum hitting sets are affine hyperplanes via order-three Latin-square affinity. Multiplication of the hyperplane count and external points yields the exact \(6^n\) completed sets. The small-dimensional additional counts are \(9\) and \(54\). Each boundary case \(n=2\) and \(n=3\) was checked by direct exhaustive enumeration of the original line-hitting property, and the four-dimensional obstruction was separately checked across its sixteen parity profiles. No unchecked computation is used to bridge finite dimensions to the infinite statement.

## Originality — PASS, qualified

The closest source, Csajbók–Mukkamala–Nagy, arXiv:2610.32789 (2026-10-23), proves the maximum \(2\cdot3^{n-1}\) but not the number or stability of sets of size one less. The difference between an extremal cardinality theorem and a complete next-to-extremal classification is substantive: the latter entails the global common-anchor lemma, the sharp four-dimensional obstruction, and small exceptional noncompletable families. Classical one-per-line MDS/quasigroup classification does not automatically imply that every one-extra-point hitting set is completable; the explicit counterexamples in dimensions two and three show why. Krotov's older quasigroup work concerns the exact-code regime, not defect-one hitting sets. Searches for equivalent one-extra-point transversal, almost-MDS, triangle-free Hamming and line-cover formulations found no covering theorem; this is not a proof of priority. A potentially relevant completion paper for Latin cuboids of order five was assessed at abstract level only and remains a limited residual risk.

## Mathematical value — PASS

A natural first stability question beneath the published sharp vertex-Turán bound is whether near-optimal sets inherit the maximum structure. Here the answer changes sharply at dimension four, with exact numerical exceptions in dimensions two and three. The all-dimensional enumeration \(6^n\), uniqueness of completion, and genuinely noncompletable small examples require a nontrivial local-to-global argument, and they provide a new structural base case for further deficit and alphabet-size questions. This is not a mere restatement of the extremal bound or an arbitrary numerical sample.

## Limitations and closest literature

The general-alphabet, larger-deficiency and other Hamming-distance cases are unproved. The primary full text was inspected at the theorem and relevant proof; the 2006 quasigroup source was compared through its definitions and main classification setting. Historical priority remains qualified. Finite verification is supplementary, not a substitute for proof. No independent review is asserted.

Self-review: passed. Independent audit: not yet performed.
