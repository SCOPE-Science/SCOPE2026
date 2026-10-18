---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n≥3 and 1≤t≤n−1, with q=n−t,A=n(n−2),C=A+t, integer cokernel generator elimination with an unmatched sink yields t=1: (Z/n)^(2n−5)⊕Z/[n(n−1)²], and t≥2: (Z/n)^(2q−2)⊕(Z/A)^(t−2)⊕Z/(AC), in actual invariant-factor divisibility order, spanning trees n^(2q−2)A^(t−1)C. The q≥2 case uses elimination of u_(t+1) and unimodular w=x+(n−2)y1. At q=1 the remaining 2×2 relation matrix [[C,0],[n,A]] has gcd entries 1 since C≡−1 (mod n), Smith diag(1,AC). Independently generated integer reduced graph Laplacians and SymPy exact Smith normal forms for all 54 parameter pairs 3≤n≤11,1≤t<n, with zero mismatches. These finite tests support but do not replace unrestricted generator-proof.

## originality

PASS

PASS for the full invariant-factor interpolation at strictly partial matching deletions, a natural graph/sandpile family. Corrales–Valencia 2010 explicitly handle completely removed perfect matchings t=n, while complete multipartite critical-group theory includes no-deletion t=0; neither directly gives t between. Related Resultary geodesic subpath numbers of deleted-matching bicliques concern a different invariant. A yet-unindexed Smith form from older graph-sandpile literature remains a priority risk.

## value

PASS

Exact invariant factors are genuinely more informative than spanning-tree count; they classify chip-firing cokernels across every nontrivial partial deletion size, including both boundary t=1 and t=n−1. Natural edge-deletion interpolation is a meaningful infinite-family arithmetic structure result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
