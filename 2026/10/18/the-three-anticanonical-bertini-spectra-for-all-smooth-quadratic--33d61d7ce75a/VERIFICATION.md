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

Exact source-level checks performed: the complete finite coefficient census (`quadric_p4.cpp`), the 720-element orthogonal stabilizer and five pencil-orbit representatives (`orbits.cpp`), the Jacobian/Gröbner geometrically smooth versus singular test for each of 31 rational hyperplanes of all five orbit representatives (`hyperplanes.py`), and independent surface Jacobian/rational-line tests (`independent_geometry.py`). The output is transcribed in `EXPECTED.txt`. Enumerative proofs are finite and exact; no bounded extension-field point tests substitute for geometric smoothness. Limits: only the specified binary quadratic pencils and rational hyperplanes were tested. Independent audit has not been performed.
