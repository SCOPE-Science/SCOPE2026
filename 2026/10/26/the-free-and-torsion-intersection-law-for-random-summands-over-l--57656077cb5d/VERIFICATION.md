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

The companion `verify_intersections.py` provides independent finite exhaustive computations. It enumerates the rank-\(\ell\) summands of \(R^n\) through canonical reduced-row-echelon residue bases, iterates every allowed radical lift, and forms each actual intersection with the coordinate summand by all \(R\)-linear combinations.

Over \(\mathbb F_p[\varepsilon]/(\varepsilon^2)\), direct enumeration covers ten instances for \(p=2,3\) and dimensions at most four. For the mixed-characteristic ring \(\mathbb Z/4\mathbb Z\), six additional instances are checked. The program compares the entire \((a,b)\)-distribution to the Gaussian formula, including zero-count cases, and separately verifies the summation identity at \(q\in\{2,3,4,5,7\}\), \(1\le n\le9\), all feasible ranks. Its successful terminal marker is `ALL_CHECKS_OK`.

A representative dimension-four balanced binary case has \(560\) free rank-two summands with type counts \(N(0,0)=256\), \(N(0,1)=144\), \(N(0,2)=6\), \(N(1,0)=144\), \(N(1,1)=9\), \(N(2,0)=1\). Both residue-characteristic-two dual numbers and \(\mathbb Z/4\mathbb Z\) yield these counts.

Finite testing does not prove all dimensions, arbitrary prime powers, or the limiting law. Those follow from the mathematical proof in RESULT.md. The verification uses no external package beyond Python's standard library; run with `python3 verify_intersections.py`.
