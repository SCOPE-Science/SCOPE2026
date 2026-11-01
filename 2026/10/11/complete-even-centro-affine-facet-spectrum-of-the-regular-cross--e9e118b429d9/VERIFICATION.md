---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Under the actual Hu--Ivaki normalization the facet normal/support are sigma/sqrt(n), 1/sqrt(n); Gram determinants n and n-1 give facet mass m=1/(n-1)! and ridge Hausdorff measure sqrt(n-1)/(n-2)!. Adjacent normals have sin(theta)=2sqrt(n-1)/n, hence every hypercube edge has c=1/[2(n-2)!] and c/m=(n-1)/2. The Walsh character of cardinality k is an eigenfunction of the unweighted cube Laplacian of eigenvalue 2k; completeness of the Walsh basis yields all 2^n eigenvectors with multiplicity binomial(n,k). Antipodal inversion retains exactly even k; first nonzero even degree is two. n=2 uses H^0=1 for a ridge point and satisfies the formulas. An independent exact-rational enumeration n=2..7 checked all Walsh eigen-equations, parity and multiplicities; the analytic argument, not finite cases, proves all n.

## originality

PASS

Best-of-knowledge new all-dimensional specialization of Hu--Ivaki facet weights to the regular n-cross-polytope, n>=4, with exact spectrum and even multiplicities. The classical Q_n Walsh spectrum supplies the diagonalization, and a published three-dimensional interpolation covers the octahedral n=3 boundary specialization; neither gives the geometric weight ratio and full result for n>=4. The parallelotope result computes a different polytope class. The claimed originality is limited to the complete weighted centro-affine cross-polytope spectrum, not to the Walsh diagonalization, the invariant definition, or the n=3 numerical value.

## value

PASS

The cross-polytope is a canonical nonsimple origin-symmetric polytope for the recently introduced centro-affine weighted facet-network invariant. The complete all-dimensional even ladder, including binomial multiplicities, is a natural benchmark that a later study can use when comparing classes and testing conjectured gap behavior. The gap 2(n-1) differs for n>=3 from the polar parallelotope gap n, demonstrating that the discrete invariant is not preserved by polarity. The calculation is elementary once the network is identified, but the exact normalization, full spectrum and polarity comparison are self-contained useful facts beyond a single tiny numeric check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
