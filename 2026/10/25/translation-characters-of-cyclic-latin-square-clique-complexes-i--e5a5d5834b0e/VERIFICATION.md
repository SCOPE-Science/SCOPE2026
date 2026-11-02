---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For odd n>=3 every edge lies on one unique row/column/sum line, and every noncollinear clique is a mixed triangle; an exceptional four-clique would require 2d=0, ruled out by odd n. All higher line simplices collapse, while row-column rectangles fill using mixed triangles, proving simple connectivity and reduced homology concentrated in degree two. The Euler characteristic 1+(n-1)^3 fixes the integral H2 rank. Translations outside three direction subgroups stabilize no simplex; a nonzero translation within one stabilizes exactly n line simplices, each with contractible geometric fixed set. The Lefschetz traces are therefore identity (n-1)^3, n-1 for a direction translation, -1 otherwise. Orthogonality of Z_n^2 characters produces exactly m_{r,s}=n-3+1_{r=0}+1_{s=0}+1_{r=s}-1_{(r,s)=0}. New independent full-clique, simplex and signed-Lefschetz enumerations for n=3,5,7 verify all translates, including small cases, but the odd-order argument is the unrestricted proof.

## originality

PASS

The 2026 primary Cioaba–Mim Theorem 3.12 explicitly supplies the ordinary all-field H2 Betti number for Latin-square graphs (and thus already covers the cyclic odd case for n>=5), which is not claimed original. The 2015 Besharati et al article studies graph chromatic questions. Neither examined source states the rational translation character, the three distinguished dual Fourier lines, or the n-1 fixed-point quotient rank. Character theory alone cannot recover equivariant traces from ordinary Betti numbers.

## value

PASS

The cyclic Latin-square graph is a natural strongly regular graph with an intrinsic order-n² translation subgroup. An exact character is a finer invariant than a Betti number: it gives each nonidentity trace, distinguishes generic versus three dual directions, and computes rational quotient homology for all odd orders including composite n. The parameter family and group action are canonical rather than arbitrary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
