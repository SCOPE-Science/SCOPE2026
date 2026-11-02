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

The bundled `CHECKER.py` reconstructs the complete graph and all 36,069 augmented independent sets. It tests all 218,036 oriented Hasse cover relations and a topological ordering after reversing 18,024 matching pairs, recovers the 9 critical three-cells and 12 critical four-cells, constructs the signed 12-by-9 integral Morse boundary by recursive elimination, checks exact Smith factors 1,1,1,1,1,1,0,0,0, and enumerates all rotation-invariant oriented simplices for each of six nonidentity powers. The expected status line is `C7_K4_ROTATION_INTEGRAL_MORSE_OK`.

Requirements: Python 3 and SymPy. Reproduce with `python CHECKER.py`; it makes no network requests and uses integer exact arithmetic. The mathematical proof explains why the Morse certificate, Lefschetz calculation and rational representation constraints establish the integral action and rational quotient claim. This same-source computation is not an independent scientific audit.
