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

The accompanying `verification/check_shadow_lp.py` reconstructs the entire weighted-shadow converse by exhaustive enumeration of all \(52\) unlabeled partitions of five positions, using exact integers. This establishes a finite lemma uniformly across alphabets because output-subsequence equality types are invariant under injective relabeling. It also verifies the three-family output profiles.

The code explicitly reconstructs rational prefix weights and all distinct output incidences for \(q=7,8,9\) with the Python `fractions.Fraction` class. The recorded output includes `VERIFY_OK`. Exact all-\(q\) sufficiency follows instead from the proof's symbolic output-orbit multiplicities and the inequality \(5/(q-2)\le1\). Finite checks alone are not claimed as a proof for unbounded alphabet sizes.

No integral length-five systematic code at seven symbols has been exhibited or ruled out. Mathematical priority and independent audit are unperformed.
