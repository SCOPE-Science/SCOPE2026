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

Original UPHCT likelihood from pinned RESULT and 2026 AIMS primary paper checked directly. Set δ=1/γ; all δ powers cancel, yielding L(δ)=(1+δ)^ν(1+δs*)^(−R*) Π(1+δxi)^(−2−Ri). Score D(δ)=ν/(1+δ)−R*s*/(1+δs*)−Σ(2+Ri)xi/(1+δxi). For yi∈(0,1), yi/(1+δyi)≥yi/(1+δ), so D≤(ν−T)/(1+δ), strict if T=ν with interior times. If T≥ν, likelihood strictly declines in δ>0 and has supremum only δ=0, γ=∞, uniform limit. If T<ν, D(0)>0, L(∞)=0 and D asymptotically negative, so a finite global maximum exists (uniqueness not claimed). Complete iid case T=2Σxi gives xbar<1/2, with positive boundary event probability [γ/(2γ+1)]^n. Independent score evaluations for two complete samples and one censored sample confirm signs; proof is analytic.

## originality

PASS

Almetwally 2026 exact source writes f,S, UPHCT L and Newton–Raphson estimation, illustrates finite profile maxima, but no iff existence boundary T<ν in examined full text. Muhammad 2016 finite-support parent distribution discusses numerical estimation rather than same censoring criterion; Jiang 2013 different bounded-support model has unrelated boundary behavior. Resultary semantic lookup surfaced different lifetime thresholds, none same likelihood. Criterion corrects the implicit blanket assumption of interior numerical maximization; inaccessible old statistical appendices remain minor risk.

## value

PASS

Identifies an exact, data-computable condition that determines whether the finite MLE exists under the specific progressive censor design. Without the test Newton iterations can drift to infinity and finite observed-information/Wald reporting is invalid for a positive-probability sample set; this is a methodologically motivated correction with direct inferential consequences, not a routine score algebra restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
