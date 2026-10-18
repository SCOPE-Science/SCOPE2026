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

# Verification and reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. This standalone program tests the exact symbolic/rational identities for the scalar derivative at 390 rational parameter pairs, validates the rational exponential brackets used in the four-dimensional witness, and checks directly computed Hessian eigenvalues versus the differentiated density at several scales, dimensions, masses and radii. The supplied execution passed 3,042 checks.

The universal inequality relies on the analytic Hessian calculation and the global unique-minimum argument for \(F_q\), not on enumeration or floating-point tests. The branch equality, unique degeneracy sphere, strict positive-curvature annulus when above threshold, and all-projection comparison follow from the written proof. The singular limiting regimes \(w\to0,1\) and \(\sigma\to\tau\) are not part of the theorem's open parameter domain.

The result has undergone self-review only; independent audit has not been performed. The closest earlier full Gaussian-mixture paper and a later general mixture preprint could not be fully inspected, so independent priority assessment remains useful.
