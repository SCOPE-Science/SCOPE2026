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

The analytical proof establishes the two complete global stable separatrix branches, their backward finite-time endpoints, and the leading radius–height–angle profiles. The key ingredients are a forward radial barrier, the exact Jacobian and divergence, Poincaré–Bendixson recurrence exclusion, a backward radial barrier, and a comparison inequality \(dr/d\tau\ge c_\mu r^5\) at large radius. The boundary coefficients are derived by integration of \(r^{-4}\), \(z\), and \(\theta\), not inferred from numerics.

Run `python verify.py` (SymPy, NumPy, SciPy required) to reproduce exact symbolic checks of the reduced vector field and noncertifying integrations from eight stable-branch seeds. A radius-100 crossing is only a finite stress test and cannot by itself establish an infinite blow-up, its finite endpoint, or global basin topology.

The motivating source's statement about separatrix basin partition for its illustrated parameter is fully acknowledged as prior description. Independent audit and independent validation have not been performed.
