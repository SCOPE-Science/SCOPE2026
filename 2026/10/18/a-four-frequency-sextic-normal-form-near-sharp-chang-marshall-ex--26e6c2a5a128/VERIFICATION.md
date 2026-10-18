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

Run `python3 verify.py` with SymPy installed. It generates the full constant Fourier coefficient of the exponential through weighted degree six, computes the logarithmic series and normalizing square root, and checks as symbolic identities both the quartic perfect square and the sextic coefficient \(2(\lambda-\lambda_m)^2/m+1/(24m)\). It also verifies the leading sextic coefficient is positive for sample positive integral orders. The executed checker returned:

`VERIFY_OK exact Fourier expansion; unique quartic cancellation; sharp four-mode sextic coefficient 1/(24m)`

The analytic argument in `RESULT.md` gives the universal proof for every positive integral order. The script is a supplementary exact identity check; it does not establish novelty, independent validation, or an unrestricted stability inequality. The checked expression only concerns the explicitly normalized four-mode jet family.
