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

# Exact reproducibility checks

Run `python3 verify.py` with standard Python 3; no network, optional packages, or other files are needed. The code reconstructs \(C_n\square K_2\) directly, checks all \(349{,}504\) cyclic four-symbol words for \(3\le n\le9\) against the graph definition and the two-step local rule, compares exact transfer-matrix polynomials, and verifies the bivariate transfer determinant by a signed seven-by-seven permutation expansion. It separately computes exact traces and maximum-set coefficients for \(3\le n\le44\). The expected successful final marker begins with `VERIFY_OK`.

These are finite independent computations supporting an unrestricted combinatorial proof; they do not establish an infinite theorem on their own. The proof's gap classification and the local bijection provide the arbitrary-order justification. Independent external audit was not performed.
