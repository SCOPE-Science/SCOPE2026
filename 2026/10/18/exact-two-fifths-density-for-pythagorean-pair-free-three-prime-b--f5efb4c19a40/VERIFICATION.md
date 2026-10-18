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
# Verification and scope

Run `python3 verify.py` (Python standard library only). The executable enumerates all integer-square Pythagorean pairs in 120 rectangular boxes with \(1\leq A\leq6\), \(1\leq B\leq5\), \(1\leq C\leq4\) and compares them with the proposed exponent graph. It also verifies the five consecutive hypotenuses of the explicit five-cycle and the independent residue-class construction.

Expected output: `VERIFY_OK rectangular_boxes=120 five_cycle_edges=5 classification_agrees=YES`.

The checker does not independently enumerate all primitive supported triples at infinite size; that exhaustion is the elementary Euclid-parametrization lemma in the paper. Neither the finite checker nor the five-cycle alone establishes exact finite extremal values. The infinite upper bound needs both the torus seam argument and translation double-counting; the infinite lower bound is the explicit residue-class construction. All arithmetic is exact integer arithmetic. Independent mathematical validation has not been performed.
