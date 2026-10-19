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

# Reproducibility

Run `python3 verify.py` from the directory containing the standalone script. It uses Python's standard library only.

The script builds the full graph from *literal compositions* of elementary collapse maps rather than taking the claimed adjacency condition as a premise. It then checks the derived adjacency rule, degrees, all clique coefficients, and all inclusion-maximal clique counts for \(2\le n\le7\). It computes the characteristic polynomial independently by exact integer matrix products, matrix-power traces, and Newton identities for \(2\le n\le6\), and matches those coefficients against the theorem's factored polynomial.

The observed output concludes with `VERIFY_OK_DEFECT_ONE_COMMUTING_SPECTRUM`. For \(n=4\), the direct maximal-size histogram is \(\{2:12,3:4\}\); for \(n=6\), it is \(\{3:120,4:210,5:6\}\). The program does not prove formulas for arbitrary \(n\), nor verify literature novelty or external independent review. The uniform proof is in `RESULT.md`.
