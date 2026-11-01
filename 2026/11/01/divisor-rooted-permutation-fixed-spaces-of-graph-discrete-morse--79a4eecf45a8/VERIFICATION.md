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

# Verification and limits

Run `python3 verify.py` with Python 3 and the standard library. Observed output ends with `VERIFY_OK 14 cases`. The program independently enumerates directed-arrow orbits in the original graph for fourteen explicit permutation cycle types, filters the admissible orbits by actual directed-forest acyclicity, compares quotient and original compatibility, computes complete face vectors, and calculates reduced mod-two simplicial homology. It tests non-chain divisibility and genuine higher-dimensional cases. The correctness of the all-parameter classification additionally depends on the written orbit-quotient proof, the published complete-source shellability theorem, the published simplicial expansion theorem, and the directed matrix–forest identity. A finite checker cannot certify those infinite statements or establish literary uniqueness. No independent mathematical audit has been performed.
