---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. Reconstructed the normalizations q=degree minus one, 0<=r<=1, c=abs(cos theta), the adjacency spectrum [-2 sqrt(q),2 sqrt(q)], and the operator identity R(u)=(1-u^2)(I-uA+qu^2 I)^{-1} for |u|<q^-1/2. The spectral real-part multiplier reduces at the extremal spectral endpoint to P_q(r,c)=2(q-1)r^2 c^2-2 sqrt(q)r(1-r^2)c+(1+r^2)(1-qr^2). Independently proved its exact discriminant factorization (qr^2+q-2)((2q-1)r^2-1), P(c=1)=(1-r^2)(1-sqrt(q)r)^2 and P(r=q^-1/2)=-2(q-1)c(1-c)/q. Sign analysis yields all stated two-band, universal-angle and singular boundary cases; the Schur edge-product argument supplies positivity beyond the summable-resolvent regime, and the neighbor-star matrix detects the boundary's singularity. Independently built a 22-vertex q=2 tree ball and evaluated the exact negative quadratic form -49/243 at r=2/3, theta=pi/3. Strict positive definiteness in the interior follows from positivity of the spectral form off a finite spectral-zero set and absence of tree-adjacency point eigenvalues, not finite tests. Scope: homogeneous infinite regular trees, not arbitrary trees or other radial classes.

## originality

PASS

PASS, qualified best-of-knowledge. Vergara 2019 gives a necessary-and-sufficient moment/operator characterization for every positive radial kernel on a homogeneous tree, and Figa-Talamanca–Picardello 1982 develops free-group spherical functions and their positive-definiteness. They supply much broader harmonic-analysis machinery; their inspected statements do not directly provide the two-resonance-band threshold formula for r^distance cos(theta distance). Elon's 2009 Gaussian waves use adjacency eigenfunction covariances, not this pure damped cosine. The explicit parameter diagram is not asserted to be independent of those general frameworks. De Michele–Figà-Talamanca 1980 is relevant and could not be materially inspected. Absence of a matching search result is not taken as proof of novelty.

## value

PASS

PASS. The family is a natural two-parameter candidate for a radial stationary Gaussian covariance on any fixed-degree homogeneous tree. Its exact sharp universal-angle threshold, split admissible angular intervals, spectral-edge limiting phase and strict-vs-semidefinite boundary distinguish genuinely different admissibility regimes. The calculation supplies a usable closed parameter classification rather than merely restating the known general moment criterion or an arbitrary numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
