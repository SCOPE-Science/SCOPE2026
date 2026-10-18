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

# Reproducibility and limitations

Run `python verify.py` with SymPy installed. The checker verifies the homogeneous sextic identity, its three derivatives, the unique base-cubic node Hessian, absence of a quadratic relation among the three cubed binary linear forms, the 27-element projective diagonal stabilizer, and a saturated primitive lattice minor.

It also visits every projective point over each of \(\mathbb F_5\) and \(\mathbb F_7\), compares direct vanishing of the six partial derivatives with membership in the four predicted reduced components, and prints `VERIFY_OK` on success. Successful run checked 3906 points over \(\mathbb F_5\) and 19608 over \(\mathbb F_7\), with 294 and 690 singular points, respectively.

The proof of the characteristic-zero theorem is mathematical, not extrapolated from finite enumeration. The checker does not calculate a primary decomposition of the full Jacobian ideal, validate nongeneric local germs, or certify publication novelty.
