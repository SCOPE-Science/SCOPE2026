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

# Exact reproduction

Run `python verify_cube9.py` in the same directory as `cube9_width_polars.json`. Both are included intact; only Python's standard library is required.

The checker reconstructs all 11440 subsets of nine corners of the four-cube, partitions them into 56 orbits using all 384 coordinate symmetries, and proves that the listed rational hulls are their width polars: candidate feasibility and full-dimensionality are exact, and every potentially supporting facet hyperplane of each hull is verified to be an original width halfspace. It next checks 290663 determinants of four vertices, also exactly, with maximum normalized determinant one. The checker reports 1066 candidate vertices, 11812 supporting quadruple incidences, a maximum of 28 vertices in one polar, and a maximum common denominator of six.

Expected terminal record:

`FOUR_CUBE_NINE_VERTEX_VOLUME_OK orbits=56 subsets=11440 certified_vertices=1066 max_vertices=28 facet_tests=11812 determinant_tests=290663 max_scale=6 max_det=1`

These checks establish only the finite combinatorial lemma. The associated analytic proof of the universal parallelotope-volume claim, including the relation between inverse edge matrices, widths, and volumes, is in `RESULT.md`. No claim is made about integer-lattice covering, larger dimensions, independent human auditing, or priority certification.
