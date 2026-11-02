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

# Reproduction and verification

Run `python VERIFY.py` with Python 3 and SymPy. The script constructs five first-step equations, checks the exact mean extinction-time rational function, and separately builds the full seven-state transient generator. It compares 60 exact-rational instances against this independently constructed chain. It then checks the normalized quintic derivative identity and its exact endpoint and limiting coefficients; the all-parameter uniqueness argument is the Descartes-sign proof in `RESULT.md`, not a finite numerical experiment.

For the unrestricted-allocation result, the verifier independently solves the symbolic seven-state chain for three distinct curing rates, substitutes rates `(x+h, y, x-h)` and `(x, y, x)`, factors their extinction-time difference, and proves its numerator is `h**2` times a polynomial with 55 positive integer terms in `(b,x,y,z)` where `z=x**2-h**2>0`. The leftover denominator factor has 16 positive integer terms in the same variables; the other factors are explicitly positive in the domain. Thus the symbolic certificate covers an infinite open domain exactly, whereas the exact-rational samples cross-check the model assembly.

Expected stdout reports `TOTAL_EXACT_ASSERTIONS_WITH_GLOBAL_SYMMETRY: 103`, as well as the 55/16 coefficient counts. The example optimum is isolated by a rational interval rather than accepted on floating-point root-finding alone. The verifier is finite code with ordinary symbolic algebra; no independent assessment, formal proof assistant, or external certification is asserted.
