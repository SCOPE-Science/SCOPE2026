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

For pi3 products e1²=e2, e1e2=e2e1=e3, e1e4=e4²=e5, Phi_tau sends e1→−e1,e2→e2,e3→−e3,e4→tau e3−e4,e5→e5 and satisfies all 25 ordered basis products. Independent exact derivation Leibniz-system nullspace gives dimension 6; imposing ten necessary pointwise local-derivation evaluations yields precisely the displayed seven-parameter upper/lower triangular necessary matrix. Its (e3,e4) block exp offdiagonal is s(e^(3x)−e^x)/(2x). Matching exp(A)[1,1]=−1 forces e^x=−1 and thus this entry zero; impossible for tau≠0. Phi_0 is exp(diag(i*pi,2i*pi,3i*pi,i*pi,2i*pi)), a genuine derivation. Refutes only pi3 Theorem13 surjectivity.

## originality

PASS

The inspected primary Theorem 13 claims exponential surjectivity onto the plus component, but its proof overlooks vanishing of the divided difference (e^{3x}−e^x)/(2x) at e^x=−1. The explicit automorphism family with nonzero (3,4) entry refutes that exact assertion; existing general literature on other local algebras is not a counterexample for this pi_3.

## value

PASS

An explicit complex one-parameter counterfamily sharply identifies a resonance that invalidates a published theorem on exponential surjectivity of local derivations. It has a clear mathematical purpose, demonstrates the zero coefficient at e^x=−1, and distinguishes tau=0 from tau≠0. No new general classification is needed for the counterexample to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
