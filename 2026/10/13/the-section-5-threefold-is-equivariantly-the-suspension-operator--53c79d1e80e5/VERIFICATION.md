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

The exact source relations are
\[
u_1v-y_1y_2=0,\qquad u_2v-(y_1+1)y_2=0,\qquad u_1(y_1+1)-u_2y_1=0.
\]
The verifier checks that their differences give \((u_2-u_1)v-y_2=0\), that the third relation equals \(u_1-y_1(u_2-u_1)=0\), and that the proposed parametrization annihilates all defining equations. It then computes a Gröbner basis of the source ideal and reduces each inverse-composition identity to zero.

The replay was run with SymPy 1.14.0 against the packaged `verify.py`; the captured output begins `VERIFY_OK`.

The proof does not rely on finite sampling. It is an exact polynomial identity argument valid over every field. The only unproved limit is bibliographic: an unindexed later correction could affect originality, not the algebraic correctness of the displayed coordinate change.
