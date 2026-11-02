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

# Reproducibility

Run `python verify_path_reps.py` with Python 3. The script is standalone, imports only the standard library, and checks the following distinct consequences of the theorem.

1. All induced-subgraph run types on vertex sets of sizes \(0\) through \(10\) are enumerated; every domain-type count agrees with the binomial/multinomial formula, and all complex simple counts agree with the independently expanded Euler product. The resulting values are \(1,2,4,8,12,24,36,63,99,162,244\).
2. For sizes \(0\) through \(6\), every possible domain and range and all bijections between them are examined, accepting only graph isomorphisms; this direct count agrees with the block-size-squared weighted group cardinality.
3. For sizes \(1\) through \(4\), the entire monoid is enumerated and **every pair** of restriction–Möbius basis elements is multiplied by explicitly expanding restrictions and composing partial maps. Each result equals the predicted groupoid product or zero.

The recorded tests returned `VERIFY_OK path graph partial-automorphism matrix blocks and simple modules` and `MOBIUS_OK` for sizes 1 through 4. These checks are finite verifications; the unrestricted theorem is proved symbolically in `RESULT.md`. In particular, positive-characteristic semisimplicity and asymptotic estimates are not claimed.
