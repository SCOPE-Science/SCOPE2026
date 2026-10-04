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

The proof was checked symbolically from the stated PolyakEG update. For \(F(x)=LJ(x-x_\star)\) with \(J^T=-J\) and \(J^TJ=I\), the identities \(J^2=-I\), \(\langle v,Jv\rangle=0\), and \(\|Jv\|=\|v\|\) yield the displayed projection step-size and update matrix directly.

`artifacts/verify_skew_isometry.py` replays the canonical \(2\times2\) quarter-turn case in exact rational arithmetic at several rational scaled steps and checks the finite product identity. Its expected terminal line is `VERIFY_OK`.

The computation does not certify non-isometric-skew cases, which are outside the claim. It also does not establish originality; literature comparison is reported separately in `REVIEW.md` and `AUDIT.json`.
