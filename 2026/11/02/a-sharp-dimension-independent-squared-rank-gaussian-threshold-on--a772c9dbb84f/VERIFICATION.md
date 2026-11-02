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
# Verification record

The analytic proof gives all quantifiers: arbitrary \(m\ge3\) and every real bandwidth \(u\in[0,1]\). The four Walsh spectral branches are derived from row-space containment counts. Polynomial factorization and monotonicity prove uniqueness of the positive cutoff, positivity of the rank-two branch through the cutoff, and negativity of the rank-two branch after the rank-three branch's recovery. Finite programs alone do not establish these global statements.

Run `python3 checker.py` in a directory containing the standalone file. The checker uses exact integer Walsh transforms for every \(U\in M_{m,3}(\mathbb F_2)\) at \(m=3,4,5\), tests all four rank shells and their multiplicities, and checks six rational kernel parameters and exact polynomial root brackets. Execution from the delivered package succeeded. The program neither assumes nor establishes an all-dimensional finite census. Reproducibility requires only Python 3 standard library.

No independent audit, human verification, or external formal certification is claimed.
