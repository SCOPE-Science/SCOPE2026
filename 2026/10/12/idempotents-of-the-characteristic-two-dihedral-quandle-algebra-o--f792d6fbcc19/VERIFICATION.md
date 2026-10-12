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

Run `python3 verify.py` in a folder containing the included file. The checker uses the standard Python library only and reports `VERIFY_OK` after verifying the exact eight formal residual-polynomial identities in a six-variable polynomial ring over \(\mathbb F_2\) and enumerating all \(2^8\) and \(4^8\) coefficient tuples over \(\mathbb F_2\), \(\mathbb F_4\).

The complete predicted and enumerated idempotent sets are checked equal, with counts \(33\) and \(257\), and the downstairs quotient idempotent counts are as checked as \(9\) and \(33\). The four nonzero downstairs lift fibers have \(q^3\) elements each and zero has one lift. Symbolic polynomial verification supports the displayed coefficient calculations; the written proof supplies the field-uniform logical steps. This checker does not attempt to establish novelty or provide independent validation.
