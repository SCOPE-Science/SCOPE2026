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

# Verification of exact two-proxy pivotality

Run `python CHECK.py` alongside the other files. It enumerates every underlying binary proxy vote and every direct/delegation choice of all leaves for the listed finite \(m\) and rational \(p\), then compares against **separately implemented** closed expressions. It also checks envelope monotonicity, sharpness at \(p=1\), symmetry at \(p=0\), and numerical consistency of the central-binomial asymptotic.

The exact probability enumeration checks the counterfactuals directly; it does not use the binomial derivation. The algebraic proof in RESULT.md, rather than any finite enumeration, establishes the theorem for all odd positive numbers of delegators, the whole continuous parameter interval, and its uniform asymptotic limit. The status in the front matter records that no independent external audit was conducted.
