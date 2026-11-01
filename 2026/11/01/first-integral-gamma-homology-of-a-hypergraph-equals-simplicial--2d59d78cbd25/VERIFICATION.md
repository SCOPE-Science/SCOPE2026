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

Run `python3 verify_gamma.py` with Python 3 and SymPy installed. The script constructs all degree-two \(\Gamma\)-cubes from the radius-one-ball definition, removes cubes constant along a coordinate, forms signed boundary matrices over \(\mathbb Z\), and compares their Hermite-normal-form integer lattices to the independently built triangle-plus-backtrack lattice. It also computes first simplicial homology using a unimodular graph cycle basis and integral Smith normal form.

The script tests seven finite hypergraphs, including graph cycles, filled and nonuniform examples, the tetrahedron boundary and a combinatorially checked six-vertex projective plane. The final example has first homology \(\mathbb Z/2\mathbb Z\). A successful run prints `ALL EXACT INTEGRAL RELATION-LATTICE COMPARISONS PASSED`; this was observed when the script was executed from the package directory.

The unrestricted homology theorem is proved by explicit chain relations in `RESULT.md`, not extrapolated from finite experiments. Degree-two or higher homology of the \(\Gamma\) construction is not asserted to agree with simplicial homology. The original construction and conventions are those of Zaidi and Jamil, arXiv:2610.08196v1, Section 3. Independent mathematical verification has not been performed.
