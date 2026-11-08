---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For irrational 0<alpha<1/2, D exactly marks the interval [1-alpha,1); DD is impossible, and adjacent-pair probabilities UU=1-2alpha, UD=DU=alpha, DD=0 give the primitive Markov chain with a=(1-2alpha)/(1-alpha), b=alpha/(1-alpha), eigenvalues 1,-b and entropy h=(1-alpha)Hb(b)>0. The n+1 distinct rotation discontinuity arcs and Morse–Hedlund force precisely n+1 positive true words, so H(P_n)<=log(n+1). Each true word has D count k=floor(x+nalpha)-floor(x), |k-nalpha|<1, and exact Markov weight pi_first*a^(n-1-2k+firstD+lastD)*b^(k-firstD). Consequently |log Q_n(w)+nh| is uniformly bounded and overlap=sum_min(P,Q) lies between c exp(-nh) and C(n+1)exp(-nh), yielding exact -log(overlap)/n -> h; cross entropy gives D(P_n||Q_n)=Hb(alpha)+(n-1)h-H(P_n). Independently reconstructed Sturmian cylinder arcs and Markov products for n=10,20,40,80 at irrational alpha, confirming n+1 support and approach of empirical logarithmic overlap rate to h. All-length conclusion is analytical, not numerical.

## originality

PASS

Best-of-knowledge originality: original claim adds the mathematically distinct sharp classification/quantitative invariant described in the four actual prior-implication checks; no dominating statement was identified in checked primary literature, with listed specific residual risks.

## value

PASS

Exact adjacent-pair matching but exponential long-block failure is a motivated limitation of finite-state symbolic surrogates; the theorem computes both the sharp total-variation overlap exponent and KL rate from a natural irrational quasiperiodic source, distinguishing model-local mixing from trajectory-law fidelity. Not merely a restatement of zero-versus-positive entropy because overlap rate needs uniform word-weight control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
