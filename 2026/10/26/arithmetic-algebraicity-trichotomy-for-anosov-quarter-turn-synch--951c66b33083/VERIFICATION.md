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

# Verification
Run `python3 verify.py` from the directory containing this document. The script requires only the Python standard library and prints `VERIFY_OK` after exact arithmetic checks.

For eleven actual positive-trace determinant-one matrices, including both signs of the skew parameter, the symmetric case, the unique singular case, and five powers of the cat matrix, all thirty-two initial coincidence determinants are compared with independent integer recurrence predictions. A rational formal power-series recurrence checks the normalized zeta coefficients; in the symmetric family it verifies the squared algebraic polynomial identity coefficient by coefficient. The example \(N_1=2,N_2=9\) and failure of divisibility by two are checked exactly.

Finite checks do not prove the universal theorem. The infinite-step proof uses Cayley–Hamilton, torus kernel cardinality, analytic sums of the generating series, and the rational-Puiseux residue obstruction. The exceptional time-one count and all parameter boundaries are explicitly included in RESULT.md. No external or independent validation was performed.
