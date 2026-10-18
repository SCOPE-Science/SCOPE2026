---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

In Q2, the affine branch has fixed p_b=(-(b+2)/5,(2b−1)/5), displacement map A=[[-1,−1],[1,−1]], A²=[[0,2],[−2,0]], |det A|=2, AᵀA=2I. With α=(b+2)/5, β=(2b−1)/5, b>1/2 gives α,β>0 and β<2α. Imposing the first three strict Q2 tests gives the stated bounded polygon v>−β,v<α/2, −α−v<u, v−β<u<β/2. Its horizontal-width integral yields C(b)=25β²/8=(2b−1)²/8 for b≤1 and (-2β²+18αβ−3α²)/8=(b²+2b−2)/8 for b>1; the latter integral independently recomputed symbolically. For every S3 point, inverse first component (−u+v)/2<β/2<α and second −(u+v)/2>−β follow from −u+v<β and u<β/2; hence A⁻¹(S3−p)+p⊂Q2 and inductively S_{n+1}=p+A⁻¹(S_n−p), n≥3. Thus area multiplies exactly 1/2 for every visit, diameters contract by 1/√2 and p is the sole eternal survivor. Strict boundary witness w=(α,α+β) gives failure at n2 by interior perturbation, proving sharp cutoff. Under uniform area on S3, tail P(τ≥3+k)=2^{-k}, hence geometric mean exit time 4. Actual rational clipping checker was read and independently symbolic-check for b>1 confirms its area branch; finite parameter tests are not proof for every b.

## originality

PASS

Cima–Gasull–Mañosa–Mañosas, arXiv:2410.01052 Proposition 17 identifies the repelling Q2 fixed point and says no other point survives forever, but does not state the exact full-parameter finite visit polygon, area profile, earliest inverse-similarity onset or conditional geometric first-exit distribution. Their subsequent entropy paper concentrates on graph-supported asymptotic dynamics, not 2D transient area. Related published SCOPE repelling-cycle and ultradiscrete Selkov first-exit laws are DIFFERENT maps or itineraries; shared halving factors from expanding branches are not an implication of the exact Q2 n3 cutoff and C(b). No strong prior containing the precise area phase and all-time survival formula was found; residual risk of independent piecewise-affine residence-time calculations remains.

## value

PASS

Finite-time escape and initial-condition area near an explicitly repelling focus quantify transient dynamics beyond qualitative eventual departure. An exact sharp onset index, polygon combinatorial transition at b=1, global geometric law and parameter-dependent area are motivated structural measurements of a naturally studied absolute-value map. Their nontrivial branch geometry prevents classification as routine linear-algebra relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
