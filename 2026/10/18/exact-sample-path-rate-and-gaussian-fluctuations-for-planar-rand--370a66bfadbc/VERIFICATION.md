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

The residual is projected onto the random perpendicular line. In eigenvector coordinates with the perpendicular line concentrated about angle zero, its angle density modulo pi is proportional to (a² cos²(phi)+b² sin²(phi))^(-1); doubling gives the Poisson kernel at q. Consecutive angle differences therefore have Poisson parameter s=q². The log of the squared-norm ratio is the first finite log factor plus a sum of stationary 1-dependent increments g(t)=log cos²(t/2). These have a finite second moment for every fixed q<1. As an independent evaluation, write exp(it)=(s+ζ)/(1+sζ) for uniform ζ on the circle; g(t)=2 log((1+s)/2)+2 log|1+ζ|−2 log|1+sζ|. Logarithmic Fourier orthogonality (valid in L² at ζ's unit modulus) gives the drift and V=π²/3+2 Li₂(s²)−4 Li₂(s)=π²/3+4 Li₂(−s). Conditioning adjacent increments on their shared angle gives covariance equal to the variance of their common conditional mean. Applying the circle map at q rather than s to that mean replaces its nonconstant part by 2(log|1+βζ|−log|1+qζ|), giving the claimed Li₂ combination for V+2C; V>0 and C≥0. The first factor and the difference between n and n−1 stationary summands vanish after normalization. At q=0 this yields the geometric-average squared factor 1/4 and variance π²/3, while the expected squared factor is 1/2. The mean-square Perron benchmark also agrees with the two-state transfer obtained from E[u_i^4] and E[u_1²u_2²]. An independent quadrature against the Poisson difference density and shared-angle conditional mean at q=0,0.2,0.6,0.9,0.97 gave errors below 3e−12 for drift and variance and 5e−15 for covariance. This is finite corroboration only.

## originality

PASS

The distinct claim supported here is the exact planar almost-sure log rate and the evaluated nondegenerate log-CLT variance. The matched exact expected-energy rate, the generic projection and line-search framework, and the general one-dependent limit theorems are not distinct claims. No inspected source gives the claimed drift and covariance evaluation or a stronger evaluated result covering them.

## value

PASS

Expected residual energy cannot answer how a typical run contracts or how it fluctuates. The exact logarithmic drift and explicit fluctuation variance answer both questions over the full SPD condition-number range in the natural planar model, separating typical performance from an expectation susceptible to rare slower trajectories. Evaluating the shared-angle covariance is essential, not a consequence of reporting an expected energy bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
