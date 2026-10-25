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

The gradient uses allowed cofactors. At rank n-1 adjugate has rank one; a Cartesian support rectangle contained in the forbidden matching forces one forbidden diagonal singleton, equivalently entire corresponding row and column zero. At rank<=n-2 all cofactors vanish. Factorization A=UV^T with r=n-2 gives k disjoint irreducible bilinear equations U_i dot V_i=0 and irreducible rank-r image of affine dimension n^2-k-4, after GL_r quotient, yielding codim 3 in X. Explicit allowed partial permutation with unused row 1,2 and columns 3,4 verifies transverse 2x2 Schur parameters and degree remains standard corank2 determinantal degree. At zero row/column loci Schur complement gives nondegenerate sum u_jv_j. Jacobian codim excludes reducibility and ensures normality by R1/S2. Independent exhaustive GF2 checks n=4 k=2 examined 16384 matrices, 2632 singular (144 corank-one extra H_i), k=4 examined 4096, 826 singular (56 extra H_i), agreeing precisely. Finite checks not the universal proof.

## originality

PASS

Generic determinantal rank singular locus is only D, whereas forcing diagonal matching zeros creates k additional singular linear loci with distinct generic slice dimensions. Boocher full PDF Theorem 1.1 studies sparse maximal-minor resolutions; Alper–Bogart–Velasco full PDF Theorem 1.2 provides general singular codimension and complexity bounds. Neither inspected result implies this k+1 primary decomposition or explicit transverse models. Giusti–Merle 1982 is highly plausible underlying prior; full text unavailable (authorized Oxford reported VPN disconnected), retained as a material priority risk, not a shortcut to failure.

## value

PASS

The all-parameter geometric classification of a natural sparse generic determinantal family supplies exact degrees, exceptional singular strata, and two local models; these are useful to sparse determinantal geometry and not an arbitrary tiny instance or purely a normality restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
