---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Derived the exact absent-indicator formula W_m=D^2 Var(K_m)=sum_i q_i(D-q_i)+2sum_{i<j}(D r_ij-q_i q_j) with D=binom(N,m), q_i=binom(N-a_i,m), r_ij=binom(N-a_i-a_j,m). Independently enumerated every integer partition of N=2..8, every unordered distinct permitted pair transfer, every possible sample subset for every m, and counted transfer totals 0,0,1,2,5,9,17; only N=8 (4,3,1)->(4,2,2) had >=2 reversals. Direct rational differences matched the full displayed vector (0,-11/784,73/3136,1/245,-55/784,-95/784,-7/64,0). Independently recomputed the full rational polynomials P_2(t),P_3(t),P_7(t) for t=k-1 from exact binomial moments and checked every coefficient against RESULT (degrees 3,5,13 with signs negative, positive, negative); coefficientwise signs prove the all-size theorem, not finite extrapolation. Pascal identity yields strict expected-richness increase. No floating approximation.

## originality

PASS

Best-of-knowledge originality based on actual compared primary scientific claims and explicit residual risks; inaccessible texts not presumed to be absent or covering.

## value

PASS

Richness sampling uncertainty is a natural statistical/ecological quantity beyond its mean. The result establishes the globally sharp first counterexample to a natural conjectured monotonicity under a single Robin Hood equalizing move, unique at the first size, and a uniform infinite family witnessing persistent nonmonotone variance while the mean improves. Exact small finite cutoff is mathematically motivated by this sharp boundary, and the all-size symbolic certificate shows it is not a one-off table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
