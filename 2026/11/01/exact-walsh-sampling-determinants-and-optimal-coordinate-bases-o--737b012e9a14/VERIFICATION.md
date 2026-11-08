---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all even N>=6, p=1/(N-1), the three possible indicator covariance entries agree with C=c_N P, where P=I-B^T(BB^T)^(-1)B is the orthogonal projection onto the kernel of the unsigned incidence matrix. Eliminating the constant from the Walsh Gram, Sylvester gives its principal determinant as (4c_N)^|S| det(B_F B_F^T)/D_N. Cauchy–Binet, unsigned odd-cycle determinants ±2, and componentwise nonbipartiteness prove the full sum and rank criterion. At |F|=N each component must be odd-unicyclic, yielding 4^b, 1<=b<=floor(N/3); 3/4/5-vertex labeled component counts 1/12/162 give exactly the three factorial optimizer formulas, including 10 at N=6 and 14112 at N=8. Empty S and N=6 boundary hold. Analytic proof extends to all allowed N, not from a finite census.

## originality

PASS

Best-of-knowledge contribution is the all-subsets probability-normalized Walsh sampling determinant plus complete maximal-volume coordinate-basis topology and labeled counts, not the underlying signless Laplacian theorem or matching incidence spectrum. General unsigned incidence rank, spanning odd-unicyclic TU subgraph formulas and first-band matching spectrum are explicit prior ingredients; a full combined D-optimal sampling-design theorem was not located, but existing matroid basis literature might recast it.

## value

PASS

Uniform perfect matchings on K_N are a natural homogeneous probability model. Which edge coordinates reconstruct all first-degree Walsh information, and which maximal independent selections maximize sampling determinant, are canonical exact design questions. The result gives every subset minor, all independence boundaries, all determinant levels and all labeled D-optimal bases for infinitely many N; not merely a renaming of known edge rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
