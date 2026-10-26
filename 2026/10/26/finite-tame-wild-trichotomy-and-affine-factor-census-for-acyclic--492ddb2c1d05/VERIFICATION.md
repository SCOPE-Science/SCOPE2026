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

# Reproducibility and boundaries

Run `OPENBLAS_NUM_THREADS=1 python verify_face_types.py` using Python 3 and NumPy. The program enumerates every directed acyclic simple quiver with at most four labeled vertices, plus seeded acyclic samples of orders five and six. For each it independently builds the synchronous-square quiver and computes the least eigenvalue of the symmetric Cartan matrix. It compares the finite/tame/wild classification with the input-component criterion. It also checks the four ordered two-fork cases and a repeated-arrow case. The result recorded on the reviewed source package is:

`VERIFY_OK 857 acyclic quivers; Cartan inertia, four affine fork products and parallel-arrow boundary`

Numerical eigenvalue checks use a stated tolerance and do not prove any infinite classification. The mathematical proof uses the standard Dynkin/extended-Dynkin classification and strict spectral-radius monotonicity; these are not computed certificates. All source and checker paths below refer to files contained in this package; no external executable artifact is necessary beyond Python and NumPy.
