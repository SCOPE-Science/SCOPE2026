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

Run `python3 verify.py` with Python 3.8 or later and its standard library. The program independently constructs each candidate endomorphism from images of the two standard cyclic generators. It checks the four coordinate congruences for a square-zero composite, constructs every attained subgroup by enumerating linear combinations of those two images, and computes its group type from subgroup order and exponent. These operations do not use the subgroup/surjection proof.

The program compares the **entire** predicted histogram and its total, including zero image, cyclic types, and rank-two noncyclic types, for \(p=2\), \(2\le b\le10\); \(p=3\), \(2\le b\le7\); and \(p=5\), \(2\le b\le4\). The actual run ended with `VERIFY_OK 18 cases`.

The proof in `RESULT.md` applies to every prime and exponent in its stated domain. The finite verifier is corroboration only; it does not establish the general case or literature priority. The independent-audit field above records that no independent mathematical audit has been performed.
