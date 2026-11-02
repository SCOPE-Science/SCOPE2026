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
# Reproduction

Compile the included `verify.cpp` with `g++ -std=c++17 -O3 -Wall -Wextra verify.cpp -o verify` and run `./verify`. This performs all coefficient and root tests modulo \(3^4\), not sampled tests, and compares each polynomial to the exact extremizer condition. The output observed was:

```
VERIFY_OK p=3 cubics=531441 max=27 extremizers=81 classification=exact 0:201852 1:277749 3:32805 7:13122 9:972 10:4374 18:486 27:81
VERIFY_OK witness_p=5 roots=75
VERIFY_OK witness_p=7 roots=147
VERIFY_OK witness_p=11 roots=363
```

Separately substituting \(p=3\) into the proved generating-function formula using exact rational arithmetic gives the same histogram and total mass one; the mean root count is one. Run `python3 verify_distribution.py` for a second, independent exact-rational generating-function check at seven primes, including the complete \(p=3\) histogram and mean-one identity. The code's exact search for \(p=3\) does not prove any statement for arbitrarily large primes. The general proof consists of the five reduction types, conditional discriminant and valuation arguments, and uniform coefficient-digit counting. No external or independent mathematical validation has been performed.
