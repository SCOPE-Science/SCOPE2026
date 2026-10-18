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

# Verification notes

The analytic proof uses the exact first-symbol mass equation, the standard two-term Euler--Maclaurin asymptotic for a Hurwitz-zeta tail, uniform Taylor expansion across complete branch-plus-gap cells, and a coupling with a genuinely independent digit sequence. This is a mathematical proof for every fixed real parameter in the stated open ranges.

`verify_endpoint.py` is standalone except for Python 3 and `mpmath` 1.3 or later. It reconstructs the distribution function by recursively locating the coded branch, checks the normalized pressure equation and its root, compares the scaled correction against its sharp predicted profile, and tests the shrinking-threshold mass for two representative parameter pairs. Run it with `python verify_endpoint.py`.

The diagnostic run passed for \((q,\lambda)=(2,0.4)\) and \((3,0.7)\), covering twelve cell positions at four increasing indices, six threshold-mass checks, and two pressure-root identities. The iterations terminate for these examples. Numerics cannot establish the all-parameter asymptotic law or an independent originality determination; those claims rest on proof and literature comparisons.
