---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The eight-dimensional normal form with basis (x,y,a,b,c,d,e,f) and eleven nonzero multiplication products satisfies the commutative Jacobi identity and spans the free object by reduction of all degree-five monomials; in characteristics not 2,3 the explicit faithful model proves independence. A nonzero linear component of z is the image of x under an automorphism inducing an invertible graded generator change, so L_z has rank 5. For z in F², the degree-three map from (x,y) is M(A,B,C)=[[-B/2,A],[C,-B/2]], determinant (B²−4AC)/4. Nonzero quadratic part has an independent quartic output, giving rank 1+rank M, i.e. 2 on the nonzero quadric and 3 off it; cubic-only gives rank1 and quartic-only gives rank0. The discriminant rank-one symmetric cone has q²−1 nonzero finite-field points and unique singular vertex, so counts are q, q(q²−1), q³(q²−1), q^5(q−1), q^6(q²−1), and rank4 never occurs. Independently reconstructed all multiplication matrices over F5, obtaining 5,120,3000,12500,375000 for ranks 0,1,2,3,5 among 5^8 states. General assertions rest on the algebraic proof, not this sample.

## originality

PASS

Remm (2022/2024) already gives the eight-dimensional free Jacobi–Jordan graded multiplication, so the basis/table are not new; Burde–Fialowski and Agore–Militaru establish the general setting. The additional statement classifies every left multiplication rank and geometric discriminant stratum, with explicit finite-field counts. This follows by a short but genuine determinantal case analysis of known structure constants; it is a natural exact result although priority could reside in previous rank/annihilator tables.

## value

PASS

Left-multiplication rank and annihilator dimension are intrinsic to a finite-dimensional algebra, and the free two-generated Jacobi–Jordan algebra is the canonical finite example with a known eight-dimensional normal form. The exact geometric rank loci, discriminant cone, forbidden rank four, and all-q arithmetic strata form a natural complete invariant rather than an arbitrary slice, and can support study of representations, generic rank and annihilator stratification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
