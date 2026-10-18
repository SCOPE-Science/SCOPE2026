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

# Verification procedure and limits

Run `python3 verify.py` from the directory containing this file. The script implements direct arithmetic in prime fields and nonsplit quadratic extensions, enumerates every ordered pair of inverse-square-curve points, and compares every representation count with the elliptic-trace formula. The expected complete execution ends with `VERIFICATION_OK`; the exact observed output is embedded in `verification_output.txt`.

Prime tests: \(5,7,11,13,17,19,23,29,31,37,41\). Extension tests: \(25,49,121,169\). The extension code obtains the least quadratic nonresidue of the prime subfield, constructs the irreducible quadratic field, and directly implements its multiplication and inversion without numerical approximations. The proof, not this finite list of checks, establishes the theorem for all prime powers of characteristic at least five.

The fourfold-fiber cutoff follows from the displayed exact small-field calculations and Hasse's bound beyond those fields. No externally independent audit or infinite computational certification has been performed.
