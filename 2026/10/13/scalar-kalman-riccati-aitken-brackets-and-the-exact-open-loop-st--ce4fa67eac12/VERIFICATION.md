---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md lines 60–194 in exact arithmetic. The fixed-point quadratic has product -qr/h² and sum q-(1-a²)r/h². Since p>q and h²p+r=a²rp/(p-q)>a²r, and h²p+r>r, the projective multiplier ρ lies strictly between zero and one. Write t=t(P_n) and Δ=P_{n+1}-P_n. From the inverse φ(t)=(p-mt)/(1-t), the ratio of successive increments is ρ(1-t)/(1-ρ²t), so the second difference divided by Δ is (ρ-1)(1+ρt)/(1-ρ²t). Substituting gives φ(ρ²t²) for the extrapolate wherever defined. For 0<|a|≤1, P₁≥q>(p+m)/2, so -1<ρt<0 for all triples from a lower start: no denominator vanishes, raw iterates increase below p, and squared coordinates give decreasing upper bounds. With h=r=1, P₀=0 and 0<q<a²-1, the second difference is positive and the first extrapolate is -q(q+1)/(a²-1-q), independently verifying sharpness. The formal identity at arbitrary t is understood only away from poles and zero differences. The proof does not cover finite precision, feedback of extrapolates, matrix covariances or over-starts.

## originality

PASS

The inspected material covers the projective viewpoint, convergence, or Aitken robustness separately, not the coupled exact relation, monotone covariance certificate, and sharp parameter-uniform bracketing boundary. Credit the classical projective conjugacy and raw monotonicity separately; this is a best-of-knowledge finding about the stated combination, not a priority claim about those ingredients.

## value

PASS

An exact signed error law explains when a standard extrapolation certifies an upper covariance bound and gives an explicit nonphysical extrapolate beyond the uniform threshold. This matters as a diagnostic for extrapolation, even though the scalar fixed point can itself be found by a quadratic formula. It is not a claim of a faster or more stable finite-precision solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
