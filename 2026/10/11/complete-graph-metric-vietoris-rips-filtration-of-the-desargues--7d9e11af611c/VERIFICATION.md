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

# Reproducible exact verification

Run `python3 verify_desargues.py` from the directory containing this file. The verifier requires only the Python 3 standard library. The observed marker was `VERIFY_OK`.

The program independently enumerates the entire graph and integer distances, and verifies agreement with the five-bit symmetric-difference metric. It generates full face sets by maximal clique enumeration for scales one through three and verifies scale-four forbidden pairs. For each ordinary elementary collapse it checks that the chosen codimension-one face has exactly one proper coface. At scale two there are 30 such pairs; a spanning-tree quotient followed by five rounds of triangle relations trivializes all 90 edge generators. At scale three, 1,040 elementary pairs reduce the complex to face vector \((20,150,540,410)\), and unimodular integral boundary elimination produces 409 unit pivots plus one zero column. Independent mod-two homology calculations confirm reduced ranks 11 in degree one at scale one, 19 in degree two at scale two, and 1 in degree three at scale three. Exactly ten disjoint distance-five forbidden pairs certify the scale-four cross-polytope sphere.

The reduction of the fundamental group, integral Smith-type unit elimination, and homological Whitehead argument are explained in `RESULT.md`. Unlike a random numerical sample, this verifier checks the entire finite combinatorial object and each claimed local certificate step. This review is not an independent audit, and it proves no corresponding statement for other graphs.
