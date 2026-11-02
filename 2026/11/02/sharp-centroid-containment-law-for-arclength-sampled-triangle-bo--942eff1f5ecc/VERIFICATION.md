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
# Verification of the centroid-containment formula

The universal assertion is proved analytically in `RESULT.md` by affine reduction, the two exact conditional integrals, disjoint Cramer bad-sign events, multinomial counting, and Schur concavity. `checker.py` provides additional finite corroboration, not an exhaustive proof.

The standalone checker was executed from the packaged source path with a standard Python interpreter and produced `ALL_CHECKS_PASSED`. It compared the exact two conditional constants against independently implemented midpoint quadrature, verified disjoint bad-sign events in 100000 independently sampled triples, simulated the full Euclidean arclength model on five triangles of different shapes with 170000 samples each, and tested 50000 random balancing/stability cases. Each Monte Carlo comparison used a stated six-standard-deviation tolerance plus \(0.0005\), so the test is deliberately nondeterministic in theory but reproducible with its fixed seed.

The proof does not require scientific software or external datasets. The program uses only Python's standard library. Reproduction: `python3 checker.py` from a directory containing the extracted file. The literature comparison is a priority assessment, not an independent mathematical audit; further historical investigation could identify an earlier equivalent formula.
