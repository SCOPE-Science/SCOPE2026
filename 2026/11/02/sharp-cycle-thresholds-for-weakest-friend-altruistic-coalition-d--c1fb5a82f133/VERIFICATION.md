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

# Verification instructions and scope

Run `python3 verify.py` in Python 3; no external dependencies are required. The checker exhaustively constructs all labeled simple graphs and canonical set partitions for orders \(1\) through \(4\), creates exactly the strict unilateral-improvement arcs, tests directed acyclicity and verifies the stated degree-multiset classification. It additionally checks the exact sum-model potential differences for every unilateral move in that finite range, and directly checks the four-move tree cycle for \(n=5,6,7,10,20,50\).

Expected output includes the cyclic-graph counts \(0,0,0,16\), degree-signature counts \(12\) and \(4\), and `VERIFIED_MIN_EQ_BOUNDARY_AND_SUM_POTENTIALS`. Complete finite enumeration is a certificate only for the explicitly bounded domain. The symbolic argument in the proof supplies the unbounded exact-potential theorem and connected-tree family; testing six values of \(n\) does not establish either infinite statement.

There has been a self-review of the scientific argument and the included checker. Independent external review and publication-priority certification have not been performed.
