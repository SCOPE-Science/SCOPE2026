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

The accompanying `check_two_site.py` uses only the Python standard library and exact integer/Fraction arithmetic. Running `python3 check_two_site.py` enumerates 81, 625, 6,561, and 28,561 parameter quadruples on success-probability grids of meshes \(1/2\), \(1/4\), \(1/8\), and \(1/12\), totaling 35,828 cases. It verifies both the pooled-mean-sensitive bound and the \(8/9\) homogeneous-product ratio bound. Four rational sharpness examples give respective ratios \(16/15\), \(80/87\), \(800/897\), and \(8000/8997\). The program is a reproducibility supplement; finite verification does not establish an inequality on an infinite continuum.

The universal proof is self-contained in RESULT.md. The critical steps are the exact two-site iid distance; total-variation contraction under coordinate marginalization; an atom-event lower bound; the two-case argument for signed marginal differences; and the explicit quadratic extremum \((2-w)(1+w)\le9/4\). Its scope is exactly two independent Bernoulli coordinates, for all parameter values in \([0,1]\).

The scientific comparison cites the primary source containing the sharpness example and the published conjecture, together with the later general-alphabet theorem. No independent mathematical audit or independent validation is claimed.
