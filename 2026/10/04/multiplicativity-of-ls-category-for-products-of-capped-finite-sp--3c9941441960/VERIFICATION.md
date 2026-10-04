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

The quantified theorem is proved symbolically in `RESULT.md`. The computational artifact is a regression check of the finite order-theoretic mechanism, not a certificate for the universal quantifiers.

`artifacts/verify.py` checks four representative products of capped antichain bases, including a three-factor product. For every test case it verifies:

- the expected product number of global maxima;
- coverage by principal opens at those maxima and contractibility of each such open via its maximum;
- for every pair of distinct global maxima, existence of a differing coordinate whose two-top slice lies below one of the pair and hence inside any lower set containing both;
- absence of beat points in the tested two-top slice; and
- order preservation of the explicit factor retraction onto that slice.

The recorded replay output is:

```text
CASE [(2, 2), (2, 2)] points 16 maxima 4 maximal_pairs 6
CASE [(2, 2), (2, 3)] points 20 maxima 6 maximal_pairs 15
CASE [(3, 3), (2, 2)] points 24 maxima 6 maximal_pairs 15
CASE [(2, 2), (2, 2), (2, 2)] points 64 maxima 8 maximal_pairs 28
VERIFY_OK cases=4 maximal_pairs=64
```

The computation tests only capped antichain bases of the displayed sizes. It neither enumerates arbitrary finite bases nor substitutes for the Stong-core argument in the proof.
