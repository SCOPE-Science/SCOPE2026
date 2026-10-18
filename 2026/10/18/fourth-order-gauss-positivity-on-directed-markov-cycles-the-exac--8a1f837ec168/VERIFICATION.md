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

# Reproducibility and mathematical checks

The included `verify.py` runs using Python and SymPy installed from `requirements.txt`. Command: `python verify.py`. Expected completion marker: `VERIFY_OK 406 exact matrix, group-inverse and polynomial checks`.

The code constructs finite directed Markov generators with exact rational positive rates; reconstructs passage times, stationary distributions, and their group inverses; tests the forward-neighbor aggregate identities; checks rational Padé transfer matrices at positive exact step sizes; and reproduces symbolic formulas for homogeneous three- and four-cycles and the latter's unique positive threshold. Inputs include three independent positive rate patterns in each dimension from two through eight. The checks use exact integer and rational arithmetic except the displayed optional decimal approximation to the threshold, which is not used in acceptance.

The proof for all dimensions, all positive real rates and all step sizes is contained in RESULT.md; no finite sampling can establish that universal claim. The large-step expansion is analytic, and the checker tests algebraic identities rather than estimating an asymptotic coefficient from floating-point data. No independent mathematical audit has been performed.
