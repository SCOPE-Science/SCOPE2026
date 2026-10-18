---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

F_m=t∏a_i−Σb_i²∏_{j≠i}a_j is primitive linear in t, so irreducible; each G_i similarly. At corank 1 at least one diagonal adjugate derivative is nonzero because adj(M)=c vv^T and some v_j²≠0 over C; hence singular iff corank≥2. Inverting nonzero leaf diagonals and separating k=0,1,2,≥3 zero leaves yields EXACT union Y_i=V(a_i,b_i,G_i) and L_ijk=V(a_i,a_j,a_k); each codim3, Y_i irreducible degree m and each L degree1, generic noncontainment, reduced support degree m²+binom(m,3). Generic Y chart gives a_i τ−b_i², generic L chart gives a nondegenerate 3-variable quadratic form Hessian determinant −2b_i²b_j²b_k² plus cubic, formally uv−w². R1 and S2 imply normality. Checked definitions, projective dimensions, k=2/boundary and m=3. Package finite checker only confirms bounded point samples and is not substituted for scheme-theoretic proof.

## originality

PASS

The inspected full Fink–Rajchgot–Sullivant work studies matrix Schubert/northeast rank conditions and CI ideals; its results do not explicitly yield the specified star-pattern reduced singular-component degrees and generic transverse nodes. Conca–Welker coordinate-section theorem treats symmetric determinantal patterns with different zero/nonzero graph restrictions. The historically pertinent Giusti–Merle coordinate-plane sections could not be retrieved with authorized Oxford access (VPN disconnected), so possible stronger coverage remains a significant risk. No concrete positive prior implication for all component degrees/nodes found; best-of-knowledge PASS with this risk.

## value

PASS

The sparse symmetric arrowhead determinant is a canonical structured determinantal hypersurface. The global, irredundant singular-component stratification, degrees, normality and generic ordinary-node transverse analytic types are natural exact algebraic invariants that locate the singular geometry, beyond a routine statement that rank-deficient matrices are singular.

The dated certificate retains the supplied scientific assessment, sources and limitations.
