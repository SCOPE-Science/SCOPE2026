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
# Verification procedure

Execute `python3 verify.py` in the directory containing the script. The checks use integer arithmetic and modular exponents: the stated Fourier multiplication rule, orbit closures under doubling/negation, the scalar-compatibility equations, exhaustive centralizer permutations for cyclic sizes at most nine, exact prime-order count formulas through thirty-one, and a non-quandle-induced algebra automorphism of order thirty-three for the eleven-point dihedral quandle. On success, the final line begins `VERIFY_OK`. The full group classification follows from the symbolic proof in `RESULT.md`; these finite tests are supplementary and do not establish the general theorem by enumeration.

The automorphism formulas assume coefficients in the complex numbers, and only odd-order finite abelian underlying groups are covered. No independent audit or formal proof assistant check is claimed.
