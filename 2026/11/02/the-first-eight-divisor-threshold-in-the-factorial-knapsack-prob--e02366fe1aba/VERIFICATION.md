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

Run `python3 verify.py` with `EXTREMAL_TARGETS.json` in the same directory. This enumerates divisors of each \(n!\) exactly and independently verifies each generated number actually divides \(n!\), then performs full cardinality-restricted bitset reachability over all \(n!+1\) positions for each \(1\le n\le12\). It checks a missing target for one fewer divisor and no missing target at the reported minimum, and confirms all 175 targets are precisely the uncovered set for seven divisors at \(n=12\).

Observed final line: `VERIFY_OK first_eight_threshold=12 exact_full_range=PASS targets=175 finite_only=YES`. The factorial-12 calculation examined 792 exact positive divisors and the full 479001601-position Boolean domain. In a reference run the script finished in about 30 seconds with peak memory about 1.24 GB; resources may vary. The check is deterministic and exhaustive for the specified finite domain; it does not extrapolate to larger factorials.

A different C++17 word-bitset implementation `crosscheck.cpp` confirms factorials \(8!\) through \(11!\). To run: `c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck && ./crosscheck`. The C++ check shares the same mathematical recurrence but uses a distinct physical representation; it does not constitute external or independent validation.

The 175-value list is essential to the claim; `verify.py` recomputes and compares the complete list rather than trusting it. Both methods are ordinary executable proof checks, not formal theorem-prover certificates. No independent audit has been performed.
