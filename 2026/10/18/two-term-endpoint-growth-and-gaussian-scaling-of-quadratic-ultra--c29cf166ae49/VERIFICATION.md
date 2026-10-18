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

# Verification details

The file `check.py` requires Python 3.10 or later and the `mpmath` package. Run `python check.py` after extracting this file and the checker from the same finding. It independently checks exact rational beta-moment reproduction, the endpoint integral between the exact kernel zeros, two-term asymptotic numerical comparisons, and Hermite rescaling. The recorded execution returned `PASS 168 assertions`.

The finite checks do not establish the theorem for all real parameters. The global sharp constant, eventual maximizing-point rigidity, weighted-density asymptotic, and perturbation of absolute-value integrals are proved analytically in `RESULT.md`. The two inaccessible older Fourier-projection full texts remain an originality limitation; no independent audit has occurred.
