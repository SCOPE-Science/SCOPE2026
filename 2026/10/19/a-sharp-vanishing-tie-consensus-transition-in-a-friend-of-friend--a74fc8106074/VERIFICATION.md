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
# Reproduction and verification

The theorem is proved in `RESULT.md`; the code `verify_foaf_threshold.py` is a supplementary consistency check, not a general proof.

1. Execute `python verify_foaf_threshold.py` using Python 3; install NumPy and SciPy to enable the optional full-ODE integrations.
2. The exact rational section checks the edge identity and both comparison inequalities for sizes \(2\le N\le8\), including the critical parameter, and performs 10,080 exact comparisons.
3. The independent numerical integrator checks nine complete-system examples across subcritical, critical and supercritical parameter regimes for \(N=2,3,5\), including the exact two-agent critical solution.
4. Infinite-time classifications, the general connected-graph time change, and uniqueness of the subcritical limiting profile are proved by deterministic comparison and transition-matrix arguments, not inferred from numerical limits.

**Scope and limitations.** The verification program samples finitely many matrices and initial conditions and cannot certify all real inputs. The proof requires exact FOAF equations, constant positive response, symmetric weights and unit diagonal. Publication priority and any extensions require further research.
