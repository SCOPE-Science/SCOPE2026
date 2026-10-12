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

The proof is symbolic and field-uniform. Its critical steps are: the rank-one determinant update; the adjugate coefficient identity for a trace-one cubic; the identification of vectors with a fixed annihilator \(h\mid f\) with units of \(\mathbb F_q[X]/(h)\); and the two recurrence simplifications that give \(s^3=0\) in degree two and \(c_1^3=0\) in degree one. No finite computation is used to infer the universal statement.

The bundled `verify.py` performs a separate finite check. It enumerates every rank-one idempotent in \(M_3(\mathbb F_p)\) and every coefficient pair \((c_0,c_1)\) for \(p\in\{2,3,5,7\}\), tests \((C_f-E)^3=0\) directly, and independently computes the polynomial Euler totients by gcd counting. A successful run ends with `VERIFY_OK`.

The computation does not enumerate extension fields, and it does not count idempotents of ranks other than one. Those are explicit limits of the computational check, not of the proved rank-one theorem.
