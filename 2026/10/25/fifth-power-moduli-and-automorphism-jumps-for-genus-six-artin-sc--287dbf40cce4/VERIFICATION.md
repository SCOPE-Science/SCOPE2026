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

The proof treats all algebraically closed characteristic-two ground fields, every parameter including zero, and the precise category of equipped \((\mathbb Z/2)^2\)-Galois covers.

1. Reconstruct the character subspace with the basis \(x^5\), \(\alpha x^5+\lambda x^3\), then check that all three nonzero characters have an odd pole of degree five at infinity.
2. Verify the four monomials in the characteristic-two binomial expansion of the fifth power and of the cube. Eliminating \(x^4\) and \(x^2\) via Artin–Schreier reduction gives equation (1) in `RESULT.md`.
3. Equality of reduced character subspaces forces \(a^5\in\mathbb F_4^\times\), then \(a^5=1\) for nonzero parameters and \(\mu=\lambda a^3\). The surviving linear terms force \(b\in\mathbb F_{16}\) and, when nonzero, \(b^3=\lambda^{-1}\).
4. Run `python3 verify_cover_moduli.py` from the same extracted directory. The checker requires no third-party dependencies; it enumerates affine transformations in \(\mathbb F_{256}\) using direct expansions, independently obtaining the three stabilizer sizes and sample parameter orbits.

Observed finite-field checker output:
```
VERIFY_OK finite_field=GF(256) alpha_F4=189
VERIFY_OK lambda_0 base_self_maps=240 cover_automorphisms=960
VERIFY_OK lambda_in_mu5 base_self_maps=4 cover_automorphisms=16
VERIFY_OK lambda_outside_mu5 base_self_maps=1 cover_automorphisms=4
VERIFY_OK exact_coarse_parameter=lambda^5 sample_orbits=1+5+5
```

**Limits.** Finite-field enumeration alone is not a proof for all \(k\), and no claim of finite-field descent, independent validation, full unmarked-curve automorphism groups, or isomorphism classification of abstract curves is made. The proof supplies the infinite-field part; the checker supplies a separate finite sanity check. Independent audit: not performed.
