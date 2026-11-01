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

# Reproducible checks

Run `python checks/verify.py` with Python 3, NumPy and SciPy. Its direct calculations solve \(2u=hB^\top W\sin(Bu)\) for \(h\) slightly above the exact spectral boundary, compute \(J_h(u)\), check the normalized square-root branch amplitude and transverse contraction, and iterate at \(h=h_*\) to compare \(t\|u_t\|^2\) with \(3\lambda/(2S_4)\). Output is deterministic and independent of any external data. Explicit unweighted \(K_{2,3}\) values are verified by rational identities.

All graphs in the computation are finite samples, and root solvers give numerical—not exhaustive—checks. The global exclusion at all graph sizes, the local analytic branch and the critical decay constant are supported by the exact analytical argument in RESULT.md. This verification is not an independent audit.
