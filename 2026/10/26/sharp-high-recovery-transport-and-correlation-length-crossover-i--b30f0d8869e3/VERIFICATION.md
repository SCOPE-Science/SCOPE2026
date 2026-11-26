---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof starts from the exact stationary formulas and the known unique positive optimizer root. It uses a simple-root expansion for the next-order transport terms and a two-state Gibbs chain calculation for the correlation length and susceptibility.

The supplied `verify_tep.py` uses Python, SymPy, NumPy and SciPy. The recorded run reports 67 symbolic and numerical check groups, covering stationary identities, direct-density optimization at sample parameters, and finite-rate checks of the fixed-density and optimizing asymptotics. This script checks the correlation quantities through the transfer eigenvalue and geometric sum; the equivalent density representation using \(D=\sqrt{1+4(q-1)\rho(1-\rho)}\) is established analytically in `RESULT.md`.

Finite tests corroborate the formulas and coefficients; they cannot establish the asymptotic remainders or uniform finite-ring claims. The thermodynamic limit is taken before the strong-recovery limit.
