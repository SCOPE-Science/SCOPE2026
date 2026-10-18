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

The self-contained program `verify.py` constructs the incidence relation without using the formula being verified. It exhausts the four-subset candidates for \((q,d)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\), checks unique attributes and geometric classification, and exhausts five-subsets for those parameter cases. It also tests a deterministic prefix of \(25,000\) four-subsets for \((q,d)=(3,4)\); that prefix is not exhaustive and does not certify the unrestricted claim. Run `python verify.py`. The all-parameter result depends on the mathematical proof, not finite enumeration. Independent audit: not performed.
