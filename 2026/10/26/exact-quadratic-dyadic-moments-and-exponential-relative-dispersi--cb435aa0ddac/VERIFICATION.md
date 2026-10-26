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

# Verification and proof boundary

Run `python3 verify.py` in a directory containing the accompanying standalone script. It requires only Python 3's standard library. The script checks all values of A383066 and its independently constructed divisor-pair tree through depth 12, computes the exact integer transfer of the quadratic observables, checks the resulting fourth-order recurrence, and compares the first nine quadratic row sums with the claimed values.

The result obtained from the packaged script was:

`VERIFY_OK depths=12 exact_tree_nodes=8191 moment_recurrences=9 base_terms=PASS`

The mathematical proof is the tree invariant, the three child-pair identities, and the resulting exact four-state transfer. The rational generating function follows algebraically and is not inferred from the finite list. Partial fractions give the infinite closed form; the known exact first moment and a strict algebraic comparison of positive spectral radii yield the exponential relative-variance asymptotic. The finite check is reproducibility evidence only; it neither establishes the infinite theorem nor determines bibliographic priority.

No external independent mathematical audit has been performed. The conclusion does not assert a limiting probability law or quantify how many dyadic entries are large relative to their mean.
