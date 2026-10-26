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

The theorem is established algebraically from the exact policy-update rule. The critical identities are the closed form for downstream odds, telescoping downstream value products, the upstream odds ratio, and the adjacent-difference sign formula. The exact turning index follows from an integer logarithmic inequality with equality handled separately; no numerical root finding is used to prove it.

The independent rational checker `checker.py` uses the standard-library `fractions.Fraction` type, assembles both state-value functions afresh at each iteration, and compares direct updates against the closed form. It checked 26,460 parameter/iteration combinations and 744 iterates of the integer-indexed family. Exact equality assertions, including the two-index minimum, require no floating-point tolerance. Run `python3 checker.py` in the directory containing this file and compare to `checker_output.txt`.

Finite recurrence tests do not establish uniqueness of an infinite-time behavior; the written proof covers all \(k\ge0\), all allowed parameters, and the asymptotic regime. The formula for the minimum has a bounded integer-rounding factor and no claim of a universal normalized limit. No sampled-policy behavior, arbitrary-MDP generalization, or independent audit is certified.
