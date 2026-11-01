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

Run `python verify.py` with Python 3 and SciPy installed. The program uses exact rational arithmetic to compare the number of edges crossed by a sectioning hyperplane against the isolated-vertex cone condition in dimensions three through six; it skips nongeneric vertex-on-plane cases. With the embedded deterministic seed, 2,764 test cases pass. It also numerically evaluates the independent simplex integral and compares the six resulting probabilities to the elementary trihedral-angle formula at interior diagonal parameters. Three near-threshold evaluations check convergence toward the explicit analytic coefficient.

The analytic proof in `RESULT.md` supplies the unbounded-dimensional arguments, including the cube graph edge boundary and the angular Jacobian. The finite verifier is not an exhaustive mathematical proof. No claim of independent certification is made.
