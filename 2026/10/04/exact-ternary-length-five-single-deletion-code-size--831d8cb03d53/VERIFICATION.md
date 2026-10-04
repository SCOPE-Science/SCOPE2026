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

The exact theorem is certified by `verify.py` using only integer arithmetic and the Python standard library. The script reconstructs every ternary length-five word and every ternary length-four deletion output, verifies pairwise disjoint deletion shadows for the 24 displayed codewords, and checks the complete rational dual certificate.

The dual weights have common denominator \(14\). Their integer numerators sum to \(348\), and the script verifies that the distinct deletion shadow of every one of the \(243\) possible input words has numerator weight at least \(14\). This proves \(14|C|\le348\) for every one-deletion-correcting code. The calculation is exhaustive over the finite domain; no probabilistic sampling or optimization solver is involved in replay.

Expected output:

`VERIFY_OK N(5,3,1)=24 dual=174/7 min_scaled_shadow_weight=14`

`certificate.json` records the checked domain sizes, the exact objective \(174/7\), the minimum verified shadow weight, and the resulting upper bound. The package does not classify all maximum codes or address other alphabet sizes or lengths.
