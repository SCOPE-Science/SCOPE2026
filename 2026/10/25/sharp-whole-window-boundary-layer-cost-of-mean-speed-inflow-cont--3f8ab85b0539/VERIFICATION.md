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

The proof in `RESULT.md` uses exact conditional least-squares projection and a uniform asymptotic decomposition. To independently check the integrals and selected finite-width instances, run `python3 verify_boundary.py`. This script requires only Python 3 standard-library modules and has no remote dependencies. Its paired output is embedded as `verification_output.txt`.

Exact rational integration gives \(1/6\) for the ordinary proxy and \(1/12\) for the clipped proxy on **each** endpoint strip. Summing the two strips yields \(1/3\) and \(1/6\), respectively. Midpoint quadrature at two positive mean speeds approaches these constants as the velocity half-width shrinks.

The finite experiments do not prove uniformity in \(\varepsilon\), infinite limits or novelty; those assertions rely on the proof and cited literature comparisons. The formula is proved only under the stated smooth affine-demand and uniform-velocity assumptions.
