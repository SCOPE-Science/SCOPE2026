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
# Exact-arithmetic verification

The standalone source `verify.py` requires only the Python 3 standard library. Invoke `python3 verify.py` from the package directory. Executing the actual packaged source produced:

`VERIFY_OK 25 independently intersected exact horizons; 456 exact branch cylinders; 273 combinatorial identities and occupation bounds`

For bases \(2\le b\le6\) and comparison lengths \(1\le m\le5\), the verifier independently partitions the unit interval into base-adic cells fine enough that every relevant iterate is affine. It intersects the strict comparison inequalities using rational arithmetic and sums survivor interval lengths. Those totals agree with the claimed closed form. It reconstructs each admissible itinerary from exact cell midpoints, checks that all 456 distinct paths are nondecreasing, and compares the exact interval mass of every path against its terminal-branch expression. It separately verifies the complete-branch composition probability and the orbit-to-fixed-point distance bound on surviving cells. For \(2\le b\le14\) and \(1\le m\le21\), it checks 273 integer combinatorial identities.

The verifier is a finite diagnostic, not a proof of statements for unbounded \(b\) or \(m\). The universal equal-cylinder-weight identity, binomial formula, geometric orbit bound, and uniform-simplex conditional limit are established analytically in `RESULT.md`. No external audit has been performed.
