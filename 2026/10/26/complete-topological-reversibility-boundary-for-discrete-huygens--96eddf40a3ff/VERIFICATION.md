---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the repaired cyclic orientation, B^T maps the vertex torus onto the stated edge torus with diagonal circle kernel, by summing the consecutive edge differences. Under signed reorientation B'=BS the torus, matrix and phase variables transform together: Z'=SZ, K'=SKS, and the sine map commutes with S. For h≤1/Λ the strict sine-secant inequality gives injectivity of the lift even at equality; lattice and rotation equivariance, compactness and degree one give a quotient homeomorphism. The lower bound on the quotient derivative is positive in the strict interval, and the boundary witnesses have a kernel (all π for even n; one zero for odd n, retaining a vector in the two-dimensional top eigenspace perpendicular to the exceptional edge). For h>1/Λ, balanced ±arccos(c) phases with c just below −1/(hΛ) obey closure, adding a zero edge for odd n. The even-cycle top eigenspace is simple, and in the odd case the exceptional edge's nonzero top Fourier projection removes one, but only one, of the two zero directions at the critical cosine. The remaining direction crosses to negative, with all others positive. On an inverse branch from this regular negative source, regular values of the full map form a nonempty open set by Sard and compactness. Degree +1 then gives at least two positive preimages in addition to the negative one.

## originality

PASS

Pass is for the cycle-specific extension to open sets of regular triple fibres at every supercritical step, giving the closed injectivity boundary. Strict-subcritical diffeomorphism and endpoint singularity of this map are covered, and the secant and degree methods have close antecedents. What is not furnished by the inspected statements is a negative-orientation witness inside the constrained cycle torus for arbitrary supercritical h, specifically the odd-cycle rank-one lifting of just one critical direction under closure.

## value

PASS

The exact interval of global reversibility is a natural classification for these phase maps. Proving an open regular multiplicity lower bound for every larger step resolves a nonlocal inverse question left open by convergence bounds and cubic onset. The odd-cycle closure obstruction makes the arbitrary-step witness substantive; this is not merely a change of incidence conventions or another near-onset example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
