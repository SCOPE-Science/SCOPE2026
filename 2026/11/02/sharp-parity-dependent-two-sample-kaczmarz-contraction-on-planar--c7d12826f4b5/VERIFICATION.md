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

Run `python verify_pairwise_skm.py` using standard Python 3.9+; no other dependencies or external data are needed. The reference output produced from the bundled script is:

`VERIFY_OK: m=3..74, 7200 angular probes, even parity gaps, odd ties, and large-m limits`

The check explicitly computes all unordered row pairs over 72 frame sizes, evaluates the two aligned/bisector candidates and additional angles, confirms parity-dependent minima numerically, and checks the uniformly sampled one-row baseline. Separately, the result's analytic proof derives the exact finite-sum formulas, excludes off-grid minima by strict concavity, proves the equality cases, and establishes the large-size limit. Neither numerical sampling of angles nor finite enumeration establishes a universal mathematical claim without that proof.

No independent scientific validation was performed. Publication priority remains qualified by the possibility of unlocated specialized equivalent results.
