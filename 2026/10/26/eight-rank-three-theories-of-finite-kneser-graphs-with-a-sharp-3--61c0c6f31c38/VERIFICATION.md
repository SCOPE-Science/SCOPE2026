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

# Reproducibility and verification

Execute `python3 verify_kneser.py` in a directory containing this script. It uses only Python standard-library modules. Its deterministic output is reproduced in `verification_output.txt`.

The script enumerates each small Kneser graph from its combinatorial definition and computes the full first-order rank-three type by atomic diagrams of ordered triples and recursive existential-extension sets, with equality and repeated vertices handled explicitly. This exact semantic recurrence is independent of the theorem's analytic parameter thresholds. Separately, it evaluates eight explicit rank-at-most-three graph properties and compares them with the proposed classification. The test matrix contains 33 parameter pairs from all eight classes, with up to 126 vertices, and confirms that all eight canonical representatives have distinct complete rank-three types and distinct separating-property vectors.

The finite checks do not by themselves establish the infinite theorem. The proof for every \(1\le k\le n\) uses vertex transitivity and exact intersection counting. The inaccessible historical literature risk is described separately. No independent scientific audit or external validation has been performed.
