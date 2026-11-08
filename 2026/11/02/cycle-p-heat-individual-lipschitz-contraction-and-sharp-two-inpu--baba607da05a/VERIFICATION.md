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

Subtract vertex p-heat equations to obtain a_i′=φ_p(a_{i+1})+φ_p(a_{i-1})−2φ_p(a_i) for cyclic edge gradients ∑a_i=0. Monotonicity of φ_p and coordinate maximum principle give single-input L contraction. For p=2 the difference edge flow is linear heat; for n=3 the cycle equals complete graph and oscillation of two-solution vertex differences contracts by comparison. For n≥4 the explicit zero-sum base a=(1,R,−(R+n−2),1,…,1) and direction b=(1,1,−1,0,…,0,−1) have L(b)=1. The first-edge derivative of normalized two-solution symmetric perturbations tends to (p−1)(R^{p−2}−3). Choose R→∞ for p>2 or R↓0 for p<2 to make it arbitrarily positive, then choose ε>0 sufficiently small, proving unbounded liminf initial rate. All base edge values are nonzero when differentiation is used. This says nothing about infinite gain at any fixed positive time.

## originality

PASS

Classical discrete p-heat works cover existence, order and vertex ℓq contraction; a *linear* graph heat gradient theorem covers p=2 only. These statements do not imply nonlinear two-input edge Lipschitz classification. The explicit n=3 exception and every n≥4 p≠2 instantaneous obstruction are the assessed novelty, not the maximum-principle lemma.

## value

PASS

Sharp boundary p=2 or triangular graph distinguishes decay along each flow from stability of the semigroup in an intrinsically meaningful edge-Lipschitz metric, with universal large instantaneous sensitivity. It is a complete natural cycle family and a structural counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
