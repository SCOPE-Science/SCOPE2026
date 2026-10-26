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

The exact post-release peak equation is \(a/\delta-a/(T+\delta)=p\log(1+T/\delta)+kT\), for \(p=3/2\), \(a>0\), \(k\ge0\), and \(T>0\). In the proof, the peak is bracketed between the end of release and one impulse-mode time later. The transformed equation for \(z=a/(p\delta)\) has an additive residual bounded by \(2a/(pT)\), independent of uptake rate. This residual and inversion of \(z-\log z\) are the crucial analytical checks.

Run `python verification.py`; it uses only the Python standard library and evaluates explicitly stated parameter sets. The executable reports `PASS` when all assertions succeed. Its bisection checks are finite tests and do not constitute a proof for continuous parameter ranges. The asymptotic theorem is proved in RESULT.md and assumes the idealized diffusion model; no finite-geometry, heterogeneous-uptake, or independent-audit claim is made.
