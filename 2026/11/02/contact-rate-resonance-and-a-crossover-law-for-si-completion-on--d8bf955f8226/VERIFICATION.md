---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For fixed k≥2, β>0, γ≥0, the petal infection count j has rate λ_j=(k−j)(β+jγ) from independent exponential edge clocks. Successive holding times and m petal times are independent, so D is a sum of k independent Exp(λ_j) and P(T_m≤t)=P(D≤t)^m. Concavity in j confines slowest λ_j to endpoints kβ and β+(k−1)γ. Distinct fixed rates yield a simple slow pole and Cexp(−at) tail, whereas γ=β gives two equal slow poles at kβ, t e^(−at) and the interior telescoping coefficient (k−1)². In the triangular array γ_m=β(1+c/log m), the exact two-exponential survival formula e^(−at)[1+a(1−e^(−δ_m t))/δ_m], δ_m=(k−1)β c/log m, combined with uniformly faster interior stages yields the coefficient (k−1)²h((k−1)c/k)·log m. This proves the stated Gumbel centering. Independently checked the resonant k=2 survival against the exact Erlang formula at m=10³,10⁶,10¹⁰; finite numerical convergence is slow, as expected, and is not the limiting proof.

## originality

PASS

Fixed phase-type maxima and their repeated-dominant-eigenvalue log-log corrections predate this result (Kang–Serfozo 1999; Asimit–Jones 2007). Those are explicitly acknowledged as context. The novelty-bearing statement is the specific two-mechanism SI bouquet slow-rate collision and uniform triangular-array crossover for γ_m−β of order 1/log m, with explicit H_k(c). The inspected Asimit–Jones full PDF treats i.i.d. fixed phase-type laws, not a sequence of generators coalescing with m; the 2023/24 epidemic first-passage paper concerns SIR peak/macroscopic timing. Published Resultary searches did not reveal the same SI-petal varying-rate expression. Other specialized hypoexponential extreme-value crossovers remain a residual risk.

## value

PASS

The SI completion time is a natural measurable epidemic timing invariant on connected clique bouquets. Competing hub seeding and within-clique spread rates create an exact resonance: its divergent log-log delay and continuous 1/log m crossover quantify a mechanistic phase transition. This extends fixed-distribution extreme-value theory to a motivated simultaneous population/parameter limit and has a plausible use in comparing nearly balanced transmission mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
