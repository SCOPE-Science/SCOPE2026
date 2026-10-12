# Review

## Correctness

PASS. The source's Section 3 reduction uses one fixed proposition vocabulary and one fixed initial epistemic state. Its final goal formula is fixed, while the PCP instance appears only in the family of \(\mathrm{add}_i\) event models; the remaining three actions are fixed. Theorem 3.19 proves exact equivalence between PCP matches and plans. All event preconditions have modal depth at most \(1\), and there are no postconditions.

The restricted problem is recursively enumerable because finite action sequences can be enumerated and each successive finite product update and final fixed-goal check is decidable. Binary PCP is \(\Sigma^0_1\)-complete, so the reduction yields the matching hardness bound.

## Originality

PASS. Achilleos states undecidability of the modal-depth-one/no-postcondition problem but does not formulate the stronger fixed-initial-state/fixed-goal restriction or the exact \(\Sigma^0_1\)-completeness classification. The earlier small-instance theorem of Lê Cong--Pinchinat--Schwarzentruber fixes the action repertoire and goal but leaves the initial state as the varying input, so it is complementary rather than covering.

Candidate-specific database and literature searches for fixed initial states, fixed goals, fixed vocabularies, and action-only input in epistemic planning did not locate the accepted theorem.

## Value

PASS. Parameter localization is central in the undecidability literature for epistemic planning: earlier work explicitly asks which parts of a planning instance must remain unbounded. The theorem shows that, in the newly settled depth-one/no-postcondition regime, neither the epistemic starting situation nor the target formula needs to encode the hard instance. All computational universality can be concentrated in the action library. The exact \(\Sigma^0_1\)-classification further identifies the computability degree rather than merely undecidability.

## Closest literature and limitations

Achilleos (2026) supplies the reduction. Lê Cong--Pinchinat--Schwarzentruber (2018) is the closest parameter-bounding result and proves the complementary fixed-action/varying-initial-state phenomenon over two-agent \(S5\).

The number and size of actions remain unbounded, and no vocabulary minimality is claimed.

Self-review: passed. Independent audit: not yet performed.
