---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For any even k>=2 and positive fixed b_j, alternating the unit vectors transforms SDP improvement over the all-path-cut into (w||v_k-v_0||^2-Σb_j||v_j-v_{j-1}||²)/4. Weighted Cauchy proves zero gain through w_c=1/S and the unit-sphere collinearity argument makes the critical Gram optimizer unique. For w near w_c, shortest great-circle replacement reduces path minimization to positive small angles, b_j sin(delta_j)=lambda. Expansion Theta=S lambda +T lambda³/6, sin Theta=S lambda-(S³-T)lambda³/6 gives lambda²=6S²(w-w_c)/(S³-T)+O((w-w_c)²). The SDP envelope derivative integrates to 3S⁴(w-w_c)²/[4(S³-T)] plus cubic error. Strict positivity D=S³-T and Jensen T>=S³/k² give the unique uniform minimum and unbounded heterogeneous curvature. Independent high-precision stationary-branch checks agree in 12 weighted small-epsilon instances; they are corroborative, not the proof. Integer cut optimum is constant near w_c since closing edge remains strictly cheapest.

## originality

PASS

The SDP/vector formulation and unweighted odd-cycle gap are old. The assessed claim is a local universal arbitrary-path-weight curvature law and its reciprocal-third-moment heterogeneity extremum, not mere proof of nonexactness on odd cycles. Delorme-Poljak 1993 full weighted spectral bound remains a material unresolved source.

## value

PASS

The exactness threshold w_c alone says nothing about onset sensitivity. The explicit sharp curvature and square-root optimizer angle identify how quickly a standard combinatorial relaxation loses tightness as one weight crosses a boundary, and characterize the most/least stable positive profiles at fixed effective resistance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
