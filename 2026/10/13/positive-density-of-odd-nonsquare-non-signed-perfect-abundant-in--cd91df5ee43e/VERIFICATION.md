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
# Verification

The standard-library script `artifacts/verify.py` independently reconstructs the explicit anchor:
\[
a=11025=3^2\cdot5^2\cdot7^2,
\quad\sigma(a)=22971>2a,
\quad Y=50000>\sigma(a)+1.
\]
It enumerates the primes through \(Y\), confirms their count, calculates the finite Euler product, and checks strict interval inequalities for both a prime and a composite nonsquare cofactor. `artifacts/replay.txt` is the output of this script from this package.

The general infinite density theorem follows from the analytic proof using exact divisor-sum identities, finite-prime congruence counting, and the telescoping series estimate; **no amount of finite experimentation certifies that infinite statement**. The proof does not assert an exact natural density or classify all counterexamples.
