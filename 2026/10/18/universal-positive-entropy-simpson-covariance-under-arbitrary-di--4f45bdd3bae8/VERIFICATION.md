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

# Reproducible verification and limits

Run `python verify.py` in an environment with Python 3.10+, `numpy` and `scipy` to reproduce 266 passing checks. The script obtains \(\operatorname{Cov}(H,Q)\) independently from separate \(\mathbb EH\), \(\mathbb EQ\), and \(\mathbb EHQ\) gamma-integral derivatives using rational harmonic-number arithmetic for small integer Dirichlet parameters, and compares the outcome with the closed-form theorem. It also performs numerical beta-quadrature on noninteger parameters, verifies the symmetric closed form, checks a deterministic nonordering example and samples asymmetric Dirichlet vectors.

This is a verification of nontrivial algebra and some numerical instances. Proof for every admissible dimension and parameter vector rests on the gamma-moment identity and weighted digamma association; simulation and finite tests are not proof for infinitely many parameters. The material has received self-review only, not independent external validation.
