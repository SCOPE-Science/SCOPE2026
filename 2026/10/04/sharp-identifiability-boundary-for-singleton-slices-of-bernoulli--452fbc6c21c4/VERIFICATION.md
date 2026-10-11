---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Writing the singleton probabilities as \(F_i=P_0 o_i\), equality of a nonzero fingerprint forces the odds vectors onto one positive ray. Along that ray the common scale is \(h(u)=u/\prod_j(1+ur_j)\) and \(h'(u)/h(u)=(1-\sum_j p_j(u))/u\), so the scale is strictly increasing up to the unique sum-one point. This proves injectivity on \(\sum p_i\le1\). The homogeneous profile \(u(1-u)^{n-1}\) has its unique maximum at \(1/n\), proving the exact cube threshold and the two-to-one fold above it. At the boundary the fingerprint change is quadratic in a homogeneous perturbation while a one-coordinate marginal gives a linear total-variation lower bound, so no uniform Lipschitz TV upper bound exists. Independent bounded numerical checks reproduced the fold and the boundary blow-up for dimensions two through eight.

## originality

PASS

The closest Bernoulli-product paper proves two-sided TV control from singleton discrepancy only on the smaller cube \([0,1/(2n)]^n\); its Theorem 1.2 was read in the primary PDF. The newer analytic-proxy work treats full product-distribution comparison rather than exact inversion of the labeled singleton slice. Targeted Resultary search over singleton probabilities, exactly-one-success conditioning, odds rays, and the \(1/n\) threshold found related Bernoulli results but no theorem implying the submitted injectivity/stability trichotomy.

## value

PASS

The labeled singleton slice is exactly the statistic used in a current Bernoulli-product TV program. Determining its sharp injectivity boundary, the precise homogeneous fold beyond it, and the loss of Lipschitz stability at the boundary gives a motivated inverse-problem phase transition rather than a small numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
