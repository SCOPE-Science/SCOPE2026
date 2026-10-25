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

# Exact checks and limits

The standalone \(\texttt{verify.py}\) uses no packages beyond Python's standard library. Its two independent calculations of all subset sums of \(1^2,\ldots,18^2\) are (a) arbitrary-precision bitset shifts/OR and (b) dictionary construction of explicit distinct-index witnesses. Each yields exactly \(2048\) reachable totals through \(2109\). Both exclude \(128\) and include every integer in \([129,324]\).

The script checks the four certification inequalities at their lower endpoints for every \(18\le B\le400\), shows the two relevant polynomials are monotone thereafter, and checks sample congruence instances for the claimed missing residue class. The universal \(B\ge18\) result uses the written induction and the exact modular bound \(0\le\sum_{j\in J}j^2\le S_B=Q_B-2\) for every subset \(J\subseteq\{1,\ldots,B\}\). These arguments are not extrapolations from the sampled bounds.

Run \(\texttt{python3 verify.py}\) with Python 3. The verifier does not check original numerical tables outside the specified square-power base. It does not constitute independent certification or audit.
