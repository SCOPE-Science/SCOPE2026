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

Use the included `verify_k34.py` with Python 3.9+ standard library; no external package or inputs are needed. `verification_output.txt` contains the exact printed output. The script constructs all weight-three reduced Świątkowski generators, computes differential columns, tests every \(\partial^2\) coefficient, determines four finite-field boundary ranks, constructs the exact actions of four generators on all chain bases, and checks chain-map commutation on all basis vectors. It then evaluates the alternating traces of all \(144\) natural graph automorphisms and resolves their degree-one and degree-two rational characters into the complete \(3\times5\) outer-product irreducible character table.

The exact algebraic argument relating these checks to rational homology requires the independent first-homology theorem of Ko and Park (2011): for \(K_{3,4}\), \(\beta_1=6\). It is not derived by merely extrapolating finite-field ranks. The natural equivariant map onto graph-cycle homology provides the first-degree representation. The rational character identity uses the finite-dimensional chain Euler identity. The finite-group orbit-space conclusion uses rational transfer, which does not assert homotopy type.

The output confirms \(C=(364,1326,1476,491)\), differential nonzero counts \((2652,5904,2946)\), rank vectors modulo \(3,5,101\) all equal \((363,957,491)\), and the characteristic-two rank vector \((363,956,491)\). The characteristic-two difference is compatible with the known degree-one \(\mathbb Z/2\) torsion; **no full integral torsion classification is independently proved here**. The integral homology groups are known externally from An (2026), so no novelty is claimed for them.

Independent mathematical audit remains unperformed. Computational replay verifies the specified finite checker, not an unlimited theorem or publication priority.
