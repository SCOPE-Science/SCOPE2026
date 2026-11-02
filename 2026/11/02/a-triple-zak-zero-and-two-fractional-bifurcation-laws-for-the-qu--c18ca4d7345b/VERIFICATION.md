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

# Reproducible algebraic checks

Run `python check.py` with SymPy installed. The script checks exact discriminant and five-term polynomial positivity identity, all endpoint evaluations, the exact algebraic critical point and derivative slope, the cubic degeneration at the integer limit, and the exact translated polynomial used in the \(2/3\)-power proof. It also evaluates the original finite Zak sum and the derived polynomial at 35 distinct pairs of real parameters, yielding numerical agreement within the stated tolerance. Expected output:

`EXACT_ZAK_CUBIC_OK; discriminant, Bernstein positivity certificate, signs, critical slope and endpoint cusp; 35 direct-sum comparisons`

The infinitely many real parameter values and the limiting exponents follow from the displayed analytic proof in RESULT.md. The numerical comparisons cannot certify infinite-domain uniqueness. No independent audit was performed.
