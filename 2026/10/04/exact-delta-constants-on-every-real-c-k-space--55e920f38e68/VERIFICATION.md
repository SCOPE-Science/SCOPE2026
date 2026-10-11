---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The arbitrary-slice lower bound is complete. Urysohn localization near a non-isolated point forces radius at least \(1+\beta(f)\). For each active isolated point, sign alignment and a one-coordinate perturbation yield the sharp atomic inequality \(a_t(R+1-|f(t)|)\ge\alpha\); combining it with the slice defect gives every finite-subsum active constraint and hence \(\Phi_f(R)\le1\). Conversely, above any feasible radius the active isolated set is finite, reciprocal-width weights define a norm-one atomic functional, and its slice separates all coordinate-bad faces. Letting the auxiliary radius decrease proves equality. Infinite sums are handled as suprema of finite subsums, and the boundary is reached by approximation. The bundled finite checker was inspected only as a verification of the finite separation algebra, not as proof of the compact-Hausdorff localization.

## originality

PASS

Best-of-knowledge originality passes for the combined exact Delta-constant formula on every infinite real C(K). Choi–Jung provide the quantitative invariant, lower bounds and special exact c0 families, plus a uniform-algebra upper estimate, while the earlier C(K) result is qualitative. Two relevant published SCOPE records separately solve all of c0 and the Daugavet constant on C(K). Neither statement mechanically yields the audited Delta formula, because the latter simultaneously requires the non-isolated localization floor and the exact isolated-atom bad-face obstruction in one arbitrary-slice argument.

## value

PASS

The theorem gives a natural exact invariant on every infinite real C(K), quantitatively separating the topological obstruction from the isolated-coordinate geometry. It strictly extends the exact c0 mechanism to arbitrary compact spaces and explains mixed examples that neither the qualitative endpoint theorem nor the Daugavet constant can resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
