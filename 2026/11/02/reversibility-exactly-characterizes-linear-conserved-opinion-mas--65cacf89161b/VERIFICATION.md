---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For F_i=x_i+sum_j I_{ji}g(x_j-x_i)/d_i and g(s)=s(1-|s|), antisymmetry gives linear-statistic drift sum_{i<j} a_ij g(x_j-x_i), a_ij=c_iI_{ji}/d_i-c_jI_{ij}/d_j. In the strict ascending chamber g(t)=t-t^2 and the mixed second derivative in x_i,x_j singles out 2a_ij, proving each a_ij=0 necessary; cancellation proves sufficiency. On strongly connected support, any nonzero solution has no zero coefficients, requires bidirectionality, and the positive edge-ratio propagation is path-independent exactly when multiplicative cycle products agree. For reciprocal weights c_i proportional to d_i. The row stochastic P(x), stationary c, self-loop P_ii>=1/d_i and weighted Jensen identity yield spectral-gap contraction when opinion range<1; a nonradical opinion propagates interiority to every vertex then range<1, while all-radical configurations may freeze. Independently evaluated the stated balanced regular triangle with rational arithmetic: F(0,1/3,2/3)=(1/9,8/27,5/9), sum drift -1/27; the forward vs reverse cycle products are 1 vs 1/8. Invariance is universal over x, not each particular trajectory.

## originality

PASS

Alvim et al. 2021/2022 introduce the exact synchronous confirmation-bias update and show consensus for regular reciprocal networks. Mangesius–Delvenne–Mitter 2015 gives weighted-average sufficiency under detailed balance for a broader continuous-time equation. The assessed all-configuration iff linear invariant criterion via mixed derivatives, multiplicative cycle obstruction and balanced regular counterexample for the precise discrete-time bias map were not identified as covered by inspected primary statements.

## value

PASS

The mathematical question is whether weighted opinion averages survive a nonlinearly state-dependent confirmation bias. A complete necessary-and-sufficient reversibility criterion is structurally informative; the explicit balanced regular counterexample shows a genuine separation from linear DeGroot mass conservation. The irregular reciprocal consensus value and geometric dissipation estimate provide motivated consequences beyond renaming detailed balance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
