---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Checked conditional nonacute angle at X=(x,0) using ordered pairs on all four rectangle edges. The disjoint contributing side pairings give A=2wh+6x(w−x)+2(L+R+G+H), and elementary integration yields the two s=x(r−x) branches separated at s=1. Integrating the short and long sides gives B and S; when r>2 integrating ΔA=−r(s−1)²/s+2(s−1)log s over central interval gives C. Since at most one angle is nonacute for a nondegenerate triangle (including collinear triples on a side), the factor three is correct. Expansion with r=2+ε,x=r/2+sqrt(ε)t yields ΔA≈−ε³t²(1−t²)², ∫_{−1}¹t²(1−t²)²dt=16/105 and final coefficient 4/945. Thin-limit expansion agrees. Independent direct Monte Carlo for six r values, square value 23/96, cusp high-precision coefficients and thin r=1000 corroborated; no infinite claim inferred from sampling.

## originality

PASS

The public 2012 square boundary answer gives r=1 but neither all-aspect F(r) nor r=2 branch onset. Gaussian random triangle and invariance-based models have distinct sampling distributions. Targeted Resultary and public literature searches did not identify stronger all-rectangle perimeter law; priority remains best of knowledge.

## value

PASS

Exact probability for a natural continuous one-parameter geometric model, including a genuine change of analytic regularity at the aspect ratio when the product threshold x(r−x)=1 first becomes possible. The new 7/2 cusp and thin-limit constant are motivated sharp invariants, not restated square data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
