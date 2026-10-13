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

The accompanying `verify.py` uses only exact integer arithmetic except for one final numerical reading of a proved logarithmic inequality. It performs the following checks:

1. For \(0\le n\le20\), it verifies the optimal atom counts \(R^2+R+4\) and \(R^2+R+5\), with \(R=2^{n+1}\), and the one-bit difference in their complex-algebra exponents.
2. It checks nearby feasible triples and the monotone lower-bound pattern.
3. For \(0\le n\le6\), it exhaustively searches a bounded box containing the predicted minimizer and verifies that, up to swapping the two first parameters, the unique minimizer is \((R,R+1,R)\).
4. For \(1\le n\le20\), it verifies the displayed half-log-log size-versus-depth inequality for the optimized larger witness.

The script terminates with:

`VERIFY_OK 601 exact assertions`

The mathematical proof of optimality does not depend on bounded enumeration: it follows for every \(n\) from \(|U|\ge R\) and \(|Q|\ge |U|+1\).
