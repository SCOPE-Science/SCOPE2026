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

# Reproducibility and scope

Run `python checker.py` using only Python's standard library (Python 3.9+). It produces `PASS; exact rational identities checked: 158` after comparing exact Fourier-recursion coefficients with direct independent integration of all branches in several rational parameter examples. It also checks \(C_n(b,p)=C_n(b,1-p)\) at the tested finite lags, \(C_0(b,p)=1/12\), and \(C_1(b,p)=1/(12b)\).

The full all-lag identity, infinite summed covariance and nonuniform critical parameter limit are **analytical**, using an exact operator resolvent, nonnegative-series boundary evaluation, a reflection-principle path count and uniform binomial asymptotics. The finite checker is not an exhaustive proof of infinitely many cases. The calculation covers the stationary single-coordinate annealed process with matched integer bases and uniform inverse branches; neither the program nor the proof provides results for other observables or for two-particle correlations. Independent validation has not been performed.
