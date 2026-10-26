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

The full quantified theorem is proved symbolically by (a) extending an underlying-ground-set partial bijection in the Ehrenfeucht–Fraïssé game and (b) producing explicit existential distinguishing patterns. The critical root-size lemma is established within `RESULT.md` for disjoint unions of paths, including singleton and two-vertex path components. No black-box computation, unverified infinite enumeration or heuristic assumption is used by the proof.

Supplementary finite replay: run `python3 check_triangular.py` with a standard Python 3 interpreter. The script canonicalizes every induced adjacency pattern on at most four distinct triangular-graph vertices, for ground orders in the tested rank-dependent ranges, then checks separation at each consecutive order against the predicted threshold. Its exact stdout is supplied as `check_triangular_output.txt`. This confirms only the enumerated finite cases, not the theorem for unbounded ranks.

The graph language here contains a single binary adjacency predicate plus equality. In particular, there are no element names for the hidden ground set, no counting quantifiers and no built-in order. Source literature is evidence of background and comparison, not a substitute for the proof. The originality check is limited by searchable accessible literature.
