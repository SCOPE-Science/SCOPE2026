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

# Reproducing the finite signed-chain checks

Run `python3 verify.py` in a Python 3 environment with `sympy` installed. The program reconstructs cyclic windows of the clique complex of \(C_n^m\), its induced boundary facets, all boundary faces and signed incidence matrices. It asserts \(\partial^2=0\), computes rational Betti numbers by exact matrix rank, and computes nonunit integral Smith factors of the top incidence matrix. Five finite cases are checked: \((10,3)\), \((11,3)\), \((13,4)\), \((14,4)\), and \((16,5)\). The script is stand-alone and needs no hidden inputs.

The observed reduced Betti ranks are respectively \((0,2,1)\), \((0,2,1)\), \((0,1,0,0)\), \((0,1,1,1)\), and \((0,1,0,1,1)\). In the \((13,4)\) case the top boundary operator has one nonunit Smith invariant equal to \(2\), and none of the other cases has a nonunit top Smith factor. For this finite chain complex the resulting torsion is the torsion of the second boundary homology group, because the quotient by that group's free image of the next differential does not change torsion of the cokernel.

The general result is proved independently of the finite range using cyclic facet orientation transport, Poincaré–Lefschetz duality with orientation coefficients, and the long exact sequence of a pair. The two prerequisite manifold and ambient-homotopy statements are taken from the cited literature and are not independently reproved by this checker. The checker does not establish uniqueness in published literature or an all-dimensional PL-homeomorphism classification.
