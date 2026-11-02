---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Starting with k>=3 cycle vertices and s=n-k off-cycle vertices, the rooted forest Laplacian minor has determinant (sum of root weights)(sum of all vertex weights)^(s-1). Consequently off-cycle child counts follow the stated occupancy enumeration. Choosing r empty nonroot bins and extracting the coefficient yields exactly N_{n,k,r}=(n!/2)((s-1)_(r-1)/r!)[z^(r-1)]exp(kz)((exp(z)-1)/z)^(s-r), for 3<=k<=n-r; zero otherwise. Fixed-degree expansion log((exp z-1)/z)=z/2+O(z^2), uniform for k in the admissible lattice, gives weights proportional to (1-(k/n)^2)^(r-1), so the Riemann sum and the map y->y^2 prove Beta(1/2,r) at fixed r. The n!/2 exact r=1 and n!(s-1)(2n-s-2)/8 r=2 cases follow directly. Independently enumerated all n-edge simple labelled connected unicyclic graphs n=4,5,6 and verified every attainable (cycle length,leaf count) cell against the extracted formula. No growing-r theorem or random-graph-component equivalence follows.

## originality

PASS

PASS, best of knowledge: The conditioned connected-graph leaf-count law and beta-square limit are not stated in the inspected sparse-G(n,M) cycle-component paper or leaf/girth Laplacian-extremal paper. The rooted-forest determinant, cycle decomposition and transfer of fixed-degree coefficients are classical, not claimed independently novel. Janson 2003 and possible multivariate graph EGFs create genuine historical-priority risk; an unsuccessful search cannot exclude implicit derivation.

## value

PASS

PASS: Cycle length and leaf count are intrinsic, well-motivated invariants of connected unicyclic graphs. The exact joint finite-size count answers practical conditional enumeration questions, the precisely uniform one-leaf law is a nontrivial all-size boundary, and the Beta(1/2,r) family quantitatively shows how more terminal vertices bias the unique cycle. It is not an arbitrary numerical slice or only a standard forest identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
