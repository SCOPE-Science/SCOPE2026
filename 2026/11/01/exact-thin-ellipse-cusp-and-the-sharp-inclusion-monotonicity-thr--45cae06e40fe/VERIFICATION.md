---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For the nested ellipses K_a=(a cos t,sin t), the frozen exact boundary integral and its differentiated decomposition Fp prime=Np+Tp are valid for p>-1 and a>0. For p>=0 both radial weight and arc-length factor increase pointwise. For -1<p<0, Tp=O(a log(1/a))=o(a^p); after t=az, Np/a^p converges by an integrable uniform majorant to 2p sqrt(pi) Gamma((1-p)/2)/Gamma(1-p/2)<0. Integrating gives the exact negative coefficient Cp a^(p+1), and Fp prime(1)=pi(p+1)>0 forces an interior minimum. The affine horizontal contraction gives d_H(K_a,K_{a/2})=a/2, so the nonzero difference quotient rules out exponent>p+1 on this smooth nested family. Independent high-precision quadrature at p=-0.5,-0.25 and a=0.002 reproduced the predicted cusp coefficient within expected pre-asymptotic error. This does not claim global decrease, unique minimum, or new universal exponent.

## originality

PASS

Best-of-knowledge originality of the complete evaluated claim: Same functional is not same assertion: a universal negative result does not entail a counterexample within every negative p on this narrower smooth centered ellipse family. Even stronger domain-wide continuity statements fail to dominate the new signed elliptic cusp and all-p monotonicity classification; the Hölder exponent itself is explicitly credited to prior work. No inspected result directly implies all-negative-p decrease on concentric thin ellipses or the evaluated coefficient. An inaccessible relevant primary source remains documented uncertainty. Residual source-access and priority risks are explicit.

## value

PASS

The all-negative-exponent smooth-ellipse counterfamily and exact signed cusp coefficient answer a natural geometric boundary question left open by general weighted perimeter rigidity or Hausdorff modulus theorems. Its fixed-major-axis, full-dimensional smooth examples distinguish it from point/disk scaling; the universally sharp exponent itself is acknowledged prior art.

The dated certificate retains the supplied scientific assessment, sources and limitations.
