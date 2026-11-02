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

# Reproducibility and limits

The proof is the complete local-chart argument in RESULT.md. Its key algebraic identities are
\[
 \operatorname{adj}(\operatorname{adj}(T))=T,\qquad \operatorname{adj}(T)=\operatorname{tr}(T)I-T,
 \qquad \det(\operatorname{tr}(T)I-T)=\det(T),
\]
and, with \(w=t-s_1/2\), exchanging the roots of the quadratic support equation sends \(w\) to \(-w\). The fixed matrix condition is \(T=(\operatorname{tr}(T)/2)I\). The quotient's three-dimensional anti-invariant transverse space follows from the linear traceless decomposition.

Run `python3 verify_local.py` using Python's standard library. The included checker verifies 625 exact integer-matrix cases, 2401 exact centered substitutions, and the closed Euler-characteristic and codimension identities on a finite testing grid. The observed result was `VERIFY_OK`. These tests are diagnostic only: the proof for every complex curve and rank is symbolic and geometric, not inferred from a finite test grid.

The theorem is scoped to a length-two Quot scheme of a trivial bundle over a smooth complex projective curve. Literature priority has residual uncertainty. No independent mathematical audit has been carried out.
