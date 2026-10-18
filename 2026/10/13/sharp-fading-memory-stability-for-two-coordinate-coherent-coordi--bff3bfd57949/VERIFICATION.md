---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Read exact CoCD elementary update rule and the derived 3-dimensional sweep state (x1,x2,h). Independently constructed first and second coordinate refresh/decay linear maps with SymPy, multiplied to reproduce T and det(zI−T)=z³+bz²+cz+d. Symbolically verified p(1)=α²(1+γ)²(1−ρ²), −p(−1)=[2−α(1+γ)]²+α²ρ²(1−γ)² and 1−c+bd−d²=α(1+γ)(1+αγρ²)Q(α). Strict real-cubic Schur criterion and determinant boundary prove stable iff 0<α<4/[1+γ+sqrt((1+γ)²−8γ(1−γ)ρ²)]. Independently checked sampled spectra and endpoint γ=0,1 and ρ=0; exact proof, not samples, handles all γ in [0,1] and |ρ|<1. Matrix still describes both full-coordinate iterate updates, not standard block CD.

## originality

PASS

The 2026 CoCD article introduces the rule and reports sufficient convergence conditions, whereas the frozen statement gives a necessary-and-sufficient two-coordinate positive-quadratic stability frontier, including strict stabilization beyond step 2 under coupling. The characteristic cubic Schur test is prior mathematics, not claimed new; new content lies in applying it to the exact nontrivial fading-buffer sweep. Closest full original article was not accessible, so possible Appendix overlap is retained as risk, not automatically failed.

## value

PASS

The exact stability set (including α>2 enabled only by partial memory and strong coupling) answers a nontrivial optimizer-design question for the algorithm, countering the naive implication that worse Hessian conditioning always contracts the stable step. Boundaries γ=0,1, ρ=0, and zero-buffer starts are treated, giving natural complete classification for the simplest coupled case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
