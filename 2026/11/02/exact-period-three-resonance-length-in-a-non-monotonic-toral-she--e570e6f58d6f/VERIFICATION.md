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

# Reproducible checks

Run `python3 verify_resonance.py` using Python 3.11 or later. No external dependencies or data files are required. The checker uses exact rational arithmetic for all 512 branch/wrap cells of the third iterate, computes full affine return constraints, and checks the twelve positive-length itinerary segments, the six maximal connected straight components, and their two exact squared-length histograms. It checks that four rank-zero identity cells have only boundary singleton feasible sets, that segment interiors have no double counting, and that their midpoints are genuinely period three. Independently multiplying the four symbolic itinerary matrices yields the determinant factors displayed in RESULT.md; these show that no other parameter in the stated range admits a nonisolated third-iterate fixed locus. The finite enumeration is exhaustive by the stated piecewise-affine cell partition, not an infinite-time numerical simulation. No independent audit or external validation has been performed.
