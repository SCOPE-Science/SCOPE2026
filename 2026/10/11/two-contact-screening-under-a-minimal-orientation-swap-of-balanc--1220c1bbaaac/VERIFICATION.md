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

# Reproducibility and limitations

Run `python3 verify.py` from this directory with Python 3's standard library. The checker builds all \(2k\) incidence vectors for every integer \(3\le k\le70\), constructs the exact claimed rational weights, checks their sum and strict positivity on the support, verifies all vertex Gram products, confirms the squared center norm, the unique optimum-radius formula, both exact contact gaps, and independently recomputes every squared vertex distance using `fractions.Fraction`.

Successful output is `VERIFY_OK nearblock_dimensions= 68 exact_rational=True`. This is a finite corroboration only. The all-integer theorem is proved by symbolic Gram and barycentric identities in `RESULT.md`, including the exceptional \(k=3\) case and the strict condition \(k\ge4\). No external mathematical validation has been performed. The source literature is cited rather than bundled; no external source files are required to run the standalone exact checker.
