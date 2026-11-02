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

Both embedded standalone C++17 programs were compiled and executed from these exact source paths. `verify_forbidden.cpp` uses a prefix-sum forbidden-next-letter recurrence; `verify_direct.cpp` uses incremental literal block sums to test every possible newly completed square. Their complete exhaustive traversals agree at all \(299596819\) visited words, identify precisely eight length-\(86\) survivors, and find no length-\(87\) survivor. Each algorithm prints all survivors; lists were sorted and compared byte-for-byte. Independent arithmetic checking directly compared all adjacent equal-length subblock sums of each of the eight survivors.

Expected final-layer counts are: length \(80\): 2696; \(81\): 1530; \(82\): 792; \(83\): 338; \(84\): 120; \(85\): 38; \(86\): 8; \(87\): 0.

Reproduction with a C++17 compiler:

```sh
g++ -O3 -std=c++17 verify_forbidden.cpp -o checker_1
./checker_1
g++ -O3 -std=c++17 verify_direct.cpp -o checker_2
./checker_2
```

The programs use only fixed-size arrays, exact integer arithmetic, and ordinary recursion; they do not download dependencies or use nondeterministic search. The explicit code path to length \(87\) is evaluated; zero survivors is an exhaustive conclusion, not a timeout. `extremizers.txt` prints all winning strings, and `verification-output.txt` records the scientific counts.

**Limits.** The computation proves the finite enumeration for the specified alphabet under the given definitions. It is not an independent external audit and does not resolve the absolute priority of the result, especially with the unavailable separately archived electronic data.
