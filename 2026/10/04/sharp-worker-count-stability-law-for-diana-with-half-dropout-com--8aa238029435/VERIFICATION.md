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

Centered worker shifts remove offsets b_i. Bernoulli half-dropout produces exact second-moment recursion on X=E x², Y=E x ebar, W=E mean e_i²; independent recomputation in sympy confirms M_n(s), char polynomial and P(1)=s[n(2+s-s²)-2s(s+2)]/(4n). Complete Jury inequalities are positive on 0<s<s_n as factored proof shows; at s_n P(1)=0, beyond necessary positivity fails. Conditional noise independence and all square-integrable initial states are in scope; arbitrary gamma<=0 not claimed. Asymptotic expansion and monotonicity checked.

## originality

PASS

Best-of-knowledge, implication-based comparison of exact theorem and primary findings; not a guarantee of globally exhaustive prior art. Independent averaging omega_av=omega/n is a qualitative ingredient of EF-BV; alone it does not yield the sharp root [n-4+sqrt(9n²+8n+16)]/[2(n+2)]. Related MARINA and EF21 have different memory transitions.

## value

PASS

Exact stability ceiling for DIANA memory plus independent Bernoulli compression as worker count grows is a motivated necessary/sufficient Schur boundary, beyond generic sufficient stepsizes. The n-dependence and limit 2 characterize a natural benchmark and can guide comparison of distributed compressor mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
