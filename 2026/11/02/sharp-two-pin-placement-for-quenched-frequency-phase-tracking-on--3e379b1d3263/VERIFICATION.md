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

# Reproducibility and verification

Execute `python3 verify.py` from this collection. The saved standalone program requires Python 3 standard-library modules only. Its successful output is:

`PASS 500343 finite checks; exact block identities, path enumeration, optimal gaps and asymptotic consistency`

The program checks exact rational inverses of Dirichlet–Neumann and Dirichlet–Dirichlet path Laplacians for lengths through 20, all pinned pairs on short paths through 12, balance inequalities for paths through 500, and seven large-path numerical consistency checks through 10000. It does not exhaust all finite sizes and cannot establish large-size asymptotics; those rely on the displayed Green-kernel identities, polynomial convexity, and unique continuum minimizer in `RESULT.md`.

No independent scientific audit, external priority verification, or exact nonlinear/finite-reset physical validation has been performed.
