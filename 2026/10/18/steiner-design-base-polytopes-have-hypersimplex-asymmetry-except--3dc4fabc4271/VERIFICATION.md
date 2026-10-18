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

# Verification and reproducibility

Run `python3 verify.py` with Python 3. The checker uses only the standard library (`fractions`, `itertools`, and `collections`), constructs each finite design rather than reading a table, and verifies its pair-incidence axiom.

Checked examples: \(\mathrm{PG}(2,2)\) with \(28\) bases and \(196\) reflection-block tests; \(\mathrm{AG}(2,3)\) with \(72\) and \(864\); \(\mathrm{PG}(2,3)\) with \(234\) and \(3042\); the \(15\)-point binary Steiner triple system with \(420\) and \(14700\); and \(\mathrm{PG}(2,5)\) with \(3875\) and \(120125\). Total: \(4629\) bases and \(138927\) rational reflection-block tests. Every case passed in the reviewed execution.

The checker also confirms exact coordinate extrema, block extrema, design replication, and equality of the claimed asymmetry with the maximum of the four analytically derived bounds. The uniqueness argument is symbolic and appears in the Proof section of `RESULT.md`. Verifying finitely many designs does not prove an all-design theorem; the analytic proof supplies the universal conclusion. No independent external audit has occurred.
