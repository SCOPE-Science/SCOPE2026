---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The frozen polynomial map with alpha+beta=2 has exact scalar identity s_{n+1}=s_n+R s_n(1-s_n), preserves Δ for 0<R<=1 and 0<alpha<2, and has strictly positive coordinate multipliers. Any stationary probability integrates R s(1-s) to zero and so is carried by O or face s=1. On this face, for kappa=R(1-alpha) nonzero, V=xyz contracts by AM–GM of the three positive factors 1+kappa(y-z),1+kappa(z-x),1+kappa(x-y) with product <=1, strictly unless C or V=0. Thus invariant measure is supported on closed edges and C. Each relative open edge is invariant with strictly signed increment x_{n+1}-x_n=kappa x(1-x) (cyclic analogues); integrating against a stationary restriction excludes edge interiors, leaving exactly 5 fixed atoms. If alpha=1 the face map is identity and arbitrary face measures are stationary. For unequal initial positive composition, normalized product P_n decreases strictly and cannot tend to a positive limit without equality of all limiting proportions, contradicting P_0<1/27; hence P_n->0 and min coordinates->0; the mass bound 1-s_n<=(1-s0)(1-Rs0)^n is exact. Independent rational calculations checked mass identity and strict product contraction for one unequal face composition, plus equal-composition scalar mass evolution at a second state. The global measure and trajectory claims are proved analytically for the stated closed compact simplex, not inferred from those examples.

## originality

PASS

Best-of-knowledge originality after primary-literature reading and Resultary queries. The explicitly identified prior statements and implication gaps are documented under the four checks. A failed search is not proof of priority, and inaccessible literature was not treated as automatic failure.

## value

PASS

The continuous May–Leonard neutral balance supports a foliation by interior periodic orbits. The exact Euler discretization, even with arbitrarily small positive admissible step, destroys those interior invariant measures at the same balance and leaves only a finite simplex of stationary probabilities. This rigorous discretization contrast and full invariant-probability classification are structurally useful in nonlinear population dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
