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

# Exact mathematical checks

Run `python verify.py` with Python 3 and SymPy. The committed output is `verify_output.txt`, which ends with `VERIFY_OK`. The script verifies the explicit affine equation and singular point, Hessian rank three, determinant eight of the three transverse directions, polynomial identities for the section parameterized by \(v\), and exact reduction of the residual function to \(-3v^5(v-1)^{11}\).

The verification is limited to the exact identities needed by the proof. Formal analytic equivalence follows from the stated parameter-dependent Morse lemma and admissible unit changes; it is not inferred from finite-field enumeration. The inverse formal substitution \(x_1=3v^5\) is valid at \(v=1\) because its derivative is nonzero modulo eleven. The independent audit has not been performed.
