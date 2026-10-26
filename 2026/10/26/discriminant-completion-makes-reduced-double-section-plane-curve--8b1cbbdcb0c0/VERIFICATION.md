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

# Verification notes

The identity \(D=(F_x)^2-4LF\) is algebraic for every \(d\ge3\). Differentiating this identity and using the Euler relation for \(f=FD\) gives the two displayed Jacobian syzygies; their determinant is exactly \(-(3d-2)^2(2d-2)f\). The determinant is nonzero in characteristic zero when \(f\) is reduced, which is the complete mathematical proof via Saito's criterion.

Run `python verify.py` after installing SymPy. Exact three-variable polynomial expansion for \(d=3,4,5\) checks the intermediate identity, both syzygies, and the determinant. The observed output for the packaged script is:

```
d=3: identities, syzygies and Saito determinant verified
d=4: identities, syzygies and Saito determinant verified
d=5: identities, syzygies and Saito determinant verified
VERIFY_OK
```

Finite checks alone do not prove universal freeness, nor do they replace checking that an input \(f\) is reduced. The cubic geometric corollary additionally uses Riemann–Hurwitz for a degree-two morphism. Independent mathematical audit was not performed.
