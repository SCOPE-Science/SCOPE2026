---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every n>=9, a signed Roman function on K(n,2) labels unordered ground-set pairs in {-1,1,2}, requiring all closed-neighborhood sums >=1 and defending every -1 with a disjoint +2. With weight W and ground-degree sums s_i, T_ij=W-s_i-s_j+2f_ij, sum_(j≠i) T_ij=(n-3)W-(n-4)s_i and sum_i s_i=2W. These exclude W<=2; W=3 forces s_i<=2 and an s_i=2 by a counted positive/zero/negative star-slack contradiction. Saturation at s_i=2 forces all s_j∈{-2,2}, hence odd n and B/A part size difference three. It forces cross -1, B-internal +1, and A-internal incident sum |A|+1; an explicit defender condition for internal -1 is retained. Hamilton cycle upgrade gives odd weight 3, and cycle in A plus three disjoint edges in B gives even weight 4. Verified direct neighborhood sums and Roman defenders for constructors n=9..30 and counted initial odd optima 84,990,15444 by A-internal exhaustive enumeration. Finite checks do not establish the unrestricted lower bound.

## originality

PASS

The complement-of-triangular-graph description is equivalent to the Kneser graph, but no inspected earlier formula uses it to derive the parity gamma or complete odd optimizing labels.

A general bound encompassing the family does not cover the exact parity theorem; prior isolated cases are strictly weaker. The odd minimum-function classification is not implied by one construction.

Earlier isolated values cannot give all odd/even gamma or the optimizer classification; no covering published table was identified.

The new star-slack lower bound excludes 2, and saturation excludes weight 3 for even n; the new even construction improves 5 to 4. None follows from prior upper/lower bounds.

## value

PASS

The exact signed Roman domination number on a classical nontrivial Kneser family closes quantitative bounds for an established invariant. The star-saturation argument additionally gives complete structural classification of odd minimizers and first enumerations, rather than renaming a known special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
