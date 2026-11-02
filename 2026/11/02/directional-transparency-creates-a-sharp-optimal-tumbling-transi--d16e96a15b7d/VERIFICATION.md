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

The point-detector boundary equations are solved exactly with \(H=(p+q-pq)z+pq>0\) for \(p,q>0\), \(z\geq0\), and the derivative sign gives the unique optimum including the equality case. An independent symbolic manipulation of the two-boundary linear system verified the displayed rational and reciprocal forms with a zero algebraic remainder.

Run `python check.py` with Python 3, NumPy and SciPy. The checker independently builds a two-direction finite-volume killed generator, solves its backward Poisson equation and compares the resulting mean against the exact continuum formula at three spatial resolutions for eight parameter sets; it also checks the exact global-optimum formula against a fixed grid of rates. During verification all checks succeeded. The finite-volume approximation converges as the step size shrinks; these finite tests are numerical consistency checks and do not prove the all-parameter assertion.

A physical Monte Carlo event simulation is not required by the proof and was not used. Historical priority and independent external scientific audit remain unverified. This verification record does not certify those channels.
