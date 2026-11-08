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

Rotational Gaussian invariance makes W=||Pi_b v||² independent Beta(q/2,p/2), while the orthogonal split Av=(a+Delta W)v+Delta sqrt(W(1-W))u gives independent Gaussian Sv,Su. Hence lambda_hat=a+Delta[W+sqrt(W(1-W)) Z/chi_k] with independent ratio. The square of the Student ratio transformed to T=U²/(1+U²) is Beta(1/2,k/2). Escape is exactly W<T or 1-W<T according to ratio sign, proving the two incomplete-beta integrals and P(k=1)=1/2. Small-t incomplete-beta and exact beta moments yield escape k^(-r/2) with r=min(p,q) and the stated sharp constant; corresponding scaled overshoot integral yields k^(-r/2-1). The one-sided Student tail and beta moment give the fixed-k t^(-k) overshoot tail with positive constant and moment cutoff s<k. The p=q=1 planar angular integral gives P(k=2)=1-2/pi and EH/Delta=2/pi-1/2. Independent Student-ratio integration reproduced P(k=1,2,3,5)=(.5,.363380227632,.297357632715,.229810176954), corroborating the k=2 closed form.

## originality

PASS

The sketched Rayleigh–Ritz framework and possibility of non-Hermitian sketched projection are prior, as are Student/Gaussian/Beta identities. The assessed new invariant is the unconditional joint Haar-direction/Gaussian-sketch probability of leaving a two-point spectral envelope, its exact edge multiplicity rate, fixed-row tail and overshoot moments. Embedding-conditional approximation bounds do not imply this rare-event distribution, but a specialized later probabilistic analysis may.

## value

PASS

A sketched eigenvalue of a symmetric two-level operator can fall outside its actual spectral interval; the probability, overshoot and moment classification quantify a real error mode of a natural randomized linear algebra estimator. The sharp decay exponent depends on extreme eigenspace multiplicity rather than ambient dimension, with a fixed-row moment cutoff, providing a mathematically motivated exact probabilistic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
