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

The theorem was checked symbolically against its proof steps and replayed by `verify_square_bias.py` over all regular integer pairs with \(0<|P|\le80\), \(0<|Q|\le500\), and positive square discriminant. The script computes the recurrence terms and the first positive-Kronecker prime occurrence using only Python's standard library. A successful run prints `VERIFY_OK`.

The finite check is corroborative only; the infinite statement is established by the proof in `RESULT.md`.
