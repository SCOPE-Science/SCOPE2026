---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n>=3, perfect matchings are derangements pi. After fixing F, the missing domain U must biject to pi(U) avoiding diagonal cells. If |U|<=1 completion is forced. For U={i,j} the only alternate assignment swaps pi(i),pi(j); it exists unless pi(i)=j or pi(j)=i. If |U|>=3, a nonadjacent pair in permutation-cycle graph can be swapped, except when every pair in U is adjacent, which forces U to be exactly a 3-cycle; reversing that 3-cycle then gives a second derangement. Hence complete all-F criterion, coefficient n-t2(pi), aggregate n*d_n - C(n,2)*d_(n-2). Independent direct count of completing derangements verified n=3,4,5,6 with respectively 16,144,1408,16960 (pi,F) cases (18,528 total), including fixed and aggregate coefficients. Infinite theorem rests on cycle argument, not finite checks.

## originality

PASS

Based on source-level and current-literature comparison, the complete surviving claim is not established by the named prior results. This is a best-of-knowledge priority judgment, not a guarantee of global novelty.

## value

PASS

For the canonical perfect-matching-deleted bipartite graph, classifying every forcing subset rather than just the known scalar minimum yields exact cycle-type sensitivity n-t2(pi), complete fixed-matching and aggregate enumerators. These distinguish matchings whose standard forcing polynomial cannot distinguish; the natural forcing-subset invariant is motivated by uniqueness of completion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
