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
# Reproducibility and proof checks

The standalone `check.py` uses Python 3 and the standard library only. Execute `python3 check.py`. The first test examines the original three- and four-quantifier confluence statements for every possible binary relation on a rooted fork with one, two, or three leaves: respectively 16, 512, and 65536 relations, totalling 66064. The second test constructs each candidate leaf-row bitmask directly and counts allowed row sequences by a union-mask dynamic program. It checks the exact formulas independently for one through six leaves.

The executable returned these pairs of FIK and IK counts: for one leaf 11 and 9; for two leaves 185 and 81; for three leaves 10943 and 2043; for four leaves 2547617 and 197529; for five leaves 2423359871 and 83847459; for six leaves 9451444403585 and 154721901201.

The proof in `RESULT.md`, not these tests, establishes the row equivalences and all-parameter counting identities. The direct exhaustive test does not cover seven or more leaves. The dynamic count has no bearing on uniqueness in other poset families. No independent external audit has been performed.
