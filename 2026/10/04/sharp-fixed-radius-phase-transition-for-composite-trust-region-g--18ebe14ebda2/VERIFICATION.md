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

After dividing by \(a>0\), each subproblem minimizes \(xz+\theta|z|\) on \([x-\eta,x+\eta]\), where \(\theta=\lambda/a\). Its two slopes give the complete set-valued update map directly. For \(\eta<2\theta\), every first crossing from an outer region lands inside \((-\theta,\theta]\); all subsequent singleton steps move toward zero, and every threshold choice enters the strict inner region, so finite absorption follows for all selections. At \(\eta=2\theta\), the threshold minimizer intervals contain the opposite threshold points. For \(\eta>2\theta\), any \(c\in(\theta,\eta-	heta)\) maps uniquely to \(c-\eta<-	heta\) and uniquely back to \(c\). The frozen exact-rational script was read and is consistent with each regime but is not used as the quantified proof.

## originality

PASS

Kovalev's primary paper presents trust-region/normalized-gradient methodology and composite convergence bounds, but the inspected full-text theorem gives a best-iterate stationarity guarantee with a radius-dependent residual rather than an exact constant-radius orbit classification. Zhu-Xu-Ji's recent abstract confirms a regularized trust-region framework, but open full-text routes failed in this run; one authorized institutional attempt returned an operational error and was not retried. Resultary searches found no matching quadratic-plus-absolute-value threshold or cycle family. The accessible prior statements therefore do not imply the exact \(2\lambda/a\) selection-robust boundary.

## value

PASS

The quadratic-plus-absolute-value model is the canonical scalar sparse composite objective, and \(\lambda/a\) is its intrinsic balance scale. The exact transition between selection-robust finite absorption, tie-driven critical cycling and an open tie-free supercritical cycling band is a motivated algorithmic boundary, not a routine verification or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
