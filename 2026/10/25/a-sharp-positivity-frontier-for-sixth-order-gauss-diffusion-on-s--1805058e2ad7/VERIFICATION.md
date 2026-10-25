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

# Verification method

`verify.py` uses Python 3 and SymPy to verify two exact scalar differential identities, the Petersen graph's exact diagonal rational function and signs at two rational timesteps, and 2,361 exact matrix-entry comparisons for six strongly regular graphs at rational timesteps. Graph structures are generated independently of the derived transition formulas; graph parameters and adjacency-square identities are recomputed. The rational timestep matrix is formed from the original numerator/denominator polynomials using exact matrix inversion and checked against its three-eigenvalue polynomial reduction. Every off-diagonal check is exact. Reproduction: install SymPy and run `python verify.py` in the package directory.

Expected successful output:

`VERIFY_OK: scalar derivative identities; 6 strongly regular graphs; 2361 exact matrix-entry comparisons; off-diagonal positivity; stochasticity; Petersen sign crossing`

The finite replay verifies identities and representative examples only. The infinite-family sign and uniqueness claims are established analytically by the proof in `RESULT.md`, including global derivative sign certificates and projector diagonals. No independent audit has been performed.
