---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

T is the last generation of new infections, with generation zero for the source. Each edge is tested at most once while joining an infectious to a susceptible vertex; independent preassigned edge indicators thus have the correct law. Induction over generations gives rooted shortest-path distances in the open subgraph. The endpoint path tail is p^t. On the cycle for t<=floor(n/2), the two t-edge arm events are independent, and neither successful arm can be shortened below t; their union has probability 2p^t-p^(2t). For larger t, an open arm gives distance t unless the complementary arc is all open, and both such long arms cannot be open without opening the whole cycle, giving 2(p^t-p^n). Subtracting and summing gives the stated duration polynomial, including n=3 and the endpoint differences 0 at p=0 and floor(n/2)-(n-1) at p=1. Normalizing by p^n leaves a sum of strictly decreasing negative powers minus n-1, from +infinity to a negative value. With p=exp(-z/n) and the defining equation divided by n, the Riemann-sum residual has the sign of exp(z)-1-2z at any fixed z>0 away from its unique positive root; signs on either side bracket -n log p_n. The cycle reachability probability for vertex j has two disjoint candidate routes of lengths j and n-j, giving p^j+p^(n-j)-p^n and strictly positive mean-size gain in the interior. Independent finite replay: python3 /workspace/check_frozen_mathematics.py 3; direct rational recursion on the susceptible set and current generation, without a bond-percolation simulation, matched both differences in 28 size/probability pairs (56 comparisons). The analytic argument, not that finite sample, verifies the universal and asymptotic claims.

## originality

PASS

The supported distinct content is the exact all-n crossover and its scaling, in contrast with the strict size increase. The bond coupling, elementary mean-size comparison and qualitative possibility of opposed size/duration effects are not treated as novel on their own. No compared statement gives or entails the exact duration law, unique threshold and scaling in this model.

## value

PASS

This minimal edge edit separates two natural statistics of the same random graph process: reachability improves throughout the interior, while the mean of the maximum rooted distance changes direction exactly once. The all-size uniqueness and nontrivial limiting scale go beyond a witness or finite calculation and quantify how added reachability competes with shorter routes. The theorem does not give a stochastic duration order, estimate actual epidemics, or cover other graph edits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
