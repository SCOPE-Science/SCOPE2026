---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For all integers m,n≥2 and α,β≥0, P=Z_{Kmn}+αΔ_A+βΔ_B in the fixed standard-coordinate Euclidean metric has diameter squared equal to mn(m+n)+2α²+2β² exactly when α≤m−1, β≤n−1. The complete source RESULT.md proof gives exact signed-matrix expression max_s [∑r_i²+∑c_j²+2αosc(r)+2βosc(c)]+2α²+2β² by extreme-point convexity; D_B≥2(m−1)osc(r) from mixed columns and D_A≥2(n−1)osc(c) from mixed rows establish upper bound. All-positive signs realize equality, a whole flipped row/column gives strict excess ≥4n(α−m+1) or ≥4m(β−n+1). Independent exact signed-matrix checks for m,n=(2,2),(2,3),(3,3),(3,4) and 16 weight cases reproduced inequalities and sharp region. Finite checks are corroborative only; universal proof is combinatorial.

## originality

PASS

Best-of-knowledge original specific quantified claim/optimization or equality classification, compared at theorem/implication level with the primary sources and indexed results below; the SCOPE same-date identical listing is the audited result itself, not independent preexisting coverage. Named residual risks do not constitute a demonstrated dominating earlier theorem.

## value

PASS

The sharp two-weight Euclidean-diameter stability rectangle and quantitative supercritical witnesses are a natural metric invariant of a combinatorially established shuffle operation. The general shuffle combinatorics and known zero-weight graphical-zonotope diameter do not give the nonzero threshold. It provides a reusable all-size exact obstruction when adding simplex summands, rather than just a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
