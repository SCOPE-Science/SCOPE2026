---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent exact computation: form the first four matrix powers and take traces, then recover the monic coefficients by Newton identities c_k=-(sum_{j=1}^k c_{k-j} tr(M^j))/k, c_0=1. The traces are (0,12,0,52) for A and (0,12,24,84) for |A|. This gives spectra {-√5,-1,1,√5} and {3,-1,-1,-1}; both correlation matrices are positive definite since (2√5/5)²=4/5<1 and the minimum eigenvalue of |C| is 3/5. For a symmetric exponent the 2-condition number is exp(spectral width). The strict ratio is exp((4√5-8)/5), approximately 1.207865. The trace-product expression is 4(cosh(t√5)+cosh(t))²/[10+6cosh(4t)]. Exact independent enclosure at t=2/5: take S(x)=sum_{k=0}^5 x^k/(2k)! and U(x)=S(x)+x^6/[12!(1-x/182)], so S(x)≤cosh(√x)≤U(x) for the three squared arguments. With Python fractions the upper bound 4[U(4/5)+U(4/25)]²/[10+6S(64/25)] is below 989/1000 by exactly 268612586886712072883756255493757/450712235476344108586334159615625000. This replays without the uploaded verifier, which was inspected only. The amplification under discussion is worst case over both nonzero base vectors and perturbation directions in Euclidean norm. At a fixed base x0 the disturbance supremum for the forward map M is just ||M||₂||x0||₂/||Mx0||₂. Equality with ||M||₂||M⁻¹||₂ entails maximizing also over x0, not claiming the same order for every fixed state or coordinate shock. The witness proves no empirical loss claim.

## originality

PASS

Best of knowledge, the exact admissible simultaneous sign reversal is not already stated or supplied by the inspected antecedents. The graph, standard switching, exponential identities and nuclear statistic are not novel. The contribution is that the signed-versus-unsigned comparisons can point in opposite directions on the very domain where the primary source gives a perturbation-sensitivity interpretation.

## value

PASS

A precisely admissible counterexample falsifies the transferable direction of a practical, previously used sensitivity comparison without disputing the published trace statistic or empirical analysis. The dimension, correlation constraint and opposite signs are substantive features. This is useful as a correctness benchmark for signed-correlation models, not merely a numerical difference between two norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
