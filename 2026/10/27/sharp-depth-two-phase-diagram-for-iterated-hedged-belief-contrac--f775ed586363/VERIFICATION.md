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

The standalone `checker.py` enumerates exactly the \(2^{n^2+n}\) finite labelled relation/valuation pairs for each \(n=1,2,3,4\), evaluating each of the four formulas after every relation update until the first fixed point. All sixteen maximum comparisons with the theorem pass, including the exceptional small sizes. The script then checks the directed path, directed cycle, clone-based three-world construction, and two-world witness at each size from 3 through 35.

Enumeration is exhaustive **only** at \(n\le4\). The bounds for arbitrarily many worlds are proved using the monotone support-set and global-falsifier arguments in `RESULT.md`. The use of an arbitrary accessibility relation is essential; equivalence relations are not assumed. Independent external verification and priority certification have not been performed.
