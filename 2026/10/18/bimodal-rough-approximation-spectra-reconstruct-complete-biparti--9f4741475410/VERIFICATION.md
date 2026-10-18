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

The general proof is in RESULT.md. Run `python3 verify.py` in the extracted files' directory. The verifier has no external dependencies and uses an independent direct evaluation of both relation-based approximation operators on all raw subsets for 19 small frames, with heterogeneous granule sizes in selected cases. It compares all bivariate coefficient counts and the total distinct-pair formula. It additionally checks 120 unordered pairs of quotient sizes for absence of lower-profile collisions and the polynomial-degree reconstruction.

Expected replayed output:

```
VERIFY_OK brute_cases 19 valuations 20656 distinct_pairs 923 inverse_profiles 120
```

Computational enumeration covers only these finite cases, not arbitrary numbers of granules or points. The proof of universal validity uses the full/active granule lemma and complete-bipartite neighborhood partition, and the inverse proof uses polynomial degrees and positivity. No formal proof assistant or independent validation is claimed.
