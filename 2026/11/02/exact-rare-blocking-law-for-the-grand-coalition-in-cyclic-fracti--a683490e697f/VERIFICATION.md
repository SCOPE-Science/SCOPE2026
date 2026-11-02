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

The bundled `verify_cycle_core.py` uses only exact integer arithmetic for the direct-utility and combinatorial counts. It checks every nonempty deviating subset for \(3\le n\le18\), verifies the run formula independently using the characteristic-polynomial recurrence for \(3\le n\le150\), and prints illustrative ratios for \(n=400,401,1000,1001\). The direct test compares \(n d_S(i)>2|S|\) for every selected agent and thus tests strict inequalities, including ties at the cutoff. All 16 direct tests and 148 matrix tests passed.

The recurrence comes from \(F(\lambda,z)=\lambda(\lambda-1)(\lambda-z)-z^2\) with trace initial values \(3\), \(1+z\), and \(1+z^2\); all arithmetic in coefficient comparisons is exact. The asymptotic constants are established by the local spectral and Fourier argument in RESULT.md, not by the finite numerical ratios. The verifier does not establish literature priority, independence, or external certification.
