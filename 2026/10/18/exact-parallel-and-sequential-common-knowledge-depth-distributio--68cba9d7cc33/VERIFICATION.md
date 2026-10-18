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

`verify.py` is standalone Python 3 and uses no nonstandard dependencies. Invoke `python3 verify.py` in a directory containing this file. A successful run ends in `VERIFY_OK`.

The program enumerates all pairs of equivalence relations with cell size at most two for \(n=1,\ldots,7\), computes parallel and sequential relation powers and component closures, and compares the cumulative histograms with the two symbolic rational-coefficient exponential generating functions. It enumerates every pair of perfect matchings on \(2,4,6,8\) worlds, and every unrestricted equivalence-relation pair for \(n=3,\ldots,6\) to check the extremal count \(n!\). For \(n\le4\), it evaluates the two modal operators on every event and checks that convergence occurs no later than the computed uniform depth.

Finite enumerations corroborate the theorem but do not establish its all-size proof; that proof is in `RESULT.md`. The program has no role in verifying originality. The science has undergone self-review only. Independent audit has not been performed.
