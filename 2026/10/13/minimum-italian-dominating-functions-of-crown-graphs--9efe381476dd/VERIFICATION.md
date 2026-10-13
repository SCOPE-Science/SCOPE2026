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

The proof uses the exact crown-graph neighborhood identity: for a zero vertex \(a_i\), feasibility is equivalent to \(W_B-f(b_i)\ge2\), and for a zero vertex \(b_i\), feasibility is equivalent to \(W_A-f(a_i)\ge2\).

The accompanying `verify.py` enumerates every labeling with labels in \(\{0,1,2\}\) and total weight at most \(4\) for \(3\le n\le12\). For each labeling it compares the direct graph-neighborhood test with the side-weight identity. It then checks the claimed minimum weight, checks that every minimum labeling belongs to the stated family, and checks conversely that every stated family member is feasible and minimum.

Replay output:

`VERIFY_OK n_range=3..12 low_weight_labelings=62067 lemma_checks=62067 classification_checks=358 expected_form_checks=358 max_order=24`

The finite replay does not establish the theorem for unbounded \(n\); that quantification is supplied by the symbolic proof in `RESULT.md`.
