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
# Reproducibility and limits

Run `python verify.py` using Python 3 and its standard library. The script computes the closed-form centralizer ratios with exact fractions, and independently squares **all** matrices of each small tested matrix algebra over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), calculating ranks by field Gaussian elimination. The canonical targets include every possible square-zero rank in dimensions two, three, and (over \(\mathbb F_2\)) four. All such fixed targets are representative up to conjugacy.

Exact checked examples: over \(\mathbb F_2\) and dimension four, root-rank multiplicities for target rank zero are \(1,105,210\) at root ranks zero, one, two; for target ranks one and two there are exactly \(12\) roots at ranks two and three respectively. Over \(\mathbb F_4\), dimension three, target rank one, there are \(12\) roots, all of rank two. The script also checks coefficient integrality, nonnegativity, existence and gap-free rank interval for every dimension from one through fifteen and field orders \(2,3,4,5,7\).

Successful terminal marker: `VERIFY_OK_NILPOTENT_SQUARE_ROOT_FIBERS`. The finite checks do not prove statements for arbitrary prime powers or unbounded dimension; those are proved by the module, orbit, and centralizer arguments in RESULT.md. Independent mathematical audit remains unperformed.
