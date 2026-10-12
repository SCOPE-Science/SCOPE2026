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

The proof is an exact case analysis, not an extrapolation from computation. For a crown graph, each \(a_i\) is adjacent to all vertices of \(B\) except \(b_i\), so the Roman condition on \(A\) is determined exactly by whether \(B\) contains zero, one, or at least two labels equal to \(2\). The symmetric statement handles \(B\). Partitioning by these two counts produces the seven terms in the claimed polynomial.

The packaged `verify.py` independently reconstructs the graph adjacency and Roman condition. For every \(n\) from \(3\) through \(6\), it enumerates all \(3^{2n}\) labelings, accumulates their exact weight histogram, constructs the closed formula using integer polynomial arithmetic, and compares every coefficient. It separately checks that the least nonzero degree is \(4\) with coefficient \(n\).

Expected successful replay:

`VERIFY_OK n_range=3..6 labelings=597780 coefficient_checks=76 minimum_checks=4 max_order=12`

The computation does not certify arbitrary \(n\); that scope is supplied by the proof. The disconnected case \(n=2\) is not part of the theorem.
