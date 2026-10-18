---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytical proof gives a finite-horizon coefficient identity for every real \(0<\alpha<1\), every \(\beta>0\), and every integer \(N\ge1\). A standalone verifier is included as `verify.py`. Its observed output was:

```text
VERIFY_OK: exact Taylor and finite combinatorial identities; independent circle quadrature of covariances, triple moments, and cumulative moments
```

The verifier uses exact rational arithmetic for the order-two Taylor iterate recurrence for five rational parameters through fifteen iterations, and exact arithmetic to compare alternative finite third-moment combinatorial sums for thirteen horizons. It separately integrates explicit circle iterates by deterministic quadrature for \(t=-1/2,0,1/2\), comparing every requested lag through six and all third moments with \(0\le i\le j\le k\le6\), plus cumulative moments for horizons one to seven. These finite checks support transcription and algebra; the proof in `RESULT.md` supplies the all-parameter statement, including analyticity and dominated convergence. The asymptotic statements do not follow from finite enumeration. The global literature novelty assessment remains bibliographic, not certified externally.
