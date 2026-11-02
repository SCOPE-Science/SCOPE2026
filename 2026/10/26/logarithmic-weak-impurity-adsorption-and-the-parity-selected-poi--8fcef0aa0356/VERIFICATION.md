---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The reduced Markov state (k,A) has exact ordinary-ordinary transition rate k(k-1)/2 and individual impurity rate k*lambda_i. Every event removes 2 vertices; the k=1 terminal rule is a rate-proportional impurity choice or ordinary vacancy. Holding-time exposure E=integral k dt until k<=ceil(log n)^2 has conditional mean sum 2/(k-1+2sum active rates)=log(n/K)+o(1), and variance O(1/K); only r one-step changes affect mesh O(1/K). Independent exponential hazard thresholds force bulk survival Bernoulli(e^-c_i) as E/log n->1. A harmonic union bound O(loglog n/log n) excludes captures at 2<=k<=K; remaining parity completes the finite state law and hence TV convergence. For r=2 even n, no impurity ever matched is product of ordinary edge selection probabilities at k=2j, giving exact finite product and limiting exp(-(c1+c2)). Independent freshly implemented exact rational labeled-edge recursion equaled reduced Markov recursion in 10 cases (r=2,3) and directly verified even-n product in tested cases; unrestricted limit rests on the exposure/threshold proof.

## originality

PASS

Best-of-knowledge new fixed-impurity weak-rate labeled parity limit and finite product; standard edge-greedy exponential clocks are prior, and 1997 weighted matching full text remains a real priority uncertainty.

## value

PASS

The 1/log n impurity rate is the mathematically natural transition scale because cumulative ordinary-vertex exposure is logarithmic. The sharp labeled Poisson-binomial survival and parity-dependent terminal selection determine more than mean coverage or bulk jamming fraction, and the r=2 finite product is an exact useful observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
