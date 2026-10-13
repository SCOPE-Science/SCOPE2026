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

The universal claim is verified analytically from the source formula. Writing \(s=1-\|x\|^2\), exact multiplication of \(R_x=I+xx^{\mathsf T}/s\) on both sides of \(D+D^{\mathsf T}\) reproduces every term of the source Bures matrix. The quadratic form
\[
v^{\mathsf T}R_xv=\|v\|^2+\frac{(x^{\mathsf T}v)^2}{s}
\]
is strictly positive for nonzero \(v\), so congruence preserves inertia.

The source's trace-distance condition and its Eq. (23) Bures matrix were inspected in the open-access full text. The source explicitly identifies its own example's Bures negative-definiteness statement as numerical. The earlier QFI-flow primary source and a later non-unital Bures/trace-distance comparison were inspected for broader coverage and did not state the congruence theorem.

`verify.py` uses exact rational arithmetic to replay the rank-one expansion and inverse identities on several nondegenerate rational test cases. It is a consistency check, not a proof by enumeration. No numerical search, asymptotic extrapolation, or external certification is needed for the theorem.

Limits: the metric expression is used on full-rank qubit states, the Bloch dynamics must be unital, and no statement is made about equality of integrated witness magnitudes or finite-separation distance trajectories.
