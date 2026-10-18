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

The proof uses exhaustive symbolic forms of the chart monoids for arbitrary \(n\), not inference from small finite instances. At each non-extreme vertex the coordinate differences generate a free signed basis; at an extreme vertex they generate the two-row rank-one matrix semigroup. The full ideal is the known prime ideal of \(2\times2\) minors. This settles the chart scheme structure and normality for every \(n\ge3\).

The separate supplied `verify.py` program was run against its actual packaged source. Its output is recorded in `verification_output.txt`: 238 charts and 20,852 exponent-difference decompositions for \(n=3,4,5,6,7\), all passing. The pairwise rank-one quadratic relations were checked on each singleton vertex chart. Optional NumPy/SciPy convex hull computations returned normalized volumes 4, 22, and 118 for \(n=3,4,5\), agreeing with the exact formula \(n!-2\).

The local integral divisor class follows independently from the unimodular subset of the primitive toric rays, and the canonical criterion follows from \(K_{\mathbb P^1\times\mathbb P^{n-2}}=\mathcal O(-2,-(n-1))\) modulo the cone hyperplane class \((1,1)\). Finite enumeration is not an infinite proof, and the optional floating-point volume checks do not establish the general degree formula. A separate all-\(n\) cube-volume argument is given in `RESULT.md`.
