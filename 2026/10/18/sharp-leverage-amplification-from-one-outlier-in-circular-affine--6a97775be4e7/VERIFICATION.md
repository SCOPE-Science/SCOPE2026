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

# Reproducible checks and limitations

Run `python3 checker.py` with a Python 3 standard-library interpreter. The checker constructs the complete finite hat matrices by independent Gram inversion, checks the closed-form special row, tests the full projection identity and ordinary-row bound, verifies shifted circular quadrature inequalities, and compares computed optimizing radii and sharp norms with the derived asymptotic formulas. In this package, it reports `PASS: 21642 independent finite assertions`.

These are **finite consistency checks**, not an exhaustive search or an infinite-family proof. The statement for all sufficiently large \(n\), every phase \(\phi\), and every optimizing radius is established by the Gram update, uniform bounded-variation quadrature and derivative estimate, stationary equation, and strict maximization of its leading profile. No external or independent review has been performed.
