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

The finite verifier `verify.py` directly enumerates all chains of the Boolean rank-selection model for 90 conjugacy classes across six parameter pairs and compares oriented fixed-chain Lefschetz traces with the cycle-weight formula. In addition, a separately implemented symmetric-function Pieri expansion checks 25 ribbon identities. Run with `python3 verify.py` (Python standard library only). Expected terminal markers: `VERIFY_OK 90`, `RIBBON_OK 25`.

The general mathematical claim uses the proofs in `RESULT.md` (especially the involution-fixed-chain bijections); finite checks do not justify universal quantifiers on their own. Integral splitting and independent scientific validation are not claimed.
