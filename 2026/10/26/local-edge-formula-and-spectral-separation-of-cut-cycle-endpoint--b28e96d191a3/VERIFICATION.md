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

# Verification of the endpoint projection formulas

The all-parameter proof appears in `RESULT.md` and does not depend on numerical enumeration. The supporting checker `check_srg.py` uses exact rational arithmetic and the Python standard library to form the grounded graph Laplacian, invert it by Gauss–Jordan elimination, reconstruct each edge-source potential, and compare every corresponding cut/cycle column \(\ell_1\) norm with the local induced-edge formula. Graph strongly regular parameters are independently recomputed from adjacency lists, not supplied as trusted inputs.

Execute `python check_srg.py` in a directory containing the checker. Expected closing line: `SRG_HODGE_EXACT_OK cases=8 columns=333`. The eight tested graphs and all \(333\) columns are enumerated in the checker. Exact expected values for the cospectral pair are \((9/4,21/8)\) for the rook graph and \((19/8,11/4)\) for the Shrikhande graph. No floating-point tolerance is used.

The mathematical proof requires \(\mu>0\), standard counting-measure edge norms and the canonical Euclidean-orthogonal projector. The finite tests do not establish arbitrary-parameter claims or exhaust all strongly regular graphs. The originality assessment is based on identified literature comparisons and may be revised if a covering source is found. Independent audit status: not performed.
