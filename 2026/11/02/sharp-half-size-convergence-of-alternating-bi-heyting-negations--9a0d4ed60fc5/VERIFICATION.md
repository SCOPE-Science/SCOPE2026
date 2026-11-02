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

# Reproducibility

The standalone `checker.py` uses Python 3 and the standard library. It implements Heyting negation via downward closure, then co-Heyting supplementation via upward closure, and implements the common-lower-bound graph separately. It checks both routes at every upset of every natural-label-compatible poset on up to six elements, including redundant encodings of isomorphic posets. It checks the sharp height-two family for sizes from two through one hundred and one. The expected terminal marker is `ALL_CHECKS_OK`.

The symbolic proof, not the finite checker, establishes the theorem for arbitrary finite carriers. The strongest checkable evidence is the matching of the two separately implemented operations on all finite test cases and the extremal constructions. External independent audit and historical priority certification have not been performed.
