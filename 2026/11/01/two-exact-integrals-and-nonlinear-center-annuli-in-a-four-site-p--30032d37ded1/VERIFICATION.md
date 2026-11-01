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

# Reproduction and limits

Execute `python verify.py` in a Python environment containing SymPy and NumPy. The program checks the two exact conservation derivatives, all components of the Nambu identity, and the central-line Jacobian symbolically; it then compares the three-dimensional reduced field with the original four-oscillator system at 280 reproducibly seeded interior configurations. It checks the two conservation derivatives and the exact elliptic versus hyperbolic inequality for the same samples.

The supplied verification program was executed successfully. Neither the numerical cases nor the symbolic checks alone certify existence of nonlinear periodic curves. That conclusion is proved in `RESULT.md` by the implicit function theorem, negative-definite Hessian, Morse lemma, and a nonvanishing vector field on each compact invariant level. No independently conducted external audit is represented.
