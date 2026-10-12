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

The displayed analytic proof, not the computer program, establishes the existence and invariance of the interval for all sufficiently small radii under the general assumptions, and for every radius through one on the concrete witness. The exact derivatives, monotonicity, and strong-convexity inequalities can be checked by elementary differentiation and Taylor expansion.

Run \(\texttt{python verify.py}\) with Python 3 and its standard library from the extracted package directory. It bisects the shifted central-difference root and tests both direction signs, several positive sampling radii, multiple points within the absorbing interval, and several relative-smoothness parameters. Its output confirms only those finite checks; the numerical tests neither prove the general theorem nor establish publication priority. The first public CARS preprint was posted on 2021-09-27; the full-text algorithm checked was its later arXiv manuscript version.
