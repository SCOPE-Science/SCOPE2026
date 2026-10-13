---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof uses the exact support criterion
\[
f(a_i)=\varnothing\Rightarrow B_1\setminus\{i\}\ne\varnothing\text{ and }B_2\setminus\{i\}\ne\varnothing,
\]
with the symmetric condition for empty \(b_i\). The standalone checker constructs the crown adjacency relation directly, evaluates the literal 2-rainbow definition, independently evaluates this criterion, and compares every feasible weight-four labeling with the structural classifier.

For \(3\le n\le12\), it enumerates every labeling of total weight at most four, which is enough to test both the lower bound and every claimed minimum family. For \(n=3\) and \(n=4\), it additionally enumerates the complete state space of all \(4^{2n}\) labelings and recomputes the minimum weight and its multiplicity from scratch.

Run command:

`python3 verify_2rainbow_crown.py`

Observed output:

`VERIFY_OK n_range=3..12 low_weight_labelings=619907 criterion_checks=619907 minimum_class_checks=1263 count_checks=10 full_small_checks=69632 max_order=24`

The computation proves only the tested finite ranges. The all-\(n\) theorem is established by the symbolic proof in `RESULT.md`.
