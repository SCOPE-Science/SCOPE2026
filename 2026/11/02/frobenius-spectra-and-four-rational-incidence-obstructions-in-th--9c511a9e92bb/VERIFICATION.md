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
# Reproducibility

Run `python3 verify.py` from this package using Python 3.9 or later. It requires only the Python standard library. The program computes the 16 node classes and 16 trope classes, verifies the 96 geometrically incident pairs, uses independent classical incidence labels, checks all 720 permutations of six points, compares spectra across the eleven cycle partitions, verifies fixed-point counts of every power up to six, and checks the four incidence obstructions. The accompanying output ends in `VERIFY_OK`.

The algebraic-geometric bridge is the classical Kummer node–trope labeling for a smooth genus-two sextic in characteristic not equal to two. Numerical field sampling is not used as a proof. No independent scientific audit has been performed; the theorem does not cover characteristic two, nonsquarefree sextics, or the full Kummer surface zeta function.
