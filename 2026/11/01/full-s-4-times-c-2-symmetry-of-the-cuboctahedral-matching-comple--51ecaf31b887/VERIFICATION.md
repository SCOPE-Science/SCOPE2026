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

Both packaged Python programs were executed as standalone programs with the standard library only. `verify_cubocta_equiv.py` independently enumerates the 2,648 nonempty simplices; certifies 1,287 pivot-matching pairs, 2,648 vertices and 9,936 oriented Hasse incidences, acyclicity by an exhaustive topological sort, and an integral unit minor of the 65-by-8 Morse boundary. It checks all forty-eight group automorphisms and all ten character-table values, dimension and invariant-space identities, and emits `VERIFY_OK`.

`verify_orbit_cycles.py` directly sums admissible unions of edge-orbits for all forty-eight automorphisms without using the dimension-by-dimension chain trace routine. It produces the same ten character values and emits `ORBIT_VERIFY_OK`. The `.out` files record the exact successful executions. These finite exhaustive checks verify this finite complex and its rational character, not any broader family. Integral representation-lattice structure and integral quotient homology were not computed; no independent audit has been performed.
