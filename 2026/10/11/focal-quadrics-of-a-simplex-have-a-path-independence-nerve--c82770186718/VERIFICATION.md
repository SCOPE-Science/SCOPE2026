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

The focal condition is a double eigenvalue d_k for D-xx^T. Negative rank-one interlacing places it at the adjacent eigenslots k-1,k, excluding adjacent k. For any independent S, interlacing target eigenvalues at upper/lower endpoints plus midpoint choices and a last point at d_n or d_n-delta give exactly the prescribed duplicated slots. Nonnegative residues p_mu(d_i)/p_D_prime(d_i) reconstruct real x by the determinant lemma; the rank-one complementary block has nullity<=1 so all repeats have multiplicity exactly two. The n=4 D=(10,6,3,1) example has four intersection points and repeated eigenvalues (6,6,1,1), shifted Jacobian (3,3,-2,-2). Independent exact rational calculations sampled all independent S through n=9 and verified the relevant characteristic-polynomial reconstruction; the all-n proof is analytic, not finite sampling.

## originality

PASS

Eydelzon characterizes each focal quadric individually via repeated eigenvalues; the examined full six-page source does not classify any simultaneous focal-incidence nerve. General rank-one inverse spectral reconstruction and interlacing are already known, so originality rests only on translating their constraints into a complete simplex focal geometric incidence classification and exact realization. Resultary closest exact-object hit is the audited claim, with no older equivalent same-object record identified.

## value

PASS

The joint degeneracy incidence nerve is a natural invariant of the source simplex focal-set family. It yields exact maximal simultaneous eigenvalue degeneracies, all possible indexed intersections, and counts in every n, rather than an arbitrary numerical slice or a standard standalone interlacing restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
