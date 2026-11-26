---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Submodularity makes adjoining a rank-zero line rank-preserving. For any nonloop secret S there is a rank-two plane through S: otherwise the induction on sums of two hyperplanes containing S in RESULT.md propagates rank one to E. Such a plane supplies a nonreconstructing line in every complement to S. If the matroid has a loop L, the rank-one plane S+L has a nonloop line other than S and L (its intersection with the loop subspace is exactly L); choose a complement of S containing that line to obtain a reconstructing line as well. In the loop-free nonuniform case, choose S in a rank-one plane; its intersection with any complement supplies a reconstructing line. Either yields two lines with different reconstruction behavior in one port, impossible for any integer dimension threshold, including an empty port. In the uniform case adjoining S increases dimension by one and increases rank exactly at dimensions zero and one, giving threshold two.

## originality

PASS

The surviving distinct claim is the converse with all nonloop secret lines and complements, for arbitrary rank-two q-matroids including those with loops. The uniform-to-threshold direction is prior work. No equivalent or dominating statement was established by the inspected primary sources and bounded Resultary searches.

## value

PASS

It settles a natural first nontrivial rank of a documented classification question. It shows exactly when threshold access survives every choice of secret line and complement, using a mixed-line obstruction that detects both loops and dependent planes. This is a structural converse, not another example of the known sufficient condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
