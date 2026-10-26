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

# Reproduction and mathematical limits

Execute `python3 verify.py`. The program requires only Python's standard library and prints `VERIFY_OK` after all assertions.

Its prime-field checks enumerate every pair of images of the two standard generators of \(\operatorname{UT}_3(\mathbb F_p)\) for \(p=3,5,7\), use the explicit group multiplication to test idempotence, and count actual image sizes. The resulting histograms are \(\{1:1,3:36,27:1\}\), \(\{1:1,5:150,125:1\}\), and \(\{1:1,7:392,343:1\}\). These are boundary-calibration cases, not a claim of novelty for prime fields.

In the nonprime field \(\mathbb F_9=\mathbb F_3[\xi]/(\xi^2+1)\), the program constructs and deduplicates all projections onto \(\mathbb F_3\)-subspaces of \(\mathbb F_9\)-lines. It gets \(1080\) rank-one projections and \(810\) rank-two projections and thus \(9720\) and \(65610\) nontrivial proper retractions after central-coordinate choices. It also directly verifies 20,000 multiplication-preservation and idempotence instances for sampled maps using field arithmetic.

The exact formulas for arbitrary \(p,e\), the absence of other retracts, the normality restriction, and the limiting distribution are established by the proof in `RESULT.md`. The enumerations are not exhaustive over all extension-field group maps, and no computational result is claimed as an independent audit.
