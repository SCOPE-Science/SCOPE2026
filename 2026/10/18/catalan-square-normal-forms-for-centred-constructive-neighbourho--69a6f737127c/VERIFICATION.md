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

# Mathematical verification

The theorem has a direct all-size proof: all formula extensions are suffix upsets; any nonempty neighbourhood meets a suffix precisely when its maximum enters that suffix, and is contained in a suffix precisely when its minimum enters that suffix. Pushing both modal clauses through future-world quantification yields the thresholds \(B_i,D_i\). The centred assumption gives \(B_i\le i\le D_i\); the suffix construction gives monotonicity. Singleton interval neighbourhoods realize each pair and preserve both modal operations; induction gives truth equivalence for all formulas. One-atom depth-one modal tests separate distinct pairs. The usual ballot count yields the Catalan square.

The included `chain_catalan_verify.py` is standalone standard-library Python. Run it from the same directory with

```sh
python3 chain_catalan_verify.py
```

It independently computes raw modal truth tables for every centred-serial frame and every upset on carriers of size one, two, and three (respectively 1, 9, 3375 total raw frames), and verifies exact agreement with canonical intervals. It also enumerates all canonical pairs through five worlds and verifies their distinct observational signatures and Catalan-square counts. Successful output ends with `CHAIN_CONSTRUCTIVE_NEIGHBOURHOOD_CATALAN_VERIFY_OK`.

The finite tests are corroborative. The general correctness assertion is the mathematical induction, construction, and ballot proof, not an extrapolation from the small computations. Historical priority was assessed by source comparison and remains imperfectly ascertainable.
