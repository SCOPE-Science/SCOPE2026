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

## Reproducible finite checks
Run `python3 verify.py` with Python 3.9 or later. The checker uses only the standard library. It compares fiber sums and closed counts across 6,897 nonnegative integer instances; independently checks every defining tetrahedral facet at both translated-segment endpoints on a second finite grid; and verifies the polynomial factorization, discriminant formula, nonempty thresholds and first high-residue transition by exact integer arithmetic.

## Scope of verification
The analytical proof handles every integer \(m\ge2\), \(L\ge1\) and every integer dilation \(t\ge0\); no finite enumeration certifies infinitely many parameters. The checked cubic roots are algebraic properties of the eventual polynomial, not extensions of the lattice-count interpretation to negative or noninteger dilation factors. Historical-priority comparisons are based on the identified primary sources and search results and are not an exhaustive bibliography.

## Actual replay
`VERIFY_OK fiber_counts=6897 direct_endpoint_counts=553 exact_polynomial_roots_checked=True` was produced by running the embedded `verify.py` after writing the new package file.
