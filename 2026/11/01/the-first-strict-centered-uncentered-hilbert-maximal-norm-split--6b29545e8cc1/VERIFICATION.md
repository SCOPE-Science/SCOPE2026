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
# Reproducible exact checks
Run `python checker.py` with Python 3 and SymPy. The program directly enumerates all distinct graph-metric balls for paths with three and four vertices, independently forming the centered and uncentered row choices. Its strict bounds use rational leading principal minors (Sylvester criterion). Its exceptions are checked by exact characteristic-polynomial identities, rational Rayleigh vectors and Sturm root counting; no floating-point tolerance enters the certificate.

Expected counts: three-vertex path uncentered 36 matrices (35 strict), centered 18 (17 strict); four-vertex path uncentered 400 (398 strict) and centered 144 (142 strict). The final line is `CERTIFICATE_OK`. The independent mathematical rationale for lifting these finite certificates to nonlinear operator norms is the positive row-selection argument in RESULT.md. Boundaries: only counting \(\ell^2\), metric balls, and connected simple unweighted graphs with at most four vertices where stated. Independent audit has not been performed.
