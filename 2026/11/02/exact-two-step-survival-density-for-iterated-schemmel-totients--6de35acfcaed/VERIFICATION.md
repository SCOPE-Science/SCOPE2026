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

# Verification notes

Run `python3 verify.py` using the standard Python library. The finite checks independently reconstruct \(L_m\), \(L_m\circ L_m\), the stopped iterate sum, and the admissible CRT residue count for \(m=4,6,8,10,12,16\), each at all integers through \(40000\). Recorded execution:

```text
VERIFY_OK tested_pairs=240000 forbidden_factor_checks=75498
EXCEPTIONAL_COUNTS_N_40000 {4: 2853, 6: 4470, 8: 1502, 10: 2010, 12: 2830, 16: 1189}
DEPTH_TWO_POSITIVE_TESTS 20241
CRT_RESIDUES_CHECKED_FOR m=4,6,8,10,12,16
```

The unrestricted equivalence is proved by the exact prime-power factorization. The asymptotic and its error require the published fixed-modulus Selberg–Delange theorem [Chang–Martin, Theorem 3.4]; finite data do not prove an asymptotic. The status indicated above means independent external mathematical review has not been performed.
