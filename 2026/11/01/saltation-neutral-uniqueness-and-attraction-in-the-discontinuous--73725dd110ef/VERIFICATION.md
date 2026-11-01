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

# Exact verification and limits
Run `python check_chazy_q1.py` after installing `sympy`. This diagnostic checks the exact \(q=1\) half-space first-integral conservation, divergence, scaling, seam normal continuity, saltation determinants, negative-energy seam constraint and inversion identity. It reports PASS for each side and both crossing directions. Global cycle existence is supplied by the theorem of Llibre–Novaes–Valls (2023); uniqueness and stability require the analytic proof in RESULT.md. An exact symbolic test is not a proof of global dynamics, literature originality, or independent mathematical validation.
