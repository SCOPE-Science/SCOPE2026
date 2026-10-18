---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The gradient step is A=a uuᵀ or B=b vvᵀ (a,b∈(0,1)); direct products give RR Gram =a²b²c²/2 (uuᵀ+vvᵀ) and IID Gram=1/4[(a⁴+a²b²c²)uuᵀ+(b⁴+a²b²c²)vvᵀ]. Since u,v are independent, x↦(uᵀx,vᵀx) is invertible and IID−RR is PSD iff a≥bc and b≥ac. Above boundary the two coefficients have opposite signs, proving true directional reversal. The bisector maximizes RR Gram; IID−RR evaluated there is (1+c)(a⁴+b⁴−2a²b²c²)/8>0, yielding strict worst-case improvement. IID = RR/2 + (a⁴(uᵀx)²+b⁴(vᵀx)²)/4 gives RR<2 IID for all nonzero x, sharp as a→0 along x⊥v. Exact rational witness a=1/4,b=3/4,c=3/5,x=(-4/5,3/5) yields RR=81/20000 versus IID=53/20000; independently checked. All continuous quantifiers follow from the exact Gram argument, not the tests.

## originality

PASS

Recht–Ré compare two-matrix product operator norms, which do not entail an all-initial-vector Loewner inequality; De Sa gives counterexamples for other sampling horizons/metrics; Safran–Shamir study multi-epoch/conditioning regimes. A related 2026 manuscript separates risk metrics in other families but does not supply this exact two-rank-one angular threshold in the inspected material. Resultary related results are about unrelated rank-one joint radii and sampling. The asserted contribution is the complete pointwise-vs-worst-case sharp frontier on a minimal noncommuting strongly convex example.

## value

PASS

Sampling without replacement versus IID is fundamental to stochastic optimization. The first nontrivial two-component case already exhibits a sharp opposite ranking depending on whether one fixes an initial direction or takes the worst direction; the iff frontier and universal factor-two limit pinpoint when common blanket intuitions fail. The parameters a/b and angle have direct geometric meaning and the classification is not an unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
