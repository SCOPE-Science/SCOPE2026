# Scientific assessment

## Correctness — PASS

The equality statement follows from strict discrete concavity and the fixed sum of cyclic window counts; an explicit periodic floor-difference construction attains the balanced bound. For width three, the sparse and intermediate cases exhaust all binary circular words, respectively by minority separation and alternating runs of lengths one or two, leading to the stated formulas. The exact-integer standalone verifier exhausts n<=12 for all widths and n<=18 for width three, and is corroborative rather than an infinite proof.

The proof covers every integer \(n\ge3\), \(1\le d\le n\), and \(0\le k\le n\), with explicitly named strict-concavity assumptions and boundary cases. Harmonic PAV satisfies the hypotheses. The exact count uses labeled rather than rotation-equivalence committees. Finite tests support, but are not substituted for, the proof.

## Originality — PASS, with residual risk

Ai 2026 classifies general PAV optimal-set complexity but does not give a cyclic equal-window characterization or formula; Janeczko–Faliszewski 2023 establishes counting hardness for general ballots. Lassota–Sornat and Avramidis et al. establish structured-domain winner determination but not these exact optimal-set counts. Actual semantic record queries gave no equal or stronger theorem; the two nearest own claims concern three-party apportionment and reverse sequential deletion. The source text inspected and residual risks are recorded separately. Classical balanced word and run-counting methods are acknowledged as ingredients.

The closest specific public sources are Ai (2026), https://arxiv.org/abs/2609.08884; Janeczko and Faliszewski (2023), https://arxiv.org/abs/2305.01769; Lassota and Sornat (2026), https://arxiv.org/abs/2607.28575; and Avramidis et al. (2026), https://arxiv.org/abs/2605.03067. The Manurangsi–Sornat 2026 abstract (https://arxiv.org/abs/2604.05953) was available, not its full paper text, so earlier implicit coverage cannot be ruled out. Standard binary-word arguments are proof ingredients, not separately claimed discoveries. Relevant mathematical-record searches returned no equivalent statement, which does not establish absolute priority.

## Value — PASS

Optimal-set counting under PAV is broadly hard and important for tie-breaking. In a natural maximally symmetric circular-local approval family, the result determines every winning committee and its common exact score for every strictly concave Thiele rule, plus a closed-form number of ties at width three. At twelve candidates and six seats, 174 co-optimal committees demonstrate meaningful multiwinner ambiguity, and the family with n=6m and k=3m has at least 3 times binomial(2m,m) squared co-optima, growing exponentially; this is not an arbitrary single-profile calculation.

The result gives an infinite family with a closed winner-set characterization, exact score and binomial-sum tie count. It concerns a structurally motivated circular election model, not an arbitrary restriction of a general counting problem. Its limitations are uniform window length and one ballot per cyclic position; it does not cover arbitrary circle-interval elections.

Self-review: passed. Independent audit: not yet performed.
