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

The proof's universal steps are the exact SPD Schur complement, the strict eigenvalue upper bound, the two unit-vector inequalities for all positive scalings, bounded near-minimizers for the sharp asymptotic infimum, and the spectral-similarity argument. No finite numerical test substitutes for them.

The rational witness takes \(\varepsilon=1/4\), \(\delta=1/65536\). It has Schur complement \(7/8\). If \(\alpha\le1/64\), the second-unit-vector gain is at least \(65/64\); if \(\alpha>1/64\), the first-unit-vector gain is larger than one.

The included `check.py` (Python 3, NumPy) was executed against its packaged source. It confirms exact rational identities, samples 575 scaling cases for safe Type II versus unsafe Type III, and performs 8,000 parameter scans showing convergence of the observed best norm toward \(\sqrt{17}/4\) at \(\varepsilon=1/4\). The finite scans are diagnostic, not an exhaustive or independent proof.
