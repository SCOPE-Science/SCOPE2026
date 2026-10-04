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

The general theorem is proved analytically in `RESULT.md`. Brown--Hoshino's full path proof was inspected at the lower-bound formulas, the protected-gap induction, the upper-bound theorem, and the final complete classification. The directed upper argument keeps their available-room inequalities but fixes the sign of short displacements and the side of endpoint-gap responses.

The executable replay is an independent finite check, not the source of the infinite theorem. It exactly solves the q-round game for every \(1\le n\le m\le17\) and \(1\le q\le4\), using exhaustive minimax over partial bijections; this includes the complete finite boundary proof that \(\vec P_7\not\equiv_3\vec P_8\). Expected output:

`VERIFY_OK cases=612 states=814707 boundary_7_8=spoiler`

Limits: the replay does not certify arbitrary q. The analytic protected-gap argument supplies that part. Independent external audit has not been performed.
