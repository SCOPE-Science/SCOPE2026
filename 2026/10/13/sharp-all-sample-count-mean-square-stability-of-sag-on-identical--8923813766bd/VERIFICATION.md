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

The supplementary symbolic reductions implemented in `verify.py` reconstruct the four conditional second-moment columns rather than entering the claimed stability threshold as a premise. They check for symbolic positive integer \(n\) and symbolic positive \(s\) that \(\det(I-T)=-2s(s-2)/n^3\); they verify the precise energy drift, its positive principal minors and rational exact tests for selected concrete memory lengths. This is not a proof by finite enumeration. Full quantified justification is the analytic argument in `RESULT.md`.

Run `python -m pip install -r requirements.txt` and `python verify.py`. Success prints `VERIFY_OK`. The checker tests algebraic identities with SymPy; the scientific review is same-model only, not independent external validation.
