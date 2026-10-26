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
# Reproducibility and limits

Execute `python3 verify.py` in a fresh Python 3 environment. It computes every Apéry residue by an independent shortest-path algorithm for all integral parameters \(2\le b\le17\), then checks the claimed analytic Apéry, genus, Frobenius, pseudo-Frobenius and recurrence reduction formulas. It also checks the supporting coin-count shift inequality on three complete multiplicity ranges per base.

The computation is finite and is not relied on as proof of unbounded parameter or index assertions. The algebraic proof is presented separately in `RESULT.md`. Independent mathematical validation remains unperformed.
