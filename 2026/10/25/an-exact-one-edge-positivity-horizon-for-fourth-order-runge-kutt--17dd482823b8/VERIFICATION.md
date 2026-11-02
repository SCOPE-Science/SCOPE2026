---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Block multiplication of Q=[[-B,b^T],[a,-diag(a)]] yields P0j=b_j h g_j(h), Pj0=a_j h g_j(h) with A=B+a_j, C=B^2+Ba_j+a_j^2+S1, D=B^3+B^2a_j+Ba_j^2+a_j^3+(2B+a_j)S1+S2 and g=1-Ah/2+Ch²/6-Dh³/24. For distinct leaves, Pij=a_i b_j h²[1/2-(B+a_i+a_j)h/6+U_ij h²/24]; 3U_ij-(B+a_i+a_j)^2>0 gives no real root. Reversibility provides real symmetric negative spectrum; scalar R4(-z)>0 for z>=0 ensures strict positive diagonals. Weighted Cauchy v=S2/B³>=(S1/B²)^2=u² makes 9AD-4C² positive via the displayed quartic with positive coefficients; hence g_j has derivative negative everywhere and exactly one positive zero. The rational 3x3 example at h=1/2 has P02=-1/96, P20=-1/32 but eigenvalues 1,3/8,83/128, while dimension two scalar stability forces off-diagonal positivity. Independent symbolic calculations reconfirmed exact example and monotonicity certificate.

## originality

PASS

General SSP positivity bounds and the classical RK4 stability polynomial are prior work, but those are method-wide sufficient bounds or scalar spectral properties. The assessed contribution is the *sharp end-step* positivity interval and one-entry-family obstruction for arbitrarily nonuniform, reversible, directed star generators, plus the minimal 3-state spectrally stable counterexample. Other published SCOPE positivity results address distinct integrators.

## value

PASS

For CTMC transition integrators, entrywise nonnegativity is required to preserve probabilistic meaning and is not implied by stable eigenvalues. The complete exact rate-dependent positivity horizon for an infinite family of reversible but nonuniform stars, together with a minimal stable/nonpositive witness, provides a natural reusable numerical-analysis boundary. Its univariate cubic certificates are not merely a textbook scalar stability computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
