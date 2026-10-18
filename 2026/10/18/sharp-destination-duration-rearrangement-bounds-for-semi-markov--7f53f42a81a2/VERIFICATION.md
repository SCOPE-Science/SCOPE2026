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

# Reproduction notes

Run `python3 verify.py` using only the Python standard library. In the recorded execution it returned `PASS: 1954 exact rational checks over 216 couplings`. It also printed the exact means and the extremal variance vectors for a three-transient-state feedback network, and checked the continuous-uniform three-state illustration: common mean \(3/2\), minimum variance \(1/12\), independent-kernel variance \(7/12\), maximum variance \(13/12\).

The finite verifier exhausts destination assignments for the specified four-atom feedback network only. The proof for all finite transient graphs, arbitrary positive holding-time laws with finite second moments, and all allowed dependent exit kernels uses the regenerative moment equations and the two-marginal quantile rearrangement inequality in `RESULT.md`. No external certification or independent audit is reported.
