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

# Reproducibility and limitations

Run `python3 verify_derangement_context.py` with the standard Python 3 interpreter. The supplied program enumerates all matching premises for \(3\le n\le7\), constructs every derangement directly, and intersects their occupied cell sets to compute Galois closures. It compares each closure with the proposed structural theorem and the closed-intent count obtained by inclusion-exclusion. For \(n=4\), it additionally checks closure for every one of the \(2^{12}\) attribute subsets. It tests the indicated symmetry generators and repeated forward chaining with the proposed Horn rules for small sizes.

Recorded successful output:

```text
CASE n=3 derangements=2 partial_matchings=18 two_hole=0 concepts=4 PASS
CASE n=4 derangements=9 partial_matchings=108 two_hole=12 concepts=35 PASS
CASE n=5 derangements=44 partial_matchings=780 two_hole=120 concepts=316 PASS
CASE n=6 derangements=265 partial_matchings=6600 two_hole=1260 concepts=3292 PASS
CASE n=7 derangements=1854 partial_matchings=63840 two_hole=13440 concepts=36954 PASS
VERIFY_OK exact_closures=PASS inclusion_exclusion=PASS two_hole_boundary=PASS automorphism_generators=PASS horn_forward_chaining=PASS n=3..7
```

Finite enumerations are neither a proof for all \(n\) nor a proof of originality. The all-order Hall argument, classification, line-graph reconstruction and optimal-premise lower bound are given in RESULT.md. Scientific publication priority and independent audit remain unperformed.
