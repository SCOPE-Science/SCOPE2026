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

# Verification of cycle rank-frequency formula

Run \(\texttt{python verify.py}\) with a standard Python interpreter (no third-party modules). It constructs each multiplication matrix directly from the edge coefficients and computes exact ranks modulo prime fields. It separately evaluates the support-induced-component formula and the coefficient polynomial of the transfer trace. The twelve prime-field cycle cases use field orders two, three, five and seven, and three extension-field cycle cases use \(\mathbb F_4\); the cyclic lengths range from four through eight. The two additional tests enumerate all \(64\) simple graphs on four labelled vertices over the fields of orders two and three; these check the support formula beyond cycles. Successful output is \(\texttt{GRAPH\_LEFSCHETZ\_RANK\_ENUMERATOR\_OK 17 families}\).

All of the proof's quantifiers extend beyond the finite tests: in particular, they include composite prime-power fields because the proof depends only on division by nonzero coefficients and on the dichotomy between characteristic two and other characteristics. No independent audit has been performed. The exact finite-field examples establish consistency, not an infinite verification by computation.
