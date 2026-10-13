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

Run `python3 verify.py` in the same directory as `RESULT.md`. Only Python 3.9+ standard-library facilities are used.

The checker reconstructs the four substituted-block profiles in a three-state binary arch automaton, confirms the level-four base case, then compares the two parity-switching recurrences as exact integer-coefficient affine identities in the variable \(q\). Consequently this part certifies the algebraic induction *scheme for all levels*, not a finite sample of substitution depths. The proof that the scheme models the correct word and that arch count equals universality index is spelled out in `RESULT.md`.

The checker separately verifies all low-level block-count errors, the morphism coding against a direct overlapping-binary-digit-pair parity calculation through \(2^{12}\), the all-prefix estimate over the first \(262144\) positions, the dyadic formula at nineteen tested scales, and brute-force subsequence universality at every prefix length up to twenty-two. These finite checks detect implementation or indexing mistakes but cannot, by themselves, establish an infinite theorem.

Observed successful output:

```
VERIFY_OK symbolic_induction=even_to_odd_and_odd_to_even small_block_bounds=yes morphism_prefix=2^12 direct_prefixes=262144 exact_dyadic_levels=19 brute_subsequences_lengths=0..22
```

No additional data files, precomputed certificates, network access, or nonstandard packages are required. No independent validation has been performed.
