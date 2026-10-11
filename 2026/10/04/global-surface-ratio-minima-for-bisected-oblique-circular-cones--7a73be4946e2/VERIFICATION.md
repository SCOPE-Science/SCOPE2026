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

Fresh calculus reconstruction confirms all three global minima. With A=sqrt((1-au)^2+b^2), B=sqrt((1+au)^2+b^2), u in (0,1), one has B>A for a,u>0, so I_- > I_+ and J_+=integral w/A > J_-=integral w/B. Since d_b I_±=b J_±, the derivative numerator for I_+/I_- is b(J_+I_- - J_-I_+)>0; adding a positive common constant preserves positivity. For the overlap-inclusive ratio the common term c(b)=sqrt(a^2+b^2)+pi/2 contributes c'(I_--I_+)>0 as well. Thus every ratio is strictly increasing in b and the global problem reduces to b->0+. The boundary formulas split at a=1; the a<=1 branches are decreasing, while for a>1 the substitutions x=asin(1/a) give the stated one-variable derivatives and unique critical equations 2x=pi cos x for lateral/overlap and 2x+pi=2pi cos x for total area. The reported minimizers and values satisfy those equations. Nonattainment follows from b>0.

## originality

PASS

PASS. Finch's primary full text is unusually decisive evidence of the gap: immediately before the ratio analysis he says rigorous proofs of minimality are not supplied and numerical confirmation guides the intuition; Sections 4 and the Addendum then explicitly conjecture that only a>1 with b->0+ is relevant and compute the boundary critical values 0.1892..., 0.4729..., and 0.5946.... The submitted monotonicity theorem proves that conjectured boundary reduction globally for all b>0 and therefore turns Finch's numerical/boundary candidates into exact unique global infima. Searches of adjacent cone-area optimization literature and Resultary did not locate a stronger theorem for these three half-cone ratios.

## value

PASS

PASS. The result closes an explicit optimization gap in a named primary source. Proving that the full two-parameter problem collapses monotonically to a singular boundary is a substantive structural step; the resulting exact unique minimizers answer Finch's question rather than merely recomputing his numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
