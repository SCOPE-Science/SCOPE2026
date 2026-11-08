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

The unnormalized Zak transform gives Zg=e^{-ax}[x+(1−x)re^{-2πiω}]/(1−re^{-2πiω})², r=e^{-a}. The integer-frequency even modulation rows and odd half-frequency rows are distinct Fourier bases; Parseval produces multiplier |Zg(x,ω)|²+|Zg(x,ω+1/2)|², without an extra density factor. Algebra gives a positive fraction strictly increasing in cos²(2πω); hence optimal frequencies are 1/4,3/4 (lower) and 0,1/2 (upper). The spatial lower and upper profiles are exponentials times positive quadratics; their stationary equations and endpoint derivative signs yield unique interior minimizer x_a and maximizer y_a. The discriminant Δ²=(1+r²)²−4a²r²>0 by cosh a>a. Substituting roots yields the stated A_a,B_a>0. Uniform limiting profile at a↓0 and stationary expansions at a→∞ prove both sharp κ scalings. Independent code directly evaluated the rational Zak fiber over 13448 grid points and exact critical fibers, and checked both asymptotic normalizations. Finite grids are not an analytic proof of all parameters.

## originality

PASS

The 2026 complete totally-positive Gabor frame-set theorem determines frame EXISTENCE for αβ<1, including this generator but not optimal bound constants. Kloos–Stöckler establish a Zak framework and lower estimates for another window; a Gabor frame-bound optimization poster explicitly treats cut-off one-sided *first-order* exponentials and two-sided exponentials, not the order-two causal Erlang window. Thus the precise two global extrema and both conditioning coefficients are not direct consequences of the published statements inspected. Janssen 1996 remains a plausible incompletely read broad frame-bound source.

## value

PASS

Exact frame *conditioning* matters even when a frame-set existence theorem guarantees positivity. The causal Erlang repeated-pole window is an elementary smooth filter with a natural shape scale; explicit optimal twofold-oversampled bounds show two distinct degeneration mechanisms—quartic inverse-power near zero and exponential at large shape. The precise coefficients and fiber optimizer locations give reproducible stability benchmarks for window selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
