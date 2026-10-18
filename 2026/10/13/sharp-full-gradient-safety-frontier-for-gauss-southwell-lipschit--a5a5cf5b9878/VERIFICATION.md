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

Starting from g+=(0,g2-c*g1/a), GSL selection imposes |g2/g1|<=sqrt(b/a)=s. The exact worst opposite-sign ratio yields q^2+2qs<=1 (q=|c|/a). For fixed q²=u and s²=y the normalized spectral spread delta²=[(1-y)²+4u]/(1+y)² is minimized over unsafe region. Along boundary y=(1-u)²/(4u), stationarity gives 3u²-8u+1=0, u*=(4-sqrt13)/3, delta_*²=(97-26sqrt13)/27. For larger q range the minimal spread >=1/8>delta_*², so the threshold is global. Strict unsafe matrices for every larger kappa arise increasing s at fixed q*. Independent exact rational check for A=[[1,1/2],[1/2,1]], g=(1,-9/10): g+=(0,-7/5), norm squared factor 196/181>1 while objective decreases 1/2. Boundary equality includes GSL ties. Verification script algebra inspected; finite checks are not the proof.

## originality

PASS

Nutini et al (2015), Section 6 GSL, establishes argmax |g_i|/sqrt(L_i) maximizes immediate objective improvement on quadratics, but the searched full primary text does not provide a threshold for Euclidean norm of the whole gradient. Nesterov studies objective complexity, not this diagnostic. The semantically nearest published Resultary Gauss–Seidel transient theorem optimizes two-coordinate one-sweep solution-error amplification, not a single GSL update or full gradient. The new claim is the global sharp two-dimensional threshold, not GSL itself. Best-of-knowledge pass, extensive older coordinate-relaxation work residual.

## value

PASS

Gradient norm is a standard practical stationarity stopping diagnostic, while a GSL update is chosen to maximize objective decrease. A sharp matrix-condition boundary for whether this distinct diagnostic can worsen has direct structural and algorithmic meaning. The explicit fixed-matrix cone criterion and a unique-choice counterexample show exactly why objective descent does not guarantee gradient-norm descent. Not merely a normalization of the GSL definition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
