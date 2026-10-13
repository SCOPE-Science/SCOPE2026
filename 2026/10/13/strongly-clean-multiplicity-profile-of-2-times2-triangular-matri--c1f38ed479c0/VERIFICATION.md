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

The proof was checked directly from the defining equations for a triangular idempotent. There are four diagonal idempotent types. The two equal types force zero off-diagonal entry. Each mixed type leaves one off-diagonal variable and commutation with \(A\) reduces to a single linear equation. The unit condition for \(A-E\) depends only on its diagonal, so the elementwise formula follows without any unproved classification input.

`verify.py` independently enumerates all elements and idempotents in \(T_2(\mathbb F_q)\) for \(q=2,3,5,7\). For every element it computes the strongly clean fiber directly, checks the formula, and compares the complete multiplicity histogram with the theorem. A successful replay prints `VERIFY_OK` together with one summary line for each field.

The enumeration is a finite consistency check only. The theorem for arbitrary prime powers is established by the symbolic proof, not extrapolated from the tested fields.
