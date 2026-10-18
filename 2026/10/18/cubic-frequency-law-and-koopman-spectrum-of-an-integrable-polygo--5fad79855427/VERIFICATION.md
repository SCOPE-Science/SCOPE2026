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
# Verification evidence

Run the included `verify_square.py` using Python 3 and no third-party libraries. It performs exact arithmetic in \(\mathbb Q(\sqrt2)\) rather than numerical fitting. The observed output is:

```
VERIFY_OK: exact Q(sqrt(2)) edge maps, polygon area, twist and cubic density identities
Outer-annulus area = (11/2)+(-7/2)sqrt(2)
```

The checker verifies a determinant-one corner map, the exact polygon vertex chain, two required affine edge joins, the full area polynomial, sample exact twist identities and the algebraic density simplification. Its finite checks are not a proof of the full dynamical statement; the measure-theoretic conjugacy and Fourier-mode argument are proved in `RESULT.md`. No external or independent validation was performed.
