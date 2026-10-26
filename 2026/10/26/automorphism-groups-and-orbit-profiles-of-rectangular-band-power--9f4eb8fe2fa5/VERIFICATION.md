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

# Verification of finite-support automorphism classification

The general proof is in `RESULT.md`. The stand-alone `verify.py` uses only Python's standard library and checks exact integer combinatorics, explicit rectangular-band setwise multiplication, support-fiber counts, and representative symmetry actions.

Run `python verify.py`. The observed result is `VERIFY_OK product_tables=(1,3),(2,2),(2,3),(3,3) maps_2x2= 2880 fiber_2x2= 7`.

The code independently constructs the multiplication tables of nonempty subsets for the four listed small base bands. In the \(2\times2\) case it enumerates all \(2!2!6!=2880\) mappings predicted by the classification and checks their bijectivity and \(15^2\) multiplication equations individually. The group-order *upper bound* and the validity for arbitrarily large finite bands are established by the mathematical proof, not by this finite test. This file records no independent audit or external certification.
