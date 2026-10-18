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

# Verification record

The included standalone `verify.py` reconstructs the section polynomial from exact signed-orthant integrals and compares the independently integrated polar volume with the formula obtained from diagonal-slab probabilities. It requires only the Python standard library. The actual embedded program was extracted and executed, returning `PASS 117 exact-rational checks`.

The analytic proof, not the finite program, establishes the universal identities for every integer \(n\ge2\), every real \(\lambda\ge0\), strictness for \(n\ge3\), and both limits. The endpoint constant agrees with an existing anchored Lipschitz-free volume product computation [3], and is not an independent novelty claim. No additional or independent audit has been performed.

References: [1] arXiv:2305.08500; [2] arXiv:2206.12234; [3] arXiv:1911.10642; [4] arXiv:1212.2544.
