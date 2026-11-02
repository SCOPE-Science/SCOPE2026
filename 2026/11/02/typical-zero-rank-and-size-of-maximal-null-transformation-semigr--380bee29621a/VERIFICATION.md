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

# Reproduction and scope

With Python 3 installed, run `python verify.py` from a directory containing the extracted standalone verifier. No third-party packages or additional data files are required.

The program enumerates every transformation on ground sets of one through four points. For every idempotent candidate zero it tests the square and two-sided-zero conditions; compatibility pairs are checked by actual function composition in both orders. Maximal cliques in the resulting compatibility graph are exactly the maximal null subsemigroups with that zero. Their zero-rank and order spectra are compared with the independent set-partition recurrence. First and second order moments are also checked, and published total counts through ten points are matched by exact integer recurrence.

Expected completion marker: `VERIFY_OK`. The direct census covers only the displayed finite dimensions. The asymptotic claims are established by the mathematical argument in `RESULT.md`, not by enumeration or simulation.

## Boundaries

No independent audit has been performed. Verification is reproducibility support, not a formal proof certificate. Publicly available structural literature on maximal null transformation semigroups supplies the classification input; the conditioned-Poisson and decorated-block arguments supply the new asymptotic deductions.
