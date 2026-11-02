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

# Reproducibility checks and limits

Run `python3 verify.py` with a Python 3 standard-library interpreter. The verifier constructs the original bipartite graph and directly checks every vertex subset for connected domination for \(3\le n\le7\). It compares the resulting set sizes with the all-CDS polynomial, independently identifies all inclusion-minimal configurations, enumerates token exchanges, and compares breadth-first-search distances from every state to the exact metric and the complete five-coefficient ordered-pair polynomial. No external data, randomness, or third-party dependencies are required. A passing execution terminates with `VERIFY_OK`.

The exhaustive verifier checks only these finite cases. The published proof uses an explicit structural characterization, Johnson common-neighbor counts, and finite case-split geodesic constructions that apply to every integer \(n\ge3\). The three-step adjacent-swap route is necessary because both shortest two-step orders collide. Prior publication of the scalar connected-domination minimum and its configuration count is credited; independent audit and exhaustive publication-priority validation have not been performed.
