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

# Verification information

The analytic argument in `RESULT.md` proves the claim; `verify.py` performs exact symbolic cross-checks for the derivative identity, linear quotient evolution, invariant-wedge normal derivative, and rational examples. Run with `python verify.py` in an environment providing SymPy. The script reports success after all assertions and prints the rational wedge-boundary expression. The finite checks establish algebraic agreement only; they do not certify statements for every initial condition or every time.

The model is defined until first contact with \(x=0\), because continuation under a constant positive harvest would enter nonbiological negative prey abundance. Strict positivity of the predator before contact follows from the scalar linear differential equation, and the positive solution within an invariant wedge remains globally defined. The proof requires smoothness of the feeding response near \(K/2\), and the rational response obeys this assumption for the displayed parameter range.

No independent mathematical audit has been performed.
