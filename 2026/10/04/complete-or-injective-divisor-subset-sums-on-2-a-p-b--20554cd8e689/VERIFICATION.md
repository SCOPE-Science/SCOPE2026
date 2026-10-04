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

The proof is symbolic and covers every parameter in the stated range. Its two critical checks are: (1) the translated intervals at successive \(p\)-power layers overlap when \(p\le2^{a+1}\); and (2) every layer coefficient is less than \(p\) when \(p>2^{a+1}\), so ordinary base-\(p\) uniqueness applies.

The accompanying `verify.py` independently enumerates small cases, constructs all sums of distinct divisors, and checks the coverage or injectivity conclusion together with the exact cardinality and deficit formula. This finite replay is corroborative and is not treated as proof of the infinite theorem.

Scientific limitation: the argument depends on the fact that subsets of \(\{1,2,\ldots,2^a\}\) have unique consecutive sums \(0,\ldots,2^{a+1}-1\). No claim is made for arbitrary initial factors.
