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

# Reproducibility and limits

Run `python3 verify_polyhedra.py`. Python 3.9+ and its standard library suffice. The executable does not download data, require pseudorandomness, or rely on a precomputed graph object. Its input graphs are generated from ordered tetrahedral darts and cube-edge incidence, respectively.

Every nonempty vertex subset is tested twice, by connected induced triples and by component flood fill. The full face poset and facet dimensions are checked, followed by the deterministic vertex-order partial matching. Acyclicity is checked by topological sorting of every oriented Hasse incidence. The integral Morse boundary is computed with signed recursive gradient-path reductions; the three-by-three matrix for the truncated tetrahedron is verified exactly zero. The original simplicial boundary matrices are independently reduced over the two-element field to corroborate reduced Betti numbers. The final success marker is `VERIFY_OK`.

The proof needs the exact integral Morse boundary, not merely homology dimensions. The independent mod-two calculation is a cross-check, not a substitute for the integral path computation. Both claims are finite and exhaustive; no inference from sampled parameter values is used. Independent scientific validation has not been carried out.
