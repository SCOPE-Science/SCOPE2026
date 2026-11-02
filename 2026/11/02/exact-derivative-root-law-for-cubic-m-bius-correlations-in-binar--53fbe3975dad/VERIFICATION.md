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

The standalone verifier `verify_cubic_mobius.py` uses root enumeration and formal derivatives of cubic polynomials for Möbius signs, without using the Berlekamp discriminant or the claimed closed formula. It independently forms the shift polynomial, computes its formal derivative, and counts rational derivative zeros. Run with `python3 verify_cubic_mobius.py` (Python standard library only).

Observed output:

```
PASS field_size 2 shift_sets 3 cubic_terms 24
PASS field_size 8 shift_sets 255 cubic_terms 130560
PASS field_size 32 shift_sets 10 cubic_terms 327680
VERIFY_OK shift_sets 268 cubic_terms 458264 sharp_even_degree_control 32
```

Over \(\mathbb F_8\) every nonempty shift subset is checked. Over \(\mathbb F_{32}\) ten shift sets are tested. A separate \(\mathbb F_4\) control gives correlation \(32\) for two distinct shifts where the proposed odd-degree-extension critical-point rule would instead give zero. The unrestricted proof uses the cited Berlekamp/Pellet formulas, bijections, and additive-character orthogonality; finite checks do not establish the infinite-field result. No independent mathematical audit has been performed.
