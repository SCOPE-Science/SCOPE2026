---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For R=f⊗a, use an x with f(x)=1 and vary the other argument in ker f, then reverse the arguments: f must be a common left/right eigenfunctional, with a^2=(lambda+mu)a. These identities are sufficient by substitution. The square-zero case forces both eigenvalues zero and forces the diagonal of a to vanish. Weighted incident-arrow vectors span aA+Aa because products of two arrows vanish. Scaling the support coordinates and negating one set of vertex columns gives an oriented graph incidence matrix whose kernel on vertex labels consists of constants on components, in every characteristic. This gives exactly r(S), also for parallel edges and for original loops that become ordinary separated edges. For nonzero square of a, the image line has a unique nonzero idempotent p, and the only admissible Peirce eigenvalues are (1,0) and (0,1), also in characteristic two. For a fixed 0/1 diagonal, crossing-arrow coefficients are free and conjugation by 1+j changes them independently by signed coordinates of j. The two cross-corner dimensions are therefore u and v. B empty or full gives zero contribution, and only the radical count requires dividing by q-1. The Tutte subset expansion gives (2), and the path's separated matching and two-state transfer matrix give (3). For the three-vertex line and fork both radical terms agree; the cut-weight sums give 4q(q-1)(q+1) and 2q(q-1)(q^2+q+2), whose difference is (4). For q=2 the matching term is 2(2^4-1)+(2^3-1)=37 and the cut terms are 24 and 32, yielding 61 and 69. The n=1 path gives zero. The checker was inspected, not run; its integer bit_count call requires Python 3.10 or later, not 3.9 as stated. Its finite enumeration is supplemental to the general proof.

## originality

PASS

The distinctive supported result is the unrestricted finite-field quiver counting law with the separated graphic rank and the two directed Peirce cuts. The standard rank-one reduction, graph subset expansion and transfer-matrix technique are not claimed new. The closest consulted enumerations count different quantities or different algebras. An unnamed reference to previous path enumerations remains a genuine risk for the path specialization, but the inspected sources do not show it or the general law is covered.

## value

PASS

Rank one is the first nonzero stratum for the defining operator identity, and the domain is a natural family with arbitrary edge multiplicity. The count distinguishes a graphic-matroid calculation for radical image from a directed cut calculation for idempotent image. These yield a usable all-length path recurrence and an exact orientation witness attributable to one stratum. This is not a claim of a polynomial-time general counting algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
