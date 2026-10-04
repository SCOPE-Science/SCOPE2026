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

The bundled `verify.py` uses only the Python standard library and performs two independent finite replays of the counting reduction.

First, for each \(m\leq 8\), it enumerates every nondecreasing threshold sequence \((t_0,\ldots,t_{m-1})\) with values in \(\{0,\ldots,m\}\). For every second-order cut \(c\) and every admissible split of the block \(t_i=c\), it evaluates the exact number of compatible new-row thresholds and first-order insertion cuts. Every threshold shape gives the same count \((m+1)(2m+1)\).

Second, for each \(m\leq 5\), it exhausts every actual finite base: every relative permutation of the two linear orders and every nondecreasing threshold sequence satisfying the diagonal irreflexivity constraints. For each base it explicitly constructs a set of one-point extension signatures recording the two order cuts and both directions of the relation to the old points. The number is constant on all bases. The numbers of valid bases for \(m=0,1,2,3,4,5\) are
\[
1,1,3,15,105,945.
\]
The corresponding counts of types with the realization distinct from the base are
\[
1,6,15,28,45,66,
\]
and after adding equality types the complete \(1\)-type counts are
\[
1,7,17,31,49,71.
\]
The program ends with `VERIFY_OK`.

This finite replay checks the extension parametrization and all small cases. It does not replace the all-\(m\) algebraic summation in the proof, and it does not independently reprove the source’s Fraïssé statement. No independent audit has been performed.
