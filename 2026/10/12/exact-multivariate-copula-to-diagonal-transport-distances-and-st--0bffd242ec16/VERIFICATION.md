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

# Verification

Run `python3 verify_exact.py` in the same directory. It requires only the standard library and prints `VERIFY_OK` on success.

Two exact rational methods are used: an integrated \(2d\)-fold Irwin--Hall CDF formula, and separately the polynomial-cell integration of \(\mathbb E[S F_d(S)]\) in the optimal transport cost. Their identity was checked for dimensions \(1\) through \(8\). The exact values at dimensions \(2,3\) and strict positivity of the first and second finite differences through dimension \(12\) were also checked.

The all-dimensional rearrangement, uniqueness, Fourier sign and asymptotic remainder bounds are supplied by the analytical proof in `RESULT.md`; no finite computation proves them. Independent audit has not been performed.
