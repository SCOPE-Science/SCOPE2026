---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n>=3, dominating subsets of Cr_n are exactly whole shores, selections of at least two from both shores, or singleton in one shore together with its matched partner in the other and at least one further opposite vertex. These disjoint cases give D_n(z)=2z^n+((1+z)^n-1-nz)^2+n z²(2(1+z)^(n-1)-1). Crown distances are 1 across nonmatched sides, 2 within a side and 3 only for matched opposite pairs. Removing these disjoint forbidden pairs from the complete partner graph still permits a perfect matching for any even chosen set size>=4. The only size-2 dominating subsets are matched pairs and cannot partner. Therefore P_pr2=(D_n(z)+D_n(-z))/2 - n z²; minimum 4 with coefficient C(n,2)^2+2nC(n-1,2)+2*[n=4]. Independent literal matching enumeration and complete histograms for n3..6 agree.

## originality

PASS

The all-set semipaired crown polynomial is not a generic paired-domination polynomial: matched opposites are exactly distance-3 partner obstructions. The all-set characterization and count are not supplied by known scalar semipaired inequalities or the published paired complete-multipartite result.

## value

PASS

Crown graphs provide an exact tractable bipartite benchmark for semipaired domination, known generally hard on bipartite graphs. The full coefficient polynomial, all minimum solutions and total count reveal the size distribution rather than just the optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
