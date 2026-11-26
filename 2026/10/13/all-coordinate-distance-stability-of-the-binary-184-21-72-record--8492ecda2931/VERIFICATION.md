---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The four factors of h, f_2, and all 14 ordered five-bit patterns match Appendix A. Its generator row j uses bit c_{j mod 5} of the printed c_0…c_4, so the reconstruction has the correct tail orientation. The first block (bg of degree <85) embeds the message space, proving dimension 21. A fresh census (`python3 /workspace/branches/r4-census.py`) used coefficientwise polynomial division, cyclic shifts and split-message XOR enumeration, not the supplied Gray-code checker. It enumerated exactly 2,097,152 distinct messages including zero, reproduced the frozen weight distribution and gave weight 72 first among the nonzero words, with 9,826 occurrences. The incidence histogram was {2108:1,2346:2,2482:2,2516:3,2550:6,3940:17,3956:17,3958:102,3968:34}, summing with multiplicities to 707,472. Thus every coordinate is both hit and missed by a minimum word. A hit yields punctured weight 71, and every weight decreases by at most one; no unit word is in C, so dimension stays 21. A miss yields shortened weight 72, and restricting to zero there is a codimension-one kernel since the coordinate is hit. Omitting that zero coordinate is weight preserving, giving [183,20,72]. Unequal incidences rule out a 1-design. This is exhaustive only for the specified finite code and single-coordinate operations.

## originality

PASS

The construction, minimum distance, and count 9,826 are prior work and rechecked here as identity/census controls. The distinct finding is the exact coordinate-incidence histogram with uniform exact distance behavior for all single-coordinate punctures and shortenings. The prior tables checked do not supply that information. The bare non-1-design conclusion is already forced by nonintegral mean incidence 72·9826/184 and is not independent novelty.

## value

PASS

For this explicit high-distance construction, the relevant question is whether selecting a coordinate for an elementary code modification can affect the resulting exact distance. The census certifies there is no such choice for either one-coordinate operation, despite materially different replication counts. The histogram provides the actual one-point minimum-shell data rather than just rechecking the construction or observing the arithmetic obstruction to a 1-design. It does not imply optimality of the resulting parameters or stability for multiple operations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
