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

The packaged `verify_154.py` was replayed from its packaged staging path before serialization. It returned `VERIFY_OK`.

Exact checks performed:

- \(X^3+X+4\) has no root in \(\mathbb F_{11}\), hence is irreducible.
- The class \(a\) has order \(1330\), verified against prime divisors \(2,5,7,19\).
- \(\zeta=a^{95}\) has order \(14\).
- Representatives \(\zeta\) and \(\zeta^3\) cover the two Frobenius orbits of primitive \(14\)-th roots in \(\mathbb F_{11^3}\).
- For each representative, all \(16383\) nonempty principal subsets were checked by exact Gaussian elimination, for \(32766\) exact determinants in total.
- Every zero count is zero for every principal-minor size from \(1\) through \(14\).

Replay output:

```text
VERIFY_OK
field=GF(11^3) modulus=x^3+x+4 elements=1331
alpha_order=1330 primitive_tests={2: 10, 5: 5, 7: 916, 19: 246}
zeta_encoded=407 zeta_order=14
primitive_14th_root_orbit_representatives_checked=2 exponents=(1, 3)
principal_subsets_per_root=16383 total_determinants_checked=32766
counts_by_size_per_root={1: 14, 2: 91, 3: 364, 4: 1001, 5: 2002, 6: 3003, 7: 3432, 8: 3003, 9: 2002, 10: 1001, 11: 364, 12: 91, 13: 14, 14: 1}
zero_counts_by_root_and_size={1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}, 3: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}}
checksum64=18127865642452742776
```

The checksum in the replay output is only a deterministic smoke check; the mathematical certificate is the exhaustive zero-count test together with the exact field and order assertions. No floating-point arithmetic is used. The final transfer to the complex order-
\(154\) matrix uses Theorem 1.4 of arXiv:2505.24326.
