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

Run `python3 verify.py` from this standalone directory. The verified output was:

```
VERIFY_OK word_counts=98 normal_forms=98 digital_profiles=192 and orbit_freeness
```

The checker independently brute-forces all binary supports of length \(1\le n\le14\) for bases \(2\le b\le8\) and compares them to the closed word-count formula. A second exhaustive loop compares every accepted support to the proposed complete support normal form. Additional tests check exact digital-profile identities at lengths adjacent to geometric powers up to base exponent eight and that finite marker configurations have no nontrivial shift stabilizer.

The computations test finite domains only. The proof of the all-base support classification is the power-sum argument; the proof of the full automorphism group uses Cantor–Bendixson strata, finite-radius locality, and the continuity of finitely supported orbit permutations. The nonconjugacy argument relies on the conjugacy invariance of the leading word-complexity coefficient, not numerical fitting. Independent mathematical audit has not occurred.
