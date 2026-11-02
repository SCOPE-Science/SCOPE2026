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

# Reproduction and limits

The package contains `verify_normality.cpp` and `independent_check.py`, which use only standard C++17 and Python 3 libraries respectively. Compile and run:

```sh
g++ -O3 -std=c++17 -o verify_normality verify_normality.cpp
./verify_normality 0 18
python3 independent_check.py
```

The complete C++ replay returned `VERIFY_OK 0_to_18`. In the size-eighteen comparison from rank eight to rank nine it printed equal achieved/required integer flows of `1837659219795`. All generated rank counts also agreed with an independent two-dimensional Delannoy recurrence; the odd central-rank bijection was checked explicitly. The separate Python program returned `INDEPENDENT_VERIFY_OK_0_TO_13`, computing normalized matching by a separately implemented augmenting-flow algorithm (including central pairs for odd sizes).

The C++ source enumerates all size-\(n\) words over \(H,V,D\) for \(n\le18\), checks every possible elementary cover transition, and saturates every necessary lower-half rank flow using exact 64-bit integers. The finite computation is exhaustive for the stated domain, whereas the printed numeric totals alone are not an independent certificate. The max-flow/min-cut and duality arguments in `RESULT.md` transfer these flows to all subsets and all ranks. The experiment neither proves nor disproves normality for \(n\ge19\), and independent assessment has not been performed.
