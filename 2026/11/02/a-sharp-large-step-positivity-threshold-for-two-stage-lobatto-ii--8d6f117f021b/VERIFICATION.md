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

The exact formula and analytic proof are given in `RESULT.md`. The standalone `verify.py` constructs matrices using exact `fractions.Fraction` arithmetic, tests row sums and nonnegativity, and independently inverts \(I-hQ_n+\frac12 h^2Q_n^2\) as an upper-triangular rational matrix. It verifies 26,022 assertion groups on dimensions \(2\) through \(41\) at 16 rational step sizes, plus additional independently inverted small matrices and radical identities. Executed command: `python3 verify.py`; observed output: `PASS 26022 assertion groups`. This is finite reproducibility evidence, not a complete computational proof of the all-dimensional theorem. No independent mathematical audit is claimed.
