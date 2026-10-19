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

Execute `python verify.py` after extracting the package; it requires NumPy and SciPy. The script checks four centered-Wishart matrix identities, rank-one integral and saddle constants for several sketch sizes, exact chi-square sign/clipping values, and 48,000 Gaussian sketch pairs for a large effective-rank family with nonconstant singular values. Independent Gaussian draws are generated using seed `240924`. Assertions are deliberately approximate for Monte Carlo evidence. Proofs of the universal effective-rank limit, uniform-integrability clipping passage, and sharp large-sketch asymptotics are analytical; a finite simulation cannot certify them.
