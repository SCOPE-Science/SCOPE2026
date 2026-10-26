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

The standalone verifier is `verify.py`; its exact recorded output is `verify_output.txt`. Execute `python3 verify.py` using Python 3 and the standard library. The program enumerates all \(7+28+84=119\) capped posets, computes both recursive and explicitly unrolled rank-three signatures, compares the two equivalence partitions, checks all listed merger groups, and computes the minimum-size representative in each class. It also checks ten instances with component lengths above seven.

The mathematical basis of the computation is the proved back-and-forth characterization of the Hintikka recursion. The infinite-family result additionally uses the proved three-round linear-order cutoff and disjoint-component strategy; no finite sampling replaces these arguments. No rank-four, unbounded-component, or independent validation claim is made.
