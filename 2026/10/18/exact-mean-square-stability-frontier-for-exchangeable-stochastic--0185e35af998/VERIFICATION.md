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

# Verification

The executable `verify.py` uses standard-library exact rational arithmetic to independently evaluate both the full Itô second-moment lift and the two-coordinate exchangeable reduction. Running `python verify.py` completed 84 exact lift identities and 632 independent trace/determinant comparisons. It also proved by exact rational arithmetic that the explicit \(s=2\) witness is Hurwitz while the printed source inequality fails; the two nontrivial covariance eigenvalues are \((-8\pm2\sqrt{13})/9\).

The infinite-time theorem is proved analytically in `RESULT.md` by positive-semidefinite moment order, not by exhaustive simulation or these finite tests. Boundary equality and arbitrary species count are handled by the same exact two-coordinate spectral reduction. No nonlinear extinction, full-system stationarity, or independent external theorem certification has been tested or claimed.
