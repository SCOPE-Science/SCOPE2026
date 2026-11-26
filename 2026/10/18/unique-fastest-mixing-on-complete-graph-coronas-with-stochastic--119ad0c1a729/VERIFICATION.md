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

Simultaneous core–leaf pair averaging preserves the feasible set and cannot increase SLEM. The invariant matrix has one constant-pair block (eigenvalues 1 and 1−2p) and m−1 transverse 2×2 blocks. The latter's upper eigenvalue dominates the lower eigenvalue in modulus since the trace is nonnegative, and also dominates |1−2p| by the bounds max(1−p,p). This includes reducible boundaries. At p=0 the SLEM is 1, while some positive feasible p,q give less than 1. For p>0 the upper branch strictly decreases in q, forcing core saturation. With c=m/(2(m−1)) and t=1−p the boundary objective is (1−c)t+sqrt((1−t)²+c²t²); its second derivative is c²/((1−t)²+c²t²)^(3/2)>0 and its endpoint derivatives are −c and 1. Squaring at the interior tangency gives the stated quadratic for μ. Its unique positive root and t=(1−(1−c)μ)/(2c) yield the stated radicals and their limits. Unrestricted uniqueness is not inferred from averaging alone. The PSD deficit μI−(Q−J) for each conjugate of an arbitrary optimizer must vanish on the average's active transverse eigenspace E={(u,ru):u⊥1}, with r>1. The leaf equations fix every p_i; the core equations fix the weighted clique Laplacian on the whole of 1-perp, and it vanishes on 1. Consequently every core-edge entry is the same, forcing the unique stated kernel. The frozen verifier was inspected but not executed; finite deterministic and random checks are not a general uniqueness proof.

## originality

PASS

The earlier signed solution is infeasible in this stochastic problem, and the earlier reversible one-edge formula excludes the uniform regime m≥3. A distinct later-dated general corona record demonstrably covers the optimal value and weights; its proof also readily implies unrestricted uniqueness in the complete-core case, despite not claiming that in general. No inspected evidence dates that stronger result earlier than this frozen record. The pass is a bounded judgment on the earlier exact stochastic finding, not a claim of content absent from the current index or of exclusive priority.

## value

PASS

The result solves the stochastic saturation regime on a canonical family where the otherwise optimal consensus chain is infeasible. It gives the exact optimum at each size rather than just an asymptotic bound, and a complete optimizer classification across all supported kernels. The active-eigenspace rigidity handles precisely the non-invariant variation that generic symmetry reduction leaves open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
