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
The proof in `RESULT.md` is arbitrary-rank and symbolic.

Critical checks:
- the source generalized snake poset has a unique minimum and maximum;
- a word of length \(n\) has source rank \(n+2\);
- the standard order polytope uses coordinate bounds and monotonicity inequalities;
- coordinate-hyperplane normals have norm \(1\);
- cover-hyperplane normals have norm \(\sqrt2\);
- longest-path levels increase by at least one across every cover;
- the proposed center satisfies every defining halfspace at radius \(1/(2+(n+2)\sqrt2)\);
- a longest min-to-max chain telescopes to the matching upper bound.

`verify.py` reconstructs every generalized snake poset for all words of length at most \(8\), checks the rank and longest-path levels, and replays the center inequalities and longest-chain upper bound. These finite checks are corroborative only and do not assess originality.
