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

# Reproduction and verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script executes exact full-function enumeration for \(2\le n\le6\), exact-rational mixed-moment and binomial-curvature checks across further sizes, checks the crossover's finite one-switch structure up to \(n=99\), and numerically compares asymptotic threshold calculations. The checked script returned `PASS: 94602 checks; exhaustive n=2..6; crossover=0.584724386479633`.

The analytical argument in `RESULT.md`, rather than the finite program, proves the asserted identities and signs for every admissible integer parameter. The numerical limit check does not prove the limit; the derivative and compact-sign argument do. The checker uses no outside data, packages or hidden files.

Scientific scope: independent uniform map images and cycle-weighted covariances; a cycle-Palm law is not an ordinary conditional law given existence of a cycle. Source priority is limited by the literature evidence described in `RESULT.md` and `REVIEW.md`.
