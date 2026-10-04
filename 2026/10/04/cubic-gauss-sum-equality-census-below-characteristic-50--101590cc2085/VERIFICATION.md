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

The exact checker is `verify.py` and uses only the Python standard library. It implements the odd-characteristic criterion of Proposition 2.9 for every character exponent at every odd prime \(p<50\). A deterministic subset of unit multipliers is used only to form a coarse partition; because equality requires agreement for every unit, separating at this stage is logically conclusive. Every cell that still contains more than one Frobenius orbit is then checked against the complete unit group.

The recorded replay output is in `verify_output.txt` and states:

`VERIFY_OK primes=14 total_characters=385032 exceptional_primes=[11, 23, 37] p37_classes=5 p37_orders=[[14, 14, 2], [42, 42], [28, 28], [42, 42], [28, 28]] order28_digits=[45,45,63,63]`

The computation proves only the finite range stated. It does not numerically approximate Gauss sums and does not infer anything beyond the published exact criterion.
