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

Execute `python3 verify.py` from a directory containing the embedded standalone verifier. The script uses only the Python standard library and reconstructs graph adjacency and legal ordinary-blue forcing from first principles. It compares every three- and four-vertex subset at prism lengths \(7\) through \(12\), computes all five dihedral/layer-switch orbits, confirms the \(13n\) count, computes exchange/sliding neighbors and exchange connectivity, and checks the representative exchange-neighbor matrix. It also checks the complete two-path/fourth-vertex local success lists at lengths \(7\) through \(24\).

Observed result: `VERIFY_OK`. At \(n=7\) the script finds 91 minimum sets and 336 exchange edges; at \(n=12\) it finds 156 minimum sets and 576 exchange edges; sliding edges are zero in every tested instance. Finite tests are not certificates for every order. The proof in `RESULT.md` supplies the all-order necessity/sufficiency argument and explains why the reconfiguration comparisons reduce to finitely many bounded relative-column patterns. This is not an independent mathematical audit.
