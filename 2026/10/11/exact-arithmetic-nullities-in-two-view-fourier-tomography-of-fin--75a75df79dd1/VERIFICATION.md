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

# Verifiable finite tests and theorem boundaries

Run `python3 verify.py` using Python 3 standard library. It builds the conic directly over \(\mathbb F_q\) for \(q=3,5,7,9,11,13,17,19,25,49\), enumerates each projective line, forms the exact integer indicator matrix of all line fibres, and finds its rank by Gaussian elimination in auxiliary prime fields. In quadratic extensions, arithmetic is implemented directly in \(\mathbb F_p[z]/(z^2-\nu)\) with explicit nonsquare \(\nu\). The rank procedure does not use the two-involution/nullity proof. Each prediction is computed separately from multiplicative-order and quadratic-character conditions.

The extracted checker completed all \(1,914\) distinct pairs of nonisotropic directions, confirming the predicted kernel dimensions and the totient enumeration; where isotropic directions exist, every isotropic single-view incidence matrix was verified injective. The output terminates:

`VERIFY_OK independent_exact_modular_incidence_rank_tests= 1914 extension_fields=[9,25,49] pair_count=PASS isotropic_single_view=PASS`

The tests establish only the indicated finite cases. The unbounded theorem follows instead from the cyclic norm-one torus, the fibre-reflection characterization and quotient involution orbit counts. No independent external audit or independent novelty certification has been performed.
