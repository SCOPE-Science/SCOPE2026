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

# Verification scope

The standalone `verify.py` uses `sympy` and `numpy`. Run `python verify.py` in a directory containing that file. The exact certificate consists of the four-step projector and scalar-monotonicity argument in `RESULT.md`; the program supplies reproducible finite cross-checks, not a substitute for the universal proof.

The program symbolically checks the rational stability function's order-six Taylor agreement and both derivative identities. It independently forms the full weighted graph Laplacian and the Padé rational matrix for four rational steps across small complete bipartite graphs, verifying 4100 individual entries exactly against the projector formulas. For 310 additional numerical cases it independently solves the matrix rational equation and checks row sums, off-diagonal signs, boundary crossings and the extremal diagonal; it also compares the large-degree behavior with the asserted limiting root.

Numerical comparisons use floating-point tolerances, and the exact rational comparisons cover only the reported finite graph sizes. The uniform asymptotic statement and uniqueness are proved analytically, not inferred from finite tests. All checks were executed with the accompanying source before packaging. Independent audit has not been performed.
