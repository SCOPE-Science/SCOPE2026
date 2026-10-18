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

For independent stationary binary CTMCs the conditional relaxation identity E(Z_i(t)-p_i|Z_i(0))=(Z_i(0)-p_i)e^{-lambda_i t} gives m=sum p_i, C(t)=sum v_i e^{-lambda_i t} and H(t)=sum v_i(1-2p_i)e^{-lambda_i t}; mixed-site centered terms vanish. Positive exponential weights identify lambda and v at unequal rates. At equal rates m and W=sum v determine unordered p via X^2-mX+(W-m+m^2)/2=0. With distinct rates each probability is 1/2 +/- sqrt(1/4-v_i); four signed sums collide in distinct labeled-rate assignments only when the positive square roots coincide and signs oppose, i.e. p1+p2=1 with p1 != p2. Exactly two inequivalent assignments remain. H(t0)=v(1-2p1)(e^{-lambda1 t0}-e^{-lambda2 t0}) is nonzero at each t0>0 and has opposite sign under the rival. Independently enumerated 36 rational two-time Bernoulli joint laws and rederived the third mixed moment and example; exact analytic argument covers all strictly positive rates.

## originality

PASS

Best-of-knowledge distinct exact two-source moment identifiability classification. Full observed-law identifiability for general aggregated chains is not equivalent to identifiability from mean and second-order moments; same-generator aggregate models cannot automatically cover heterogeneous rate–occupancy assignments. Basic exponential-mixture uniqueness and Bernoulli moments are credited. Closest broad aggregated Markov texts were not fully available; this is an explicit priority risk, not asserted absence.

## value

PASS

The exact information threshold of a natural anonymous two-patch model is a motivated structural identifiability statement. It proves exactly where covariance loses labels and gives a minimal-in-moment-order single-lag remedy; neither a parameter rewrite nor a numerical threshold without mechanism. The twofold sharp witness is essential and could guide moment design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
