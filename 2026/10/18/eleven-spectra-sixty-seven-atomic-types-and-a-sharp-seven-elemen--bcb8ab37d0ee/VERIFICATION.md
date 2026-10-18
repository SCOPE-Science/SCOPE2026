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

# Reproduction and limits

Run `python3 verify_two_noun.py` with Python 3 and no external packages. The expected terminal marker is `TWO_NOUN_CARDINALITY_VERIFY_OK`.

The checker constructs every four-cell integer vector of total size 1 through 18. It evaluates all 64 ordered atomic statements directly, separately constructs the support/sign invariant, and verifies that these induce exactly the same 67 partitions. It checks minimum representative counts `4,6,16,9,20,4,8` for sizes 1 through 7. It independently tests ten explicit atomic theories against their asserted finite-tail spectra through size 18, including the six- and seven-element boundary cases.

The infinite theorem rests on the cell decomposition, the two-difference hyperplane arrangement, the bounded integer representative construction, and Jiang's published spectrum theorem; no finite enumeration is offered as an infinite proof. Original-source comparison is limited by the unavailable full text of Moss (2016). All program outputs are same-package reproducibility checks and not independent mathematical certification.
