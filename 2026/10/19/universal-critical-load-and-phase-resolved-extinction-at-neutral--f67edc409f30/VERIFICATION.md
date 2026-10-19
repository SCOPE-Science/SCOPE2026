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

# Reproducible finite checks

The executable `checks/pulse_critical_check.py` uses NumPy and SciPy; run it using `python checks/pulse_critical_check.py`. It computes the resident pulse-map fixed point and the positive period integral \(I\), verifies neutral growth-pulse balance to machine precision, and integrates 2,800 seasons of the full two-population system. In the illustrative two-pulse model it returns \(I\approx0.797417250742\), maximum tested cyclic log-ratio identity error \(5.05\times10^{-11}\), final \(nJ_n\approx1.00004209\), and final \(nz_nI\approx0.99997223\). The last values demonstrate numerical approach to one but do not imply the infinite-time theorem.

Proof-based checks also verify that the resident reciprocal monodromy contracts when \(P e^{\int r}>1\), that exact invasion neutrality cancels the pulse-growth contribution to \(z_{n+1}/z_n\), that uniform within-season bounds support the zero-limit contradiction, and that the inverse-ratio increments converge to \(I\). All arguments are contained in `RESULT.md`; no outside proof assistant or external certificate was used.

Limits: finite numerical checks are not exhaustive; classical sources can contain unrecognized equivalent statements; independent audit has not been performed.
