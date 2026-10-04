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

The theorem is analytic. For a function on \(K_{a,b}\), let \(X\) and \(Y\) be the total assigned weights on the two sides. If a side contains a vertex at the upper bound \(u\), then every saturated vertex on that side imposes the same constraint on the opposite-side total: \(u+Y\le k\) for saturation in the \(a\)-side and \(u+X\le k\) for saturation in the \(b\)-side. If a side has no saturated vertex, every value there is at most \(u-1\). These observations yield four exhaustive cases and the four displayed maxima.

The bundled `verify.py` independently enumerates all assignments for \(1\le a,b\le3\), \(1\le u\le3\), and \(0\le k\le u(a+b+1)\), evaluates the released condition directly from closed neighborhoods, and compares the brute-force optimum with the formula. It also checks the \(K_{3,1}\), \(u=k=2\) witness.

The finite enumeration is a stress test and not evidence for the universal quantifier beyond the tested range. The universal statement rests on the exhaustive analytic case split.
