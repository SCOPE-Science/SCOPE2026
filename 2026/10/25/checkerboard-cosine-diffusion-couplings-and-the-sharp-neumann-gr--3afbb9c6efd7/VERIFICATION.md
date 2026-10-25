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

# Reproducibility and verification limits

The complete proof, definitions, and boundaries appear in `RESULT.md`. Run the standalone Python 3 script `CHECK.py` with no nonstandard packages; successful execution prints a deterministic PASS line. It evaluates the original modal cosine sums and the derived cotangent-square formula independently over all node pairs for finitely many grid sizes, checks the exact three-node spectral projectors with rational arithmetic, brackets the unique cubic root with rational numbers, and tests representative eventually positive steps.

The script passed 19,645 deterministic finite checks. Those checks support the implementation details but are not a substitute for the analytical proof of the identities for every integer grid size and every real time. The global eventual-positivity time estimate is sufficient rather than a sharp general-grid recovery time. Publication-priority uncertainty remains because equivalent representations can arise from classical periodic spectral-differentiation formulas.
