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

# Computational and analytic verification

The exact normalized radial function is \(r_\rho(\theta)=-R\cos\theta+\sqrt{\rho^2-R^2\sin^2\theta}\), with \(R=\sec(\pi/(2n))/2\) and \(\rho=1-t\). The proof uses exact integration over symmetric angular sectors and the standard planar convex Cheeger inner-parallel-area characterization.

Run `python check_cheeger.py` with SymPy and mpmath installed. The script tests the exact rational Taylor coefficients and the first disk-area deficit symbolically, and evaluates roots of the exact area equation to 60 decimal digits for odd orders \(3,5,7,9,15,31,101,401\). Execution yields `EXACT_SYMBOLIC_CHECKS_PASSED`. The 60-digit finite checks do not establish asymptotic validity for all odd orders. Uniform analyticity and the nonzero implicit derivative in the proof supply that step.

An independent scientific audit has not been performed. The priority assessment relies on the cited accessible scientific material and acknowledges an inaccessible closely related 2026 paper.
