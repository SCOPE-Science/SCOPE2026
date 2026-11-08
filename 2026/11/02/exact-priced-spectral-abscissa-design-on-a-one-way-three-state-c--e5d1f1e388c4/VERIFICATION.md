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

Det(lambda I-Q)=lambda(lambda²+S lambda+T), with Δ=S²−4T=−(u+v+w)(−u+v+w)(u−v+w)(u+v−w) for square-root rates. For Δ>0 decreasing unique too-large u to v+w raises the gap while lowering cost, so no positive optimum outside the triangle domain. Inside Γ=S/2 and cost ratio is quadratic Rayleigh quotient. For unequal prices the cheapest coordinate grows to a triangle facet u=v+w; 2x2 generalized eigenvalue equation yields Λ=3/(P−δ). Perron positivity gives unique interior facet if least price strictly unique; tie cases produce boundary nonattainment or all-price continuum. Repeated nonzero eigenvalues cannot be diagonalizable in irreducible one-way Q because that would force every off-diagonal positive. Independent 6 specific price triples' generator eigenvalues match the formula. All-real parameter result rests on analytical argument.

## originality

PASS

Boyd–Diaconis–Xiao optimize reversible/discrete-time transition SLEM, and Gerencsér–Hendrickx–Van Dooren 2015 require discrete-time doubly stochastic cycle kernels. None fixes three independently priced one-way CTMC jump rates or yields price ties and Jordan exceptional point. Relevant Resultary searches found different cycle spectral problems but not this exact constrained spectral abscissa. Specialist nonnormal Markov design remains a risk.

## value

PASS

Complete analytic solution of smallest genuinely directed nonreversible mixing design with cost asymmetry, sharp distinction between attained and unattained optimum and a defective eigenvalue mechanism. It explicitly separates asymptotic exponent from finite-time mixing, making a useful benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
