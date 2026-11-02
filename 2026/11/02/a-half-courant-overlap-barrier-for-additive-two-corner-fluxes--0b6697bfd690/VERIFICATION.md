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

The continuum proof reduces the two-dimensional conservation law to two exact contact transports, then measures the overlap of their finite-face influence intervals. An inclusion-exclusion identity and one-dimensional exact integration give the full flux for every horizon in the stated range. The hyperbolicity and characteristic bound are proved analytically, not inferred from sampled eigenvalues.

Run `python3 verify.py` (standard-library Python 3). Exact rational tests use an independent spatial partition and integrate the face flux directly in time, split at the contact-intersection point. The checker performs 10,500 comparisons, and independently confirms the sharp rational example and the Courant inequality. The tests are finite and do not prove the continuum theorem by themselves.

Scope: no floating-point robustness, full finite-volume scheme stability, entropy admissibility of general multidimensional weak solutions, or independent mathematical validation is established here. The exhibited solution is explicitly transported and obtained as a limit of smooth data.
