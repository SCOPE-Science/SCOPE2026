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

The only required program is `verify.py`; run `python3 verify.py` using Python 3.8 or later. No packages or network access are needed.

The program constructs all 4,096 possible pairs of seven-bit boundaries with prescribed first/last bits and rejects each pair if a prefix and suffix match at an overlap length between one and seven. It computes the corresponding Galois closure on subsets of the 64 prefixes. The lectic NextClosure successor enumerates each closed set exactly once. For each it computes the product of the closed-prefix cardinality and the cardinality of the common compatible-suffix set.

Expected k-seven certificate: exactly 1,944 formal concepts and maximum product 744. The program also checks the published 24-by-31 construction directly, reruns the dual relation with sides reversed, verifies the established maxima 64 and 216 at cutoffs five and six, and directly enumerates all 65,536 prefix subsets at cutoff five to cross-check the closed-set enumeration method. It ends with `VERIFY_OK` on success.

This finite exhaustive computation certifies the 64-by-64 compatibility optimum, conditional on the transparent code's correctness. The accompanying mathematical proof justifies the reduction to this finite problem and applies to every word length at least fourteen. No external human or independent audit has been performed, and no automated test alone establishes originality.
