---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The frozen Finding is correct, but the proof's Step 4 (RESULT.md line 68) reverses the sign of the upper-endpoint derivative in the increasing-y coordinate. Step 3 uses the increasing-x inward coordinate, so its strictly negative derivative implies a strictly positive derivative in increasing y. The complete corrected RESULT.md supplies this change and a short independent endpoint calculation. Specifically, existence follows from connectedness, positive definiteness and compactness. For a nonzero diagonal perturbation the Hessian trace is strictly positive since it is twice the trace of a positive definite weight times the square of a nonzero symmetric matrix. Uniqueness then forces within-part equality. The two within-part zero-sum spaces and the part-constant 2-by-2 block give the stated trace; taking the budget derivative at y=0 yields (q/p^2)[p(p-1)/(z+q)^2-1-2/z], which expands to the negative multiple of H in the source. At x=0 the swapped expression for the inward increasing-x derivative is strictly negative because q(q-1)<p^2. The feasible restriction is strictly convex with positive increasing-y derivative at the upper end, giving exactly the stated KKT support rule including zero derivative at y=0, and the unique interior marginal equation otherwise. H(z)/z=R_q(z)-(p^2-p), and strict convexity and divergence at both ends give the conditional root classification. Independent rational inline evaluation of K_{6,2} verified signs 1117/216, -487/216, 1396/27 and two sign-changing transition brackets (3.34679965326,3.34679965327) and (10.38249485813,10.38249485814); it did not create a persistent script. The frozen verify.py is a separate finite replay path, inspected, not executed. The repaired q=3 example uses the exact values H_{8,3}(1/4)=625/64, H_{8,3}(1)=-8, and H_{8,3}(4)=70. Numerical and finite sign checks do not establish the all-parameter result.

## originality

PASS

The repaired text credits exact existing coverage of the two-hub q=2 support law, including its worked example, and claims the arbitrary-part-size phase diagram including q>=3. Neither a fixed count of equally weighted leaders, a Laplacian extremal spectral problem, nor a clique–independent-set join gives that general unit K_{p,q} continuous pinning result in the compared statements. This is not an originality claim about strict convexity or KKT, nor a priority ruling on the two-hub case.

## value

PASS

The supported result is a complete support phase diagram for a natural family of convex stochastic-network design problems. It identifies when extra budget makes an entire part lose positive gain and when further budget restores it, with exact endpoints and a new scope beyond the two-hub overlap. This is a useful diagnostic beyond either generic optimization principles or recompilation of one numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
