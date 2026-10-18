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

The bundled `verify_quartic.py` directly enumerates ordered graph-pair sums in thirteen prime fields of orders \(5,7,11,13,17,19,23,29,31,37,41,43,47\), plus three quadratic extension fields of orders \(25,49,121\). It constructs each field using integer residues and an irreducible quadratic polynomial and checks the complete \(N_0,\ldots,N_4\) distribution, total representations, exact sumset size, and total squared multiplicities.

The run prints `ALL exhaustive direct convolution checks passed.` and the full actual output is embedded as `verification_output.txt`. The proof's general ingredients are the square-substitution identity, the affine involution on the square variable, the standard quadratic Jacobi sum, and the multiplicative structure of fourth powers. Those are mathematical arguments valid for every field in the stated characteristic range; the finite verifier cannot certify an infinite family on its own.

Independent audit has not been performed.
