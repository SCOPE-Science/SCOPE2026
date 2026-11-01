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

# Reproduction and verification

Run `python verify.py` with Python 3 and its standard library; no third-party packages are needed. The executable independently generates dihedral groups using the multiplication law on pairs \((u,\varepsilon)\), constructs every specified maximal subgroup, checks the subgroup-lattice maximality independently for \(n\le12\), verifies the Frattini intersection, and evaluates the actual nerve predicate against the claimed blockwise description for every family of maximal-subgroup vertices. It also checks all automorphisms \(\alpha_{a,b}\) for each tested parameter, their induced maximal-subgroup action, the cyclic trace count, and the reduced Euler characteristic.

Tested parameters were \(n\in\{3,4,5,6,8,9,10,12,15,18,21,30,36,42,60\}\). All checks completed, ending in `ALL_VERIFY_OK direct_subgroup_intersections_nerve_affine_action_and_euler`. The larger squarefree examples include two- and three-prime blocks. The proof in `RESULT.md` establishes the all-parameter theorem; the tests are supplementary finite verification and do not establish universal acyclicity or homotopy equivalence by themselves. The standard equivariant nerve and cofibration arguments are mathematical deductions, not executable certificates.

Independent mathematical audit and independent validation have not been performed.
