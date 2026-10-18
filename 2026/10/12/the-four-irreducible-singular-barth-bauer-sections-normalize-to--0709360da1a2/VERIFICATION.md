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

On g1(α)=(α²−2α−1)(α²+2α−1)=α⁴−6α²+1=0 the z3⁴ term in the plane quartic cancels. Since α²+1≠0 at all four roots, projection from source unique ordinary node [0:0:1] gives 6(α²+1)(x²+1)z3²=x⁴−6x²+1. Multiply z3 by sqrt(6(α²+1))(x²+1) to obtain the same quadratic function-field extension y²=(x²+1)(x⁴−6x²+1) for each α. The sextic expands to x⁶−5x⁴−5x²+1 and is squarefree, so normalization has genus two. Naskręcki proves irreducibility, genus and nodality; Goldstein–Guralnick–Howe–Zieve record Igusa’s reduced geometric S4 classification for this exact sextic over char≠2,5, giving full Aut order 48 over C. Independently reverified symbolic g1, square-free sextic, node coefficient and distinct roots.

## originality

PASS

The lead paper identifies exactly these four geometrically irreducible nodal genus-two plane sections, without naming their common normalized sextic. Goldstein et al. identify the sextic as the unique reduced-S4 genus-two case, without associating it to the Barth–Bauer family. The algebraic projection is the bridge not provided by either prior statement. Claim does not rename already published classification as newly derived; it is the cross-identification of a natural four-member stratum.

## value

PASS

Naskręcki’s entire exceptional irreducible singular stratum of four members is located at a single explicit genus-two moduli point with maximal reduced automorphism S4. The bridge is a motivated, exact and reusable geometric identification rather than a generic renaming of a known model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
