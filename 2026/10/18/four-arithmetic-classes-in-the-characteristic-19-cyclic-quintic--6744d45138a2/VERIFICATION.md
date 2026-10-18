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
# Reproducibility checks

Run `python3 verify.py` with the Python standard library. The program independently expands the two binomial Cartier coefficients modulo \(19\), verifies their factorizations, exhausts all \(17\) legal rational parameters under the anharmonic action, and counts points in the explicitly defined field \(\mathbf F_{19^2}=\mathbf F_{19}[u]/(u^2-2)\). It confirms the four orbit sizes, corresponding extension counts \(514,354,404,424\), and the maximum bound. All programmed assertions passed when executed.

The proof for *all* geometric parameters is algebraic and appears in RESULT.md; the finite checks are neither assumed to certify infinite-field statements nor substitutes for their Cartier proof. Mathematical independence or formal certification is not claimed. Independent audit: not performed.
