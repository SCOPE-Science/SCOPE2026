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

The independent Laplace check is 1/(2d²) times [1/(w+a)-2/(w+a+d)+1/(w+a+2d)], which equals the product of the three original transforms. The window is real and causal, so with T=|τ| the substitution t=u+T/2 gives the prefactor e^(-aT-iπνT)/(4d⁴) and a one-sided integral. Setting z=e^(-du) gives the extra 1/d and the integral of z^(s-1)(1-z)²(1-ρz)² over [0,1], analytic for Re s>0. Expanding yields beta terms B(s,3)-2ρB(s+1,3)+ρ²B(s+2,3); their common denominator is D and the numerator is 2[(s+3)(s+4)-2ρs(s+4)+ρ²s(s+1)], exactly 2P_ρ. In s+3 the three coefficients are (1-ρ)², (1-ρ)(1+5ρ), and 6ρ(1+ρ); all are positive for 0<ρ<1, so the real parts of both roots are negative in that variable. Hence real ν (Re s=2a/d) cannot be a zero. The five P_ρ(-j) are positive in the same range, so no poles cancel. The discriminant has sign of ρ²-14ρ+1, with the unique admissible root 7-4√3; at that root the double zero is -2-√3. For smaller ρ, the shifted s+4 roots are real with positive sum and product, giving -4<s<-3. For larger ρ they are conjugate nonreal in s. At T=0, ρ=1 gives the nonzero constant 12, so no finite zeros. The affine map s(ν) is invertible over C and the exponential prefactor has no finite zeros or poles, yielding exactly the stated meromorphic census and preserving multiplicities.

## originality

PASS

The strongest inspected prior paper proves real ambiguity nonvanishing with two distinct rates or arbitrarily many equal rates, and expressly leaves distinct higher convolutions for separate study. The supported new scope is the three-distinct arithmetic family and its exact complex-Doppler zero/pole classification; neither a new general criterion for total positivity nor novelty of the window family or ambiguity/Zak methods is credited.

## value

PASS

This is a tractable but non-equal-rate instance of a specific distinct-rate problem identified in primary time–frequency literature. It settles the entire real ambiguity plane for a natural first higher cascade and describes how the continuation zeros appear, collide and split at finite delay. The exact shift and noncancellation show why the complex transition does not obstruct real zero-freeness. This gives a concrete benchmark for a broader theory, not just a single parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
