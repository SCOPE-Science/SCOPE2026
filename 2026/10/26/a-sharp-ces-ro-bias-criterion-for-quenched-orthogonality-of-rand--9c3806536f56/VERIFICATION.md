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

`verify_sign_mask.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run `python verify_sign_mask.py` to check the finite mask and input spaces for horizons 1 through 5, including biased and deterministic masks, six predictable-sign families, the exact centered second-moment relation, cross-mean relation, and maximal finite-horizon deterministic bias. The script's observed output is `PASS: 3116 exact rational identities and finite-horizon extremal checks`.

The actual infinite proof requires the independent-variable strong law and a vector martingale functional CLT. No finite computation can certify those statements. The theorem excludes masks dependent on the chosen predictable family and requires fixed-rule-before-mask quantifiers.
