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

For m,n≥2, 2-token vertices partition into X_A=2-subsets of A, Y=mixed pairs, X_B=2-subsets of B. The token graph is connected and bipartite. For its signless Laplacian Q, the equitable quotient B has rows (2n,2n,0), (m−1,m+n−2,n−1), (0,2m,2m). Direct multiplication gives B(n(n−1),(m−1)(n−1),m(m−1))^T=2(m+n−1) times the vector. Every entry is positive; lifting across cells and using irreducible Perron–Frobenius yields rho(Q)=2(m+n−1). Bipartite signature similarity gives rho(L)=rho(Q). Source boundaries m=n=2 are covered; m=1 excluded. Independent reconstruction of 25 whole token matrices 2≤m,n≤6 matched full spectra and quotient, but unbounded correctness rests on the positive-eigenvector argument.

## originality

PASS

Song et al prove the same value as a universal lower bound and equality for balanced K_{n,n} only. Their result does not imply unbalanced equality. Reyes–Dalfó–Fiol handle bipartite distance-regular token bases, which do not include unbalanced complete bipartite graphs because such bases are not regular. The new all-unbalanced exact formula removes that parameter restriction.

## value

PASS

It sharpens a stated general lower bound to exactness on every nonstar complete bipartite 2-token graph by a small but revealing Perron quotient witness. The unbalanced family is natural and not a parameter substitution within the old balanced/distance-regular proofs. It identifies a non-obvious spectral-radius rigidity and provides a usable exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
