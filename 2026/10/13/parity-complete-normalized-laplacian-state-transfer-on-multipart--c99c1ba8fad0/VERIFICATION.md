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

Reconstructed symmetric normalized adjacency S=D^{-1/2}AD^{-1/2} on K_{2,...,2,m} with r>=2. Orthogonal decomposition has within-cell zero-sum eigenvalue 0 (dimension r+m-1), small-cell transverse eigenvalue -2/d (dimension r-1), and remaining quotient eigenvalues 1,-m/d, d=m+2r-2. All non-Perron signs for transfer between twin vertices require e^{-it}=-1, e^{-it(1+2/d)}=e^{-it(1+m/d)}=1. Setting t=h*pi with h odd yields 2h/d,mh/d odd integers iff d/2 odd and m=2 mod4, equivalent r odd, m=2 mod4. All t=(2j+1)d*pi/2 follow; only size-two twin pairs qualify because projected within-cell zero-sum components of other vertex pairs are nonparallel or disjoint. At first t, U=I-2P_Z gives direct sum r swaps and 2J_m/m-I_m. Handles m=1 singleton and m=2 eigenvalue degeneracy, and excludes r=1. Independent symbolic eigenmultisets for (r,m)=(2,1),(3,2),(3,6),(4,2),(5,10) match predicted multiplicities; finite checks corroborate, do not prove full parameter range.

## originality

PASS

Best-of-knowledge original complete two-parameter irregular-multipartite normalized-Laplacian PST classification. Coutinho–Ferreira Baptista Theorem 5 provides a general strong-cospectral phase criterion and minimum-time formula; Monterde analyzes twins and multipartite joins; general Sun–Das spectrum is credited. Applying those tools still requires the explicit quotient/projector decomposition, parity arithmetic, global propagator and exclusion of other transfer pairs. Known regular cocktail-party m=2 boundary is not claimed new; irregular m>2 family and full simultaneous operator are the surviving contribution.

## value

PASS

A natural architecture of repeated twin pairs with one tunable exceptional cell has a sharp arithmetic all-parameter criterion, complete timing and a global simultaneous-swap/reflection operator. The irregular K_{2,2,2,6} example separates the result from uniform regular cocktail-party graphs and gives a reusable exact quantum-walk test architecture; not a generic strong-cospectrality theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
