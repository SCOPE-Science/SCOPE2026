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

The general theorem is proved by identifying the algebra automorphism group with an affine semilinear group, then determining affine and Frobenius-semilinear conjugacy orbits by slope, norm, and trace.

Run `python3 check_semiaffine.py` in the directory containing this file and the attached standalone checker. The checker exhaustively constructs finite quadratic extensions and both groups involved in the proof: the binary quadratic-form similitudes and the affine semilinear group. It independently enumerates all inner-conjugacy orbits and every involution for \(q=3,5,7,9\); the final line is `ALL_EXACT_CHECKS_PASSED` when the checks succeed. The test for \(q=9\) is a nonprime-base-field check. No random samples, floating-point approximations or outside datasets are used.

Finite experiments alone do not prove formulas for arbitrarily large fields. The proof in `RESULT.md` supplies the required unrestricted finite-field arguments. No independent audit has been performed.
