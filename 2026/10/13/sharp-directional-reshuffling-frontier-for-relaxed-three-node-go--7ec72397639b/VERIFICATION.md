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

## Reproducible checks

Run `python verify.py` with `sympy==1.14.0` installed. The script reconstructs both two-step Gram matrices from the four independent sequences and the two permutation sequences, checks their symbolic difference and the two bisector eigenvalues, tests several exact rational orthogonal decompositions, and verifies the physical three-node path example with exact rational transition matrices. All 45 reported checks passed on the included source file. No random Monte Carlo evidence is needed.

## Logical scope

The eigenvalue calculation in `RESULT.md` proves the threshold for every real angle \(0<c<1\) and every relaxation \(0<\omega<2\). The finite checks do not prove the infinite continuum of parameter values. The same argument shows that \(\omega=2\) is a boundary degeneracy at which the Gram difference vanishes. No claims are made about later epochs or floating-point behavior. No independent audit has been performed.
