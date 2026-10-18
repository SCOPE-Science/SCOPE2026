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

The proof in `RESULT.md` establishes the theorem for every finite group and \(n\ge2\) without relying on finite enumeration. Reproduction code is provided as `verify_maximal_commuting.py`, using only the Python 3 standard library.

The program constructs Brandt multiplication tables directly; enumerates all maximal pairwise commuting sets via Bron--Kerbosch; independently constructs the two claimed families from source/target index assignments and maximal abelian group subsets; compares the sets exactly (not merely their counts); checks closure under multiplication; and checks the closed total-count formula.

Cases checked: trivial group, \(C_2\), \(C_3\), and \(S_3\) for \(n=2,3,4\); order-eight dihedral group for \(n=2,3\). The resulting maximal commuting-set counts for \(S_3\) are \(18,94,558\) at \(n=2,3,4\). For the trivial group the corresponding counts are \(3,13,51\). These computations are exact but finite, and cannot establish the statement for all groups by themselves.

To reproduce, run `python3 verify_maximal_commuting.py` and check that each case prints `OK` and that the process exits normally. The accompanying scientific limitation is the possibility of an equivalent theorem in literature not covered by the documented comparisons; this is not an external mathematical certification.
