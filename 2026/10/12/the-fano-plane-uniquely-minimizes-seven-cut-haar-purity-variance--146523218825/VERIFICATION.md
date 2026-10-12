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

# Reproducible verification

Run `python3 verify.py` from the directory containing the supplied files. It requires only the Python 3 standard library.

The script directly enumerates the 24 elements of \(S_4\), evaluates the replica-cycle trace independently of the polynomial formula, and checks their equality for all four overlap sizes and local dimensions \(p=2,3,4,5\). It computes the exact rational Fano and cyclic variance, checks the closed variance difference, verifies the displayed rational qubit values, and enumerates the entire family of labeled seven-triple set systems with every pair intersection equal to one. It finds exactly 30 labeled optimal systems and prints `VERIFY_OK`.

General local-dimension optimality and the uniqueness up to relabeling follow from the analytic inequalities and combinatorial proof in `RESULT.md`, not from four sample dimensions or finite enumeration alone. These checks provide no independent audit or experimental measurement evidence.
