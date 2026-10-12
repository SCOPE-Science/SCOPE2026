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

The infinite statement is verified analytically in `RESULT.md`. For every integer \(d\ge3\), the squared diagonal entries of the two Kraus operators sum to one. The first branch has probability \(1/3\), becomes maximally entangled, and has raw top concurrence \(1/d^d\); the second branch has probability \(2/3\), becomes a product state, and has raw top concurrence zero. Thus the average is \(1/(3d^d)\), while the input value is \((2d+1)/(3d)^d\).

The exact ratio is
\[
\frac{3^{d-1}}{2d+1}.
\]
It exceeds one at \(d=3\). If it exceeds one at \(d\), then \(3^d>6d+3>2d+3\), establishing the next case. This is the proof for all dimensions, not an extrapolation from samples.

`verify_counterexample.py` uses only Python's standard library and exact rational arithmetic to replay the algebra for representative dimensions \(d\in\{3,4,5,8,16,32\}\). The captured output in `verification_output.txt` reports `VERIFY_OK` after checking completeness in squared Kraus amplitudes, the probabilities, the input and output products, and the exact gain ratio.

The checker is deliberately finite and is not an infinite certificate. No computation is required for the induction argument. The result does not assert failure of Gour's rooted \(G_d\), nor does it classify lower raw concurrence-hierarchy members.
