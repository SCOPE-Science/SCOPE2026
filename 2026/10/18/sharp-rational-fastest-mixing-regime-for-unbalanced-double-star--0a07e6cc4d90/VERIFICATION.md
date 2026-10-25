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

For any symmetric row-stochastic chain on the p-leaf/q-leaf double star, automorphism averaging does not decrease lambda_2 of weighted Laplacian because minimum Rayleigh quotient on 1-perp is concave. Increasing spoke weights to saturated a(b)=(1-b)/p,c(b)=(1-b)/q increases lambda_2 in PSD order, so saturated symmetric families bound any original chain. For candidate a*=(p-q)/K, c*=p(p-q)/(qK), b*=(p(q+1)-q)/K (K=p^2+p-q), quotient 4x4 block M-a*I has inertia 1 negative, 1 zero, 2 positive (Schur complement rank1 PSD) and leaf differences a*,c*>a*; hence lambda2=a*. Fixed quotient eigenvector Rayleigh derivative is N/[p^2(p-q)^2]. If N>=0 it bounds lambda2 for b<b*, while for b>=b* the leaf eigenvalue a(b)<=a*; if N<0, moving b down slightly raises lambda2 by eigenvalue perturbation. Perron-Frobenius using hubs 1 and leaves 1/2 bounds lambda_max(L(b)) <= (3+b)/2 <=2-a(b); thus SLEM=1-lambda2 in saturated family. This proves globally optimal candidate iff N>=0, and strict improvability otherwise. Descartes sign test for N(q+h,q) gives unique threshold, asymptotic root t=1+sqrt2. Independently reproduced identities and low-parameter Fiedler eigenchecks against actual verify.py. No claimed optimum for N<0.

## originality

PASS

No exact prior implication was located after source-specific comparison of definitions and named parameters; best-of-knowledge, with explicit residual risks. The searches and source inspections below are not a novelty certificate.

## value

PASS

An exact algebraic necessary-and-sufficient criterion when a simple rational Markov chain is the globally fastest mixing on all unbalanced double-star trees, despite unrestricted unequal leaf weights, plus a sharp imbalance transition and asymptotic ratio. This is a motivated exact network-optimization frontier not a textbook numeric SDP instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
