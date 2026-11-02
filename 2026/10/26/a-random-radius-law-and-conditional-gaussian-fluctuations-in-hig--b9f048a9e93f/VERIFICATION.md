---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For GEM(α) weights P_j=V_j∏_{i<j}(1−V_i), V_i∼Beta(1,α), the stick-break recursion yields ES=1/(α+1), ET=6/[(α+1)(α+2)(α+3)] and ES²=(α+6)/[(α+1)(α+2)(α+3)] for S=ΣP_j²,T=ΣP_j⁴. Independent spherical directions imply E(Q_d|P)=S, Var(Q_d|P)=2(S²−T)/d and hence E(Q_d−S)²=2α/[d(α+1)(α+2)(α+3)]. For fixed truncation, representing directions as Gaussian vectors divided by their Euclidean norms shows a multivariate ordinary CLT over d coordinates for the first coordinate and off-diagonal quadratic terms; odd Gaussian moments cancel mixed covariance, giving conditionally independent N(0,S) and N(0,2(S²−T)). Truncation tails vanish in conditional L² using Σ_{j>K}P_j²→0, yielding the stated joint stable conditional convergence. Independently checked beta recursions, finite-d kurtosis, and sphere covariance; the bounded diagnostics are not an asymptotic proof.

## originality

PASS

Guéneau–Majumdar–Schehr, arXiv:2602.08436v2, already derives the physical model, Kesten/stick-breaking representation (Eq.43), arbitrary-coordinate moments (Eq.47), radial moments (Appendix A3), and explicit radial laws at d=1,2,3. These premises and finite moment consequences are credited. Its inspected main sections and appendices do not state the joint P-conditional high-d Gaussian limit with independent first-coordinate and radius fluctuations and the nonconcentrating random radial limit. General Dirichlet mean laws do not automatically give this two-statistic stable CLT. Priority is provisional given broad stochastic-geometry literature.

## value

PASS

A natural high-dimensional question is whether the trapped active-particle radius self-averages. The answer is a genuinely random GEM diversity radius, accompanied by a quantified 1/√d conditional fluctuation law and a separate Gaussian coordinate scale mixture. This supplies a structural explanation of persistent sample-to-sample radial disorder at fixed tumble rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
