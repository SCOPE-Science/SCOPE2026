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

# Computational verification and analytic boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The program constructs partial injections by separately choosing each source domain and injective image tuple. For every pair in dimensions zero through four, it evaluates composition directly and records the two ranks of zero products. Each cell is tested against the formula stated in `RESULT.md`. The program also compares the total with the known Laguerre-sequence representation and checks the independent cardinality count of the whole rook monoid. Exact-ratio numerical diagnostics are checked through dimension 70. The observed result was `VERIFY_OK: direct pair products through n=4 and 70 exact-ratio cases`.

The analytic proof, not this program, supplies convergence as dimension tends to infinity. The relevant non-finite steps are dominated convergence of a summably bounded vacancy mass function, a fixed-vacancy central hypergeometric approximation from Stirling's formula with a variance tightness bound, and the final tight mixture argument. The program is not an exhaustive verification of any infinite statement. Publication priority has not been independently validated.
