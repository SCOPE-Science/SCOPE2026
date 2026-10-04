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

The analytic proof reduces the fixed-concurrence Bell-diagonal slice to a triangle in the two smaller absolute correlation coordinates. The three triangle vertices are evaluated symbolically, and the two upper candidates differ by \((1-C)(13C-1)/144\). This establishes the crossover exactly at \(C=1/13\) inside \([0,1]\), with the Bell-state endpoint \(C=1\) shared by all extremal families.

`verify.py` replays the relevant identities using exact rational arithmetic and scans finite rational Bell-eigenvalue grids for supplementary sanity checks. A finite grid is not used to prove the continuous theorem; the proof is the analytic simplex/triangle argument in `RESULT.md`.

The result does not verify or claim monotonicity of Hilbert–Schmidt geometric discord under arbitrary quantum operations. No independent audit has been performed.
