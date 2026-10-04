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

The general proof has four independently checkable steps.

1. **Domination criterion.** A family of subgroup vertices dominates exactly when its union contains every minimal subgroup. This follows because any nontrivial intersection with a minimal subgroup contains that whole minimal subgroup.

2. **Exponent \(p\).** Every nonidentity element has order \(p\), so domination means covering \(G\) by proper subgroups. Replacing selected subgroups by maximal ones turns the problem into covering the \(2n\)-dimensional vector space \(G/Z(G)\) by hyperplanes. At least \(p+1\) are required; the \(p+1\) hyperplanes through a fixed codimension-two subspace attain the bound and form a clique.

3. **Exponent \(p^2\).** For odd \(p\), class two gives \((xy)^p=x^py^p\). Hence the \(p\)-th-power map is a nonzero homomorphism to the order-\(p\) center. Its kernel is proper and contains every subgroup of order \(p\), so it is a dominating vertex. Pairing it with the center gives sharp total and paired domination number \(2\).

4. **Finite replay.** The standalone checker constructs the Heisenberg extraspecial group of order \(27\) and exponent \(3\), and the modular extraspecial group of order \(27\) and exponent \(9\), enumerates every subgroup, builds each intersection graph, and exhaustively searches ordinary, total, and paired dominating sets. It separately checks the cube-map kernel and the \(\mathbb F_3^2\) hyperplane-cover minimum.

Exact output:

```text
VERIFY_OK
Heisenberg27_exp3: vertices=17 subgroup_orders={3: 13, 9: 4} gamma=4 gamma_t=4 gamma_pr=4
Modular27_exp9: vertices=8 subgroup_orders={3: 4, 9: 4} gamma=1 gamma_t=2 gamma_pr=2
M27_pth_power_kernel_size=9_contains_all_order3_elements
F3^2_hyperplane_cover_minimum=4
```

The finite calculations are corroborative only. The arbitrary-order result is proved symbolically.
