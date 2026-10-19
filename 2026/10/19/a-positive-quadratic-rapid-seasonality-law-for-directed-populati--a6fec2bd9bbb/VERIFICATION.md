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
# Verification of the rapid-period dispersal coefficient

Run `python3 verify.py` with Python 3, NumPy, SciPy and SymPy available. The program reconstructs the three-patch directed-cycle centered temporal primitives by exact rational symbolic integration and verifies that its covariance matrix has diagonal entries \(1/27\), off-diagonal entries \(-1/54\), and exact second-order coefficient \(1/18\). It independently checks the weighted Dirichlet identity.

The program then assembles genuine Floquet monodromy products for three and four unequal seasons, checks the expected quadratic approach to the averaged Perron growth rate, verifies both Perron equations and coefficient representations in a nonreversible six-edge system, and checks exact scalar-forcing invariance for several periods. The recorded execution passed 36 assertions. Finite numerical calculations do **not** constitute the general proof or certify the sign for every model; the self-contained perturbation and Perron-weighted identity in RESULT.md do that.

The verification does not test nonlinear populations, seasonally varying migration, arbitrary period monotonicity, or publication novelty. No independent scientific audit has been carried out.
