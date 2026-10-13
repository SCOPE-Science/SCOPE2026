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

The bundled `verify.py` is a standard-library exhaustive verifier for all finite claims in the finding.

It checks:

- all 105 perfect matchings of \(K_8\);
- all 416 one-factorizations containing the fixed factor \(01|23|45|67\);
- exact partition validity for every factorization;
- that every triangle in a one-factorization is trichromatic;
- the exact histogram of the number of realized three-colour sets:
  \(7^{\times2},11^{\times42},13^{\times28},17^{\times168},26^{\times112},35^{\times64}\);
- for every one of the 416 instances, full qualitative coverage iff every pair of factors has Hamiltonian union;
- the seven-matchings finite lemma used in the converse hand proof;
- canonicalization under all vertex relabellings, yielding exactly six one-factorization classes and exactly one qualitative/perfect class;
- the atom-permuting automorphism group of the good class, of order \(42\), with vertex-orbit sizes \(1,7\);
- direct canonicalization of all eight seven-point deletions, yielding exactly two classes with multiplicities \(1,7\).

The current run returns:

```
fixed_factor_factorizations=416
isomorphism_classes=6
triangle_triple_histogram={7: 2, 11: 42, 13: 28, 17: 168, 26: 112, 35: 64}
qualitative_fixed_factor_instances=64
qualitative_isomorphism_classes=1
good_automorphism_group_order=42
good_vertex_orbit_sizes=[1, 7]
seven_point_deletion_classes=2
seven_point_deletion_multiplicities=[1, 7]
VERIFY_OK 164307 exact assertions
```

The verifier does not re-prove the published theorem that every seven-point qualitative representation uniquely extends to eight points; that infinite-literature dependency is isolated explicitly in the proof.
