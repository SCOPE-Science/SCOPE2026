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

The supplied `verify.py` uses only exact integer bit arithmetic and the Python standard library. It reconstructs the polynomial monomial-collision map for dimensions 1 through 8 and both possible normalized endpoints, where defined. It separately enumerates all binary matrices for dimensions two and three and computes the square-root Hankel ranks by Gaussian elimination over GF(2). It confirms that three specific matrices generate all 16 and all 512 binary matrices, respectively, and checks a six-by-six binary-alphabet witness minor. The exact output is included in `verification_output.txt`.

Run with `python3 verify.py` in a directory containing this program; no additional inputs are required. The program terminates with an exception if a check fails and otherwise prints `ALL CHECKS PASS`.

The proof of the all-dimension statement relies on the symbolic monomial-basis argument and elementary generation of the full matrix monoid; the finite verifier is independent cross-check evidence, not an exhaustive test of infinitely many dimensions. No independent external audit has occurred.
