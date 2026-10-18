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

# Exact reproducibility checks

Run `python verify.py` with an installation of SymPy. The checker recomputes the two quotient binary-quartic invariants, fully verifies the cleared equality polynomial and its expansion in symmetric variables, derives the symmetric-Jacobi quartic invariant \(J_*(r)\), verifies the bidegree-four residual polynomial and the complex rational parametrization, checks its four generically distinct fourth-root images, and tests the birational inverse. It also verifies the smooth nonsymmetric specialization \(a=2+8\sqrt2/3\), \(b=2-8\sqrt2/3\) and the three exact \(j\)-values.

The expected terminal line is `VERIFY_OK: quartic j formulas; complete coincidence factorization; bidegree-(4,4) off-diagonal relation; birational parametrization; smooth nonsymmetric witness`.

The checker is exact symbolic arithmetic; it is not an independent proof assistant or external audit. The field-degree and no-boundary-component arguments in RESULT.md supply the general irreducibility/completeness proofs. No test asserts all possible global moduli equivalences or an unrestricted priority claim.
