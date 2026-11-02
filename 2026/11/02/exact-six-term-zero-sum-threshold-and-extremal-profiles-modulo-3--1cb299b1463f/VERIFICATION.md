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

The complete exact-computation certificate is `artifacts/sun6_extremals.txt` (23,970 sorted twelve-element rows, SHA-256 `c1e36c249abab1240f35d029f52526e4f24555c0850529d5a765eec4245542f1`). Its generator and a distinct direct-combination checker are provided alongside it.

Reproduce with:

```sh
c++ -std=c++17 -O2 artifacts/sun6_enumerate.cpp -o sun6_enumerate
c++ -std=c++17 -O2 artifacts/sun6_crosscheck.cpp -o sun6_crosscheck
./sun6_enumerate > regenerated.txt
cmp regenerated.txt artifacts/sun6_extremals.txt
./sun6_crosscheck < artifacts/sun6_extremals.txt
```

Observed generator output: `GENERATOR_OK width12=23970 nonextendible=23970`; observed independent checker output: `CROSSCHECK_OK rows=23970 orbits=361 patterns=11`. The generator tests an exact six-subset-sum recurrence modulo \(36\) for every sorted admissible multiset and uses only hereditary pruning. The checker directly enumerates the five- and six-position sums for each listed row, independently checks no admissible extension, and constructs the affine orbits from group actions.

The lower-bound witness is the twelve-term list \((1,1,1,1,1,31,2,2,2,2,2,26)\). A six-element sum can be divisible by \(6\) only by taking all six members of either residue class modulo \(6\), in which case its sum is \(36\). The exhaustive upper bound is finite and does not require probabilistic assumptions. The numerical orbits are exact for modulus six only. Independent audit and general-modulus validation are not performed.
