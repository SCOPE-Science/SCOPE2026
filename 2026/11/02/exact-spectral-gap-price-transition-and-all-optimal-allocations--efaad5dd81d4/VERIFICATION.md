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

# Reproducibility and proof boundary

The complete proof is in `RESULT.md`. Its core is a pair of dimension-\(m-1\) Rayleigh-trace upper bounds, an explicit certificate for each price regime, and an eigenvector equality argument that determines all unrestricted optima. The proof does not depend on probabilistic sampling or on external certification.

To repeat supplementary computational checks, run `python verify.py` with NumPy and SymPy installed. The executable independently constructs weighted Laplacians on both bipartite parts, factors their exact small-size characteristic polynomials, tests rational price-regime and critical-boundary formulas, and compares freely asymmetric numerical allocations to the analytic trace bounds. The executed script reported `PASS: 4506 exact symbolic/rational and independent numerical checks`.

Scope of the computation: exact characteristic-polynomial factors for \(m=3,4,5,6\) and three nontrivial conductance pairs, rational checks for \(m=3,\ldots,8\), and 2,160 non-symmetric random allocations. These checks do **not** exhaust all conductances or establish infinite statements on their own. The all-\(m\) theorem and all-optimizer classification are supported by the algebraic proof in `RESULT.md`. The self-review is not an independent audit.
