---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: The equilibrium equations force y=x, exp(x^2)=d and x(z-b)=-k. For d<=1 no solution; for d>1 the two sign branches are exhaustive. The positive branch z=0 iff d=exp((k/b)^2), at which w is free, while the negative branch has w=0. The 3x3 Jacobian cubic at baseline has A=14/5, B_sigma=17 log(17)+sigma*39/(5 sqrt(log(17))), C=(442/5) log(17); Routh AB-C<0 gives exactly two RHP roots in the base block at either branch. Fresh numerical eigenvalues of the base are (-4.248453, 0.724226 +/-7.643808i) at positive x and (-4.746319,0.973159 +/-7.198712i) at negative x; the fiber eigenvalues are respectively -7.911517 and 9.911517, so full unstable indices are 2,3. Direct differentiation gives divergence -a-b+cz, changing sign above z=14/25 at baseline. The supplied rational-Taylor verifier's inequalities are sufficient for the rigorous Routh signs; numerical roots are cross-checks only.

## originality

PASS

PASS best of knowledge: This is an exact correction to the displayed vector field's published assertion of two stable equilibria, not a restatement of Routh-Hurwitz alone. The source's -2.3 divergence is one substituted state, not its global expression.

## value

PASS

PASS: This materially changes the local dynamical interpretation of a published hyperchaotic model, identifies a true exceptional equilibrium line, and prevents using a false stability premise to assert a hidden attractor. It does not overclaim basin structure or average volume contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
