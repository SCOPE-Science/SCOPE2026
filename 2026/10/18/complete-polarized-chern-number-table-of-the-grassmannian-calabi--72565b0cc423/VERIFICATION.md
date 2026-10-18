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
# Reproducible numerical verification

Run `python3 verify.py` from the same directory as these files. The script uses only exact Python standard-library fractions and integers, expands Chern roots through degree six, calculates the 11 required Grassmannian coefficient residues and independently evaluates them by localization at the 45 torus-fixed points. It then reproduces the already-published \(\chi_y\) and Hodge-genus information, solely as a cross-check.

Expected output begins with `VERIFY_OK fixed_points=45 degree=1430 euler=24920 middle_betti=24912`; the `chern_numbers` line includes `c2c3H: -12210`, `c2cube: 32480`, `c2c4: 26720`, `c3sq: 13200` and the other seven values. Exact inputs are the universal tautological Chern roots and the Schubert top coefficient; no stochastic or sample-based inference is needed.

**Boundaries:** The machine check does not independently establish the geometric normal sequence, Bertini smoothness, the Schubert residue rule, or priority. These are supplied by the mathematical proof and cited literature. The existing Hodge-number table is not a novelty claim. No independent audit or expert validation has been performed.
