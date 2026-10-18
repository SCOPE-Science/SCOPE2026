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

# Exact reproducibility
Run `python3 CHECK.py` with Python 3 and no external packages. For each integer base \(2\le b\le20\), the script independently builds the denumerant using coin-change recurrence, identifies the first element in every residue class with two representations, and checks the complete symbolic threshold, \(g_1\), and \(n_1\). It confirms all \(3097\) residue classes and all corresponding finite gap cardinalities. For integer bases \(2\le b\le8\), a separate sum over the last generator's coefficient solves the two-generator congruence directly and checks \(4594\) integer inputs. The script stops with an assertion if a comparison differs.

The mathematical proof uses an exact height parametrization and is valid for **all** \(b\ge2\), independently of test coverage. The finite computations alone neither establish any universal statement nor certify novelty. No independent mathematical audit has been performed.
