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

The weighted Cayley extension formula gives P(d(u,v)=k)=(k+1)(n-2)_{k-1}/n^k. Conditioning the squared degrees on a fixed marked path via the weighted contracted-tree Pruefer code yields E[Z|distance k]=5n-11+6/n+(k-1)(2n-k(k+1))/(n(k+1)). The n-vertex Hamiltonian-path boundary is treated directly. Using t_k=(n-2)_{k-1}/n^k, sum identities S1=1-h, S2=(n+1)h-1 and S4=(3n^2+11n+1)h-(8n+1) yield Cov(Z,d)=4-(n+6)h. The first four terms give (n+6)sum_{k=1}^4 t_k-4=8(n-3)^2(n-2)/n^4>0 when n>=4; at n=2,3 Z is constant. Janson Wiener first moment supplies the stated asymptotic, independently of the finite proof. Independently reconstructed enumerations of all n^(n-2) Cayley trees n=2,...,7 give exact covariances 0,0,-3/8,-192/125,-35/9,-131520/16807 matching formula; these are corroborative only.

## originality

PASS

Best-of-knowledge originality of the final specific quantitative/mathematical statement after semantic published-finding search and primary source comparisons; precise coverage and residual risks are recorded. No literature search is represented as exhaustive or as independent priority certification.

## value

PASS

The first Zagreb squared-degree and Wiener total-distance indices capture complementary local and global structural statistics on the same standard random-tree law. Their exact negative mixed moment, strict all-size sign and distance-conditioned regression cannot be recovered by combining their one-dimensional means. The calculation is a reusable structural covariance identity, not a routine parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
