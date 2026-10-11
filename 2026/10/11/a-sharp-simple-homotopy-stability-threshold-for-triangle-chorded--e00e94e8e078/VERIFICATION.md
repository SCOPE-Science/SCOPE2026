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

The standalone `verify.py` program requires only Python 3. It independently enumerates all subsets of cardinality at most six on cycles of sizes 7 through 18 and tests the absence of independent triples. It compares exactly the resulting full face sets before and after inserting the chord, and verifies each elementary free-face collapse by checking uniqueness among the current maximal cofaces. It separately enumerates every face for the six-vertex boundary and executes 27 verified collapses to a single vertex. Run with `python3 verify.py`.

Output: `VERIFY_OK 27 six-vertex collapses; 12 full enumerations and exact two-stage elementary collapses`.

The infinite-parameter assertion rests on the combinatorial proof in `RESULT.md`. Finite computation is not used to extrapolate the assertion. The homotopy type of the original cycle complex comes from the cited published Corollary 39. Integral simple-homotopy equivalence follows directly from elementary collapses. Independent audit: not performed.
