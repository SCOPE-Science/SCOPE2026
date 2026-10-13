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
The standalone `verification/verify_mersenne.py` checks that the four prime squares \(3^2,5^2,7^2,11^2\) respectively divide \(2^6-1,2^{20}-1,2^{21}-1,2^{110}-1\). It exhaustively computes the periodic union over \(4620\) residue classes and agrees with the independent inclusion-exclusion proof.

Exact output is embedded as `verification/verification_output.txt`. The checker uses no nonstandard dependency and can be run with `python3 verification/verify_mersenne.py`.

Limits: this verifies arithmetic for the four selected periods, not an exhaustive list of all possible square-divisibility periods and not the exact density of the full set. The infinite lower bound follows from periodic containment proved in `RESULT.md`.
