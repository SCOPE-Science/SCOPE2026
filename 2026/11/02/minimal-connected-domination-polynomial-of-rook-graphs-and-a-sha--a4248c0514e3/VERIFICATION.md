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

Run `python3 verify_rook_minimal_connected_domination.py` with Python 3.10 or newer; it uses only the standard library. The verifier performs exhaustive adjacency-based tests of domination and induced connectivity, checks every single-deletion minimality condition, compares all coefficients against the closed Stirling formula for 17 ordered small rectangles, and separately enumerates all surjective words of length at most six to corroborate the Prüfer factor.

Observed output begins `VERIFY_OK: 17 graph orders; 1444991 nonempty subsets; Prüfer surjection checks through length 6`. The full output prints five sample exact polynomials. This computational result is independently recomputable from the embedded source and was not obtained by assuming the structural characterization while deciding graph feasibility.

Finite exhaustive checks do not certify infinitely many parameter choices, do not prove publication priority, and are not an independent audit. The infinite result follows from the written mathematical proof, including the Prüfer encoding and the minimality equivalence.
