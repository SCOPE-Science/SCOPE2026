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

Pinned RESULT.md uses unsigned incidence B of K_n minus t pairwise disjoint edges and the exact identity L(line graph)=diag(d_u+d_v)-B^T B. Its rational determinant reduces to pair-difference, pair-constant, unpaired-vertex difference, and two-dimensional quotient subspaces, giving the polynomial in U,V,W,Q. Exact factor cancellations at t=1,r=1,r=2 avoid false spectral poles; t=0 and r=0 handled separately. For t>=2,0<r, discriminant (n-3)^2+8(t-1) lies between nearby squares with parity exclusion; for t=1,n>=5 the W discriminant (n-3)^2+8 is nonsquare. Thus Laplacian integral iff t=0 or 2t=n or (n,t)=(4,1). Independent symbolic line-graph characteristic polynomials matched 14 legal n,t pairs (n=4..7).

## originality

PASS

Cámara--Haemers (2012) analyzes spectra of the base almost-complete graph, not the Laplacian of its line graph. The classical incidence identity and general integral-graph literature provide the technique but not the complete two-parameter factorization and sharp integrality boundary found here. Possible known formulas under cocktail-party line-graph terminology remain a priority risk.

## value

PASS

The full Laplacian spectrum and exact sharp integrality threshold form a natural all-order spectral classification of an explicitly motivated graph family. The isolated n=4,t=1 exception and cancellation edge cases are mathematically informative, not a tiny arbitrary gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
