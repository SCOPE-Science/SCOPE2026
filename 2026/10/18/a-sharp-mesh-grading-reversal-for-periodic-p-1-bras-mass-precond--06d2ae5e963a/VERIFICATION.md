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

# Reproduction checks

Run `python3 verify.py` using a standard Python 3 installation. The file uses only `fractions`, `decimal`, and `random` from the standard library, with deterministic inputs and no network access. Expected output: `PASS 2577 exact-and-assembly checks; crossover 0.27114057472819640557916457468727741869071212128946`.

The script assembles exactly the finite-element mass matrix and BRAS inverse from the two-by-two element blocks, checks the scalar two-cell identity, the two three-cell characteristic polynomials, and the crossover root enclosure using rational/decimal arithmetic. The infinite-grading and dimension-general eigenvalue conclusions require the analytical rank-two/min-max proof in RESULT.md and are not verified by finite enumeration. No outside experimental data or independent audit is claimed.
