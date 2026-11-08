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

# Reproducibility and boundaries

Run `python3 verify.py` in the directory containing the accompanying standalone script. The exact finite calculation returned `VERIFY_OK`; it enumerates all 35 degree-three monomials, 5 distinct derivative weights, 30 residual Hodge weights, 60 possible multipliers, 12 subgroup cosets, and 6 selected CM-type orbits.

The program also records, for each non-stabilizing coset representative, a concrete eigencharacter mapped outside the selected type. The counterwitness certificate covers all eleven nontrivial cosets and proves that the stabilizer is exactly the five-element subgroup.

All arithmetic is integer modular arithmetic, with no floating-point approximations or random sampling. The script verifies the finite weight and stabilizer steps; the inference to a simple sixfold uses Griffiths' Hodge/Jacobian-ring correspondence and established CM classification (Milne Propositions 1.9, 3.12 and 3.13). No independent audit, polarized product theorem, or integral isogeny-map certificate is claimed.
