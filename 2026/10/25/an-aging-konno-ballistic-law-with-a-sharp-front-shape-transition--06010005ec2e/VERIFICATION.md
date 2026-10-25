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

# Reproducibility checks and limits

Run `python verification.py` with Python 3, NumPy and SciPy. It independently implements the position-space weighted three-state Grover coin, its shift, the finite lattice quantum amplitudes up to 650 steps, and the renewal mass/survival recurrence. It also evaluates the limiting one-dimensional density by endpoint-aware Gaussian quadrature rather than assuming the weak limit numerically.

The run completed with `PASS 18 analytic-edge/center and independent finite-walk comparisons`. At \(\ell=2\), \(\alpha=0.3\), and \(t=650\), the scaled second moment was \(0.17489691377678718\), versus the proposed limiting coefficient \(0.1742714651940042\). Tests also checked probability normalization, four scaled CDF values (tolerance 0.006) and both exact endpoint coefficients for each \(\alpha\in\{0.3,0.5,0.7\}\) at two approach distances. The tolerated finite-time discrepancies are expected and are not claimed to be certified error estimates.

Critical analytic inputs separately reconstructed in the proof are the renewal-age beta density (including its normalization and finite-endpoint tightness), the flat-band orthogonality of the stated coin, the normalized group-velocity density, the transformed product integral, and the two endpoint beta integrals. These establish the limiting statement; the finite computations only check selected instances. There is no independent audit, formal proof assistant output, or external validation certificate.
