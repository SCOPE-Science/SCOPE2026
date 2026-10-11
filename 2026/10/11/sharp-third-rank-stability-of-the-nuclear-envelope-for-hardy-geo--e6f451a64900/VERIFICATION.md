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

# Reproduction and limitations

Mathematical proof: see RESULT.md. All-dimensional correctness relies on exact beta/angular integrals, the integral-test bounds for the polygamma series, and the singular-value decomposition; no finite sample supplies an infinite proof.

Run `python3 verify_hardy_rational.py` from this package. It uses only the Python standard library `fractions` and `math` to enclose \(e^1\), \(e^{1/2}\), \(e^{4/3}\), and \(e^{3/4}\) by rational Taylor bounds and prove the initial diminishing-increment inequalities. It also checks the elementary strict concavity coefficient bound at \(x=5/2\). The printed success strings indicate precisely these finite inequalities and no more.

The published motivating paper's full text was unavailable through the permitted retrieval paths, so coverage beyond the accessible material remains a documented risk. Same-model review is recorded in REVIEW.md and AUDIT.json. Independent audit was not performed.
