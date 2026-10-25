---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Unit hub constraints yield |x_i|<=1 and path edges |x_i-x_{i+1}|<=1, so Fubini expresses V_n=<1,T^(n-1)1> with symmetric integral kernel 1_{|x-y|<=1} on [-1,1]. Resolvent u=1+zTu even and for x>=0 satisfies u'(x)=-z u(1-x), u''(x)=-z²u(x). Endpoint identities u(0)=2u(1)-1 and u'(0)=-z u(1) yield G(z)=4sin(z/2)/[z(cos(z/2)-3sin(z/2))]. With alpha=2 arctan(1/3), cotangent partial fractions give V_n=(4/5)sum_{j in Z}(alpha+2pi j)^-(n+1), convergent absolutely. Nonzero-pole corrections alternate sign, since paired negative pole a_-k is closer to zero than a_+k; each 1+epsilon_n>0 from geometric volume, establishing strict parity-sign ratio inequalities all n. Independent exact polynomial-transfer integration matched Ehrhart finite differences for n<=8, and numerical ratio signs through n=11; infinite signs proven by pole pairing, not computation.

## originality

PASS

Best-of-knowledge: targeted published finding search and primary-source theorem comparison did not identify a prior result implying the entire final claim; known components are explicitly credited, not counted as novel. Closed meromorphic generating function and exact all-index alternating spectral correction for the coordinate-volume sequence of natural fan-graph Lipschitz balls. Unindexed-equivalent risk retained.

## value

PASS

Anchored-coordinate volumes of Lipschitz duals for the natural fan graph give a nontrivial graph-indexed convex-body volume sequence. Explicit resolvent, rational coefficients, exact spectrum and strict all-index parity oscillations supply an independently useful analytic benchmark unavailable from generic facet counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
