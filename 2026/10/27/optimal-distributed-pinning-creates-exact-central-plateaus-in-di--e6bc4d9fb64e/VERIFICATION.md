---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For fixed w, positivity of the Dirichlet inverse makes the constant-phase dual vector optimal, giving F=1^T A_w^{-1}1. Differentiation gives gradient -g_j^2 and positive definite Hessian 2 diag(g) A_w^{-1} diag(g), so the simplex optimum is unique and reflected. In the KKT conditions support sites have g=H and the others have g<=H. An unpinned gap between support sites solves Lg=1 with equal boundary values H, so is strictly above H, impossible. On a tail the unique solution is i(m-i)/2+iH/m, and summation of the loaded equation gives (Lambda+2/m)H=d+1-m. The last unpinned site yields H>=m(m-1)/2, which also controls the whole tail since H-g_i=(m-i)(H/m-i/2). With two or more plateau sites nonnegative end weights give H<=m(m+1)/2; a single center instead gives H<=m^2/2 and the zero-budget endpoint. At a shared t_m the (m-1)-st site has g=H and zero weight, so both formulas agree. The zero-budget simplex is a singleton, and d=1,2 give the full flat profile directly. Summing g yields the displayed constant and equality uses a common phase. Independent replay (python3 -B /workspace/branches/independent_replay.py 3) passed 468 exact rational cases across d=1..24, with direct tridiagonal solves, budget and support checks and endpoint samples; finite evidence is corroboration only. The frozen checker clips negative candidates and its line-49 inequality is vacuous with the supplied initial value, so neither is relied on to certify nonnegativity or KKT.

## originality

PASS

Pass for the complete fixed-total-budget solution on the discrete Dirichlet path, including the exact support transitions and piecewise rational value. The unpinned constant, general inverse derivative, and general potential/spectral optimization are not credited as new. The inspected sources do not establish the specific all-ones compliance solution; this is a bounded best-of-knowledge assessment.

## value

PASS

The design problem asks where to put a fixed amount of damping to improve a sharp, structured norm bound, not just to evaluate an already selected matrix. The answer identifies exactly which sites switch from unpinned to pinned as budget increases, certifies the global optimizer among asymmetric allocations, and gives the corresponding sharp inequality rather than a numerical optimization prescription. The support transition and flat-torsion mechanism are informative independently of bibliographic novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
