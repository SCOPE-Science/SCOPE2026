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

With the frozen unnormalized Fourier convention, each side is real and hence the real-valued other side is even; positivity yields both zero entries f(0) and f̂(0) strictly positive. Thus inversion pairs plus the origin give the two odd sizes; Tao's prime-order uncertainty gives k+ℓ≥p+1. For k≤ℓ, set p=2m+1, k=2r+1, ℓ=p−2s. The inequalities give s≤r≤m−s. Consequently the s smallest sampled cosines c_j=cos(2πj/p) have j≥m−s+1>p/4 and are negative. The product of (t−c_j) over these roots times (t+2)^(r−s) is exactly zero there and positive at every other cosine node. The substituted Laurent factors have positive coefficients at exponents −1,0,1; for any |h|≤r one can choose |h| signed linear terms and constants elsewhere, proving a_h>0 and no cancellation. The exponents are distinct mod p, and evaluating at e^(−2πij/p) yields the advertised Fourier support. Empty products give (1,p); Fourier involution swaps the pair, including (p,1). The phrase 'nonzero group elements' in the frozen scope is understood as elements where the function is nonzero; the proof explicitly includes the origin.

## originality

PASS

The positively constrained converse is the distinct result. Tao exactly covers the unconstrained problem, including prescribed sets, but its witnesses do not meet the two sign inequalities. The positive-definite sources inspected optimize mass or other function values; the closest verified indexed objects concern one-sided positivity, positive tight-frame sampling, or unconstrained composite-order support incidence, not this cone's full support-size diagram. The bounded comparison does not establish historical priority.

## value

PASS

This answers a natural constrained sharpness question for prime-order Fourier uncertainty: both a nonnegative signal and a positive spectrum can achieve the entire allowed size region, including the sharp boundary, with explicit witnesses. That complements both the abstract uncertainty converse, which does not keep signs, and fixed-support mass problems. The classification is uniform in prime order and gives a concrete feasibility baseline for sign-constrained spectral constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
