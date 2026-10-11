---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

There are 64 upper-triangular binary 3 by 3 matrices. Exactly the eight matrices with all three diagonal entries equal to one are units; in a finite ring every other element is a zero-divisor, leaving 55 nonzero standard vertices. Independent brute-force multiplication verified a nonzero one-sided annihilator for every such vertex, tested AB=0 or BA=0 on all 1485 unordered pairs to obtain 420 edges, and exact BFS from every vertex gave diameter two. The current 2025 source text independently confirms that its host retains only 27 matrices.

## originality

PASS

General finite-ring facts make the 55-vertex count elementary once the standard convention is fixed, so that count alone is not claimed as a new theorem. The source-specific diagnosis and the corrected standard host's exact 420-edge and diameter-two census are not stated in the inspected matrix-ring literature or the 2025 article. The latter instead explicitly constructs a 27-vertex host after starting from the same 64-element ring. No independent correction or exact standard-host census was located.

## value

PASS

Although the corrected vertex count is elementary, the finding repairs the host graph underlying published metric-dimension claims and supplies the basic edge and diameter census for the standard object. That is a substantive reproducibility correction with direct consequences for any invariant claimed for T3(F2).

The dated certificate retains the supplied scientific assessment, sources and limitations.
