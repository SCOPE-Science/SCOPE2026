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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 standard library. It checks exact partition-number formulas, multiple moduli and residue subsets, and small overpartition counts through an independently computed generating function; a successful run ends with `VERIFY_OK`.

The infinite theorem is established mathematically by the exact compulsory-part deletion bijection, the uniform Hardy–Ramanujan ratio for shifts of order \(\sqrt n\), and the continuous-mapping theorem. The finite verifier is an implementation cross-check only; it does not exhaust infinite parameter ranges. The modulus remains fixed.
