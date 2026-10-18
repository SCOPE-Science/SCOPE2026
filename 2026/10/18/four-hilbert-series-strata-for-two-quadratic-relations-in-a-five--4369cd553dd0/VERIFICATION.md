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

The proof is a direct calculation of exterior wedge images and a Gaussian-subspace counting argument, uniform in field characteristic. Check the count formulas by evaluating Gaussian coefficients, and execute `python verify.py` for a complete independent rank census of all \(174251\) binary pencils. The executable enumerates reduced echelon bases of two-subspaces without duplications and calculates degree-three and degree-four wedge images directly. Binary expected counts by Hilbert series are \(1085,16926,52080,104160\). A direct symbolic expansion verifies \(C_{5,0}=q(q-1)C_{5,1}\). Additional sampled wedge-rank checks over the finite fields of orders three, four, five, and seven corroborated the classification; they are not an exhaustive general-q verification. Independent audit: not performed. The binary line census is already covered by Shaw-Maks-Gordon (2005); the asserted contribution is the uniform prime-power theorem.
