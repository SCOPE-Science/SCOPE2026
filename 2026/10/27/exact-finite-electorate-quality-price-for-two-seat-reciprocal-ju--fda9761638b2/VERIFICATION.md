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

The accompanying `checker.cpp` is a self-contained C++17 regression. The command `g++ -std=c++17 -O2 checker.cpp -o checker && ./checker` completed with `ALL EXACT CHECKS PASS`.

Verified by exhaustive exact-integer arithmetic over all nonempty candidate-support subsets for \(n=2,3,4,5\), \(m=3\), and \(n=2,3\), \(m=4\), at qualities \(\{1/2,2/3,3/4,1\}\), for 1,728; 21,952; 216,000; 1,906,624; 20,736; and 614,656 support/quality instances respectively. Also verified the symbolic extremal construction by rational integer cross multiplication for \(2\le n\le15\).

All checks use the exact violation condition \(2h_c|N(c)\cap U(W)|\ge n\), with equality treated as violation. Enumerated cases do not prove the theorem for arbitrary real qualities or unbounded candidate counts. The analytic proof in `RESULT.md` supplies that coverage. This is self-review only; independent audit remains unperformed.
