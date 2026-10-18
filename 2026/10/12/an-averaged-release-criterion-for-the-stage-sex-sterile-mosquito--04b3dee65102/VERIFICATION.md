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

Normalize x=BF/C and u=BHM: q=(A/C)*x/[(1+x)((D+u)x+u)]. Differentiating gives sign u-(D+u)x², maximizer x=√(u/(D+u)) for M>0, continuous envelope limit at M=0. Thus F’/F<=Q(M_s(t))-delta_F and integration yields the exact comparison bound for each F(0)>0. Strict eventual negative limsup average gives global exponential decay; for periodic profiles the time average is a single period integral. Independent 80-digit quadrature with the same source-derived K=416990000/20553, A=2499/40000, C=2/25, D=51/200, H=1/10, delta_F=1/25 gives 0.038221770950267804205... at s=120000 (<.04), and 0.073750171814416675109... at s=60000 (>.04). The result says nothing about persistence when the sufficient test fails. The application is separated from proof: quadrature establishes numerical strict inequality, analytic envelope establishes global theorem.

## originality

PASS

He–Li–Liu 2023 derive exactly this model, an asymptotic pointwise sterile-population threshold, and simulation Figure2a of extinction for the crossing-threshold sinusoid; those are credited. The new state-uniform maximization Q(M) and negative average comparison yield an analytic sufficient criterion applicable where their pointwise theorem is silent. Other periodic sterile-release results involve distinct models and stability notions; precise equivalence in a less accessible periodic paper remains a risk.

## value

PASS

A natural gap is that pointwise release thresholds do not explain why periodically subthreshold release eliminates the mosquito population in the motivating simulations. The explicit integral envelope closes that source-specific question and supplies a checkable sufficient criterion for arbitrary nonnegative periodic input, relevant for periodic-control design, while carefully not claiming necessity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
