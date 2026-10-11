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

# Reproduction and scope

Run `python verify_symbolic.py` with Python 3 and SymPy. It checks, using exact symbolic algebra, the generators of the six stationary moments, the Liouville divergence, the equality-locus tangency derivative, the Hopf characteristic polynomial, the harmonic solvability conditions, and the leading squared-defect coefficient. Expected terminal line: `PASS: five moment generators, divergence, tangency, Hopf spectrum, order-two equation, order-three solvability, defect coefficient 1.`

The exact invariant-measure identity requires: compact invariant probability, zero mass on the reflection plane, and the specified polynomial vector field. The proof handles possible support accumulation on that plane by smooth truncation, and finite moment integrals follow from compact support. Equality rigidity invokes real analyticity of polynomial ODE trajectories. The periodic-orbit limit invokes the nondegenerate analytic Hopf theorem after explicit transversality and third-order solvability.

No finite computation certifies all possible invariant measures or the absence of stronger prior literature. The cited 2023 symmetry review was only inspected through its publisher-indexed Section 2.2 excerpt; its full text could not be fetched. No independent audit has been conducted.
