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

The included `verify.cpp` implements immediate-neighbor three-site OR updates, exhaustive sweep permutations, exact singleton reach times, antipodal-descending witness detection, and the expected binomial schedule counts.

Build with `c++ -std=c++17 -O2 verify.cpp -o verify`, then run `./verify`. The verification performed on the included source returned:

```
n=3 permutations=6 sharp_bound=1
n=4 permutations=24 slow=24 multiple_witness=8
n=5 permutations=120 sharp_bound=2
n=6 permutations=720 slow=216 multiple_witness=0
n=7 permutations=5040 sharp_bound=3
n=8 permutations=40320 slow=1280 multiple_witness=0
n=9 permutations=362880 sharp_bound=4
n=10 permutations=3628800 slow=7000 multiple_witness=0
VERIFY_OK permutations=4037910 singleton_tests=39916794 all_state_tests=695472
```

Every update order was checked for sizes \(3\) to \(10\); all initial binary states were additionally checked for sizes \(3\) to \(7\). Finite tests do not prove the unrestricted formulas. The all-size reasoning is supplied in the path-clock, descent-chain and nonoverlap arguments in `RESULT.md`. Historical priority is not certified, and no independent scientific audit has been performed.
