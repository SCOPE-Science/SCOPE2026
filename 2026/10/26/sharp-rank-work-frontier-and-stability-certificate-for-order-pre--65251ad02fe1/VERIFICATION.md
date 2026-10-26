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

# Verification of the rank–work frontier

Run `python3 verify.py` from the containing folder. The program requires only the Python standard library.

The direct enumeration uses `itertools.combinations_with_replacement` to visit every weakly increasing function from \([n]\) to itself for \(1\le n\le9\), with the exact rank and work independently computed for each map. It checks the sharp upper bound, equality set, and all rational stability remainders without floating-point approximation.

The second verification computes maximum achievable work and exact tie counts using dynamic-programming states indexed by last output and number of distinct output values, for \(2\le n\le20\). It is independent of the analytic vertex proof.

Terminal success marker: `VERIFY_OK_RANK_RESOLVED_CHAIN_WORK_FRONTIER`.

Finite exhaustion through \(n=9\) and dynamic programming through \(n=20\) are evidence for these ranges only. Correctness for unbounded \(n\) is established by the proof in `RESULT.md`, not inferred from these tests.
