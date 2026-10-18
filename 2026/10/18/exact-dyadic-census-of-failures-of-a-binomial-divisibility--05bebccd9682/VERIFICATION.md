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

# Exact replay and mathematical limits

Execute `python verify.py` in the directory containing this file, using Python 3's standard library. The program prints `VERIFY_OK` when every assertion succeeds.

The exact algebraic certificate consists of seven polynomial identities:
\[
H_i(z)=Q(z)t_i+z\sum_{i\to j}H_j(z),\qquad Q(z)=1-z-z^2+z^3-z^4,
\]
where \(t_i\) is the terminal acceptance indicator. The code checks all coefficients over integers, including trailing zeros of both polynomial sides. Since \(Q(0)=1\), these identities rigorously imply the generating-function equality within formal power series, given the independently proved seven-state transition semantics.

The verifier separately checks the state table against integer binary arithmetic, evaluates 599 exact integer binomial divisibility cases, compares the proposed characterization against independent binary-digit valuation formulas for all 16,383 inputs through fourteen bits, and cross-checks nineteen rational-series coefficients against finite-state matrix counts. These computations were rerun from the serialized package's extracted `verify.py` and passed. They are finite support, not a substitute for the orbit argument, the Kummer equivalence, or the universally quantified state induction. Numerical approximations to the dominant root are not proof of the exact generating function.

No independent review or external validation was performed.
