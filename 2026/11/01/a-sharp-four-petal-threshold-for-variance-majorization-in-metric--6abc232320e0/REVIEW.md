# Review of the metric-flower variance-majorization theorem

## Correctness — PASS

For two points on one loop, the shortest arc is uniform on half the loop; for different loops the distance is a sum of independent uniform half-loop distances. The conditional first and second moments give the displayed symmetric polynomials. The pair-transfer gradient identities and the nonnegative inequalities prove the raw-second-moment Schur result and the exact three-versus-four petal variance threshold. The four-petal counterexample has exact positive rational lengths and a strictly negative rational variance difference; the higher-petal extension uses continuity from an explicit differential coefficient. Exact checks reproduce 21,844 conditional-moment identities and the interpolated three-petal gradient identity. These tests are auxiliary to the analytic proof.

## Originality — PASS, with a stated historical limitation

Doyle–Graver (1982) introduced continuous mean distance for shapes, not a demonstrated variance-majorization theorem. Garijo–Márquez–Silveira (arXiv:2103.11676) treats continuous first-moment computation. Baptista–Kennedy–Mugnolo (arXiv:2312.04952) explicitly supplies the flower mean and its equal-length minimizer; that first moment is not original here. Their open-access analysis of flower graphs (Example 4.3 and Lemma 4.4) does not give the displayed second-moment polynomial, the centered variance comparison, or the four-petal boundary. Semantic result-record searches for petals, bouquets, shortest-path distance variance, Schur majorization, and second moments returned no covering equivalent in the closest inspected records. The longer 1982 full text was not accessible, and unindexed prior work remains a risk; the search is not a priority certificate.

## Mathematical value — PASS

Mean distance and second raw moment are natural measures of network transport scale; centered variance quantifies trip-to-trip variability. The theorem identifies the **exact topological threshold** at which variance ceases to respond monotonically to balancing while the second raw moment remains monotonically improved. An explicit rational four-petal counterexample shows that the two raw moments can increase while variance decreases under the same majorization step. The parameter is natural (number of loops), not a hand-picked finite case, and the statement is complete within this symmetric-topology class.

## Scope and remaining risk

The result concerns metric flowers and arclength-uniform point pairs, not Euclidean straight-line distance, unrelated network classes, or global variance optimizers for four or more petals. The 1982 historical full text remains inaccessible. No independent validation or priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
