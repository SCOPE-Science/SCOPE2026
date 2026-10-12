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

# Reproducibility and proof checks

Execute `python verify.py` in the extracted artifact directory after installing `requirements.txt`. The exact output in this review was `VERIFY_OK`.

The script verifies the five right-hand sides at a proposed strictly positive equilibrium using exact rational arithmetic, checks conservation of food and the human balance identity, derives the contaminated-food quadratic, checks the infection/environmental Jacobian on the fixed-food leaf, and verifies the index test-vector identity. The rational example has \(F=9/10\), \(\widehat{\mathcal R}=2/3\), and \(\mathcal T_F=20/3\).

The proof of the strict decrease of \(C(B)/B\) and hence uniqueness for every positive parameter uses analytic implicit differentiation, not finite computation. It treats all three signs of \(\Delta=p-a_4F\) and the equality case \(\mathcal T_F=1\). The Jacobian test-vector argument establishes local disease-free stability only on fixed-mass leaves; at the equality boundary a zero eigenvalue exists. The verifier is a supplemental algebra check, not an independent audit or an exhaustive infinite-parameter certificate. No empirical or global-dynamics result is inferred.
