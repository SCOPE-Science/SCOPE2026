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

# Verification notes

`verify.py` implements literal one-coordinate deletion and insertion as sets of distinct strings. Invoke `python3 verify.py` in the extracted directory. The expected final line begins `VERIFY_OK` and lists three test ranges: explicit extremizers for all lengths \(3\) through \(250\); VT residue noncollision on every binary word through length \(13\); and the two-common-supersequence lemma on all distinct binary reads of length \(1\) through \(8\).

The induction and checksum argument in `RESULT.md` are the all-length proof. Checking finitely many words cannot establish an infinite theorem, and this code does not attempt to classify all extremizers or exclude equivalent published work.
