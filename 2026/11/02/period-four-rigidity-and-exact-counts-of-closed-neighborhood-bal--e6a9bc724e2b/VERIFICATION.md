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

# Reproducible checks and limits

Run `python3 verify_balance.py` with Python 3.9 or later. The checker is a standalone standard-library script. `valid` independently builds each graph's full closed-neighborhood counts by explicit vertex-index arithmetic, while `seed_count` iterates all first-two-column assignments and propagates the local equations without using the claimed classification.

The direct full-assignment test covers all six circumferences \(3\le n\le8\) for \(m=2\), the three cases \(3\le n\le5\) for \(m=4\), and \((m,n)=(6,3)\): ten graphs in total. The separate seed-propagation test covers \(m\in\{2,4,6,8\}\) and every circumference \(3\le n\le12\): 40 parameter pairs. Representative exact counts: \(B(2,4)=6\), \(B(2,6)=2\), \(B(4,4)=36\), and \(B(8,4)=4900\). The run prints `VERIFY_OK 10 direct brute-force graphs; 40 cyclic seed cases`.

These tests are independent implementations in the limited sense of different algorithms, not an independent mathematical audit. The direct algorithm is exponential and covers only the stated finite instances. The infinite correctness argument is the written proof based on the column-sum recurrence, maximum modulus, and cyclic sum-of-squares identity; the finite data do not establish it. Priority comparisons may be incomplete, especially for older unindexed graph-product work.
