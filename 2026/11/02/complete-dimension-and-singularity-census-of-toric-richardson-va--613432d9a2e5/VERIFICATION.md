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

# Exact computational verification

Compile with a standard ISO C++17 compiler; execute `sh VERIFY_ALL.sh` in the directory containing all embedded files. It compiles `VERIFY_RPOLY.cpp` and `VERIFY_CROWN.cpp`, runs both over every permutation pair in \(S_7\), and compares their outputs against the exact counts in `COUNTS.tsv`. The two independent programs print `VERIFY_OK` on success and exit nonzero on a failed internal assertion.

The \(R\)-polynomial algorithm uses the standard exact recurrence, caching saturation values in \(\{0,1,2\}\). The crown algorithm enumerates Bruhat covers independently and detects forbidden rank-three intervals, recursively propagating obstructions. Both compute the full toric dimension profile. The latter independently computes each good interval cardinality by intersections of incidence bitsets to determine its Boolean/smooth profile; its rank-three detector additionally checks actual interval sizes.

The theoretical bridge from the integer algorithms to the geometric claim is Theorem 1.2 and Lemma 3.1 in arXiv:2603.29260 and the established smoothness criterion; finite enumeration alone without this bridge would not prove the geometry. The computation is exhaustive for \(n=7\), not an assertion about all \(n\). No independent external mathematical audit has been carried out.
