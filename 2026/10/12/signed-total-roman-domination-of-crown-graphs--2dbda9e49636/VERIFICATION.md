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

The unrestricted proof is symbolic. On \(\operatorname{Cr}_n\), the verifier independently constructs the two shores, tests the literal signed total Roman conditions for every labeling considered, and does not call the theorem's lower-bound argument.

For every \(3\le n\le8\), it exhaustively searches shore labelings by total weight, verifies that the first feasible weight is \(6\), and counts every minimum function. The resulting counts are
\[
10,\ 84,\ 900,\ 3280,\ 44100,\ 189000.
\]
It separately evaluates the closed counting formula and the explicit parity constructions, and checks those constructions and the formula through \(n=40\).

Replay output:

`ALL CHECKS PASSED; exhaustive_orders=[3,4,5,6,7,8]; minimum_counts=[10,84,900,3280,44100,189000]; formula_range=3..40`

The exhaustive range is finite and is not used to infer the theorem for larger \(n\). The general statement rests on the symbolic shore-sum and rescue arguments in `RESULT.md`.
