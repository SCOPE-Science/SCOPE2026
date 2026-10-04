---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The accepted claim is the single interval statement \(10 \le m_{\mathrm{FPP}}(S^1) \le 14\).

For the lower bound, the checked implication chain is:

1. fixed point property plus at most \(9\) points \(\Rightarrow\) connectedly collapsible (Rutkowski small-set result, explicitly restated by Schröder);
2. connectedly collapsible \(\Rightarrow\) link collapsible \(\Rightarrow\) pseudo cone (Baclawski, Proposition 6.5 and Corollary 6.9);
3. pseudo cone \(\Rightarrow\) contractible order-complex realization, hence \(H_1=0\);
4. McCord's weak equivalence transfers the homology obstruction to the finite \(T_0\)-space;
5. \(S^1\) has \(H_1(S^1;\mathbb Z)\cong\mathbb Z\), so weak circle type is impossible at cardinality at most \(9\).

For the upper bound, Barmak's arXiv:1307.1722, Lemma 10, was inspected for the explicit \(14\)-point space and the two required properties: fixed point property and weak homotopy type \(S^1\).

No computation, finite enumeration, or machine certificate is used in the proof. The principal verification limit is source access: the Rutkowski 1989 primary full text was unavailable, so the exact at-most-nine formulation was checked in Schröder's later explicit restatement. The exact minimum remains open within the five candidate sizes \(10,11,12,13,14\).
