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

# Reproducibility

Use a recent Python interpreter and install `requirements.txt`; then run `python verify.py` in this directory. The program has no input data files or external network dependencies. It builds the displayed finite matrices directly, computes their dark and bright projections, and compares explicit formulas with finite-time Lindblad evolution and exact kernel multiplicities at small sizes. It also compares finite Fourier sums with the projector formula and checks the approach of bridge-site dark weights to one half. It reports a `PASS` line only if all assertions succeed.

The tests examine finitely many sizes and phases and therefore do not certify a theorem for all \(n\) or all positive rates. The analytic proof in RESULT.md carries those quantifiers. The numerical time horizon is a consistency check only and is not presented as a universal mixing-time guarantee.
