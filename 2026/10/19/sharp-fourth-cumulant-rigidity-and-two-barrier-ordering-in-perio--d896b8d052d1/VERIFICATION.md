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

# Computational and analytical verification

Install SymPy (specified in `requirements.txt`) and run `python verify.py` in the directory containing the files. The independent finite-state check differentiates the full tilted generator perturbatively, solving exact-rational Poisson equations; it does not substitute a specially arranged determinant for the computation being checked. The script checks 42 heterogeneous profiles for \(3\le n\le8\), five homogeneous profiles, 90 cyclic primitive-energy identities for \(3\le n\le12\), and 240 two-defect comparisons for \(3\le n\le18\). These checks were executed with all assertions passing.

Infinite-period universality follows instead from the determinant-winding identity, the cycle rooted-forest expansion, and the exact discrete summation-by-parts identity detailed in `RESULT.md`. The sharp upper constant is reached only as a singular limit of positive-rate models; all finite positive-rate instances obey the strict inequality. The software does not prove that no historical paper contains an equivalent theorem, and the relevant 1990 disordered-walk paper's full body was not available for comparison.
