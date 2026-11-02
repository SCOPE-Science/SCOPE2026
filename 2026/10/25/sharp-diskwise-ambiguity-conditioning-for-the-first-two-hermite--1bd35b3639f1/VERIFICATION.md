---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Direct Hermite–Laguerre identities give A h0=e^(−s/2) and A h1=(1−s)e^(−s/2) with s=π(x²+ω²). The sharp multiplier squared is F_w(s)=e^(−s)[1+w s(s−2)] and the essential infimum is its minimum on [0,R]. F_w derivative e^(−s){−1+w[2−(s−2)²]} shows only possible interior minimum 2−u for w>1/2, while s=R is an increasing-in-w bottleneck for R>2. Inner A(w) decreases strictly and endpoint B_R(w) increases strictly; their unique crossing solves the displayed root equation. For R<=2 direct sign gives all optimizers. Implicit derivatives and Taylor/asymptotic expansions prove monotone w*, 1/2+(R−2)²/16 near threshold and 1−w*~(R−1)²e^(1−R). Independently compared analytic minima and the allocation root against 501 alternative weights at ten radii, matching the scalar bound. This tests samples only, not the continuum proof.

## originality

PASS

The exact submitted statement was compared against equivalent terminology, general bounds, named exact prior tables and their logical implications. Inspected relevant sources support a distinct increment; missing full texts and hidden equivalent special cases remain documented best-of-knowledge risks.

## value

PASS

The design problem of allocating finite measurement precision between two physically natural Hermite ambiguity windows is an exact condition-number minimax problem for unrestricted linearized inversion. Its radius threshold, all optimizers and asymptotic inverse-norm gain are quantitatively useful in choosing windows and interpreting stability annuli. The paper carefully excludes the nonlinear signal-constrained problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
