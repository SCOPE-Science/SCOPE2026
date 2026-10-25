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

# Reproducibility and verification

Run `python verify.py` with Python 3, NumPy, and SymPy. The program symbolically verifies the equality witness Gram spectrum and the two-by-two characteristic polynomial, checks the critical coupling threshold algebraically, and reconstructs the general sketched Ritz formula for one thousand randomly generated SPD matrices with random bounded-distortion sketch metrics. It also checks three sharp positive-imaginary-part examples. The successful output begins with `VERIFY_OK`.

These computational checks substantiate the derivations but do not exhaust all real symmetric matrices or all embeddings. The proof in `RESULT.md` covers the universal quantifiers. The independent-audit channel has not been performed.
