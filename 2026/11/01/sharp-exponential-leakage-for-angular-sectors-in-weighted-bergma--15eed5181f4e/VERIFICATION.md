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

# Verification and limitations

The analytical argument in `RESULT.md` first invokes the established normalized Mellin multiplier, then proves unique nondegenerate frequency balancing using separated positive pairwise integrals. Uniform Laplace estimates give the sharp two-tail coefficient and maximizing-frequency drift. This establishes the statement for all fixed \(0<a<b<\pi\) and all \(\lambda>-1\) for uniqueness, and \(\lambda\to\infty\) for the asymptotics.

Run `python checks/sector_leakage_check.py` with SciPy installed. The checker evaluates the exact symmetric coefficients, numerical optimizing-frequency crossings and finite-weight leakage in four sectors over four weight values. It successfully passed 89 finite assertions. These computations test formulas and normalizations but cannot certify an infinite limit, novelty, or historical priority. Independent mathematical review has not been performed.
