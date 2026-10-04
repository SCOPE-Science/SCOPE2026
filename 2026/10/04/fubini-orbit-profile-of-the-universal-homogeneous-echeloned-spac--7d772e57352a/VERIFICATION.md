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

The proof in `RESULT.md` is structural. On distinct labeled vertices, the echelon axioms leave exactly a weak order on the unordered pairs after the forced diagonal bottom class. Universality and homogeneity of the cited Fraïssé limit turn this finite-structure classification into an automorphism-orbit classification.

`verify.py` is a finite arithmetic and encoding replay. It computes Stirling and Fubini numbers exactly; checks the displayed injective orbit counts and the repeated-coordinate Stirling transform; and independently brute-enumerates rank-surjections representing all weak orders on up to six labeled elements, recovering in particular 4683 weak orders on six labels. This supports the finite arithmetic and the weak-order encoding, but it is not used to infer the all-arity theorem.

Scientific limit: targeted literature and semantic-index searches found no covering orbit-profile statement, but an elementary consequence of a homogeneous structure can persist as unindexed folklore.
