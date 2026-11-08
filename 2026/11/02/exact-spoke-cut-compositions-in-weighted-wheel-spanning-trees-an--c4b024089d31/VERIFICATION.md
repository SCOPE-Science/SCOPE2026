---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A spanning tree with k spokes necessarily has k missing rim edges, forming k path components with exactly one spoke each; alternation of cut/spoke marks gives a bijection between pointed trees and a root vertex times ordered weak compositions of n−k into 2k gaps. Counting gives kc_nk=n*binom(n+k−1,2k−1), component-size fiber multiplicity product s_i, and Chebyshev determinant normalizer. For t=s/n², c_nk/n^{2k} -> 2/(2k)!, with uniform summable (4s)^k/(2k)! bound, so TV Poisson-even limit; simplex lattice weak convergence and Dirichlet aggregation give spatial law. Independently enumerated 33 spanning-tree/spoke classes and verified the marked composition bijection directly for n=3..8, rather than only trusting source checker.

## originality

PASS

Classical matrix-tree rooted-forest determinant and Chebyshev wheel count are prior and expressly excluded from novelty. Grunwald–Mednykh 2019/2020 primary texts count rooted forests and cone spanning trees, but do not describe the conditioned alternating spoke/cut gap law or joint Poisson-even/Dirichlet critical scaling in inspected full PDFs. Avena et al. general determinantal root-process theory is background but need not directly imply the joint cut/length distribution.

## value

PASS

The exact conditioned spatial law and joint critical limit supply a complete natural distribution for a simple weighted spanning-tree family; they distinguish root count from geometry of resulting forest components and are useful for weighted random spanning-tree scaling questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
