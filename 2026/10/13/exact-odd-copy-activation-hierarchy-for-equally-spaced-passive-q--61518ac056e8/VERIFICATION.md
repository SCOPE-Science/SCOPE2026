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

Execute `python3 verify.py` using Python 3 (standard library only). The recorded output was:

```
VERIFY_OK exact_count_vector_cases=1430 activation_onsets=3,5,7,9 witness_5=(64,32)
```

All finite tests use exact integer populations, which is equivalent to normalized rational populations for comparison purposes. The code exhausts all occupation-count vectors for each chosen copy number, testing every distinct-energy comparison; a repeated word with the same occupation counts has the same energy and population, so these comparisons are sufficient for the **finite tested configurations only**.

The unbounded quantifiers in the theorem are established analytically by \(-\log(P_h/P_l)=[(u+v)d+(u-v)\Delta\ell]/2\), excitation/occupation parity, the two extremal word pairs, and strict threshold arithmetic. The verifier does not certify infinitely many copy numbers, all real populations, optimal extracted work, nonequidistant levels, or rank-deficient states.
