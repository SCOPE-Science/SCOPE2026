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

# Reproducibility of the integral counterexample

Run both provided programs from the same directory using Python 3 and SymPy. The first program rebuilds all \(312\) nonempty faces of the bidirected \(K_{2,4}\) multipath complex, checks the complete acyclic matching, and produces the exact integer chain reduction. Its resulting \(1\times12\) and \(12\times4\) integer boundary matrices have nonzero Smith factors \((1)\) and \((1,1,1,2)\). The order-two factor is the decisive integer certificate.

The second program independently enumerates all face subsets with a different arc ordering and computes exact modular boundary ranks. It verifies the characteristic-two increase in both second and third Betti numbers, consistent with the universal coefficient theorem. These field computations alone would not determine the order-two torsion; the integral reduction is essential.

The directed-module argument is proved in `RESULT.md`, not inferred from numeric calculations. Both programs were executed successfully; the stdout is embedded as `CHECK_OUTPUT.txt`. This is not an independent mathematical audit or a certification by an external authority.
