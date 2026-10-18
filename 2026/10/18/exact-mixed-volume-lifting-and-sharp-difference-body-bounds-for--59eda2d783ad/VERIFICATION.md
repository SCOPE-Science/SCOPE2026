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

# Reproducibility and verification

The analytic proof uses (i) exact level-set identities for the Minkowski sum of a pyramid with its reflection; (ii) Fubini integration; (iii) Minkowski polynomial expansion; (iv) Brunn–Minkowski and equality conditions; and (v) the classical Rogers–Shephard upper bound. Only the first two require object-specific geometric reasoning, which is supplied explicitly in `RESULT.md`.

Execute `python check_pyramidal_difference.py` using Python 3 with NumPy and SciPy. The program calculates exact rational planar hull areas, compares independently computed 3D and 4D hull-volume ratios, and tests non-unit unbalanced parameters. The verified output begins `PYRAMID_DIFFERENCE_CHECK_OK rational_3d=5 hull_3d=5 hull_4d=2`; it also reports sharp ratios of 14 and 20 in 3D and 30 and 70 in 4D. These are finite numerical consistency checks; exact infinite-dimensional and arbitrary-base assertions rely on the written proof.

The 1957 difference-body upper bound is prior mathematical literature, not independently reproved or newly attributed here. The claimed exact lifting identity has not undergone an external independent audit, and historical-priority risk persists.
