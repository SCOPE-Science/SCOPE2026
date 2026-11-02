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

# Reproduction

Run `python VERIFY.py` in an environment with SymPy. The file requires no source downloads or other repository artifacts.

It constructs all varying BDF4 interpolation coefficients from the four-step mesh \((1,r,r,1)\), checks the difference recurrence and exact four-step characteristic polynomial, and recomputes the four cubic Schur inequality certificates. Positivity is proved for all \(r>0\) by substituting \(t=r+r^{-1}=u+2\) and replacing \(\sqrt{21}\) with the upper bound 5 or lower bound 4 as appropriate in every coefficient. It also checks the exact limiting polynomial and six rational examples.

# Limits

Finite root checks do not prove the infinite statement; the polynomial inequalities do. The computation establishes no general nonperiodic-grid stability, external certification, or convergence guarantee for nonzero right-hand sides. No independent audit has yet been performed.
