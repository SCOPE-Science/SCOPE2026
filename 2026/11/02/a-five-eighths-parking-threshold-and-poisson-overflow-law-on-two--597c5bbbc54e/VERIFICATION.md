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

# Verification and reproducing checks

Run `python CHECKER.py` from the folder containing this file. The script uses Python 3 and only standard-library modules.

The program performs exhaustive direct sequential processing on all \(50{,}549\) preference sequences for \(b=2\) and \(b=3\) at the specified small car counts and checks equality against an independently formulated bottom-up flux recursion. The code also prints deterministic, seeded Monte Carlo estimates for moderate \(b\), which display slow finite-size convergence; this is consistent with the analytic \(O_t(b^{-1/4})\) bound in the Poissonized model. Such simulations cannot prove the infinite-size limit.

The proof's noncomputational checks are the bound \(\Pr(G_b^c)=O_t(b^{-1/4})\), the parent collision probability \(b\Pr(B_i\ge2)\to t^4/8\), independent Poissonization across parents, and a monotone Poisson-sandwich argument for fixed car counts. All hypotheses and limits are stated in `RESULT.md`.

This verification does not constitute an independent audit or external certification.
