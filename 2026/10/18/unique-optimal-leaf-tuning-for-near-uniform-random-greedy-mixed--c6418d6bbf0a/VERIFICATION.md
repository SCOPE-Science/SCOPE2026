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

The standalone `verify.py` rebuilds each finite mixed spider directly from adjacency bitsets and computes greedy maximal-independent-set probabilities from the independent first-arrival recursion. It checks twelve pairs of parameters, including both sides of the small exceptional \(k=1,3\) choices, without using the closed formula in the recurrence. The obtained probabilities agree exactly with the claimed \(q_j\), centre mass and total-variation distance.

For \(0\le k\le10\), the script then checks exact positive/negative-deviation identities over a bounded range of direct-leaf counts using rational arithmetic. It also checks the exact inequalities deciding the two competing leaf counts for \(1\le k\le10\). The unrestricted proof for all \(k\) is not inferred from these tests: it uses monotonicity, symmetric binomial pairing, the analytic bound \(2^k+1>2k(k+1)\) for \(k\ge7\), and the six explicitly evaluated remaining cases. The sharp leading constant follows from the exact expectation identity and the central-binomial estimate.

Run from the package directory with `python3 verify.py`; expected success marker: `VERIFICATION_OK`.
