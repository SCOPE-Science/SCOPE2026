---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

A selected cell set with a occupied rows and b occupied columns has residual graph precisely K_(m-a) square K_(n-b). For both residual factors nonempty, residual degree m+n-a-b-2, so absence of K_(1,ell) is equivalent to a=m or b=n or m+n-a-b<=ell+1. Unique occupied support and row/column inclusion-exclusion give the all-size polynomial. For p<m selected cells, a+b<=2p forces p>=ceil((m+n-ell-1)/2); partial permutation matrices attain the bound unless all m rows must be hit. Equality forces support sizes (t,t) or, at odd L, (t,t-1)/(t-1,t), giving exactly the claimed factorial/binomial optimizer counts including t=m exceptional boundary. Rebuilt rook adjacency and residuals independently, checking the feasibility equivalence for 23 triples with m=2,3 and n<=4. The general argument is structural, not inferred from finite enumeration.

## originality

PASS

No dominating equivalent or stronger complete statement identified in the targeted primary-source and Resultary searches; assessment is best-of-knowledge, not exhaustive priority certification. A star-as-induced-subgraph condition would differ; the audited theorem explicitly uses ordinary subgraphs and fixes its indexing. Scalar isolation bounds alone do not give the complete coefficient-by-coefficient inclusion-exclusion sum or all equality-support types. The full product-isolation primary text was not retrievable for exhaustive comparison. No exact all-size star-isolation table was recovered; independent tables outside indexed sources remain possible. An extremal scalar cannot determine all polynomial coefficients; proving the support characterization and inclusion-exclusion adds a separately usable classification.

## value

PASS

For the natural two-factor rook graphs, the complete star-isolation polynomial and exhaustive parity-sensitive minimum-set classification extend scalar isolation parameters into a useful all-size invariant. Recovery of unordered factor orders from polynomial degrees and the empty-set threshold provides additional structural motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
