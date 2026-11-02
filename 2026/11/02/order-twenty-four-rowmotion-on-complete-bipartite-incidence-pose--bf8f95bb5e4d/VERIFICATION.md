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

The proof's nonstandard finite claim is the exact 48-case support-period table. `verify_support.py` creates the incidence poset for each admissible nonempty support, with each distinct column type represented once. It iterates the original definition of rowmotion by checking which missing elements have all lower covers present, generates their downward closure, and returns the first positive period. It asserts that precisely 48 supports exist and that the complete period-by-size table equals that in `RESULT.md`.

Run:

```sh
python3 verify_support.py
python3 verify_direct.py
```

Observed outputs included:

```text
SUPPORT_PERIOD_CERTIFICATE_OK supports=48
period_by_support_size= {2: {1: 2, 2: 1}, 3: {1: 3, 3: 1}, 4: {2: 4}, 6: {3: 3, 4: 5, 5: 1}, 8: {1: 8, 2: 12}, 24: {3: 8}}
FULL_CENSUS_OK n=1 ideals=13 cycles={2: 1, 3: 1, 8: 1}
FULL_CENSUS_OK n=2 ideals=47 cycles={2: 2, 3: 1, 4: 2, 8: 4}
FULL_CENSUS_OK n=3 ideals=187 cycles={2: 4, 3: 3, 4: 6, 6: 3, 8: 10, 24: 2}
FULL_CENSUS_OK n=4 ideals=803 cycles={2: 8, 3: 13, 4: 14, 6: 38, 8: 22, 24: 12}
FULL_CENSUS_OK n=5 ideals=3643 cycles={2: 16, 3: 51, 4: 30, 6: 295, 8: 46, 24: 50}
FULL_CENSUS_OK n=6 ideals=17147 cycles={2: 32, 3: 181, 4: 62, 6: 1870, 8: 94, 24: 180}
FULL_REPLAY_OK
```

`verify_direct.py` independently enumerates all ideals for \(1\le n\le6\), uses the Boolean update derived from minimal complement, constructs their permutation, and obtains the complete cycles. Its finite bound does not prove the infinite-family theorem by itself. The proof of uniformity is the support lemma in `RESULT.md` together with the fully checked 48-case table. Python 3 standard library is the only software dependency.

No independent external validation or scholarly peer audit has been performed.
