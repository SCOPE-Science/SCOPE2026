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

Run `python verify.py` with the pinned minimum dependencies from `requirements.txt`. The actual executed script printed: `VERIFY_OK 40 exact beta identities; 1500 eigenvector and residual identities; 11 asymptotic checks; 1235 budget monotonic checks; 90000 Monte Carlo samples; 200 power trajectories`.

The exact-rational Beta(a,a) binomial-tail examples and independent eigensystem checks support the closed-form identities; the standardized chi-square limit, Stirling expansion and the global assertions remain proved by the analytic argument in `RESULT.md`, not by sampling. Near-degenerate sketch-size estimates are finite numerical corroboration of the asymptotic claim. No independently performed audit or independent scientific certification is represented.
