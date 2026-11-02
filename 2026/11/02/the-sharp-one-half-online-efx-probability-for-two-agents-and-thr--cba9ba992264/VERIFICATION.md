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

# Reproducibility and limits

Run `python3 verify_online_efx.py` with Python 3.9 or later in the same directory. The checker depends only on the standard library. It enumerates all \(15{,}625\) nonnegative integer profiles over \(\{0,1,2,3,4\}\) for two agents and three goods, explicitly tests the EFX inequalities, and evaluates the two-stage randomized decision tree with exact fractions, granting the third-good choice only when one of its two actually legal completions is EFX.

Observed output: `VERIFY_OK profiles=15625 min_probability=1/2 histogram= {Fraction(1, 2): 9200, Fraction(3, 4): 2800, Fraction(1, 1): 3625} upper_witnesses=2`.

The checker additionally enumerates all recipient strings for the two identical-prefix adversarial examples and verifies that one demands splitting the first two goods while the other demands pairing them. This verifies finite examples and the implementation, **not** all possible real valuations nor every randomized algorithm. The analytical case split and indistinguishable-prefix argument in `RESULT.md` establish those universal claims.

No external or independent audit was performed.
