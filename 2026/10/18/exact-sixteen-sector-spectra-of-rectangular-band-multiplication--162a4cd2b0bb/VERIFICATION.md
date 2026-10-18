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

Run \(\texttt{python3 verify.py}\) in a directory containing the attached Python file. It uses no third-party packages. The script derives the adjacency relation directly from the three semigroup coordinates, then verifies every tensor eigenvector equation in integer arithmetic, as well as degree, trace, connectivity, factor recovery, and the strongly regular Clebsch parameters. It checks all sixteen pairs \(1\le a,b\le4\), and prints \(\texttt{VERIFY_OK 16 rectangular bands}\) on success. The independent-audit channel above is intentionally unperformed; the finite replay is only computational corroboration of the symbolic proof.
