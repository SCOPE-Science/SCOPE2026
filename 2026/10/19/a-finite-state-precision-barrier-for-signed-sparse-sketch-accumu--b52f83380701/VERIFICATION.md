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
# Reproduction and verification

Execute `python3 check.py` with Python 3.11 or another version supporting `struct` binary16 (`'e'`). The file `CHECKS.txt` records the program's actual output. The tests enumerate every binary16 state transition for both allowed layer counts and compute complete hash/sign sample spaces for four small-dimensional parameter choices. The mathematical proof, not the finite script, establishes the arbitrary-input-height statement and stationary limit.

The verifiable transition rule is \(J\mapsto\min\{2048,\max\{-2048,J\pm1\}\}\). The exact-arithmetic moment law is \(\mathbb E Q_\infty=N\) and \(\operatorname{Var}(Q_\infty)=2N(N-1)/m\). A standard symmetric finite-state irreducible aperiodic Markov chain argument proves the limiting uniform distribution.

Only correctly rounded binary16 sequential sums with exact increments \(1\) and \(1/2\) were checked. This does not verify actual CUDA device execution, independent hardware scheduling, broader input distributions, or other rounding modes. External independent audit has not been performed.
