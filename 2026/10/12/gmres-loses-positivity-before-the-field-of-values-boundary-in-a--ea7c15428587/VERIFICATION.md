---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Nilpotence S^4=0 gives A_t^−1=I+tS+t²S²+t³S³≥0 for t>0. Spectrum of path adjacency gives Hermitian positive-definiteness iff 0<t<sec(pi/5)=sqrt5−1. First GMRES coefficient alpha=2(5−4t)/(9t²−16t+10)>0 in that interval. Exact 2x2 normal equations yield the stated x2 coordinates over positive Gram D(t), with fourth coordinate −2(t−1)(8t²−15t+13)/D(t). Quadratic is everywhere positive, first three coordinates are positive on 0<t<sqrt5−1 by monotonicity/evaluations at 5/4. Independent rational normal equations at t=6/5 give x1=(5,10,10,5)/47, x2=(6445,5630,2000,−815)/1777, and positive exact x*. Direct residual-square check 10>468/47>6480/1777 corroborates valid GMRES decrease. A counterexample is not a claim about later iterates or general M-matrices.

## originality

PASS

Classical GMRES and numerical-range convergence theorems are prior work, but their residual-polynomial/field-of-values estimates do not imply coordinatewise nonnegativity. Published Resultary neighbor theorems concern other algorithms (MINRES, CG, SOR, steepest descent), different SPD settings and universal condition-number barriers. No compared primary result states this family-specific exact M-matrix GMRES sign boundary.

## value

PASS

Inverse-positive M-matrices naturally arise in monotone linear systems, and preservation of nonnegative intermediate approximate solutions is a useful algorithmic requirement. The exact 4-state t=1 threshold separates GMRES cone safety from a wider 0<t<sqrt5−1 numerical-range stability regime. This independently motivated counterexample cleanly disproves several natural but false inference chains without extrapolating to all M-matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
