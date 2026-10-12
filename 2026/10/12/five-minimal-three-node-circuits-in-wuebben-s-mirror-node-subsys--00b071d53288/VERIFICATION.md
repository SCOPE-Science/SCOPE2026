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

The bundled `verify.py` is standalone and uses only exact integer arithmetic plus rational Gaussian elimination from Python's standard library.

It starts from the \(22\) vertices of \(\Delta_{\mathbb F_1}\) printed in Wuebben's Theorem 6.1. It reconstructs all supporting facets, obtains the \(26\) vertices of the polar, enumerates the polar two-faces, and selects the \(26\) four-vertex faces. For each such face it identifies the unique parallelogram diagonal equality and builds the corresponding relation row in \(\mathbf Z^{26}\).

Before testing the new claim, the script reproduces the published checks
\[
\operatorname{rank}=18,
\]
the two coloop rows \(9\) and \(11\), and
\[
\operatorname{rank}=16
\]
after deleting both coloops.

It then performs a complete search through all \(325\) row pairs and all
\[
\binom{26}{3}=2600
\]
row triples. No pair is dependent, and exactly five triples are dependent. Each of those triples is therefore a circuit, and direct integer addition verifies the listed primitive signs.

The replay output records the five row-index supports, the corresponding one-based square-face vertex sets, and the relation coefficients, and terminates with `VERIFY_OK`.

This exhaustive finite computation proves exactly the stated finite matroid classification. It is not used to infer an infinite or asymptotic statement. The only unproved limit is interpretive: no smoothing consequence for the four-cone mixed-singularity threefold is asserted.
