---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed Laplacian character eigenvalues 3(W-w_i) (double per kernel line) and resistance r_i=(2/9)sum_{j != i}(W-w_j)^-1; nonconstant powered-distance eigenvalues 3r_i^p-sum_j r_j^p double. Independently constructed and inverted the exact 9-by-9 regularized Laplacian for conductances (1,1,0,0) and (1,2,3,4), checking all 72 off-diagonal resistance entries each; other three rational Gram-gap instances matched. For min conductance t, set a_j=w_j-t and q_min=1/(W-t). The identity sum_{j<k}a_ja_k/[(S-a_j)(S-a_k)]=1-2a1a2a3/[(a1+a2)(a1+a3)(a2+a3)]<=1 (with boundary cases) bounds cross terms and implies min Gram eigenvalue >=14 q_min^2/81, equality precisely 2 active directions. Strict decreasing normalized positive resistance powers give unique finite threshold p>2 when k=1,2; for k>=3 all p finite are strict; doubled Fourier sectors yield endpoint rank. Universal conclusion rests on exact algebra not sampled networks.

## originality

PASS

Compared precise mathematical statements with their strongest identified precursors and published mathematical finding searches. Originality is best-of-knowledge with explicitly named inaccessible/unindexed priority risks, not certification.

## value

PASS

The four line directions exhaust a natural connected noncyclic order-nine Cayley electrical family; sharp coercivity for every anisotropic weight and complete generalized-roundness/embedding-rank diagram are genuine structural invariants, not merely one computed graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
