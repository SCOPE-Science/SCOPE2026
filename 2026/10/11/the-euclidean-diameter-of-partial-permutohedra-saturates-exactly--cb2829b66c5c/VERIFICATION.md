---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

A Euclidean diametral endpoint of any polytope must be a vertex by strict convexity of the Euclidean norm. The actual source Proposition 2.7 says each k-support vertex uses labels n,n-1,...,n-k+1. For nonnegative coordinates, (u_i-v_i)^2 = u_i^2+v_i^2-2u_iv_i <= max(u_i^2,v_i^2), strict when both are positive. Summation selects at most m of the doubled strictly ordered square labels; the maximal m entries are split evenly into two possible prefix lengths, and disjoint supports realize them. Equality forces no overlap and exactly those labels. Checked m,n=(2,3),(3,2),(4,3),(5,3),(6,2) by independently enumerated vertex pairs, with matching squared diameters 18,9,26,27,10. These finite cases corroborate, not prove, the all-parameter bound. Domain n,m positive including m=1 and saturation m>=2n.

## originality

PASS

Best-of-knowledge originality: targeted Resultary comparisons, exact primary theorem/parameter inspection and implication tests do not reveal prior coverage of the specifically identified surviving result. A self-indexed copy of the assigned finding is not prior coverage; risks are documented.

## value

PASS

A complete Euclidean-diameter formula and equality classification for a named natural two-parameter family of anti-blocking permutation polytopes fills an exact metric invariant gap. The sharp ambient dimension threshold m=2n is a structural phenomenon, not an arbitrary numeric slice; it differs essentially from inradius and minimum enclosing radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
