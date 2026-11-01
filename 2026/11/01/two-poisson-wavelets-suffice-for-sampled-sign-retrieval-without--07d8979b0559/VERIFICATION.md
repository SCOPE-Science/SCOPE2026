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

The analytic proof establishes the universal statement for all real square-integrable signals, all \(p>0\), and every hyperbolic lattice satisfying the specified sufficient density bound. It reduces the two separate magnitudes to sampled values of the real part of a square difference, proves an explicit weighted harmonic uniqueness estimate by disk mean-value identities and a complete half-plane tiling, and uses the weighted Bergman norm to exclude nonzero imaginary constants.

A standalone Python standard-library script, `checks/proof_checks.py`, was executed successfully. It tests the scalar contraction coefficient at several exponents, the node-to-tile/disk containments and counting bound on representative lattice parameters, and the algebraic real-part-of-square identity. These checks are neither an exhaustive parameter search nor a substitute for the proof. The Cauchy-wavelet/Bergman correspondence used in the proof is established in the cited primary paper.

Two-window recovery is not claimed at the much larger sampling ranges of the prior three-window theorem. No noise-stability theorem or algorithm is supplied. Historical priority and correctness have not been independently audited or validated.
