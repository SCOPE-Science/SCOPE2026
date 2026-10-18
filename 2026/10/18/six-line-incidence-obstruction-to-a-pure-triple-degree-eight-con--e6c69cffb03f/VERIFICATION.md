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

# Reproducibility and proof checks

Run `python verify.py` using Python 3.9 or newer; no third-party packages or external data are needed. The script exactly enumerates the permitted three-triple six-line incidence hypergraphs, recomputes the symbolic determinant of the conic-evaluation matrix by the Leibniz formula, checks a normalized six-line coordinate example, and independently confirms the integer Bézout counts and the necessary near-free numerical identity.

The verified determinant polynomial is \(u^2(u-1)^2\). The proof requires \(u\ne0,1\), the distinctness and nonconcurrency boundary conditions for the normalized lines. The sample \(u=2\) calculation checks only a representative and is not substituted for the symbolic identity. The theorem is solely a geometric nonrealizability statement, not an exhaustive census of degree-eight nearly-free arrangements.

The mathematical review reported in `REVIEW.md` is not an independent audit.
