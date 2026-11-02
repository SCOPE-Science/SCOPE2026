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

# Exact checks and proof boundaries

Run `python3 verify.py` with the Python standard library. The program enumerates 120 permutations of the five residues and verifies they produce six distinct projective directions. It separately enumerates the projective plane over \(\mathbf F_5\) to compare the six solutions, checks that the quadratic is nonsingular, and computes the evaluation ranks \(1,3,5,6,6\) for homogeneous degrees \(0\) through \(4\).

The general geometric assertion over an algebraic closure is obtained from reducedness and the length-six plane complete intersection, not from sampling. The conductor and delta invariant use the homogeneous-coordinate Hilbert series and normalization along the six lines; the Picard scheme is computed through the normalization exact sequence for unit sheaves and truncated logarithm (valid because the relevant nilpotence is three and the characteristic is five). These geometric arguments, supplied in `RESULT.md`, are necessary in addition to the executable checks.

The check does not prove historical uniqueness or determine the stable reduction after base change. Such independent validation has not been performed.
