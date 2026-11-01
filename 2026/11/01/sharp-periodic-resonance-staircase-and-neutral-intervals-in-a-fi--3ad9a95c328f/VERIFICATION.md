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

Run `python checker.py` in the same directory as this document with Python 3 and SymPy installed. The included script checks seven symbolic half-return identities, six strict periodic orbits and multiplier signs with exact rational arithmetic, and exact algebraic samples from the multiplier-one periodic intervals. Its output on the stated environment was `PASS: 63 symbolic/explicit checks; general proof is in RESULT.md`.

The complete classification for every real \(M>1\), \(0<\alpha<1\), and integer \(k\ge1\) is established by the proof in RESULT.md, not by finite enumeration. The original public paper was examined as full text; two older plausible comparative sources could be accessed only in abstracts or previews. Publication priority is therefore subject to those residual risks. No independent mathematical audit has taken place.
