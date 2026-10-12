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

# Reproducibility notes

Run `python3 verify_subset_defects.py` using the Python standard library only. The script computes the Möbius function and the exact relatively-prime subset counts, independently checks both deficit inequalities for every integer from \(2\) through \(1500\), enumerates actual subset gcds for \(2\le n\le16\), and checks all least-nondivisor residue-class counts through \(200000\). It also checks the prime-power support and five least-prime-factor fibers using independent inclusion–exclusion.

The infinite probability limit and parity escape are proved in `RESULT.md` by exact inclusion–exclusion, union bounds, and residue densities. Finite tests cannot certify a limiting theorem by themselves. No external independent audit or validation has been performed.
