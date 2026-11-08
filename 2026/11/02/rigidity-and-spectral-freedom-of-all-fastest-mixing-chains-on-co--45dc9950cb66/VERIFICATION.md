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

Let S be total cross transition mass, bounded by p. A trace-compression on Y-zero-sum gives mu >=1-S/q; the X-Y contrast Rayleigh bound gives mu>=(p+q)S/(pq)-1. Their minimax intersection S*=2pq/(q+2p) when q<=2p, otherwise saturated S=p. At equality, positivity of tI-P on 1-perp forces P to equal t on the Y-zero-sum eigenspace and -t on the contrast vector; these equalities make every cross row uniform and all cross row sums equal, hence every cross entry forced. In q>=2p, saturated row budgets kill all clique/internal holding weights and give uniqueness. With cross weights fixed, block diagonalization leaves eigenvalues 1, -t, +t of multiplicity q-1, and 1-qb-lambda_j(L_W); the displayed degree and eigenvalue conditions are precisely necessary/sufficient. Constructive clique weights attain all regimes and give connectivity iff p>q. Independent exact-rational numerical spectra for 48 parameter pairs corroborated attainability; finite tests do not prove global rigidity.

## originality

PASS

The optimum scalar SLEM and existence of clique-lifted symmetric solutions are known from Boyd et al and Jafarizadeh 2020; novelty must NOT claim the optimal value. The explicit unrestricted all-optimizer face, uniformity of cross-edge weights despite no automorphism invariance and exact internal Laplacian/degree constraints are distinct from an existence lifting theorem. Full-optimizer uniqueness might be obtainable from general SDP complementary slackness but is not implied by the inspected specific lifted-solution theorems without the equality argument.

## value

PASS

Characterizes an entire optimal face rather than only the known optimal objective value, with forced connectivity when p>q, optional clique support for p<=q<2p and forced deletion for q>=2p. This reveals nontrivial structural constraints for all fastest-mixing chain designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
