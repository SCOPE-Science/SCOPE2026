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

The infinite theorem is verified by the proof in RESULT.md. The finite checker is an independent stress test of the core-orbit mechanism and does not certify the theorem by enumeration.

Checks performed by `verify.py`:

- enumerate every admissible core type for \(d=2,3,4\) and determine its bipartition-preserving automorphisms;
- verify that the automorphism action on the \(d\)-vertex side is faithful for every enumerated core;
- for every enumerated core and every leaf total from zero through eight, compare direct orbit construction of weak compositions with the Burnside fixed-point count;
- verify the reciprocal-automorphism identity implied by the labelled-core formula \(d^{k-1}k!S(d-1,k)\);
- reproduce the known exact \(K_{2,m}\) and \(K_{3,m}\) formulas for the tested ranges;
- reproduce the 2009 \(K_{4,m}\) values \(28,45,73,105,152\) for \(m=5,6,7,8,9\);
- independently enumerate all spanning-tree types of \(K_{3,4}\) and \(K_{3,5}\), obtaining \(7\) and \(10\);
- verify the leading coefficients \(1/2\), \(1/3\), and \(29/144\) for \(d=2,3,4\).

The stored checker output is reproduced by running `python3 verify.py`. The computation does not test arbitrary \(d\) or arbitrary \(m\); those ranges are covered by the proof, not by extrapolation.
