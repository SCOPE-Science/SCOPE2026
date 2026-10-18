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

# Verification scope

From this directory run `python verify.py` with Python 3 and standard-library dependencies only. The program calculates the algebraic return-series coefficients in exact rational arithmetic, compares each with an independent killed Markov-chain implementation for six rational parameters through time \(25\), and checks positivity and basic identities. It also evaluates finite-length diagnostics for the three stated coefficient asymptotics at lengths \(200\) and \(400\).

The result of the packaged run was `PASS 318 exact-positive/coefficient and asymptotic diagnostics`. These computations check implementation and finite examples only. The general nonrationality, the obstruction to finite hidden-state Markov representations, the infinite Hankel-rank claim, and the asymptotic equivalences are established analytically in `RESULT.md`, not inferred from the finite checks. No separate independent audit has been performed.
