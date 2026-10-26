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

Run `python3 verify.py` using Python 3's standard library. The program asserts directly that the specified three-voter, three-round, two-candidate outcome is Pareto efficient, satisfies EJR+ and FJR, and violates FJR+. It enumerates every approval profile and every outcome on a two-candidate domain for voter/round size pairs \((1,1),(2,1),(2,2),(2,3),(3,1),(3,2)\), and checks that each Pareto-efficient EJR+ outcome also satisfies FJR+.

Observed run: `WITNESS PASS`, then `EXHAUSTIVE PASS` in all six listed domains. The numbers of complete profile/outcome checks are respectively \(8,32,1024,32768,128,16384\); the corresponding counts of Pareto-efficient EJR+ outcomes were \(6,22,476,10488,90,7968\). The verifier computes exact integers and Boolean operations and does not use statistical sampling. It is a bounded computational corroboration only. The theorem for arbitrary numbers of candidates and rounds relies on the written proof in RESULT.md.

A self-review assessed correctness, published-priority comparisons and mathematical value. No independent audit has been performed.
