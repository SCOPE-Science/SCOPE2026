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
# Verification of algebraic six-cycle law

Execute `python3 verify.py` in this directory with Python 3.10 or later; only the Python standard library is used.

The program works in the exact finite quotient ring \(\mathbb Q[t]/(F(t))\). It checks (1) opposite rational signs and strict derivative monotonicity for the unique specified root, (2) coefficient-wise rigorous lower bounds for positivity of each of the six total orbit masses, (3) normalization and equal edge marginals, (4) factorization of the indicator monomials for all 36 pairs of vertex-disjoint nonempty edge families, and (5) disconnection of the 32 supported labeled configurations. These are exhaustive *finite symbolic* checks, and the supporting proof explains why they establish the asserted stochastic independence.

There are no empirical confidence intervals, simulations, infinite-size limits, or numerical optimizations in the proof. The calculation does not verify the claim that the constructed parameter is globally optimal, and no such claim is made. Independent external review has not occurred.
