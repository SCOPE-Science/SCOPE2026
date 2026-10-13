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

The analytic proof reduces restrained domination in a complete multipartite graph to two exact tests: the selected set must dominate, and its complement must be empty or meet at least two partite classes. This proves the infinite classification without enumeration.

The accompanying `verify.py` independently constructs each labeled complete multipartite graph for every integer part-size profile of total order \(2\) through \(8\) with at least two parts. It enumerates every set partition of the vertex set, checks every block directly against the restrained-dominating definition, tests coalition partners, and maximizes the partition cardinality. The expected formula is not used inside the definition checker.

A successful replay reports \(58\) profiles and \(101632\) candidate vertex partitions. It separately checks \(K_{3,1,1}\) and obtains \(4\).

Limits: enumeration is finite corroboration only. No claim of exhaustive computation beyond order \(8\) is made, and no computational result is used as a proof of the all-orders theorem.
