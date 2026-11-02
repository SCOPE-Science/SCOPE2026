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
# Verification record

The algebraic proof treats all applicable odd finite fields and all nonzero constant shifts. `verify_mobius.py` is standalone and uses finite-field coefficient tables and polynomial root multiplicities rather than the discriminant-character reduction. Execute it with `python3 verify_mobius.py` from the same directory. It reports `VERIFY_OK fields 10 shift_cases 130`, including fields of orders \(9\), \(25\), and \(27\). The negative-control orders \(7\), \(13\), and \(25\) have nonzero correlations for some shifts. Root multiplicity detection is complete for cubics: a repeated factor of a cubic must contain a repeated linear factor. The checks constitute finite corroboration, not a proof for infinitely many fields. No external or independent review has been performed.
