---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For m,n>=2 and q odd, the multiplication gives E^2=ks_m⊕ks_n, with its intrinsic determinant pencil beta^m alpha^n. An automorphism must preserve or exchange the two characteristic lines; exchange requires m=n. In a side-preserving 2x2 block matrix, the nondegenerate Gram equations force off-diagonal blocks B,C=0, and the remaining blocks satisfy A^TA=bI_m, As_m=a s_m, D^TD=aI_n, Ds_n=b s_n. If p does not divide a part size, the all-ones vector is nonisotropic and its multiplier must equal the square of its eigenvalue, leaving an O_{d-1}(q) count. If p divides d, a hyperbolic plane through the isotropic all-ones vector leaves T_{d-2} with discriminant -1, q^{d-2} unipotent choices and a square-multiplier restriction only in odd d. Summing the two sides gives the exact four arithmetic regimes. Independent exhaustive F3 Gram-stabilizer enumeration returned 8 for K_{2,2}, 12 for K_{2,3}, 72 for K_{3,3}, including double-isotropic d=3. All-d structure uses characteristic pencil/orthogonal arguments, not those finite counts.

## originality

PASS

PASS at the evaluated complete-bipartite, all-odd-finite-fields level: prior graph framework and symmetry-action papers discuss graph automorphisms, diagonal actions and perfect/algebraically closed settings, not the full coupled rational orthogonal-similitude stabilizer counts in the four regimes (especially p divides both part sizes). These are mathematical extensions of standard orthogonal stabilizer machinery, so unindexed or broad evolution-algebra automorphism classifications remain priority risks.

## value

PASS

K_{m,n} is a canonical connected family with E^2 of dimension two and a large nonlinear-in-the-basis automorphism group. The theorem classifies the full group and rational point counts in all dimensions and detects a real divisibility-driven double-isotropic change. This is a natural infinite family and invariant useful in graph-evolution algebra studies, beyond simply listing graph symmetries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
