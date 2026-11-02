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

# Reproducibility

The result is an algebraically exact computation over all binary three-gram supports, not an extrapolation from finite samples. The complete proof reduction appears in `RESULT.md`.

Run `python3 verify_threegram.py`. It enumerates all support masks and imbalance cases, evaluates geometric sums with integer polynomial division, verifies the numerator and denominator exactly, and checks every binary input word through length \(14\). Run `g++ -O2 -std=c++17 verify_threegram_independent.cpp -o verify_threegram_independent` followed by `./verify_threegram_independent 85` to independently enumerate nonnegative balanced integer flows for all lengths \(3\) through \(87\). Its output is supplied in `threegram_independent_results.txt`. Both were executed and matched the rational formula; recorded checks appear in `verification_output.txt`.

The C++ test uses 64-bit integers and was run only in the stated finite range. It does not purport to prove an all-length identity independently. The separate exact support-and-geometric-sums calculation does establish the formal generating function for all lengths, conditional on its transparent Euler-trail reduction and checkable implementation. There is no human independent audit.
