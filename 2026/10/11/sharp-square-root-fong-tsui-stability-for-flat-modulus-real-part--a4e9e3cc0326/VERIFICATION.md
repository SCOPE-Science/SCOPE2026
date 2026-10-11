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
# Mathematical verification and reproducibility

The proof is analytic. Every bounded self-adjoint \(B\) has approximate unit eigenvectors for an endpoint \(\lambda\) of its spectrum satisfying \(|\lambda|=\|B\|\). These vectors justify the limiting inequality without assuming finite dimensionality or genuine eigenvectors. The inequalities \(|T|^2\le\|T\||T|\) and \(|T|\le aP+d(T)I\) follow from the continuous functional calculus and operator order, respectively; \(\|A\|\le\|T\|\le a+d(T)\) closes the estimate. The equality witness is checked exactly in the proof, including \(a=0\) and \(d=0\).

Run `python3 verify.py` from the extracted files to check exact scalar Pythagorean witnesses and the closed-form matrix-square-root inequality for an exhaustive declared rational grid of noncommuting \(2\times2\) test matrices. The script uses only the Python standard library. The tests are finite sanity checks and cannot prove the infinite-dimensional assertion or bibliographic originality.

No model-external expert certification or independent audit is claimed. The result has undergone same-model scientific review; independent audit has not been performed.
