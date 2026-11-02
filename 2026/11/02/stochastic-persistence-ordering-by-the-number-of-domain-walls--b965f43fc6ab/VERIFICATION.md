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
Run `python verify.py` using a standard Python 3 interpreter. The script exhaustively lists both initial signs and every switch subset for lengths \(2\) through \(14\), calculates normalized masses using exact rational arithmetic, and checks the run-count formulas, switch-pair equality, decreasing likelihood-ratio formula, all conditional tail orders and eleven rational persistence values (including boundaries). Its expected output is recorded verbatim in `verification_output.txt`.

The verification uses exact integer/fraction arithmetic, not floating-point heuristics or stochastic simulation. Exhaustion is limited to the listed finite horizons and does not prove the theorem at all lengths; the analytic binomial identities, likelihood-ratio argument and switch-indicator coupling supply that proof. The public mathematical claim has not undergone independent audit.
