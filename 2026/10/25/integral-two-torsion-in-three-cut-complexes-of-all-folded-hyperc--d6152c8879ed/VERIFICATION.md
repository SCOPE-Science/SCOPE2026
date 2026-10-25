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

# Verification of the finite checks

Run `python3 verify.py` using only Python 3's standard library. The checker reconstructs the antipodal cube graphs for dimensions \(5,6,7\), enumerates all vertices, edges, induced two-edge paths and four-cycle tetrahedra of the ordinary three-cut Alexander dual, and exhausts the candidate four-subsets. It checks exact free-face eligibility for both simplicial collapses per square on the evolving complex and calculates signed boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). It independently cross-checks the combinatorial rank formulas and stops with `VERIFY_OK`.

Expected dimension-zero through dimension-three face vectors: \((16,120,160,40)\), \((32,496,480,120)\), \((64,2016,1344,336)\). Expected counts of extra long edges: \(0,160,1120\). The free rank of second dual homology is predicted to be \(15,55,175\). Difference in characteristic-two versus characteristic-three Betti numbers is compatible with two-torsion in each tested case, but **does not itself establish integral torsion or exclude higher odd-primary torsion**. The integral conclusion and infinite-family result follow from the exact cubical quotient of the sphere, its fundamental group, cellular H2, the universal-coefficient theorem, and combinatorial Alexander duality proved in `RESULT.md`.

The complex whose homotopy type is given is the **combinatorial Alexander dual**. The original ordinary cut complex is classified only up to its reduced integral homology, not its homotopy type. Scientific conclusions were reviewed in the same model and have not undergone independent audit.
