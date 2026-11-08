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

The characteristic-two symbolic verifier `verify.py` and its actual stdout `verification_output.txt` accompany this statement. It checks the universal polar-kernel equation, the six partial derivatives, smooth strict-transform equations in all three standard blowup charts, and the dimension-one Frobenius–Euler cokernel spanned by the cubic \(DEF\). It enumerates projective conic-discriminant points and exceptional incidence points over finite fields of cardinalities \(2\), \(4\), and \(8\); the recorded result ends with `ALL_COHOMOLOGY_CHECKS_PASSED`.

The script uses Python 3 and SymPy for symbolic reductions modulo two; its finite-field arithmetic and enumeration are standalone. The exact output is from execution of the enclosed script. Finite tests do not prove the all-field result: the bundle exact sequences, regularity criterion, blowup discrepancy calculation, and cohomological obstruction in `RESULT.md` are the general proofs. There is no independent mathematical audit.
