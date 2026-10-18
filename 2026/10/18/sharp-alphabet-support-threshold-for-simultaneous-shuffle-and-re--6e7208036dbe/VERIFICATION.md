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

# Verification and reproducibility

Run `python verify_joint_shuffle_support.py` in the directory containing this document and the checker. No third-party libraries or external files are required.

The checker enumerates all Catalan non-nesting matchings and all permutations without an increasing triple for half-lengths from one through eight, confirms the characterizations directly on those configurations, computes alternating-union component counts, and compares the complete component histogram with independently stored expected finite values. It checks 2,248,355 pairs. It also explicitly tests the palindromic construction and enumerates all binary and ternary words of length up to eight having even letter multiplicities, testing the two subsequence-partition properties directly. Even multiplicity is a necessary condition for either property, not a substitute for exhaustive checking of remaining candidates.

The expected program completion marker is `JOINT_SHUFFLE_SUPPORT_PASS`; a failure raises an assertion. The source proof is combinatorial and covers all \(n\ge1\), while the checker is finite and establishes no infinite implication by itself. The alphabet-growth statement is an exponent assertion only, not an exact enumerator.
