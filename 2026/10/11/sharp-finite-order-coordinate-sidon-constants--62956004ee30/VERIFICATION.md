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

The universal proof is analytic. The critical chain is: discrete phase maximization equals the circumradius of a Minkowski sum of regular polygons; planar perimeter is additive under Minkowski addition; that sum has at most \(mn\) edge directions; the sharp perimeter of a convex polygon with at most \(mn\) sides in a radius-\(R\) disk is \(2mnR\sin(\pi/(mn))\); equality forces a regular \(mn\)-gon; and regularity forces equal coefficient moduli and complete interlacing of the summand edge directions.

The accompanying `verify.py` checks the proposed extremizers by exhaustive evaluation of every group point for \(3\le m\le7\) and \(2\le n\le4\). It also stress-tests random coefficient vectors in smaller parameter ranges and verifies that none exceeds the analytic constant within floating-point tolerance. These computations are finite corroboration only and are not used as proof of the all-parameter theorem.

No statement is made for \(m=2\), dependent character systems, mixed coordinate orders, or arbitrary subsets.
