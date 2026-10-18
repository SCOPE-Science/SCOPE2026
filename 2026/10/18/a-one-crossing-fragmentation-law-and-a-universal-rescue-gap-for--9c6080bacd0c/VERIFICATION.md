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

# Mathematical verification record

The complete proof is in `RESULT.md`. Execute `python check.py` using Python 3 with SymPy installed. The program checks the transient resolvent, exact Laplace transform, extinction-time mean, characteristic-polynomial threshold and constant-width threshold relation by symbolic identity. It then compares the exact mean derived from a separately inverted transient Markov generator with the formula for 256 deterministic rational test triples, and computes the unique crossover time for the specified example.

Observed result from the actual packaged checker:

`PASS: exact generator, Laplace and moment identities; 256 independent rational parameter cases; example crossover and critical asymptotics`

These are reproducibility checks, not an exhaustive enumeration of real parameters or a separate independent audit. Universality follows from the explicit hazard monotonicity, the characteristic-root comparison, the coupling and critical-limit calculation in `RESULT.md`. Numerical crossover values and near-critical approximations are illustrative only.
