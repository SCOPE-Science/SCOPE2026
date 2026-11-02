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

# Verification and limits

The analytical certificate is the four-step proof in `RESULT.md`: (1) the exact branch-conditioned recursion; (2) a uniform conditional \(L^2\) bound on all late martingale innovations; (3) the product limit for both finite and infinite \(\varepsilon_N\log N\); (4) coupling a fixed initial time segment to a classical Pólya urn and then increasing that segment length. The rigorous convergence result is not inferred from numerical enumeration.

Running `python checker.py` with the Python standard library produces `checker_output.txt` and terminates with `ALL_ASSERTIONS_PASSED 3439`. The code validates finite exact-rational transition and moment formulas for several parameters, balanced-recursion consistency, and numerically compares three large finite-row examples to their predicted limiting means and variances. The latter convergence is logarithmically slow, so these are deliberately loose diagnostics, not certified error bounds. No general symbolic proof package or independent external validation is provided.

Scientific limits: fixed positive initial masses, integer nonnegative additions with \(c,b>0\), rowwise Bernoulli rule probability \(\varepsilon_N\to0\), and endpoint weak convergence. General stochastic-approximation priority and quantitative rates remain unchecked.
