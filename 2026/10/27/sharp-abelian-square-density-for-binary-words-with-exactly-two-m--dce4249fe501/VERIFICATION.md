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

The finite reproducer is `verify.py`, requiring only Python 3 standard-library modules. From the directory containing it, run `python3 verify.py`. It directly enumerates all even-length contiguous factors and checks the two-half symbol counts; the resulting distinct-string sets are compared with a separately implemented run-parameter description. It also checks the diagonal counting formula. The verified grid is all \(13^3=2197\) triples \((a,b,c)\) with each coordinate in \(\{0,\ldots,12\}\). The closed form for the \((3k,2k,3k)\) witness and the previously published \((k,k,2k)\) specialization are checked for \(1\le k\le25\).

These tests cannot establish a theorem for unbounded run lengths. The proof of the all-parameter classification, the uniformly bounded lattice discrepancy, the sharp area inequality, and uniqueness of its maximizing proportions is in RESULT.md. No external independent audit was performed.
