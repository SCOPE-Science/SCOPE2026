---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

At θ=π, nonnegativity gives b+c≥a−1, and at 4π/5 all three cosine factors equal r=−(1+√5)/4, giving a+b+c≤√5−1. Thus a≤√5/2. Equality makes both contacts zero and the derivative condition −a+4b−6c=0 solves b=(7√5−12)/20, c=(3√5−8)/20 uniquely. With x=cosθ, independent exact Chebyshev expansion verifies (x+1)(x−r)²R(x). R′(x) has negative leading coefficient and strictly negative discriminant 32(1063−477√5)/25<0, so R decreases on ℝ and R(x)≥R(1)=−1+3√5/5>0 on [−1,1]. Hence global feasibility and uniqueness.

## originality

PASS

Best-of-knowledge PASS for the precise real-even continuous-circle support {1,4,6} exact optimal first-harmonic coefficient √5/2 with unique optimizer. The primary general support papers and explicit exact families were compared statement-wise; general definitions/duality and adjacent nonnested supports do not supply this formula. This is not a novelty proof from failed searches: Resultary unavailable; hidden exact sparse polynomial literature remains a residual risk.

## value

PASS

Sparse Carathéodory–Fejér coefficient extrema are canonical invariants of frequency support and positive-definite Fourier sequences. For {1,4,6}, Fifth-root resonance and simultaneous contact of frequencies 1,4,6 select a motivated support; computing its exact √5/2 optimum and unique extremizer strengthens a qualitative strict-improvement statement with a sharp full-circle certificate. The exact optimizing value, a globally certified feasible extremizer and uniqueness are precise reusable mathematical benchmarks; no paper-sized downstream theorem is required for this motivated exact fact. It is not a routine evaluation of a full consecutive Fourier support problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
