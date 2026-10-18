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

For original pre-update-table SAGA on scalar f_i(x)=a_i x^2/2, write state z=(x,y1,y2). Direct gradient-memory expansion yields exact 3×3 index matrices; second moments lift to six monomials. IID transition is (L(M1)+L(M2))/2 per step; independent random reshuffle transition (L(M2M1)+L(M1M2))/2 per epoch. At (a,b,eta)=(1,1,23/20), Q=[[253,-53,-53],[-53,230,-114],[-53,-114,230]] and iid mean residual Q-E[M_i^T Q M_i] have strictly positive leading principal minors (Q: 253,55381,8163120; residual: 563/400,789489/640000,5427/5120), proving all-initial-state geometric mean-square stability. At (1,4,27/100), epoch reshuffling Q=[[259,5,-34],[5,3,-3],[-34,-3,9]] has minors 259,752,1989 and residual positive minors 192531773/50000000, 7694776875239369/1600000000000000, 2268049442949819/640000000000000. Both sets of minors were recomputed exactly. For the opposite schemes, the source supplies full exact initialized rational generating functions for E[x_k^2] with denominators positive at 0, negative at 1, and numerator coprime to denominator; therefore an uncancelled real pole inside (0,1), giving limsup geometric growth along subsequences by Cauchy-Hadamard/nonnegative coefficients. Source exact six-monomial lift and rational-function verification algorithm were inspected, and independently constructed 3×3 matrices and first 0..3 grouped moments matched across direct path enumeration and lifted matrix propagation. Strict inequalities persist locally in parameters; no almost-sure divergence or full frontier claimed.

## originality

PASS

The original Defazio–Bach–Lacoste-Julien SAGA defines saved gradients at the previous iterate, which is crucial to these matrices. Ying–Yuan–Sayed 2017 random reshuffling variance reduction instead updates its selected stored gradient at the post-update point and proves convergence for sufficiently small steps, not this pre-update memory law. Qian–Qu–Richtárik 2019 studies iid arbitrary sampling sufficient bounds, not a bidirectional comparison. The same pre-update SAGA two-parameter counterexample pair was not found in materially inspected sources. Resultary nearby SARAH/STORM findings are different algorithms.

## value

PASS

Two-way failure of a universal stability ordering is a structural algorithmic counterexample, not a tiny accuracy gain. In one example even identical component curvatures do not prevent reshuffling instability; the reverse witness establishes that neither iid nor reshuffle generally dominates. Strict Lyapunov and pole certificates make both contrasts robust and precisely distinguish sampling correlation from curvature heterogeneity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
