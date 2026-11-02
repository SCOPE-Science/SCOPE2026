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

Run `python3 verify.py` with Python 3 and no external dependencies. The verifier evaluates the finite parity-coset distributions and independent signs using `fractions.Fraction`. Its output is `VERIFY_OK exact_cases=16774 exhaustive_integer_coefficient_matrices=15625`.

The exhaustive integer-grid test enumerates all six off-diagonal positions from five integer values, for 15,625 matrices; it does not exhaust all real matrices or all feasible sign laws. The proof in `RESULT.md` establishes the universal assertion analytically through pairwise moments, three disjoint edges, the fourth parity moment, and Walsh inversion. No independent scientific audit is asserted.
