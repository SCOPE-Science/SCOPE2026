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

Split the coefficient sequence into even and odd channels and use unitary Fourier series in the cell index. This gives the exact min and max squared fiber singular values, with no density factor. At the midpoint the fiber rows for value and derivative are h=(u,conj u) and d=(u′,−conj u′). In |u_x|² the change from (n,m) to (n−m,n+m) forces equal parities; the two parity sums in the spatial variable are A_a(x) and A_a(x+1). At x=1/2 their values coincide and their derivatives are opposite, yielding ||h||²=2Aϑ₃ and det(h,d)=−Dϑ₄. The Poisson formula and the logarithmic derivative of the theta product at π/4 give D<0. Unitary sum and difference of the sample rows give a determinant 2ε det(h,d)+O_a(ε³), uniformly on the frequency circle, and the large squared singular value is 2||h||²+O_a(ε²) with a uniform positive leading term. Their quotient gives the stated small squared singular value with O_a(ε⁴) error. The real theta products are positive and have opposite strict monotonicities on [0,π/2]; hence the leading minimum and upper limiting maximum both occur at frequency zero. The Hermite symbol is invertible with continuous bounded inverse because its determinant is bounded away from zero. Poisson summation gives A∼√(π/(8a)), D∼−2πA exp(−π²/(8a)), and ϑ₄(0,e^(−2a))∼2√(π/(2a)) exp(−π²/(8a)) at small a; at large a the nearest Gaussian term gives A∼exp(−a/2) and D∼−2aA. These recover both displayed width regimes and the squared bound ratio.

## originality

PASS

The distinct claim is quantitative: the exact Gaussian collision coefficient, the frequency profile yielding the sharp minimum, and the critical Hermite symbol. Ordinary alternating complete interpolation is covered by an earlier theorem and is not credited as new. The closest structural catalogue match uses a different generator, and the inspected derivative-sampling theorem does not give the critical Gaussian design.

## value

PASS

Two samples per period-two cell are a natural critical design. The global sharp coefficient measures noise amplification as value observations merge; its pronounced width dependence would not follow from interpolation existence. The exact critical value-plus-derivative replacement is stable and has an explicit symbol, explaining why the confluent observations do not share the duplicated-value degeneracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
