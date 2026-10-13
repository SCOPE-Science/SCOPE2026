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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The first enumeration engine constructs only ternary square-free prefixes, rejecting a new letter exactly when it creates a square suffix. The second independently checks all \(3^{13}\) ternary words by direct factor scanning. They must return the same \(342\) words.

Every candidate is then checked under all \(11\) interior deletions. Two separate least-period scans—one ordered by square position and one ordered by period—must agree after every deletion. This yields \(30\) irreducibly square-free words and the exact radius histogram \(3:18,6:12\).

Finally, the verifier recomputes all alphabet-permutation/reversal orbits, their sizes \(12,6,12\), and the fact that every word in the radius-\(6\) class has exactly one deletion whose least square period is \(6\). For the canonical representative, deleting position \(11\) produces \((\mathtt{010212})^2\).

Independent audit has not been performed.
