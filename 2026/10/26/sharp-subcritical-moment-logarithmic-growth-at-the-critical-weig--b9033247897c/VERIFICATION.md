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

# Scientific verification record

The infinite-dimensional assertion follows from the proof in `RESULT.md`, not from a finite test. The weighted-space-to-probability-vector reduction is an equality. The bound on each short-time column and the reciprocal identity in the long-time range establish a uniform upper estimate for all nonnegative probability vectors, including infinitely supported ones. Concave tangency yields the sharp constant after optimization. The constructed finite-support vector has unit norm, and its orbit moments converge uniformly on each compact fraction-of-horizon interval by a harmonic-sum argument; monotone nonnegativity allows the endpoint cutoff to shrink. These steps prove the two-sided limit for every fixed \(1\le p<\infty\) and \(0<q<p\).

The optional `checks/reproduce.py` computes finite-horizon orbit moments of the explicit witness and validates normalization for several pairs of exponents. Its output is only a finite diagnostic and cannot certify asymptotics, novelty, or an unattained supremum. The coefficient is not asserted uniformly near \(q=p\), and independent verification is not represented as having occurred.
