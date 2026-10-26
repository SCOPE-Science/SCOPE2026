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

Run `python3 verify_gap.py` using Python 3 standard library with this file's companion proof. The checker verifies the rational branch identities exactly for \(2\le m\le6\), tests the radical-branch constraints for 493 values, independently assembles 30 full weighted Laplacians and compares their spectra, and examines 1600 additional sampled feasible symmetric allocations. Its standard successful output begins `PASS: exact rational identities`.

The proof of the optimal value for all \(n\ge3\) is analytic in `RESULT.md`; finite testing does not constitute exhaustive verification of the infinite theorem. The reduction to general nonsymmetric allocations uses concavity, not sampled asymmetries. No independent audit or external validation has been performed.
