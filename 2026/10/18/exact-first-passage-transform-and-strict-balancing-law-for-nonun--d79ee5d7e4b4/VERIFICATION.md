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

The proof uses exact product transition probabilities for independent Poissonized coordinate refresh processes, the strong Markov convolution at first hitting, the small-parameter expansion of the ratio of two Laplace resolvents, and the strict Karamata comparison of logarithmic product factors. These steps cover all positive probability vectors with a fixed finite number of types and common loss probability from zero to strictly less than one.

Run `python3 check.py` from the extracted package directory. It uses only Python's standard library (`fractions` and `itertools`) and exact rational Gaussian elimination. Its matrix calculations are separate from the subset-sum calculation and check expected values, generating functions, and finite strict balancing cases. The observed result is `PASS: 207 exact rational checks; full matrix mean/PGF, sample strict minimizers.`

These finite diagnostics cannot prove the theorem for arbitrary type count or real-valued sampling probabilities; those quantifiers are resolved by the written analytical proof. They do not verify novelty or independence and are not a substitute for external mathematical review.
