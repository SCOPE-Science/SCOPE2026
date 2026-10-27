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

# Reproducibility and limits

Execute `python3 geodesic_degree_checker.py` with the Python standard library. The checker enumerates all Prüfer codes for every tree order from 2 through 8 and independently traces the path between vertices 1 and 2. It checks every possible excess-degree vector probability against the exact multinomial-plus-categorical formula, including zero-probability vectors; it also checks the exact distance counts and each conditional off-path degree covariance. Successful execution prints `PASS 648 exact rational Prüfer/path/joint-law checks for n=2..8`.

The unrestricted proof in RESULT.md relies on a general forest-extension identity and a finite polynomial/factorial-moment argument. Exact enumeration through eight vertices does not establish universal validity; asymptotic convergence is proved analytically by multinomial rare-category convergence. The historical-priority comparison has a residual risk of an older equivalent multivariate forest identity. Independent audit remains unperformed.
