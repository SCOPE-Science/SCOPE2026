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

# Verification

**Theorem scope.** Fixed finite connected bidirected network; positive directional rates and positive recovery rates; limit of a shared transmission multiplier to infinity. No finite-check enumeration is used as a proof for all networks.

**Analytic checks.** The generator identity for the test function \(f(S)=(K/\lambda)^{|S|}\) is exactly \((\lambda-K)(M(S)/K-c(S))\), which is negative under the prescribed constant \(K\). Optional stopping supplies the uniform small hitting probability needed for the coefficient induction. The renewal cycle formula is exact, with an \(O(\lambda^{-1})\) expected excursion correction. The order-chamber and tree-edge transforms each have unit absolute Jacobian; each tree edge contributes exactly \(1/w_{uv}+1/w_{vu}\).

**Runnable exact checker.** Use `python3 verify.py` from the extracted package directory. The checker uses only the Python standard library, exact rational arithmetic, and Gaussian elimination for selected finite absorbing chains. The saved replay reported:

```
ALL_CHECKS_PASSED
tree_product_checks: 1441
total_exact_checks: 1576
path_P3_C: 4
triangle_K3_C: 3/2
tree_directed_heterogeneous_factor: 4/45
```

**Limits of the checks.** The finite enumerations cover labelled trees through six vertices, connected graphs through four vertices, and a few large-transmission test points. They neither exhaust all network sizes nor establish the asymptotic without the analytical proof. The 2015 exact survival-time paper was accessible only at the abstract level; its full implication to the claimed formula remains unresolved. Independent verification has not been performed.
