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

## Actual checks

`python3 verify.py` executed successfully against the complete files of this mathematical package. Its full stdout is in `expected.txt`, terminating in `VERIFIED`. The program uses exact polynomial arithmetic over a stated representation of the degree-six binary field and compares homogeneous rational-function identities symbolically; it does not use numerical approximations. It verifies the three cyclic Möbius invariances, the sole nonzero invariant polar numerator for each nonsplit support type, all rational pole-stabilizer sizes and quadratic-twist behavior, the geometric critical values, and point counts over the three first relevant binary extensions.

## Proof limits

The program's finite arithmetic is corroboration, not a substitute for the group-theoretic reduction from arbitrary tame cubic morphisms or the Artin–Schreier conductor and genus arguments in RESULT.md. The four-case completeness proof and uniqueness of quotients are mathematical, not inferred from a bounded enumeration of curve equations. No independent scientific audit or outside certification is claimed. Related older classification of genus-two models is cited as stronger *background* on curve enumeration, and scientific publication priority remains qualified.
