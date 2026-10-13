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
The standalone `verify.py` constructs the displayed natural basis algebra, verifies all basis multiplication and ideal inclusions, evaluates sample scalar products, and computes the predicted bilinear restriction ranks in characteristic two. Independently tested fields are \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\); tested radical dimensions are respectively \(1\)–\(4\), \(1\)–\(2\), and \(1\). It terminates with `VERIFY_OK`. The general lower bound is the symbolic dimension-of-kernel plus rank-of-restriction argument in `RESULT.md`, not an inference from these cases. No external or independent audit was performed.
