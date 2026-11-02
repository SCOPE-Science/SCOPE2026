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

# Verification and reproducibility

Execute `python3 verify_ehrhart.py` and `python3 verify_intersections.py` in the directory containing these files. Both are standalone Python standard-library programs.

The first enumerates all \(57\) relevant subsets of the six normals, constructs exact rational polygons, computes lattice-normalized areas and boundary steps, and checks the following grouped coefficient triples in the order quadratic, linear, constant:

- Pair through sixfold subset counts: \((60,60,15)\), \((39,39,20)\), \((21,21,15)\), \((7,7,6)\), \((1,1,1)\).
- Finite intersection multiplicities two through six: \((14,14,0)\), \((5,5,0)\), \((1,1,0)\), \((1,1,0)\), \((1,1,1)\).
- Chern numbers after adding points at infinity: \((86,62,-13)\) and \((36,24,-4)\).

It printed `EXACT_EHRHART_CERTIFICATE_OK` upon successful completion.

The second enumerates primitive homogeneous projective intersection points directly from all pairs of distinct lines, reconstructs their incident line sets, and checks the claimed multiplicities and Chern numbers for \(n=6,12,18,24\). It printed `INDEPENDENT_PROJECTIVE_CENSUS_OK`.

The all-width conclusion additionally rests on the lattice-polygon Ehrhart argument and finite symbolic subset identity given in `RESULT.md`; checking only finitely many widths would not suffice. The published logarithmic Chern identities and density lemma are cited there. No separate external or independent scientific audit was performed.
