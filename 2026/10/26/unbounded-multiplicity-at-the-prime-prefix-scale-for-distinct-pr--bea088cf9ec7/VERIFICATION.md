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
# Verification of the new theorem

This is a deductive analytic proof, not a finite-computation certificate.

The required source implications were checked against Campbell, arXiv:2610.19534v1: Lemma 3 gives arbitrarily large odd sums with product-minimal distinct-prime sets of each prescribed size above one; Lemma 4 gives a triple of pairwise distinct primes for each sufficiently large such odd sum; Lemma 6 identifies the unique product-maximizing complement after a following prime gap strictly greater than eleven times the relevant minimal product. Choosing a common fixed threshold applies the same argument to an arbitrary but fixed number of distinct deletion sums.

For every fixed positive integer \(H\), the classical pair-sieve estimate \(\#\{p\le y:p,p+h\text{ prime}\}=O_h(y/(\log y)^2)\) summed over \(1\le h\le H\) shows the excluded primes are \(o(\pi(y))\). This is a theorem citation, not a computational observation. The inequality \(\Sigma(p'')-\Sigma(p')\ge p''\) for distinct primes \(p'<p''\) rules out collisions across different prefixes whenever \(p''\) exceeds the maximum offset difference. Prime number theorem plus partial summation gives \(\pi(y_X)\sim2\sqrt{X/\log X}\) for the maximal prime \(y_X\) whose prime-prefix sum does not exceed \(X\). Since adjacent prime-prefix sums eventually exceed every fixed offset, the difference between that baseline cutoff and each shifted cutoff adds at most one term per offset.

Thus the \(J\)-template family has \((2J+o(1))\sqrt{X/\log X}\) distinct members, all meeting the discrepancy threshold. Since \(J\) is arbitrary but fixed before the limit, this implies the claimed infinite normalized liminf. No claim is made about effective convergence rates or full exceptional-set asymptotics. Independent mathematical audit has not been performed.
