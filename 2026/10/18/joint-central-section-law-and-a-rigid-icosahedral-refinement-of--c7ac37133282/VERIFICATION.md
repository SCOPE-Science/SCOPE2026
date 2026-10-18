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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and the standard library; expect `EXACT_DUAL_CHAMBER_ENUMERATION_OK`, the exact `(V,E,F)` triples `(90,180,92)`, `(30,60,32)`, `(90,240,152)`, and joint count dictionary `((6,10):60), ((6,12):20), ((8,10):60), ((10,10):12)`. The executable is included alongside this document; it does not require a network or third-party mathematical package.

The checker verifies: regular vertex sets and both 30-edge graphs by exact squared lengths; zero-cross comparisons and exact incidence tests in integer pairs representing the golden-ratio ring; strict sign realizability of each spherical chamber mask and independent Euler cell totals; cut-edge section counts for all 152 chambers and each individual marginal; and every D/I single-chamber exterior turning-angle algebraic cosine multiset from all weakly feasible circle-pair intersections. The final four probabilities are evaluated numerically as an additional normalization test, while their exact evaluation follows algebraically from Gauss–Bonnet and the certified angle multisets.

Finite exhaustive sign enumeration is valid because every full-dimensional sign chamber contains sectors adjacent to arrangement vertices and unique feasible sign vectors define disjoint convex chambers; Euler's independent equality establishes none omitted. The continuum of random orientations is handled by spherical area, not sampled directions. No independent audit, external theorem verification, or definitive historical-priority certification has been performed.
