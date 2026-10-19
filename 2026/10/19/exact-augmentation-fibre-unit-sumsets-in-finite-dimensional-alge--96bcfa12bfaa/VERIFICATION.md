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

The supplementary `verify.py` uses Python 3's standard library only. Run `python3 verify.py`.

It independently enumerates the full algebra \(\mathbb F_3[S_3]\) (729 elements), determines 324 units using matrix ranks, and computes exactly the two-fold sums for both the singleton augmentation set \(U=\{1\}\) and the whole \(\mathbb F_3^\times\). It also examines all 2,197 elements of the upper triangular algebra \(T_2(\mathbb F_{13})\), checking both a six-element multiplicative-square subgroup and \(U=\{1\}\); this tests an arbitrary augmentation map on a nonsemisimple ring. Finally it confirms the \(\mathbb F_2\times\mathbb F_2\) boundary failure. Successful replay prints `VERIFY_OK`.

All these checks are exact finite computations. They are not evidence of proof for every finite-dimensional algebra; the proof is the Artin--Wedderburn, matrix decomposition, and Jacobson-radical argument in RESULT.md. No independent mathematical audit has been performed.
