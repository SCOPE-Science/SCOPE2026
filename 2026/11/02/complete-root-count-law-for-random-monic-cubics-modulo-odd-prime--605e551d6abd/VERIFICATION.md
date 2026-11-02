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

# Reproducible verification

`verify.cpp` is a self-contained C++17 exhaustive enumerator. Compile with `g++ -O3 -std=c++17 verify.cpp -o verify`, then run `./verify`. It evaluates every monic cubic for every residue modulo the cubed modulus, not only Hensel-predicted roots, and independently checks the complete integer histograms for primes 3 and 5.

Recorded result from executing the C++ program:

```
VERIFY_OK p=3 0:7452 1:9963 3:1215 4:486 7:486 9:81 total=19683
VERIFY_OK p=5 0:690000 1:1056250 3:156250 5:12500 6:12500 11:25000 25:625 total=1953125
```

The code is exhaustive for these two prime values, not for infinitely many primes. The unrestricted claim relies on the complete reduction-type proof. The symbolic first three moments are exactly 1, \(4-3/p\) and \(5p+5-17/p+8/p^2\), while the fourth is \(p^3+8p^2+2p+4-42/p+28/p^2\). Independent mathematical audit has not been performed.
