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

The frozen complex equality sentence was false: at p=q=1, beta=2 the optimal vector (1,3/2,1) can be multiplied by -1 with no change in norm or absolute objective, so even an orbit-constant maximizing bridge need not be positive real. The frozen proof's broad permutation-invariance assertion was also false without restriction to graph automorphisms (two equal unit weights on adjacent vs disjoint edges of a three-link path have different adjacency radii). The complete repair retains the true dual value, restricts permutation invariance to the leaf automorphisms, and proves activation for the modulus of every maximizing bridge, with strict real positivity only after phase normalization. Indeed the tree gauge and depth grading give half the nonnegative adjacency radius; modulus and averaging preserve the bridge modulus of any maximizer. The four-node quotient gives the exact determinant condition 4c^2 <= (4-u^2)(4-v^2), together with 0<=u,v<=2. Maximizing first over one angle gives a strictly concave scalar function with derivative at zero of sign beta^2-sqrt(pq). Its unique endpoint/critical point determines the value and forces c=0 even at beta=0 and at the threshold; above threshold strict increase in c forces the positive feasible boundary value. Triangle equality yields the common phase since all nonzero coefficients are counted with positive weight, except for the already zero bridge at beta=0. Independent two-by-two operator/nuclear duality reproduces both branches and bounded grid checks corroborate the witnesses.

## originality

PASS

Best of current evidence for the repaired claim: the primal adjacency formulation and the uniform three-link path special case are not novel, but neither gives the explicit dual value and activation for an independently varied bridge price and arbitrary pendant counts. The phase wording is a correction, not the ground for originality.

## value

PASS

The independent bridge multiplier probes a natural face of the primal unit ball. The plateau, sharp threshold and bridge activation give exact information about which graph features support the dual extremum, including the degenerate zero-price case and the transition itself. They apply to a full family, not just an isolated uniform path. The correction preserves this value without making a false claim about complex positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
