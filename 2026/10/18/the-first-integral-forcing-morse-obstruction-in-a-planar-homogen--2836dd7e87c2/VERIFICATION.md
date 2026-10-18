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

# Exact verification

Execute `python3 verification.py`. The verifier requires only the Python 3 standard library and uses integer and rational arithmetic. Observed output: `PASS: 14 exact identities / principal-minor certificates`.

It reconstructs the field, the quartic and sextic coefficients; verifies both exact Gram identities and all seven positive leading principal minors; and checks the necessary Hessian constraints at \((1,0)\), \((1,1)\), the angular derivative at \((1,0)\), and the final positive derivative at \((2,1)\).

These finite exact computations verify the advertised algebraic certificates, not an arbitrary infinite sampling. Sylvester's criterion and the homogeneous Taylor leading-term argument yield the universal conclusions. No external independent verification has been performed. Local absence of a Morse Lyapunov function does not imply absence of all smooth Lyapunov functions.
