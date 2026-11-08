---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Three independent uniformly sampled eccentric anomalies on axis-aligned ellipse (a cosθ,b sinθ), a>=b>0, are NOT uniform arclength points. For a fixed first angle α, two independent differences U,V uniform (0,π), and Δ=U−V has triangular density. The chord inner product under diag(a,b) has sign cosΔ+τ cos(2m) for τ=(a²−b²)/(a²+b²); uniform α makes m uniform mod π independent of Δ. Integrating the obtuse probability gives one angle P_obtuse=1/4+[1/(2π²)]Li₂(τ²), by arcsin² Taylor series and averaged cosine even moments. Three mutually exclusive obtuse events imply P_acute=1/4−3/(2π²)Li₂(τ²). Positive series coefficients establish strict shape monotonicity, Taylor expansion τ=tanh(log r) gives near-circle expansion, and dilog reflection near τ²=1 gives slender asymptotic 6/(π² r²)(2log r+1−log4)+O(log r/r⁴). Independent 400-node Gaussian quadrature of arcsin² for r=1,1.5,2,4,10 matched formula to ~1e−14; Monte Carlo in inspected checker is only corroboration.

## originality

PASS

Best-of-knowledge PASS: exact result and mathematical object are not established by accessible identified prior statements; reviewed aliases, reductions, stronger coverage and checked data. Distinct original ingredient: chord-direction integration for affine-angular ellipse acuteness, not known dilogarithm itself. Residual priority and access risks retained.

## value

PASS

Obtains the exact natural Euclidean acuteness statistic for independently sampled points on a noncircular ellipse under the affine image of angular-uniform circle sampling, distinguishing the physically different arclength law. The exact dilogarithm anisotropy profile and sharp end asymptotics quantify a significant geometric transition. Known identical offcenter-circle containment probability is acknowledged and not separately claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
