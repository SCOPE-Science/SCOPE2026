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

# Reproduction and limits

Run `python3 check.py` with a standard Python 3 interpreter from the directory containing the files. The recorded successful output from the supplied source is `VERIFY_OK assertions=67180`.

The checker uses exact rational arithmetic to recompute the cubic mean/variance/skewness identity, the two-class boundary drift formula, the binary moment coefficient, the symmetric two-patch cancellation, the three-patch coefficient \(1/81\), and two complementary data sets with the same mean and variance but opposite skewness. It also integrates representative two-class systems over several patch counts and mixing rates and numerically brackets threshold shifts; those calculations test examples, not the infinite set of parameter values.

The complete proof, including its comparison theorem, endpoint basin argument, convergence, singular perturbation error control, and exact majority law, appears in RESULT.md. The checker is not an independent theorem prover and no independent scientific audit was performed. Re-run it against the supplied `check.py`, not any unrelated implementation.
