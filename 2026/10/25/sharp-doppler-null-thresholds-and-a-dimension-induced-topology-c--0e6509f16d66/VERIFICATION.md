---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The shifted quadratic-Gaussian product and Gaussian second/fourth Fourier moments give exactly A=(pi^(d/2)/16)exp(-(X+Y)/4)[(X-Y+a)^2+4Z-16(Y-Y0)], with Z=(T·omega)^2, a=4c+2d-4 and Y0=2c+3d/2-1. For d>=2 the feasibility of Z=0 and X>=0 is equivalent to 16(Y-Y0)>=(max(a-Y,0))^2, giving exact piecewise sharp Doppler minimum, unbounded perpendicular families and X/Y->1. For d=1 Z=XY and the explicit parameter s=X+Y in [4c+6-2sqrt(8c+6),4c+6+2sqrt(8c+6)] exhausts both smooth frequency-sign ovals; optimizing quadratic X(s),Y(s) produces the sharp delay and fold c*=(sqrt(3)-1)/4. Independently verified symbolic expansion, parameter roots, delay optimum. Examined the two actual checker source files; their bounded quadratures/witnesses do not prove the all-d statement.

## originality

PASS

General Hermite/Wigner transform formulas are old, but the sharp positive radial family real-zero geometry, d=1 compactness versus d>=2 unboundedness and both parameter thresholds require a distinct constrained real-geometry argument and were not found in inspected full sources.

## value

PASS

A precise complete zero-locus classification for a natural strictly positive Schwartz pulse, with a sharp uniformly zero-free delay strip, frequency thresholds and dimension-induced qualitative contrast; beyond reparametrizing a transform polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
