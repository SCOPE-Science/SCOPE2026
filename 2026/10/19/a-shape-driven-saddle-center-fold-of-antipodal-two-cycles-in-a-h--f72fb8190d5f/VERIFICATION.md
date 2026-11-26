---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Substitution of (y,−y) in the stated map gives K⁻¹V′(y)=−4y, with y>0 forcing 0<s=βy<β, and the exact reduced equation R_p(s)=4(1+p)/t. Direct differentiation gives the sign of R′ as the sign of p−N/D, where D=sA′−A>0 and N=sB′−B for A=sinh(2s)/2 and B=sinh(4s)/8−sinh(2s)/4. The coefficient ratios r_n=(4^n−1)/2 in the two positive series strictly increase. In the variable s² the ratio derivative, multiplied by s², is the positive weighted covariance of n and r_n; its limit at zero is r_1=3/2. Hence R_p falls for p≤3/2 and has exactly one nondegenerate maximum for p>3/2, since R_p′(β)<0. The excluded zero endpoint, R_p(0)=1, and R_p(β)=0 give all equality and open-interval counts. At the maximum the scalar root is quadratic and the parameter derivative of R_p−A_c/t is positive. At each antipodal point the one-step derivative has trace τ=−2−4sR′/R and unit determinant; the return derivative is its square. The inner branch has τ<−2 and is saddle-type. On the outer branch sufficiently close to the fold, −2<τ<−1 by continuity, so the squared multipliers are on the unit circle and nonreal; the wider interval (−2,2) alone would not exclude τ=0. At the fold the double unit multiplier is nonsemisimple. Also, the sum of the two fixed-point equations of F² requires V′(u)+V′(v)=0; at the fold V″(y)=−4K, so locally this equation uniquely gives u+v=0 by the implicit function theorem. This confirms the local fold without extrapolating the count to non-antipodal orbits elsewhere. At p=3/2 the quadratic term vanishes and the quartic is −8/15, giving s⁴∼3(t−10)/16. For ε=p−3/2>0 the quadratic coefficient is 4ε/9+O(ε²), giving s_*²=5ε/12+O(ε²) and peak excess 5ε²/54+O(ε³). Multiplication by A_c∼10 gives the width 25ε²/27. The supplied code was inspected as finite diagnostics only.

## originality

PASS

Credit the fixed-minima map, origin flip and earlier numerical period-two studies to Dikandé. The distinct result supported by the checked evidence is the global-in-parameter antipodal count, including the fold before the origin flip for p>3/2 and the exact degeneracy and width laws. A proof of that count must control the whole positive radius interval, not just the Taylor coefficients or numerical branches near the origin. The inaccessible journal full text leaves a specific priority risk, not an adverse finding.

## value

PASS

This resolves a natural orbit-count question in an already studied map family. It identifies when the origin flip is not the first appearance of antipodal cycles and quantifies the interval with two different orbit types. The proof of global unimodality is the substantive step beyond generic local normal forms or plots, and the fourth-root transition and fold width have meaningful exact normalizations. No nonlinear elliptic stability or full period-two census is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
