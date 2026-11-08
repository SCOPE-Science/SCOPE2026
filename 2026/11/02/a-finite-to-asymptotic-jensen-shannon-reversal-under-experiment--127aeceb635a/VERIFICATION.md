---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The two original alternating categorical product laws share exactly one 2m-string (C,A)^m of equal mass t^m, hence their JS=(1-t^m)log2. Grouping homogenized A/C words by count produces exact entropy defect H_m=(1/2)sum_{k=0}^{2m}h(a_mk,b_mk). Its m=1 expansion gives Delta_1=(3/4)log(4/3)t+O(t²log(1/t))>0 near zero. For any fixed t∈(0,1), choosing k=m+floor(cm) for small c>0 makes BOTH word-type probabilities decay exponentially slower than t^m: Stirling exponents -I(c)+(1-c)log(2-t)+c log t and -I(c)-c log t are positive. Since h(a,b)>=2log2*min(a,b) and equal-ratio words can be grouped, H_m>t^m log2 eventually, thus Delta_m<0. Independently recomputed high-precision finite entropy defects at t=.1: m=1 +.00698573, m=2 +.000216649, m=3 -.0000692693, m=4 -.00002007175; inspected exact Fraction logarithm verifier.

## originality

PASS

The homogenization operation and general f-divergence comparison framework are prior art, as are the binary-entropy formula and classical JS. The inspected Kontorovich 2026 manuscript discusses unit constants and product/marginal averaging, but does not state this ternary experiment where Jensen–Shannon difference changes sign from finite to asymptotic repeated blocks.

## value

PASS

Motivated explicit counterexample where hiding coordinate labels via marginal homogenization first increases but eventually decreases full-product Jensen–Shannon information. The exact short-block expansion, four certified signs and for-every-t asymptotic reversal reveal a genuine information-theoretic boundary, not a mechanically known inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
