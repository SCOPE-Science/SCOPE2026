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

For 2<=k<=n-2 over C, Cauchy–Binet identifies Σ p_I² with det(AA^T). On chart A=[I B], d(det G)/d b_ij=2(adj(G)B)_ij; adj(G)=det G I−adj(G)BB^T shows equality of the Jacobian ideal (det G and derivatives) with entries of adj(G), not merely equality of radicals. Thus singular locus scheme has rad dimension >=2. For exact rad dimension r, choose isotropic R in OGr(r,n), dimension r(n-r)-r(r+1)/2, and a nondegenerate (k-r)-plane in R^perp/R, dimension (k-r)(n-k-r); total Grassmann codim r(r+1)/2, hence 3 at r=2. Deformation of symmetric restricted Gram is submersive in normal coordinates and Schur complement yields transverse det Sym_2=ac-b² A1, plus higher-radical degeneration to r2. OGr(2,n) irreducible for n>=5; n4,k2 splits into two P1 components. Source SymPy script independently inspected and dimension arithmetic rechecked for n<=11; universal argument is symbolic.

## originality

PASS

Friedman–Hoşten–Rosana 2026 explicitly identifies related singular ideals (Prop 2.4), gives codimension upper bound binom(k+1,2) (Theorem 2.3), and exact codimension three for k=2 (Corollary 2.5). The result strengthens that to every interior k,n and adds all radical strata, A1 local analytic model, and component classification. A separate Resultary squared-Grassmannian singularity classification addresses a coordinate-sign quotient, not this Plücker quadric. Best-of-knowledge PASS with classical orthogonal-degeneracy implication risk.

## value

PASS

The sharp uniform singular codimension and transverse type across every interior Grassmannian directly describe geometry of a canonical quadric section arising in Euclidean-distance optimization; the exceptional component split is a natural boundary classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
