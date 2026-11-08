---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. Translating the additive baseline yields residual efficient sum zero. Coalition U and its complement D force excess >=max(b-t,t)>=b/2, and symmetric residual point attains b/2. Complement bounds at optimality constrain every residual subset sum to [-b/2,b/2], forcing nonnegative useful and nonpositive distractor residues with sums +/-b/2. Thus entire least core equals T Delta_{u-1} x (-T Delta_{d-1}), T=b/2, dimension u+d-2 and ud vertices. Symmetry plus uniqueness of the prenucleolus gives equal within-group residuals; strict convexity/KKT yields water-filled useful minimum-norm allocation and uniform distractor allocation. Exact pivotal coalition probabilities yield phi_D=a-b/(d binom(u+d,u)), while all least-core distractor totals equal da-b/2, hence universal-negative-vs-positive-Shapley precisely 2ad<b<ad binom(u+d,u). Independently checked all eight simplex vertices, efficient payoffs and excesses for u=4,d=2,a=5,b=60, and exact Shapley weights; finite check corroborates proof.

## originality

PASS

PASS, best of knowledge with high priority qualification. Kera–Yamauchi–Nagarajan 2026 already study the exact u=4,d=2 contextual-distractor numerical example, with Shapley distractor credit +3 and nucleolus/minimum-norm -10; this numerical instance is NOT new and is explicitly credited. What survives is the all-positive-parameter product-of-simplices least-core geometry, every-vertex count, general KKT min-norm water-filling and if-and-only-if sign interval. Primary full text of Kera and a related Nagarajan paper was not available, so mathematical implication of their full sections/appendices is a substantial residual risk. No proof of historical priority is asserted.

## value

PASS

PASS, qualified. The game is a natural parametrization of an already-used contextual-distractor counterexample, and the exact geometry of its least core, full optimizer selector formula, and universal vs pointwise sign-gap threshold clarify real attribution-model behavior. Although basic coalition inequalities are elementary, the complete parametric classification of this motivated model gives an interpretable exact invariant beyond copying the known single numerical table. Only signed efficient, no individual rationality or positivity constraints are addressed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
