---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For all k>=3 and r>=3, the binary-edge-status map on k-uniform loose r-cycles has exact mixed-edge transfer M=[[q-1,q],[q,q-1]], q=2^(k-2), with eigenvalues B=2^(k-1)-1 and -1. Definite edges force both core bits and private vertices, so a prescribed status word has fiber equal to the product of constrained mixed-run matrix powers; all mixed has trace M^r=B^r+(-1)^r. Adjacently opposing forced colors yield zero. For >=2 definite edges, bound each entry by (B^ell+1)/2 and use m_a m_b<=m_(a+b) to obtain strict runner-up separation from the 2r single-definite words with fiber (B^(r-1)+(-1)^(r-1))/2. T cyclic status adjacency matrix eigenvalues 1,1±sqrt2 reproduce known smooth-word count. Independently enumerated all vertex subsets and output-word fibers for k=3,r=3..5; k=4,r=3..4; k=5,r=3; k=6,r=3: all exact fibers, maximum and runner-up multiplicities match. Finite runs corroborate rather than prove all r,k.

## originality

PASS

No inspected primary theorem or relevant published finding implies the additional exact claim; the explicitly identified preexisting components are excluded from novelty. This is best-of-knowledge only, with detailed source-access and equivalence risks below.

## value

PASS

Edge-status rough approximation is a natural many-to-one observation of a binary vertex subset in a uniform hypergraph. Exact inverse-image multiplicities measure worst-case ambiguity, quantify a unique most ambiguous outcome, and identify exactly 2r strict runner-ups; general k-dependence with an information-loss interpretation is a motivated structural extreme not inferred from the pre-existing observation count or k=2 graph case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
