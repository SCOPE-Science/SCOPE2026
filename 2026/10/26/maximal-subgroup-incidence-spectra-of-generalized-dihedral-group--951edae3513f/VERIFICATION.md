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

# Verification of maximal-subgroup incidence spectra

The finite checks construct the multiplication table directly from \((a,\epsilon)(b,\delta)=(a+(-1)^\epsilon b,\epsilon+\delta\bmod2)\) and enumerate all subgroups by iterative closure. Maximal subgroups are selected by inclusion, without presupposing their classification. The script computes the Frattini intersection and every incidence degree, then compares them with the formula. The uniform intersection number is obtained as one more than the greatest observed incidence degree outside the computed Frattini subgroup.

Run `python3 verify_incidence.py` with Python 3's standard library. All sixteen test kernels, including noncyclic odd kernels, mixed-prime kernels, and kernels with even torsion, returned `VERIFY_OK`. The complete printed subgroup counts, maximal-subgroup counts, Frattini sizes and incidence profiles are reproducible from this file.

The correctness claim for *all* finite abelian kernels rests on the explicit classification and hyperplane-count proof in RESULT.md, not on extrapolation from these finite computations. No independent mathematical audit has been performed.
