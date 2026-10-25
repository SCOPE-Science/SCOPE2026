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
# Verification of the wheel forcing formula

Execute `python3 verify.py` in the same directory as this file. The code is self-contained and requires only standard-library modules.

- Directly simulates every initial assignment among \(5^{n+1}\) possibilities for each \(5\le n\le7\), rejecting improper initial conditions and iterating the local rule until no further move is possible.
- Independently enumerates rim words containing seeded three-colour vertices and isolated unseeded holes through \(n=9\), with a separate surjectivity test when the hub is not seeded.
- Enumerates every independent rim hole mask through \(n=12\) and compares with the closed binomial expression.
- Verifies the exact seed-size polynomial coefficients and the minimum seed coefficients for all displayed orders.

Observed output ends with `VERIFY_OK (64 independently cross-checked identities)`; the separately listed orders \(n=5,6,7,8\) have minimum-seed counts \(120,48,336,96\). The computational tests are finite, while the proof's if-and-only-if decomposition and cyclic colour count apply to every integer \(n\ge5\). No independent audit has been performed.
