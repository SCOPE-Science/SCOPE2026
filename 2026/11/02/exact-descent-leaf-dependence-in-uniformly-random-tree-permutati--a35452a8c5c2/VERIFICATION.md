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

The complete proof is in RESULT.md and is checkable from definitions and the independently cited insertion and leaf/run lemmas. To repeat the finite checks, run `python verify_tree_permutation_dependence.py` using the embedded standalone standard-library script. Expected output:

`PASS 16499 exact assertions; 4094 coded trees; 126 independently brute-classified trees`

The program checks all encoded trees through size 13 and independently brute-classifies all tree permutations through size 8. Exact arithmetic is used. It does not test the infinite limit empirically and does not replace the unrestricted combinatorial proof. Independent audit has not been performed.
